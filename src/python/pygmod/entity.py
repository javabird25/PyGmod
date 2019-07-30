"""
Provides the :class:`Entity` class which allows creating scripted entities (a.k.a. SENTs)
by the means of PyGmod.
"""

import os
from pathlib import Path
import atexit

from pygmod import addons

__all__ = ["Entity"]

# Dictionary for keeping Entity subclasses.
# Keys are entity classnames *(not subclass __name__)*, values are subclasses.
entity_registry = {}


def generate_stub(ent_cls, classname):
    """
    Generates a Lua source file ``<addon_path>\\lua\\entities\\<classname>.lua``
    where entity attributes and methods are copied from ``ent_cls``.
    This file is required for Garry's Mod addon loader to detect the entity class.
    """
    entity_stubs_path = Path(addons.current_addon_path, "lua", "entities")
    entity_stubs_path.mkdir(parents=True, exist_ok=True)
    stub_file_path = entity_stubs_path / Path(classname + ".lua")
    with open(stub_file_path, "w+") as f:
        f.write(generate_stub_source(ent_cls, classname))
    atexit.register(os.remove, stub_file_path)


def generate_stub_source(ent_cls, classname):
    """Generates Lua source code for a file that gets created in :func:`generate_stub`."""
    src = f'-- This is a Lua stub for PyGmod entity "{classname}".\n' \
          "-- Do not edit this file, as it will be regenerated " \
          "upon the game/server restart.\n" \
          "AddCSLuaFile()\nlocal pygmod_entity = py.Import('pygmod.entity')\n"
    ent_hierarchy_class_dict = hierarchy_class_dict(ent_cls)
    for attr_name, attr_val in ent_hierarchy_class_dict.items():
        if callable(attr_val):
            src += generate_stub_source_for_callable(attr_name, classname, ent_hierarchy_class_dict)
        else:
            src += f"ENT.{attr_name} = pygmod_entity.entity_registry" \
                   f".__getitem__({classname!r}).{attr_name}  -- {attr_val!r}\n"

    return src


def generate_stub_source_for_callable(attr_name, classname, ent_hierarchy_class_dict):
    if isinstance(ent_hierarchy_class_dict[attr_name], staticmethod):
        return f"function ENT.{attr_name}(...) " \
               f"return pygmod_entity.entity_registry" \
               f".__getitem__({classname!r}).{attr_name}(...) " \
               f"end\n"
    if isinstance(ent_hierarchy_class_dict[attr_name], classmethod):
        return f"function ENT.{attr_name}(...) " \
               f"return pygmod_entity.entity_registry" \
               f".__getitem__({classname!r}).{attr_name}(" \
               f"pygmod_entity.entity_registry.__getitem__({classname!r}), ...) " \
               f"end\n"
    # Regular method
    return f"function ENT:{attr_name}(...) " \
           f"return pygmod_entity.entity_registry" \
           f".__getitem__({classname!r}).{attr_name}(self, ...) " \
           f"end\n"


def hierarchy_class_dict(cls):
    """Returns the summary dictionary of class ``cls`` and its superclasses."""
    dict_extension_order = cls.__mro__[-2::-1]  # Reversed __mro__ without object class
    ent_dict = {}
    for base_class in dict_extension_order:
        ent_dict.update(vars(base_class))
    return ent_dict


class Entity:
    """Base class for scripted entities. To create a scripted entity, simply inherit this class.

    ::

        class MyEntity(Entity):
            def Initialize(self):
                ...
            ...

    Entity classname will be generated automatically and will look something like
    ``MyAddon.python.__shared_autorun__.MyEntity``. You can set custom classname by passing it
    as a keyword argument to class inheritance parameters::

        class MyEntity(Entity, classname="ent_myentity"):
            ...

    You can set entity fields (described `here <http://wiki.garrysmod.com/page/Structures/ENT>`_)
    by setting class-level attributes::

        class MyEntity(Entity):
            Type = "point"
            Category = "My Entities"
            PrintName = "My Entity"
            Author = "Me"
            ...

    By default, ``Base`` is set to ``"base_entity"`` and ``Type`` is set to ``"anim"``.
    Also, there is a default version of ``Draw()``, so you don't have to write it by yourself::

        def Draw(self, _):
            self._.DrawModel()

    .. note:: To initialize your entity, you should use ``Initialize`` instead of ``__init__()``.
    """

    Base = "base_entity"
    Type = "anim"

    def __init_subclass__(cls, classname=None):
        if classname is None:
            classname = (cls.__module__ + "." + cls.__name__)

        generate_stub(cls, classname)
        entity_registry[classname] = cls

    def Draw(self, _):
        self._.DrawModel()
