init -1 python hide:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    config.window_title = u"Discouraged Workers"
    config.font_replacement_map["gui/fonts/NanumBarunGothic.ttf",  True,  False ]  =  ("gui/fonts/NanumBarunGothicBold.ttf",  False,  False)
    persistent.steam = False
init -2 python:
    mod_name = [ ]
    mod_desc = [ ]
    mod_label = [ ]
define config.name = _("Discouraged Workers")
define config.default_language = None
define config.hw_video = True
define config.gl_enable = True
define config.optimize_texture_bounds = True
define config.cache_surfaces = True
define config.image_cache_size_mb = 300
define config.framerate = 60
define config.manage_gc = True
define config.narrator_menu = True
define config.developer = False
define config.fast_skipping = False
define config.debug = False
define config.debug_sound = False
define config.joystick = True
define config.always_has_joystick = True
define config.keymap = dict(
    rollback = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ],
    screenshot = [ 's', 'alt_K_s', 'alt_shift_K_s' ],
    toggle_afm = [ ],
    toggle_fullscreen = [ 'f', 'alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11' ],
    game_menu = [ 'K_ESCAPE', 'K_MENU', 'mouseup_3' ],
    hide_windows = [ 'mouseup_2', 'h' ],
    launch_editor = [ 'E' ],
    dump_styles = [ ],
    reload_game = [ 'R', 'alt_shift_K_r' ],
    inspector = [ 'I' ],
    full_inspector = [ 'alt_shift_K_i' ],
    developer = [ 'D', 'alt_shift_K_d' ],
    quit = [ ],
    iconify = [ ],
    help = [ 'K_F1', 'meta_shift_/' ],
    choose_renderer = [ 'G', 'alt_shift_K_g' ],
    progress_screen = [ 'alt_shift_K_p', 'meta_shift_K_p', 'K_F2' ],
    self_voicing = [ 'v', 'V', 'alt_K_v'  ],
    clipboard_voicing = [ 'C', 'alt_shift_K_c' ],
    debug_voicing = [ 'alt_shift_K_v', 'meta_shift_K_v' ],
    rollforward = [ 'mousedown_5', 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],
    dismiss = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT' ],
    dismiss_unfocused = [ ],
    dismiss_hard_pause = [ ],
    focus_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    focus_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    focus_up = [ 'K_UP', 'repeat_K_UP' ],
    focus_down = [ 'K_DOWN', 'repeat_K_DOWN' ],
    button_ignore = [ 'mousedown_1' ],
    button_select = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    button_alternate = [ 'mouseup_3' ],
    button_alternate_ignore = [ 'mousedown_3' ],
    input_backspace = [ 'K_BACKSPACE', 'repeat_K_BACKSPACE' ],
    input_enter = [ 'K_RETURN', 'K_KP_ENTER' ],
    input_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    input_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    input_up = [ 'K_UP', 'repeat_K_UP' ],
    input_down = [ 'K_DOWN', 'repeat_K_DOWN' ],
    input_delete = [ 'K_DELETE', 'repeat_K_DELETE' ],
    input_home = [ 'K_HOME' ],
    input_end = [ 'K_END' ],
    viewport_leftarrow = [ 'K_LEFT', 'repeat_K_LEFT' ],
    viewport_rightarrow = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    viewport_uparrow = [ 'K_UP', 'repeat_K_UP' ],
    viewport_downarrow = [ 'K_DOWN', 'repeat_K_DOWN' ],
    viewport_wheelup = [ 'mousedown_4' ],
    viewport_wheeldown = [ 'mousedown_5' ],
    viewport_drag_start = [ 'mousedown_1' ],
    viewport_drag_end = [ 'mouseup_1' ],
    viewport_pageup = [  'K_PAGEUP', 'repeat_K_PAGEUP' ],
    viewport_pagedown = [  'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],
    skip = [ 'K_LCTRL', 'K_RCTRL' ],
    stop_skipping = [ ],
    toggle_skip = [ 'K_TAB' ],
    fast_skip = [ '>' ],
    bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    bar_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    bar_up = [ 'K_UP', 'repeat_K_UP' ],
    bar_down = [ 'K_DOWN', 'repeat_K_DOWN' ],
    save_delete = [ 'K_DELETE' ],
    drag_activate = [ 'mousedown_1' ],
    drag_deactivate = [ 'mouseup_1' ],
    console = [ 'shift_O', 'alt_shift_K_o' ],
    console_older = [ 'K_UP', 'repeat_K_UP' ],
    console_newer = [ 'K_DOWN', 'repeat_K_DOWN'],
    director = [ 'd' ],
    toggle_music = [ 'm' ],
    viewport_up = [ 'mousedown_4' ],
    viewport_down = [ 'mousedown_5' ],
    profile_once = [ 'K_F8' ],
    memory_profile = [ 'K_F7' ])
define config.pad_bindings = {
    "pad_leftshoulder_press" : [ "rollback", ],
    "pad_lefttrigger_pos" : [ "hide_windows", ],
    "pad_back_press" : [ "quit", ],
    "pad_guide_press" : [ "game_menu", ],
    "pad_start_press" : [ "game_menu", ],
    "pad_y_press" : [ "button_alternate" ],
    "pad_x_press" : [ "button_alternate" ],
    "pad_rightshoulder_press" : [ "rollforward", ],
    "pad_righttrigger_pos" : [ "toggle_skip" ],
    "pad_a_press" : [ "dismiss", "button_select", "bar_activate", "bar_deactivate"],
    "pad_b_press" : [ "button_alternate" ],
    "pad_dpleft_press" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
    "pad_leftx_neg" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
    "pad_rightx_neg" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
    "pad_dpright_press" : [ "focus_right", "bar_right", "viewport_rightarrow" ],
    "pad_leftx_pos" : [ "focus_right", "bar_right", "viewport_rightarrow" ],
    "pad_rightx_pos" : [ "focus_right", "bar_right", "viewport_rightarrow" ],
    "pad_dpup_press" : [ "focus_up", "bar_up", "viewport_uparrow" ],
    "pad_lefty_neg" :  [ "focus_up", "bar_up", "viewport_pageup" ],
    "pad_righty_neg" : [ "focus_up", "bar_up", "viewport_uparrow" ],
    "pad_dpdown_press" : [ "focus_down", "bar_down", "viewport_downarrow" ],
    "pad_lefty_pos" : [ "focus_down", "bar_down", "viewport_pagedown" ],
    "pad_righty_pos" : [ "focus_down", "bar_down", "viewport_downarrow" ],
    "pad_leftstick_press" : [ "screenshot" ],
    "pad_rightstick_press" : [ "save_delete" ]}
define config.autosave_on_quit = True
define config.has_autosave = True
define config.default_fullscreen = True
define config.save_on_mobile_background = True
define config.key_repeat = (0, 0)
define config.mouse = {"default": [('gui/cursor.webp', 0, 0)]}
define config.nvl_list_length = 6
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.enter_sound = "se/over.opus"
define config.exit_sound = "se/over.opus"
define config.sample_sound = "se/over.opus"
define config.main_menu_music = "bgm/Pandemic.opus"
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.main_game_transition = dissolve
define config.end_splash_transition = dissolve
define config.enter_replay_transition = dissolve
define config.exit_replay_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve
define config.window = "hide"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
define config.save_directory = "Discouraged-Workers-saves"
define config.window_icon = "gui/icon.webp"
define config.windows_icon = "gui/icon.webp"
define config.default_afm_enable = True
define config.version = "1.8.4.246"
define build.name = "Discouraged-Workers"
define gui.show_name = True
define gui.history_allow_tags = set()
default preferences.gl_framerate = 60
default preferences.gl_powersave = True
default preferences.text_cps = 50
default preferences.afm_time = 7
default preferences.afm_after_click = True
init python:
    build.exclude_empty_directories = True
    build.include_update = False
    build.allow_integrated_gpu = True
    build.archive("scripts", "all")
    build.archive("assets", "all")
    build.archive("translations", "all")
    build.archive("solimages", "windows")
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/**.py', "android")
    build.classify('**/**.rpy', None)
    build.classify('saves/**.**', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/*.rpyc', 'scripts')
    build.classify('game/images/**.**', 'assets')
    build.classify('game/gui/**.**', 'assets')
    build.classify('game/bgm/**.opus', 'assets')
    build.classify('game/se/**.opus', 'assets')
    build.classify('game/tl/**.**', 'translations')
    build.classify('game/mods/solitaire/images/**.**', None)
    build.classify('game/mods/solitaire/**.rpyc', None)
    build.classify('game/mods/fimbulvetr/**.**', None)
    build.classify('game/mods/wimcj/**.**', None)
    build.documentation('*.html')
    build.documentation('*.pdf')
    build.documentation('*.txt')
