init -2 python:
    config.image_cache_size = 64
    config.narrator_menu = True
    config.default_afm_time = 7
    config.default_afm_enable = None
    style.pref_button.size_group = "pref"
    style.pref_label_text.size = 48
    style.pref_label_text.xalign = 0.5
    style.pref_text.color = "#000"
    style.pref_text.size = 24
    style.pref_button_text.size = 48
    style.pref_vbox.xalign = 0.5
    style.pref_hbox.xalign = 0.5
    style.pref_button.xalign = 0.5
    style.pref_label.xalign = 0.5
    style.arc_button.size_group = "arc"
    style.arc_vbox.xalign = 0.5
    style.arc_hbox.xalign = 0.5
    style.arc_button.xalign = 0.5
    style.arc_label.xalign = 0.5
    style.arc_slider.xalign = 0.5
    style.arc_label_text.size = 48
    style.arc_text.color = "#000"
    style.arc_text.size = 24
    style.arc_button_text.size = 48
    style.arc_button.xsize = 332
    style.arcu_button.size_group = "arcu"
    style.arcu_label_text.size = 48
    style.arcu_text.color = "#4d4d4d"
    style.arcu_text.size = 32
    style.arcc_button.size_group = "arcc"
    style.arcc_button.xsize = 350
    style.arcc_button_text.size = 48
    style.arcc_label.xalign = 0.5
    style.arcc_label_text.size = 48
    style.arcc_text.color = "#4d4d4d"
    style.arcc_text.size = 24
    style.arcc_text.xalign = 0.5
    style.arcc_vbox.xalign = 0.5
    style.arcc_hbox.xalign = 0.5
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    style.file_picker_frame = Style(style.menu_frame)
    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)
    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)
init -1 python hide:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    config.automatic_images = True
    config.window_icon = "icon.png"
    config.windows_icon = "icon.png"
    config.developer = False
    config.debug = False
    config.debug_sound = False
    config.autosave_on_quit = True
    config.has_autosave = True
    config.rtl = True
    config.thumbnail_width = 615
    config.thumbnail_height = 346
    config.screen_width = 1920
    config.screen_height = 1080
    config.window_title = u"Discouraged Workers Demo"
    config.name = "Discouraged-workers-Demo"
    config.version = "1.0.0"
    config.default_fullscreen = True
    config.default_language = None
    config.key_repeat = None
    config.keymap['input_backspace'].remove('K_BACKSPACE')
    config.keymap['rollback'].remove('K_PAGEUP')
    config.keymap['rollback'].remove('mousedown_4')
    config.keymap['rollforward'].remove('mousedown_5')
    config.keymap['rollforward'].remove('K_PAGEDOWN')
    config.keymap['hide_windows'].remove('mouseup_2')
    config.keymap['hide_windows'].remove('h')
    config.keymap['skip'].remove('K_LCTRL')
    config.keymap['skip'].remove('K_RCTRL')
    config.keymap['toggle_skip'].remove('K_TAB')
    config.keymap['toggle_music'].remove('m')
    config.keymap['fast_skip'].remove('>')
    config.default_text_cps = 20
    config.mouse = {"default": [('cursor.png', 0, 0)]}
    config.has_sound = True
    config.has_music = True
    config.has_voice = False
    config.enter_sound = "se/over.ogg"
    config.exit_sound = "se/over.ogg"
    config.sample_sound = "se/over.ogg"
    config.main_menu_music = "bgm/Love song.ogg"
    config.help = "README_demo.html"
    config.enter_transition = Dissolve(1.0)
    config.exit_transition = Dissolve(1.0)
    config.intra_transition = Dissolve(1.0)
    config.main_game_transition = Dissolve(1.0)
    config.game_main_transition = Dissolve(1.0)
    config.end_splash_transition = Dissolve(1.0)
    config.end_game_transition = Dissolve(1.0)
    config.after_load_transition = Dissolve(1.0)
    config.window_show_transition = None
    config.window_hide_transition = None
    config.font_replacement_map [ "NanumBarunGothic.ttf" ,  True ,  False ]  =  ( "NanumBarunGothicBold.ttf" ,  False ,  False )
    style.window.background = Frame("dialogue", 0, 0)
    style.window.yminimum = 600
    style.window.top_padding = 160
    style.window.left_padding = 200
    style.window.right_padding = 200
    style.default.font = "NanumBarunGothic.ttf"
    style.default.antialias = True
    style.default.size = 48
    style.awesome = Style(style.default)
    style.awesomeg = Style(style.awesome)
    style.awesomeq = Style(style.awesome)
    style.awesomea = Style(style.awesomeq)
    style.awesomeag = Style(style.awesomea)
    style.mscreen = Style(style.default)
    style.qscreen = Style(style.mscreen)
    style.mscreeng = Style(style.mscreen)
    style.systext = Style(style.default)
    style.extext = Style(style.default)
    style.part = Style(style.extext)
    style.gall = Style(style.awesome)
    style.extext.size = 72
    style.extext.yalign = 0.5
    style.part.size = 128
    style.awesome.font = "fontawesome.ttf"
    style.awesome.size = 256
    style.awesome.color = "#000"
    style.awesomeg.color = "#4d4d4d"
    style.awesomeq.size = 160
    style.awesomeq.color = "#fff"
    style.awesomea.color = "#000"
    style.awesomeag.color = "#4d4d4d"
    style.mscreen.size = 32
    style.mscreen.color = "#000"
    style.qscreen.size = 24
    style.qscreen.color = "#fff"
    style.mscreeng.color = "#4d4d4d"
    style.systext.size = 36
    style.systext.color = "#000"
    style.gall.size = 384
    style.gall.color ="#4d4d4d"
    style.button.activate_sound = "se/over.ogg"
    style.button.hover_sound = "se/over.ogg"
    style.image_button.activate_sound = "se/over.ogg"
    style.image_button.hover_sound = "se/over.ogg"
    theme.tv(
        widget = "#999",
        widget_hover = "#1f1f1f",
        widget_text = "#000",
        widget_selected = "#fff",
        disabled = "#666",
        disabled_text = "#4d4d4d",
        label = "#000",
        frame = "#fff",
        mm_root = "#fff",
        gm_root = "#fff",
        rounded_window = False,
        )
python early:
    config.save_directory = "saves"
init python:
    build.directory_name = "Discouraged-Workers-Demo"
    build.executable_name = "Discouraged-Workers-Demo"
    build.exclude_empty_directories = True
    build.include_update = False
    build.archive("assets", "all")
    build.archive("script", "all")
    #build.archive("korean", "all")
    build.classify('game/tl/**.**', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpy', None)
    build.classify('saves/**.**', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.ttf', 'assets')
    build.classify('**.ogg', 'assets')
    build.classify('**.jpg', 'assets')
    build.classify('game/demosprites01.png', 'assets')
    build.classify('game/demosprites02.png', 'assets')
    build.classify('game/cursor.png', 'assets')
    build.classify('game/icon.png', 'assets')
    #build.classify('game/tl/Korean/*.rpyc', 'korean')
    build.classify('game/*.rpyb', 'script')
    build.classify('game/*.rpyc', 'script')
    build.documentation('*.html')
    build.documentation('*.txt')