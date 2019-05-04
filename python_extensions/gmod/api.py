import lua

_G = lua.Globals()


def _extend(names):
    """Puts all names from ``names`` to the module namespace."""
    gl = globals()

    for n in names:
        gl[n] = _G[n]


# Global functions
_global_funcs = [
    'AccessorFunc',
    'Add_NPC_Class',
    'AddCSLuaFile',
    'AddonMaterial',
    'AddOriginToPVS',
    'AddWorldTip',
    'Angle',
    'AngleRand',
    'BroadcastLua',
    'BuildNetworkedVarsTable',
    'ChangeTooltip',
    'ClientsideModel',
    'ClientsideRagdoll',
    'ClientsideScene',
    'CloseDermaMenus',
    'collectgarbage',
    'Color',
    'ColorAlpha',
    'ColorRand',
    'ColorToHSV',
    'CompileFile',
    'CompileString',
    'ConVarExists',
    'CreateClientConVar',
    'CreateConVar',
    'CreateMaterial',
    'CreateParticleSystem',
    'CreatePhysCollideBox',
    'CreatePhysCollidesFromModel',
    'CreateSound',
    'CreateSprite',
    'CurTime',
    'DamageInfo',
    'DebugInfo',
    'DEFINE_BASECLASS',
    'DeriveGamemode',
    'Derma_Anim',
    'Derma_DrawBackgroundBlur',
    'Derma_Hook',
    'Derma_Install_Convar_Functions',
    'Derma_Message',
    'Derma_Query',
    'Derma_StringRequest',
    'DermaMenu',
    'DisableClipping',
    'DOF_Kill',
    'DOF_Start',
    'DOFModeHack',
    'DrawBloom',
    'DrawColorModify',
    'DrawMaterialOverlay',
    'DrawMotionBlur',
    'DrawSharpen',
    'DrawSobel',
    'DrawSunbeams',
    'DrawTexturize',
    'DrawToyTown',
    'DropEntityIfHeld',
    'DynamicLight',
    'EffectData',
    'Either',
    'EmitSentence',
    'EmitSound',
    'EndTooltip',
    'Entity',
    'Error',
    'error',
    'ErrorNoHalt',
    'EyeAngles',
    'EyePos',
    'EyeVector',
    'FindMetaTable',
    'FindTooltip',
    'Format',
    'FrameNumber',
    'FrameTime',
    'GetConVar',
    'getfenv',
    'GetGlobalAngle',
    'GetGlobalBool',
    'GetGlobalEntity',
    'GetGlobalFloat',
    'GetGlobalInt',
    'GetGlobalString',
    'GetGlobalVector',
    'GetHostName',
    'GetHUDPanel',
    'getmetatable',
    'GetRenderTarget',
    'GetRenderTargetEx',
    'GetViewEntity',
    'HSVToColor',
    'HTTP',
    'include',
    'ipairs',
    'isangle',
    'isbool',
    'IsColor',
    'IsEnemyEntityName',
    'IsEntity',
    'isentity',
    'IsFirstTimePredicted',
    'IsFriendEntityName',
    'isfunction',
    'ismatrix',
    'IsMounted',
    'isnumber',
    'ispanel',
    'isstring',
    'istable',
    'IsTableOfEntitiesValid',
    'IsUselessModel',
    'IsValid',
    'isvector',
    'JS_Language',
    'JS_Utility',
    'JS_Workshop',
    'Label',
    'Lerp',
    'LerpAngle',
    'LerpVector',
    'LoadPresets',
    'Localize',
    'LocalPlayer',
    'LocalToWorld',
    'Material',
    'Matrix',
    'Mesh',
    'Model',
    'module',
    'Msg',
    'MsgAll',
    'MsgC',
    'MsgN',
    'NamedColor',
    'newproxy',
    'NumModelSkins',
    'OrderVectors',
    'pairs',
    'Particle',
    'ParticleEffect',
    'ParticleEffectAttach',
    'ParticleEmitter',
    'Path',
    'pcall',
    'Player',
    'PositionSpawnIcon',
    'PrecacheParticleSystem',
    'PrecacheScene',
    'PrecacheSentenceFile',
    'PrecacheSentenceGroup',
    'PrintMessage',
    'PrintTable',
    'ProjectedTexture',
    'ProtectedCall',
    'RandomPairs',
    'rawequal',
    'rawget',
    'rawset',
    'RealFrameTime',
    'RealTime',
    'RecipientFilter',
    'RegisterDermaMenuForClose',
    'RememberCursorPosition',
    'RemoveTooltip',
    'RenderAngles',
    'RenderDoF',
    'RenderStereoscopy',
    'RenderSuperDoF',
    'require',
    'RestoreCursorPosition',
    'RunConsoleCommand',
    'RunString',
    'SafeRemoveEntity',
    'SafeRemoveEntityDelayed',
    'SavePresets',
    'ScreenScale',
    'ScrH',
    'ScrW',
    'select',
    'SendUserMessage',
    'ServerLog',
    'SetClipboardText',
    'setfenv',
    'SetGlobalAngle',
    'SetGlobalBool',
    'SetGlobalEntity',
    'SetGlobalFloat',
    'SetGlobalInt',
    'SetGlobalString',
    'SetGlobalVector',
    'setmetatable',
    'SetPhysConstraintSystem',
    'SortedPairs',
    'SortedPairsByMemberValue',
    'SortedPairsByValue',
    'Sound',
    'SoundDuration',
    'SQLStr',
    'STNDRD',
    'SuppressHostEvents',
    'SysTime',
    'TauntCamera',
    'TextEntryLoseFocus',
    'TimedCos',
    'TimedSin',
    'tobool',
    'tonumber',
    'tostring',
    'TypeID',
    'unpack',
    'UnPredictedCurTime',
    'UTIL_IsUselessModel',
    'Vector',
    'VectorRand',
    'VGUIFrameTime',
    'VGUIRect',
    'VisualizeLayout',
    'WorldToLocal',
    'xpcall',
]

_extend(_global_funcs)
del _global_funcs

_global_vars = [
    'GAMEMODE',
    'GM',
    'ENT',
    'SWEP',
    'EFFECT',
    '_MODULES',

    'CLIENT',
    'CLIENT_DLL',
    'SERVER',
    'GAME_DLL',
    'MENU_DLL',
    'GAMEMODE_NAME',
    'NULL',
    'VERSION',
    'VERSIONSTR',
    'BRANCH',
    '_VERSION',

    'g_SkyPaint',
    'g_ContextMenu',
    'g_VoicePanelList',
    'g_SpawnMenu',

    'vector_origin',
    'vector_up',
    'angle_zero',
    'color_white',
    'color_black',
    'color_transparent',
]

_extend(_global_vars)
del _global_vars

_libs = [
    'GWEN',
    'achievements',
    'ai',
    'ai_schedule',
    'ai_task',
    'baseclass',
    'bit',
    'cam',
    'chat',
    'cleanup',
    'concommand',
    'constraint',
    'construct',
    'controlpanel',
    'cookie',
    'coroutine',
    'cvars',
    'debug',
    'debugoverlay',
    'derma',
    'dragndrop',
    'draw',
    'drive',
    'duplicator',
    'effects',
    'engine',
    'ents',
    'file',
    'frame_blend',
    'game',
    'gameevent',
    'gamemode',
    'gmod',
    'gmsave',
    'gui',
    'halo',
    'hammer',
    'hook',
    'http',
    'jit',
    'killicon',
    'language',
    'markup',
    'matproxy',
    'menu',
    'menubar',
    'mesh',
    'motionsensor',
    'navmesh',
    'net',
    'notification',
    'numpad',
    'package',
    'physenv',
    'player',
    'player_manager',
    'presets',
    'properties',
    'render',
    'resource',
    'saverestore',
    'scripted_ents',
    'search',
    'serverlist',
    'sound',
    'spawnmenu',
    'sql',
    'steamworks',
    'string',
    'surface',
    'system',
    'table',
    'team',
    'timer',
    'undo',
    'utf8',
    'util',
    'vgui',
    'video',
    'weapons',
    'widgets',
]

_extend(_libs)
del _libs

_classes = [
    'Angle',
    'CEffectData',
    'CLuaEmitter',
    'CLuaLocomotion',
    'CLuaParticle',
    'CMoveData',
    'CNavArea',
    'CNavLadder',
    'CNewParticleEffect',
    'CRecipientFilter',
    'CSEnt',
    'CSoundPatch',
    'CTakeDamageInfo',
    'CUserCmd',
    'ConVar',
    'Entity',
    'File',
    'IGModAudioChannel',
    'IMaterial',
    'IMesh',
    'IRestore',
    'ISave',
    'ITexture',
    'IVideoWriter',
    'MarkupObject',
    'NPC',
    'NextBot',
    'Panel',
    'PathFollower',
    'PhysCollide',
    'PhysObj',
    'Player',
    'ProjectedTexture',
    'Schedule',
    'Stack',
    'Task',
    'Tool',
    'VMatrix',
    'Vector',
    'Vehicle',
    'Weapon',
    'bf_read',
]

_extend(_classes)
del _classes

del _extend