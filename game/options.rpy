init -1 python hide:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    config.window_title = u"Discouraged Workers"
    config.font_replacement_map["gui/fonts/NanumBarunGothic.ttf",  True,  False ]  =  ("gui/fonts/NanumBarunGothicBold.ttf",  False,  False)
    persistent.steam = False
    persistent.build_mobile = False
init -1 python:
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
define config.version = "1.8.3.880"
define build.name = "Discouraged-Workers"
define build_date = _("Jan 01, 2019")
define copyright = _("©2019 YGGDRASIL STUDIO")
define code.license = _("")
define font.license = _("")
define valve.license = _("")
define xbox.license = _("")
define cc.license = _("")
define gui.show_name = True
define gui.attention = _("Attention")
define gui.language = _("")
define gui.start = _("{size=86}Start Reading{/size}")
define gui.bookmarks = _("{size=86}Bookmarks{/size}")
define gui.load = _("{size=86}Load{/size}")
define gui.archives = _("{size=86}Archives{/size}")
define gui.dlc = _("{size=86}DLC&MOD{/size}")
define gui.conf = _("{size=86}Configuration{/size}")
define gui.blind_char  = _("{size=86}Characters{/size}")
define gui.blind_con  = _("{size=86}Concept{/size}")
define gui.blind_diary  = _("{size=86}Diary{/size}")
define gui.conq = _("Config")
define gui.play = _("Play")
define gui.stop = _("Stop")
define gui.skip = _("Skip")
define gui.arcq = _("Archives")
define gui.history = _("History")
define gui.hisq = _("History")
define gui.hide = _("Hide")
define gui.save = _("Save")
define gui.credits = _("Credits")
define gui.quit = _("{size=86}Quit{/size}")
define gui.unlocked = _("Unlocked")
define gui.heal = _("Healing")
define gui.judge = _("Onlooking")
define gui.left = _("Back home")
define gui.right = _("Road not taken")
define gui.choice = _("You can make a choice here. Listen to the following explanation and choose what you want.")
define gui.teddy = _("Find Teddy")
define gui.about = _("")
define gui.lang = ("")
define gui.part01 = _("")
define gui.part02 = _("")
define gui.part03 = _("")
define gui.part04 = _("")
define gui.part05 = _("")
define gui.part06 = _("")
define gui.part07 = _("")
define gui.part08 = _("")
define gui.part09 = _("")
define gui.part10 = _("")
define gui.part11 = _("")
define gui.part12 = _("")
define gui.part13 = _("")
define gui.part14 = _("")
define gui.part15 = _("")
define gui.part16 = _("")
define gui.part17 = _("")
define gui.part18 = _("")
define gui.part19 = _("")
define gui.part20 = _("")
define gui.part21 = _("")
define gui.part22 = _("")
define gui.part23 = _("")
define gui.part24 = _("")
define gui.part25 = _("")
define gui.the_end = _("")
define gui.game_over = _("")
define gui.bgm01 = _("")
define gui.bgm02 = _("")
define gui.bgm03 = _("")
define gui.bgm04 = _("")
define gui.bgm05 = _("")
define gui.bgm06 = _("")
define gui.bgm07 = _("")
define gui.bgm08 = _("")
define gui.bgm09 = _("")
define gui.bgm10 = _("")
define gui.bgm11 = _("")
define gui.bgm12 = _("")
define gui.bgm13 = _("")
default preferences.gl_framerate = 60
default preferences.gl_powersave = True
default preferences.text_cps = 50
default preferences.afm_time = 7
default preferences.afm_after_click = True
init python:
    build.exclude_empty_directories = True
    build.include_update = False
    build.allow_integrated_gpu = True
    build.archive("script", "all")
    build.archive("assets", "all")
    build.archive("translations", "all")
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/**.py', None)
    build.classify('**/**.rpy', None)
    build.classify('saves/**.**', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    if persistent.build_mobile is False:
        build.classify('ouya-icon.png', None)
    build.classify('game/*.rpyc', 'script')
    build.classify('game/images/**.**', 'assets')
    build.classify('game/gui/**.**', 'assets')
    build.classify('**.opus', 'assets')
    build.classify('game/tl/**.**', 'translations')
    build.classify('game/rig/**.**', None)
    build.classify('game/mesh/**.**', None)
    build.classify('game/shader/**.**', None)
    build.classify('game/mods/solitaire/**.**', None)
    build.classify('game/mods/fimbulvetr/**.**', None)
    build.classify('game/mods/wimcj/**.**', None)
    build.documentation('*.html')
    build.documentation('*.pdf')
    build.documentation('*.txt')
