﻿init offset = -2
init python:
    gui.init(1920, 1080)
    if persistent.ending is True:
        gui.main_menu_illust = "gui/overlay/main_angel.webp"
    else:
        gui.main_menu_illust = "gui/overlay/main_illust.webp"
define gui.accent_color = '#000000'
define gui.idle_color = '#aaaaaa'
define gui.idle_small_color = '#888888'
define gui.hover_color = '#000000'
define gui.selected_color = '#555555'
define gui.insensitive_color = '#aaaaaa7f'
define gui.muted_color = '#666666'
define gui.hover_muted_color = '#999999'
define gui.text_color = '#fff'
define gui.interface_text_color = '#404040'
define gui.main_font = "gui/fonts/BrokenGlass.ttf"
define gui.fontawesome = "gui/fonts/fontawesome.ttf"
define gui.text_font = "gui/fonts/NanumBarunGothic.ttf"
define gui.name_text_font = "gui/fonts/NanumBarunGothicBold.ttf"
define gui.interface_text_font = "gui/fonts/NanumBarunGothic.ttf"
define gui.text_size = 33
define gui.name_text_size = 45
define gui.interface_text_size = 24
define gui.label_text_size = 42
define gui.notify_text_size = 24
define gui.title_text_size = 128
define gui.title_button_text_size = 72
define gui.main_menu_background = "gui/overlay/main_menu.webp"
define gui.gradiant = "images/gradiant.webp"
define gui.game_menu_background = im.Alpha("gui/overlay/game_menu.webp", 0.3)
define gui.main_balls = Fixed(SnowBlossom("gui/overlay/main_ball.webp", count=50, yspeed=(200, 300)), xmaximum=960, xpos=0.5)
define gui.textbox_height = 380
define gui.textbox_yalign = 1.0
define gui.name_xpos = 30
define gui.name_ypos = 70
define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_text_color = '#fff'
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False
define gui.dialogue_xpos = 30
define gui.dialogue_ypos = 140
define gui.dialogue_width = 1540
define gui.dialogue_text_xalign = 0.0
define gui.button_width = None
define gui.button_height = 54
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0
define gui.radio_button_borders = Borders(38, 6, 6, 6)
define gui.check_button_borders = Borders(38, 6, 6, 6)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.quick_button_borders = Borders(0, 0, 0, 0)
define gui.quick_button_text_size = 24
define gui.quick_button_text_idle_color = "#B76E79"
define gui.quick_button_text_hover_color = gui.text_color
define gui.quick_button_text_selected_color = "#ccc"
define gui.quick_button_text_muted_color = "#883e35"
define gui.quick_hbox_xpos = .818
define gui.quick_hbox_ypos = .77
define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define config.thumbnail_width = 384
define config.thumbnail_height = 216
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2
define gui.navigation_xpos = 60
define gui.skip_ypos = 15
define gui.notify_ypos = 68
define gui.choice_spacing = 33
define gui.navigation_spacing = 6
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 15
define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.frame_tile = False
define gui.bar_size = 54
define gui.scrollbar_size = 18
define gui.slider_size = 45
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)
define gui.unscrollable = "hide"
define config.history_length = 250
define gui.history_height = 210
define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 225
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 255
define gui.history_text_ypos = 8
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0
define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_height = 173
define gui.nvl_spacing = 15
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0
init python:
    if renpy.variant("small"):
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 54
        gui.button_text_size = 51
        gui.label_text_size = 54
        gui.textbox_height = 360
        gui.name_xpos = 30
        gui.dialogue_xpos = 30
        gui.dialogue_width = 1540
        gui.choice_button_width = 1860
        gui.navigation_xpos = 10
        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15
        gui.history_height = 285
        gui.history_text_width = 1035
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        gui.nvl_height = 255
        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488
        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8
        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30
        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
        gui.quick_button_text_size = 24