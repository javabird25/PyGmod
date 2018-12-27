"""
``loader.py`` is the second part of the initialization system.

Here is what it does:

#. Redirects I/O to Garry's Mod console with :mod:`gmod.streams` I/O classes.
#. Scans ``addons\`` directory for PyGmod addons and initializes them.
"""

import sys
import os.path
import traceback

# noinspection PyUnresolvedReferences
import luastack
from gmod import lua, streams, error_notif

__all__ = ['main']


def log(msg, end='\n'):
    print('[PyGmod]', msg, end=end)


ADDONS_PATH = 'garrysmod\\addons'
SHARED_PACKAGE = '__shared_autorun__'


def prepare_and_print_tb(exc_type, exc_value, tb):
    # Getting traceback text as a list of strings,
    # string at index 0 is "Traceback (most recent call last):", next strings are the frames.
    # The first frame is this loader's frame where it imports an addon.
    # We don't need this frame because it has no relation to the addon, so we will get rid of it
    # by deleting the string at index 1 from the text list.
    traceback_text = traceback.format_exception(exc_type, exc_value, tb)

    # Printing the clean traceback
    for l in traceback_text:
        sys.stderr.write(l)


def handle_exception(exc_type, exc_value, tb):
    error_notif.show()

    # Constructing a bar of 50 underscores to visually separate tracebacks from other output.
    bar = '_' * 50 + '\n'

    def print_bar():
        print(bar, file=sys.stderr)

    print()
    print_bar()
    prepare_and_print_tb(exc_type, exc_value, tb)
    print_bar()


sys.excepthook = handle_exception


def try_import(addon_dir, pkg):
    try:
        __import__(addon_dir + '.python.' + pkg)
        return True
    except ImportError:
        pass
    except BaseException:
        sys.excepthook(*sys.exc_info())


def redirect_output():
    streams.setup()


def main():
    """Finishes the PyGmod initialization."""
    redirect_output()

    lua.exec('''
    hook.Add('ShutDown', 'PyGmod: safe shutdown', function()
        py._SwitchToClient()
    end)
    ''')

    error_notif.setup()

    log('Loading addons...')

    realm = 'client' if lua.G.CLIENT else 'server'
    realm_pkg = f'__{realm}_autorun__'

    sys.path.append(os.path.abspath(ADDONS_PATH))

    for addon_dir in (d for d in os.listdir(ADDONS_PATH) if os.path.isdir(os.path.join(ADDONS_PATH, d))):
        sys.path.append(os.path.join(ADDONS_PATH, addon_dir, 'python'))

        success = (try_import(addon_dir, SHARED_PACKAGE), try_import(addon_dir, realm_pkg))

        del sys.path[-1]

        if any(success):
            log('"' + addon_dir + '" successfully loaded.')

    log('Loading finished')

    luastack.setup_complete = True