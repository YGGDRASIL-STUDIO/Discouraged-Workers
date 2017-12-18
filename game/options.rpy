init -1 python hide:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    config.window_title = u"Discouraged Workers"
    config.font_replacement_map["gui/fonts/NanumBarunGothic.ttf",  True,  False ]  =  ("gui/fonts/NanumBarunGothicBold.ttf",  False,  False)
    persistent.steam = False
init -1 python:
    mod_name = [ ]
    mod_desc = [ ]
    mod_label = [ ]
define config.name = _("Discouraged Workers")
define config.hw_video = True
define config.image_cache_size = 32
define config.framerate = 60
define config.narrator_menu = True
define config.developer = False
define config.fast_skipping = False
define config.debug = False
define config.debug_sound = False
define config.joystick = True
define config.always_has_joystick = True
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
define config.version = "1.7.9.751"
define build.name = "Discouraged-Workers"
define build_date = _("Dec 18, 2017")
define copyright = _("©2017 YGGDRASIL STUDIO")
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
default preferences.text_cps = 50
default preferences.afm_time = 7
default preferences.afm_after_click = True
init python:
    build.exclude_empty_directories = True
    build.include_update = False
    build.archive("script", "all")
    build.archive("assets", "all")
    build.archive("translations", "all")
    build.archive("mod", "all")
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/**.py', None)
    build.classify('**/**.rpy', None)
    build.classify('saves/**.**', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/languages.rpyc', None)
    build.classify('game/mod/testing/**.**', 'mod')
    build.classify('game/*.rpyc', 'script')
    build.classify('game/images/**.**', 'assets')
    build.classify('game/gui/**.**', 'assets')
    build.classify('**.opus', 'assets')
    build.classify('game/tl/**.**', 'translations')
    build.documentation('*.html')
    build.documentation('*.pdf')
    build.documentation('*.txt')