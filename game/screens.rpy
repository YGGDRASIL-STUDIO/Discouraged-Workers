init offset = -1
style default:
    font gui.text_font size gui.text_size color gui.text_color
style input:
    color gui.text_color
style hyperlink_text:
    color gui.accent_color hover_color gui.hover_color hover_underline True
style gui_text:
    font gui.interface_text_font color gui.interface_text_color size gui.interface_text_size
style button:
    properties gui.button_properties("button")
style button_text is gui_text:
    properties gui.button_text_properties("button") yalign 0.5
style label_text is gui_text:
    color gui.accent_color size gui.label_text_size
style prompt_text is gui_text:
    color gui.text_color size gui.interface_text_size
style bar:
    ysize gui.bar_size left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile) right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile) xmaximum 525
style vbar:
    xsize gui.bar_size top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile) thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile) thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile) thumb "gui/slider/horizontal_[prefix_]thumb.webp"
style vslider:
    xsize gui.slider_size base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile) thumb "gui/slider/vertical_[prefix_]thumb.webp"
style frame:
    padding gui.frame_borders.padding background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)
style part_title:
    font gui.main_font size gui.title_text_size color "#fff" xalign .97 yalign .99
style gallery_title is part_title:
    outlines [ ((5), '#0000007f', (0), (0)) ]
style unlocked_title:
    font gui.main_font size gui.title_text_size color "#000" xalign .5 yalign .2
style credits_title:
    font gui.main_font size gui.title_text_size color "#fff" outlines [ ((5), '#0000007f', (0), (0)) ] xpos .8 yalign .1
style thanks_title is credits_title:
    xalign .5 yalign .7
style credits_text:
    font gui.text_font size gui.text_size color "#fff" outlines [ ((3), '#0000007f', (0), (0)) ] xpos .8 yalign .5
style thanks_text is centered_text:
    yalign .8
style extext is default:
    size 72 yalign .5
style awegall:
    font gui.fontawesome size 320
style awearc:
    font gui.fontawesome size 320 color "#ccc"
if renpy.variant("small"):
    style arc_text:
        size 32 color gui.accent_color
    style arc_text_gray:
        size 32 color gui.interface_text_color
else:
    style arc_text:
        color gui.accent_color
    style arc_text_gray:
        color gui.interface_text_color
style arc_text_small:
    size 16 color gui.accent_color xmaximum 210 text_align .5
style arc_text_small_gray is arc_text_small:
    color gui.interface_text_color
style arc_diary_small is arc_text_small:
    xmaximum 230 text_align 0
style arc_diary_small_sepia is arc_diary_small:
    color "#704214"
style wimcj_large_message:
    font 'gui/fonts/GameJoltInspired.ttf' size 256
style wimcj_level_say_text is default:
    xalign .5 ypos .8 outlines [(1, "#000", 1, 1)]
style wimcj_message is default:
    font 'gui/fonts/GameJoltInspired.ttf' color "#ffff00" size 48 outlines [(1, "#000", 0, 0)]
screen say(who, what):
    default side_image = None
    default two_window = False
    style_prefix "say"
    window:
        id "window"
        text what id "what"
        if who is not None:
            window:
                style "namebox"
                text who id "who"
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    if show_quick_menu:
        use quick_menu
style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label
style window:
    xalign 0.5 xfill True yalign gui.textbox_yalign ysize gui.textbox_height background Image("gui/dialogue.webp", xalign=0.5, yalign=1.0)
style namebox:
    xpos gui.name_xpos xanchor gui.name_xalign xsize gui.namebox_width ypos gui.name_ypos ysize gui.namebox_height background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign) padding gui.namebox_borders.padding
style say_label:
    color gui.text_color font gui.name_text_font size gui.name_text_size xalign gui.name_xalign yalign 0.5
style say_dialogue:
    xpos gui.dialogue_xpos xanchor gui.dialogue_text_xalign xsize gui.dialogue_width ypos gui.dialogue_ypos text_align gui.dialogue_text_xalign layout ("subtitle" if gui.dialogue_text_xalign else "tex")
screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xpos gui.dialogue_xpos xanchor gui.dialogue_text_xalign ypos gui.dialogue_ypos
            text prompt style "input_prompt"
            input id "input"
style input_prompt is default
style input_prompt:
    xmaximum gui.dialogue_width xalign gui.dialogue_text_xalign text_align gui.dialogue_text_xalign
style input:
    xmaximum gui.dialogue_width xalign gui.dialogue_text_xalign text_align gui.dialogue_text_xalign
screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action
style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style choice_vbox:
    xalign 0.5 ypos 405 yanchor 0.5 spacing gui.choice_spacing
style choice_button is default:
    properties gui.button_properties("choice_button")
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
screen quick_menu():
    zorder 100
    style_prefix "quick"
    if persistent.blind is True:
        pass
    elif persistent.controllers == None:
        hbox xpos gui.quick_hbox_xpos ypos gui.quick_hbox_ypos:
            grid 3 2:
                if _preferences.afm_enable is True:
                    button xsize 120:
                        vbox xalign 0.5:
                            textbutton ('{font=[gui.fontawesome]}{size=96}{/size}{/font}') action [SetField(_preferences, 'afm_enable', False), SetField(_preferences, 'afm_after_click', False)] at menuback:
                                xalign 0.5
                            textbutton ('{size=[gui.quick_button_text_size]}Stop{/size}') action [SetField(_preferences, 'afm_enable', False), SetField(_preferences, 'afm_after_click', False)] at menuback:
                                xalign 0.5
                else:
                    button xsize 120:
                        vbox xalign 0.5:
                            textbutton ('{font=[gui.fontawesome]}{size=96}{/size}{/font}') action [SetField(_preferences, 'afm_enable', True), SetField(_preferences, 'afm_after_click', True)] at menuback:
                                xalign 0.5
                            textbutton ('{size=[gui.quick_button_text_size]}Play{/size}') action [SetField(_preferences, 'afm_enable', True), SetField(_preferences, 'afm_after_click', True)] at menuback:
                                xalign 0.5
                button xsize 120:
                        vbox xalign 0.5:
                            textbutton ('{font=[gui.fontawesome]}{size=96}{/size}{/font}') action Skip() at menuback:
                                xalign 0.5
                            textbutton ('{size=[gui.quick_button_text_size]}Skip{/size}') action Skip() at menuback:
                                xalign 0.5
                button xsize 120:
                        vbox xalign 0.5:
                            textbutton ('{font=[gui.fontawesome]}{size=96}{/size}{/font}') action ShowMenu('history') at menuback:
                                xalign 0.5
                            textbutton ('{size=[gui.quick_button_text_size]}History{/size}') action ShowMenu('history') at menuback:
                                xalign 0.5
                button xsize 120:
                        vbox xalign 0.5:
                            textbutton ('{font=[gui.fontawesome]}{size=96}{/size}{/font}') at menuback:
                                xalign 0.5
                                action ShowMenu('save')
                            textbutton ('{size=[gui.quick_button_text_size]}Save{/size}') at menuback:
                                xalign 0.5
                                action ShowMenu('save')
                button xsize 120:
                        vbox xalign 0.5:
                            textbutton ('{font=[gui.fontawesome]}{size=96}{/size}{/font}') action [SetField(persistent, 'archives', True), ShowMenu('archives')] at menuback:
                                xalign 0.5
                            textbutton ('{size=[gui.quick_button_text_size]}Archives{/size}') action [SetField(persistent, 'archives', True), ShowMenu('archives')] at menuback:
                                xalign 0.5
                button xsize 120:
                        vbox xalign 0.5:
                            textbutton ('{font=[gui.fontawesome]}{size=96}{/size}{/font}') action ShowMenu('preferences') at menuback:
                                xalign 0.5
                            textbutton ('{size=[gui.quick_button_text_size]}Config{/size}') action ShowMenu('preferences') at menuback:
                                xalign 0.5
    else:
        hbox xpos gui.quick_hbox_xpos ypos gui.quick_hbox_ypos:
            grid 3 2:
                if _preferences.afm_enable is True:
                    button xsize 120:
                        vbox xalign .5:
                            spacing 5
                            add 'controller_play' xalign .5
                            text ('{size=[gui.quick_button_text_size]}Stop{/size}') xalign .5
                else:
                    button xsize 120:
                        vbox xalign 0.5:
                            spacing 5
                            add 'controller_play'  xalign .5
                            text ('{size=[gui.quick_button_text_size]}Play{/size}') xalign .5
                button xsize 120:
                    vbox xalign 0.5:
                        spacing 5
                        add 'controller_arc' xalign .5
                        text ('{size=[gui.quick_button_text_size]}Archives{/size}') xalign .5
                button xsize 120:
                    vbox xalign 0.5:
                        spacing 5
                        add 'controller_config' xalign .5
                        text ('{size=[gui.quick_button_text_size]}Config{/size}') xalign .5
                button xsize 120:
                    vbox xalign 0.5:
                        spacing 5
                        add 'controller_save' xalign .5
                        text ('{size=[gui.quick_button_text_size]}Save{/size}') xalign .5
                button xsize 120:
                    vbox xalign 0.5:
                        spacing 5
                        add 'controller_hide' xalign .5
                        text ('{size=[gui.quick_button_text_size]}Hide{/size}') xalign .5
                button xsize 120:
                    vbox xalign 0.5:
                        spacing 5
                        add 'controller_skip' xalign .5
                        text ('{size=[gui.quick_button_text_size]}Skip{/size}') xalign .5
style quick_button is default
style quick_button_text is button_text
style quick_button:
    properties gui.button_properties("quick_button")
style quick_button_text:
    properties gui.button_text_properties("quick_button")
screen navigation():
    vbox:
        style_prefix "navigation" xpos gui.navigation_xpos yalign 0.5 spacing gui.navigation_spacing
        if persistent.opening is None:
            textbutton _("{font=[gui.fontawesome]}{/font} Basic Settings") action Show("default_language")
            textbutton _("{font=[gui.fontawesome]}{/font} About") action Show("about")
            if renpy.variant("pc"):
                textbutton _("{font=[gui.fontawesome]}{/font} Help") action Show("help")
        elif persistent.archives is True:
            textbutton ("{font=[gui.fontawesome]}{/font} Archives") action Show("archives")
            textbutton _("{font=[gui.fontawesome]}{/font} Characters") action Show("characters")
            textbutton _("{font=[gui.fontawesome]}{/font} Concept") action Show("concept")
            textbutton _("{font=[gui.fontawesome]}{/font} Diary") action Show("diary")
            textbutton _("{font=[gui.fontawesome]}{/font} Gallery") action Show("gallery")
            textbutton _("{font=[gui.fontawesome]}{/font} Music") action Show("music_room")
            textbutton _("{font=[gui.fontawesome]}{/font} Replay") action Show("replay")
            textbutton _("{font=[gui.fontawesome]}{/font} Credits") action Show("credits")
        elif persistent.downloadable is True:
            textbutton _("{font=[gui.fontawesome]}{/font} DLC") action SetScreenVariable("downloadable", "dlc")
            textbutton _("{font=[gui.fontawesome]}{/font} MOD") action SetScreenVariable("downloadable", "mod")
            textbutton _("{font=[gui.fontawesome]}{/font} Window") action Preference("display", "window")
            textbutton _("{font=[gui.fontawesome]}{/font} Fullscreen") action Preference("display", "fullscreen")
            textbutton _("{font=[gui.fontawesome]}{/font} Refresh") action Jump("refresh")
        elif persistent.part_clear is True:
            textbutton ("{font=[gui.fontawesome]}{/font} Unlocked") action Show('part_clear')
            textbutton ("{font=[gui.fontawesome]}{/font} History") action Show("history")
            textbutton _("{font=[gui.fontawesome]}{/font} Save") action Show("save")
            textbutton ("{font=[gui.fontawesome]}{/font} Archives") action Show("archives")
        else:
            if main_menu:
                textbutton _("{font=[gui.fontawesome]}{/font} Start Reading") action Start()
            else:
                textbutton ("{font=[gui.fontawesome]}{/font} History") action ShowMenu("history")
                textbutton _("{font=[gui.fontawesome]}{/font} Save") action ShowMenu("save")
            textbutton _("{font=[gui.fontawesome]}{/font} Load") action ShowMenu("load")
            textbutton _("{font=[gui.fontawesome]}{/font} Basic Settings") action ShowMenu("default_language")
            textbutton _("{font=[gui.fontawesome]}{/font} Configuration") action ShowMenu("preferences")
            if _in_replay:
                textbutton _("{font=[gui.fontawesome]}{/font} End Replay") action EndReplay(confirm=True)
            elif not main_menu:
                textbutton _("{font=[gui.fontawesome]}{/font} Main Menu") action MainMenu()
            textbutton _("{font=[gui.fontawesome]}{/font} About") action ShowMenu("about")
            if renpy.variant("pc"):
                textbutton _("{font=[gui.fontawesome]}{/font} Help") action ShowMenu("help")
                textbutton _("{font=[gui.fontawesome]}{/font} Quit") action Quit(confirm=not main_menu)
style navigation_button is gui_button
style navigation_button_text is gui_button_text
style navigation_button:
    size_group "navigation" properties gui.button_properties("navigation_button")
style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
screen main_menu():
    tag menu
    style_prefix "main_menu"
    add gui.main_menu_background
    add gui.main_menu_illust
    add gui.main_balls at main_balls
    vbox xsize 960 xpos .5:
        text "[config.name]":
            style "main_menu_title"
    vbox xsize 960 xpos .5 yalign .68 spacing 30:
        if persistent.controllers == None:
            textbutton _("{size=86}Start Reading{/size}") action Start()
            if persistent.blind is True:
                textbutton _("{size=86}Load{/size}") action QuickLoad() alt _("Load")
                textbutton _("{size=86}Characters{/size}") action [SetVariable('blind_set', 1), ShowMenu("blind_arc")]
                textbutton _("{size=86}Concept{/size}") action [SetVariable('blind_set', 2), ShowMenu("blind_arc")]
                textbutton _("{size=86}Diary{/size}") action [SetVariable('blind_set', 0), ShowMenu("blind_arc")]
            else:
                textbutton _("{size=86}Bookmarks{/size}") action ShowMenu("load")
                textbutton _("{size=86}Archives{/size}") action [SetField(persistent, 'archives', True), ShowMenu("archives")]
                if persistent.steam is True:
                    textbutton _("{size=86}DLC&MOD{/size}") action [SetField(persistent, 'downloadable', True), ShowMenu("downloadable")]
                textbutton _("{size=86}Configuration{/size}") action ShowMenu("preferences")
            if renpy.variant("pc"):
                textbutton _("{size=86}Quit{/size}") action Quit()
        else:
            if persistent.controllers == "steam":
                textbutton _("{image=gui/controllers/[persistent.controllers]/grip_r.webp} {size=86}Start Reading{/size}") action Start()
            else:
                textbutton _("{image=gui/controllers/[persistent.controllers]/guide.webp} {size=86}Start Reading{/size}") action Start()
            if persistent.controllers == "ouya":
                if persistent.blind is True:
                    textbutton _("{image=gui/controllers/[persistent.controllers]/shoulder_r.webp} {size=86}Load{/size}") action QuickLoad() alt _("Load")
                else:
                    textbutton _("{image=gui/controllers/[persistent.controllers]/shoulder_r.webp} {size=86}Bookmarks{/size}") action ShowMenu("load")
            else:
                if persistent.blind is True:
                    textbutton _("{image=gui/controllers/[persistent.controllers]/button_start.webp} {size=86}Load{/size}") action QuickLoad() alt _("Load")
                else:
                    textbutton _("{image=gui/controllers/[persistent.controllers]/button_start.webp} {size=86}Bookmarks{/size}") action ShowMenu("load")
            if persistent.blind is True:
                textbutton _("{image=gui/controllers/[persistent.controllers]/button_b.webp} {size=86}Characters{/size}") action [SetVariable('blind_set', 1), ShowMenu("blind_arc")]
                textbutton _("{image=gui/controllers/[persistent.controllers]/button_x.webp} {size=86}Concept{/size}") action [SetVariable('blind_set', 2), ShowMenu("blind_arc")]
                textbutton _("{image=gui/controllers/[persistent.controllers]/button_y.webp} {size=86}Diary{/size}") action [SetVariable('blind_set', 0), ShowMenu("blind_arc")]
            else:
                textbutton _("{image=gui/controllers/[persistent.controllers]/button_b.webp} {size=86}Archives{/size}") action [SetField(persistent, 'archives', True), ShowMenu("archives")]
                if persistent.steam is True:
                    textbutton _("{image=gui/controllers/[persistent.controllers]/button_x.webp} {size=86}DLC&MOD{/size}")  action [SetField(persistent, 'downloadable', True), ShowMenu("downloadable")]
                textbutton _("{image=gui/controllers/[persistent.controllers]/button_y.webp} {size=86}Configuration{/size}") action ShowMenu("preferences")
            if renpy.variant("pc"):
                if persistent.controllers == "ouya":
                    textbutton _("{image=gui/controllers/[persistent.controllers]/shoulder_l.webp} {size=86}Quit{/size}") action Quit()
                else:
                    textbutton _("{image=gui/controllers/[persistent.controllers]/button_select.webp} {size=86}Quit{/size}") action Quit()
    add gui.gradiant
    if gui.show_name:
        vbox:
            imagebutton idle NewsThumb() action ShowNews()
            text "June 06, 2020 - V[config.version]":
                style "main_menu_version"
            text "©2020 YGGDRASIL STUDIO":
                style "main_menu_version"
    key "game_menu" action ShowMenu('load')
    if persistent.blind is True:
        key 'K_a' action [SetVariable('blind_set', 1), ShowMenu("blind_arc")]
        key 'K_p' action [SetVariable('blind_set', 2), ShowMenu("blind_arc")]
        key 'K_c' action [SetVariable('blind_set', 0), ShowMenu("blind_arc")]
        key 'pad_b_press' action [SetVariable('blind_set', 1), ShowMenu("blind_arc")]
        key 'pad_x_press'  action [SetVariable('blind_set', 2), ShowMenu("blind_arc")]
        key 'pad_y_press' action [SetVariable('blind_set', 0), ShowMenu("blind_arc")]
        key 'K_b' action QuickLoad()
        key 'pad_start_press' action QuickLoad()
        key 'mouseup_3' action QuickLoad()
    else:
        key 'K_a' action [SetField(persistent, 'archives', True), ShowMenu('archives')]
        key 'K_p' action [SetField(persistent, 'downloadable', True), ShowMenu("downloadable")]
        key 'K_c' action ShowMenu('preferences')
        key 'pad_b_press' action [SetField(persistent, 'archives', True), ShowMenu('archives')]
        key 'pad_x_press'  action [SetField(persistent, 'downloadable', True), ShowMenu("downloadable")]
        key 'pad_y_press' action ShowMenu('preferences')
        key 'K_b' action ShowMenu('load')
    key 'K_q' action Quit(confirm=False)
    key 'pad_guide_press' action Start()
    key 'K_PERIOD' action Start()
    key 'pad_back_press' action Quit(confirm=False)
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 420 yfill True background "gui/overlay/main_menu.webp"
style main_menu_vbox:
    xoffset 10 xmaximum 1200 yalign 1.0 yoffset -3
style main_menu_text:
    layout "subtitle" color gui.accent_color
style main_menu_title:
    xalign .5 yoffset -720 size gui.title_text_size font gui.main_font
style main_menu_button:
    xalign .5
style main_menu_button_text:
    font gui.main_font size gui.title_button_text_size
screen game_menu(title, scroll=None):
    add gui.main_menu_background
    add gui.game_menu_background
    style_prefix "game_menu"
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial 1.0
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        transclude
                else:
                    transclude
    use navigation
    if persistent.opening is None:
        textbutton _("{font=[gui.fontawesome]}{/font} Done"):
            style "return_button"
            action Return()
    elif persistent.part_clear is True:
        textbutton _("{font=[gui.fontawesome]}{/font} Done"):
            style "return_button"
            action [Return(), SetField(persistent, 'part_clear', False)]
        key "game_menu" action [Return(), SetField(persistent, 'part_clear', False)]
        key 'pad_b_press' action [Return(), SetField(persistent, 'part_clear', False)]
    else:
        textbutton _("{font=[gui.fontawesome]}{/font} Return"):
            style "return_button"
            action [Return(), SetField(persistent, 'archives', None), SetField(persistent, 'downloadable', None)]
        key "game_menu" action [Return(), SetField(persistent, 'archives', None), SetField(persistent, 'downloadable', None)]
        key 'pad_b_press' action [Return(), SetField(persistent, 'archives', None), SetField(persistent, 'downloadable', None)]
    label title
style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text
style game_menu_outer_frame:
    bottom_padding 45 top_padding 180 background gui.game_menu_background
style game_menu_navigation_frame:
    xsize 420 yfill True
style game_menu_content_frame:
    left_margin 60 right_margin 30 top_margin 15
style game_menu_viewport:
    xsize 1380
style game_menu_vscrollbar:
    unscrollable gui.unscrollable
style game_menu_side:
    spacing 15
style game_menu_label:
    xpos 75 ysize 180
style game_menu_label_text:
    font gui.main_font size gui.title_text_size color gui.accent_color yalign 0.5
style return_button:
    xpos gui.navigation_xpos yalign 1.0 yoffset -45
screen about():
    tag menu
    modal True
    use game_menu(_("{font=[gui.fontawesome]}{/font} About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            text _("Discouraged Workers ©2020 YGGDRASIL STUDIO Co, Pte. All Rights Reserved. All literary works/trademarks are property of their respective owners. Do not distribute our program or any alterations of our program files. For the End User License Agreement, please view the EULA.txt file in the licenses directory, or visit {a=https://github.com/YGGDRASIL-STUDIO/Discouraged-Workers/blob/gh-pages/EULA.txt}here{/a}.\n\nThe source code of Discouraged Workers is covered by the terms of the GNU Lesser General Public License v3.0. The source code can be found {a=https://github.com/YGGDRASIL-STUDIO/Discouraged-Workers/tree/source-codes}here{/a}.\n")
            text _("Created with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\nThis program contains free software under a number of licenses, including the MIT License and GNU Lesser General Public License. A complete list of software, including links to full source code, can be found {a=https://www.renpy.org/l/license/}here{/a}.\n")
            text _("This program contains free font software under a number of licenses, including the SIL Open Font License. A complete list of font software, including links to download can be found {a=https://github.com/YGGDRASIL-STUDIO/Discouraged-Workers/wiki/about#licenses}here{/a}, or please view the fonts-LICENSE.txt file in the licenses directory.\n\nThis program contains a number of assets that are covered by the terms of the Creative Commons License. For a list of assets, and a location where the original assets can be downloaded from, please view the assets-LICENSE.txt file in the licenses directory or visit {a=https://github.com/YGGDRASIL-STUDIO/Discouraged-Workers/wiki/about#licenses}here{/a}.\n")
            text _("This program contains Xbox 360 Controller/Button images. The asset pack can be found {a=http://xbox.create.msdn.com/en-us/education/catalog/utility/controller_buttons}here{/a}.\n")
            text _("©2020 Valve Corporation. Steam and the Steam logo are trademarks and/or registered trademarks of Valve Corporation in the U.S. and/or other countries.\n\n©2020 Valve Corporation. Steamworks and the Steamworks logo are trademarks and/or registered trademarks of Valve Corporation in the U.S. and/or other countries.")
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style about_label_text:
    size gui.label_text_size
screen save():
    tag menu
    modal True
    use file_slots(_("{font=[gui.fontawesome]}{/font} Save"))
    key 'K_b' action Return()
screen load():
    tag menu
    modal True
    use file_slots(_("{font=[gui.fontawesome]}{/font} Load"))
    key 'K_b' action Return()
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    use game_menu(title):
        fixed:
            order_reverse True
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                textbutton _("{#auto_page}A") action FilePage("auto")
                textbutton _("{#quick_page}Q") action FilePage("quick")
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()
style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
style page_label:
    xpadding 75 ypadding 5
style page_label_text:
    text_align 0.5 layout "subtitle" hover_color gui.hover_color
style page_button:
    properties gui.button_properties("page_button")
style page_button_text:
    properties gui.button_text_properties("page_button")
style slot_button:
    properties gui.button_properties("slot_button")
style slot_button_text:
    properties gui.button_text_properties("slot_button")
screen preferences():
    tag menu
    modal True
    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4
    use game_menu(_("{font=[gui.fontawesome]}{/font} Configuration"), scroll="viewport"):
        vbox:
            hbox:
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("{font=[gui.fontawesome]}{/font} Display")
                        textbutton _("{font=[gui.fontawesome]}{/font} Window") action Preference("display", "window")
                        textbutton _("{font=[gui.fontawesome]}{/font} Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "radio"
                    label _("{font=[gui.fontawesome]}{/font} Rollback Side")
                    textbutton _("{font=[gui.fontawesome]}{/font} Disable") action Preference("rollback side", "disable")
                    textbutton _("{font=[gui.fontawesome]}{/font} Left") action Preference("rollback side", "left")
                    textbutton _("{font=[gui.fontawesome]}{/font} Right") action Preference("rollback side", "right")
                vbox:
                    style_prefix "check"
                    label _("{font=[gui.fontawesome]}{/font} Skip")
                    textbutton _("{font=[gui.fontawesome]}{/font} Seen Text") action Preference("skip", "seen")
                    textbutton _("{font=[gui.fontawesome]}{/font} After Choices") action Preference("after choices", "toggle")
                    textbutton _("{font=[gui.fontawesome]}{/font} Transitions") action InvertSelected(Preference("transitions", "toggle"))
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                vbox:
                    label _("{font=[gui.fontawesome]}{/font} Text Speed")
                    bar value Preference("text speed")
                    label _("{font=[gui.fontawesome]}{/font} Auto-Forward Time")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("{font=[gui.fontawesome]}{/font} Music Volume")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("{font=[gui.fontawesome]}{/font} Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                    if config.has_voice:
                        label _("{font=[gui.fontawesome]}{/font} Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("{font=[gui.fontawesome]}{/font} Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        hbox:
                            if config.sample_sound:
                                    textbutton _("{font=[gui.fontawesome]}{/font} Test") action Play("sound", config.sample_sound)
                            textbutton _("{font=[gui.fontawesome]}{/font} Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"
    key 'K_c' action Return()
    key 'pad_y_press' action Return()
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text
style pref_label:
    top_margin gui.pref_spacing bottom_margin 3
style pref_label_text:
    yalign 1.0
style pref_vbox:
    xsize 338
style radio_vbox:
    spacing gui.pref_button_spacing
style radio_button:
    properties gui.button_properties("radio_button") foreground "gui/button/check_[prefix_]foreground.webp"
style radio_button_text:
    properties gui.button_text_properties("radio_button")
style check_vbox:
    spacing gui.pref_button_spacing
style check_button:
    properties gui.button_properties("check_button") foreground "gui/button/check_[prefix_]foreground.webp"
style check_button_text:
    properties gui.button_text_properties("check_button")
style slider_slider:
    xsize 525
style slider_button:
    properties gui.button_properties("slider_button") yalign 0.5 left_margin 15
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_vbox:
    xsize 675
screen history():
    tag menu
    modal True
    predict False
    use game_menu(_("{font=[gui.fontawesome]}{/font} History"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"
        for h in _history_list:
            window:
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what substitute False
        if not _history_list:
            label _("The dialogue history is empty.")
style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text
style history_window:
    xfill True ysize gui.history_height
style history_name:
    xpos gui.history_name_xpos xanchor gui.history_name_xalign ypos gui.history_name_ypos xsize gui.history_name_width
style history_name_text:
    min_width gui.history_name_width text_align gui.history_name_xalign
style history_text:
    xpos gui.history_text_xpos ypos gui.history_text_ypos xanchor gui.history_text_xalign xsize gui.history_text_width min_width gui.history_text_width text_align gui.history_text_xalign layout ("subtitle" if gui.history_text_xalign else "tex")
style history_label:
    xfill True
style history_label_text:
    xalign 0.5
screen help():
    tag menu
    modal True
    default device = "keyboard"
    use game_menu(_("{font=[gui.fontawesome]}{/font} Help"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 23
            hbox:
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                if persistent.controllers is not None:
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
screen keyboard_help():
    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")
    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")
    hbox:
        label _("Escape")
        text _("Accesses the game menu.")
    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")
    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")
    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")
    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")
    hbox:
        label "H"
        text _("Hides the user interface.")
    hbox:
        label "S"
        text _("Takes a screenshot.")
    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
screen mouse_help():
    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")
    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")
    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")
    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")
screen gamepad_help():
    hbox:
        label _("A/Bottom Button")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label ("Left Bumper")
        text _("Rolls back to earlier dialogue.")
    hbox:
        label _("Right Bumper")
        text _("Rolls forward to later dialogue.")
    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")
    hbox:
        label _("Start")
        text _("Accesses the game menu.")
    textbutton _("Calibrate") action GamepadCalibrate()
style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text
style help_button:
    properties gui.button_properties("help_button") xmargin 12
style help_button_text:
    properties gui.button_text_properties("help_button")
style help_label:
    xsize 375 right_padding 30
style help_label_text:
    size gui.text_size xalign 1.0 text_align 1.0
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.webp"
    frame:
        vbox:
            xalign .5 yalign .5 spacing 45
            label _(message):
                style "confirm_prompt" xalign 0.5
            if persistent.blind is True:
                label _("Left arrow key: Yes, Right arrow key: No."):
                    style "confirm_prompt" xalign 0.5
            hbox:
                xalign 0.5 spacing 150
                textbutton _("{font=[gui.fontawesome]}{/font} Yes") action yes_action
                textbutton _("{font=[gui.fontawesome]}{/font} No") action no_action
    if persistent.blind is True:
        key 'pad_leftx_neg' action yes_action
        key 'K_LEFT' action yes_action
        key 'pad_leftx_pos' action no_action
        key 'K_RIGHT' action no_action
    key 'K_o' action yes_action
    key 'K_p' action no_action
    key 'pad_a_press' action yes_action
    key 'pad_x_press' action no_action
    key "game_menu" action no_action
style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text
style confirm_frame:
    background Frame([ "gui/confirm_frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=gui.frame_tile) padding gui.confirm_frame_borders.padding xalign .5 yalign .5
style confirm_prompt_text:
    text_align 0.5 layout "subtitle" color gui.accent_color
style confirm_button:
    properties gui.button_properties("confirm_button")
style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
screen save_confirm():
    if persistent.blind is True:
        use confirm(_("The next step is an important scene. Do you want to save here?"), [Return(), QuickSave()], Return())
    else:
        use confirm(_("The next step is an important scene. Do you want to save here?"), [Return(), ShowMenu('save')], Return())
screen self_inflicted():
    tag menu
    add 'dialoguer' ypos .649
    style_prefix "quick"
    hbox xalign .5 yalign .99 spacing 250:
        if sicount == 0:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('sicount', 1), Jump('self_inflicted')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Healing{/size}') action [SetVariable('sicount', 1), Jump('self_inflicted')] at menuback:
                        xalign .5
        if sicount == 1:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('sicount', 2), Jump('self_inflicted')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Healing{/size}') action [SetVariable('sicount', 2), Jump('self_inflicted')] at menuback:
                        xalign .5
        elif sicount == 2:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('sicount', 3), Jump('self_inflicted')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Healing{/size}') action [SetVariable('sicount', 3), Jump('self_inflicted')] at menuback:
                        xalign .5
        if sicount == 2:
            button xsize 256:
                vbox xalign .5 :
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('sigiveup', 1), Jump('self_inflicted')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Onlooking{/size}') action [SetVariable('sigiveup', 1), Jump('self_inflicted')] at menuback:
                        xalign .5
        else:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('sigiveup', -1), Jump('self_inflicted')] at menuback:
                        xalign 0.5
                    textbutton ('{size=[gui.interface_text_size]}Onlooking{/size}') action [SetVariable('sigiveup', -1), Jump('self_inflicted')] at menuback:
                        xalign .5
    if sicount == 0:
        key 'pad_leftx_neg' action [SetVariable('sicount', 1), Jump('self_inflicted')]
        key 'K_LEFT' action [SetVariable('sicount', 1), Jump('self_inflicted')]
    if sicount == 1:
        key 'pad_leftx_neg' action [SetVariable('sicount', 2), Jump('self_inflicted')]
        key 'K_LEFT' action [SetVariable('sicount', 2), Jump('self_inflicted')]
    elif sicount == 2:
        key 'pad_leftx_neg' action [SetVariable('sicount', 3), Jump('self_inflicted')]
        key 'K_LEFT' action [SetVariable('sicount', 3), Jump('self_inflicted')]
    if sicount == 2:
        key 'pad_leftx_pos' action [SetVariable('sigiveup', 1), Jump('self_inflicted')]
        key 'K_RIGHT' action [SetVariable('sigiveup', 1), Jump('self_inflicted')]
    else:
        key 'pad_leftx_pos' action [SetVariable('sigiveup', -1), Jump('self_inflicted')]
        key 'K_RIGHT' action [SetVariable('sigiveup', -1), Jump('self_inflicted')]
screen bridge():
    tag menu
    if go == 0:
        add 'bridge' at bridge_left
    else:
        add 'bridge' at bridge_right
    if go == 0:
        add 'girl_walk_flip' xalign .5 yalign .5
        add 'bridge_handrail' at bridge_left ypos .3365
    else:
        add 'girl_walk' xalign .5 yalign .5
        add 'bridge_handrail' at bridge_right ypos .3365
    add 'bridge_light' xalign .5 yalign .35
    add 'night'
screen bridge_control():
    add 'dialoguer' ypos .649
    style_prefix "quick"
    hbox xalign .5 yalign .99 spacing 250:
        if gocount == -2:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 0), SetVariable('gocount', -3), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Back home{/size}') action [SetVariable('go', 0), SetVariable('gocount', -3), Jump('bridge_control')] at menuback:
                        xalign .5
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Road not taken{/size}') action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')] at menuback:
                        xalign .5
        elif gocount == -1:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 0), SetVariable('gocount', -2), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Back home{/size}') action [SetVariable('go', 0), SetVariable('gocount', -2), Jump('bridge_control')] at menuback:
                        xalign .5
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Road not taken{/size}') action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')] at menuback:
                        xalign .5
        elif gocount == 0:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 0), SetVariable('gocount', -1), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Back home{/size}') action [SetVariable('go', 0), SetVariable('gocount', -1), Jump('bridge_control')] at menuback:
                        xalign .5
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Road not taken{/size}') action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')] at menuback:
                        xalign .5
        elif gocount == 1 or gocount == -4:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 0), SetVariable('gocount', -1), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Back home{/size}') action [SetVariable('go', 0), SetVariable('gocount', -1), Jump('bridge_control')] at menuback:
                        xalign .5
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 1), SetVariable('gocount', 2), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Road not taken{/size}') action [SetVariable('go', 1), SetVariable('gocount', 2), Jump('bridge_control')] at menuback:
                        xalign .5
        elif gocount == 2 or gocount == -5:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 0), SetVariable('gocount', -4), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Back home{/size}') action [SetVariable('go', 0), SetVariable('gocount', -4), Jump('bridge_control')] at menuback:
                        xalign .5
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 1), SetVariable('gocount', 3), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Road not taken{/size}') action [SetVariable('go', 1), SetVariable('gocount', 3), Jump('bridge_control')] at menuback:
                        xalign .5
        elif gocount == 3 or gocount == -6:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 0), SetVariable('gocount', -5), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Back home{/size}') action [SetVariable('go', 0), SetVariable('gocount', -5), Jump('bridge_control')] at menuback:
                        xalign .5
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 1), SetVariable('gocount', 4), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Road not taken{/size}') action [SetVariable('go', 1), SetVariable('gocount', 4), Jump('bridge_control')] at menuback:
                        xalign .5
        elif gocount == 4 or gocount == -7:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 0), SetVariable('gocount', -6), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Back home{/size}') action [SetVariable('go', 0), SetVariable('gocount', -6), Jump('bridge_control')] at menuback:
                        xalign .5
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 1), SetVariable('gocount', 5), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Road not taken{/size}') action [SetVariable('go', 1), SetVariable('gocount', 5), Jump('bridge_control')] at menuback:
                        xalign .5
        elif gocount == 5:
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 0), SetVariable('gocount', -7), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Back home{/size}') action [SetVariable('go', 0), SetVariable('gocount', -7), Jump('bridge_control')] at menuback:
                        xalign .5
            button xsize 256:
                vbox xalign .5:
                    textbutton ('{font=[gui.fontawesome]}{size=192}{/size}{/font}') action [SetVariable('go', 1), SetVariable('gocount', 6), Jump('bridge_control')] at menuback:
                        xalign .5
                    textbutton ('{size=[gui.interface_text_size]}Road not taken{/size}') action [SetVariable('go', 1), SetVariable('gocount', 6), Jump('bridge_control')] at menuback:
                        xalign .5
    if gocount == -2:
        key 'pad_leftx_neg' action [SetVariable('go', 0), SetVariable('gocount', -3), Jump('bridge_control')]
        key 'pad_leftx_pos' action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')]
        key 'K_LEFT' action [SetVariable('go', 0), SetVariable('gocount', -3), Jump('bridge_control')]
        key 'K_RIGHT' action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')]
    elif gocount == -1:
        key 'pad_leftx_neg' action [SetVariable('go', 0), SetVariable('gocount', -2), Jump('bridge_control')]
        key 'pad_leftx_pos' action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')]
        key 'K_LEFT' action [SetVariable('go', 0), SetVariable('gocount', -2), Jump('bridge_control')]
        key 'K_RIGHT' action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')]
    elif gocount == 0:
        key 'pad_leftx_neg' action [SetVariable('go', 0), SetVariable('gocount', -1), Jump('bridge_control')]
        key 'pad_leftx_pos' action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')]
        key 'K_LEFT' action [SetVariable('go', 0), SetVariable('gocount', -1), Jump('bridge_control')]
        key 'K_RIGHT' action [SetVariable('go', 1), SetVariable('gocount', 1), Jump('bridge_control')]
    elif gocount == 1 or gocount == -4:
        key 'pad_leftx_neg' action [SetVariable('go', 1), SetVariable('go', 0), SetVariable('gocount', -1), Jump('bridge_control')]
        key 'pad_leftx_pos' action [SetVariable('gocount', 2), Jump('bridge_control')]
        key 'K_LEFT' action [SetVariable('go', 0), SetVariable('gocount', -1), Jump('bridge_control')]
        key 'K_RIGHT' action [SetVariable('go', 1), SetVariable('gocount', 2), Jump('bridge_control')]
    elif gocount == 2 or gocount == -5:
        key 'pad_leftx_neg' action [SetVariable('go', 0), SetVariable('gocount', -4), Jump('bridge_control')]
        key 'pad_leftx_pos' action [SetVariable('go', 1), SetVariable('gocount', 3), Jump('bridge_control')]
        key 'K_LEFT' action [SetVariable('go', 0), SetVariable('gocount', -4), Jump('bridge_control')]
        key 'K_RIGHT' action [SetVariable('go', 1), SetVariable('gocount', 3), Jump('bridge_control')]
    elif gocount == 3 or gocount == -6:
        key 'pad_leftx_neg' action [SetVariable('go', 0), SetVariable('gocount', -5), Jump('bridge_control')]
        key 'pad_leftx_pos' action [SetVariable('go', 1), SetVariable('gocount', 4), Jump('bridge_control')]
        key 'K_LEFT' action [SetVariable('go', 0), SetVariable('gocount', -5), Jump('bridge_control')]
        key 'K_RIGHT' action [SetVariable('go', 1), SetVariable('gocount', 4), Jump('bridge_control')]
    elif gocount == 4 or gocount == -7:
        key 'pad_leftx_neg' action [SetVariable('go', 0), SetVariable('gocount', -6), Jump('bridge_control')]
        key 'pad_leftx_pos' action [SetVariable('go', 1), SetVariable('gocount', 5), Jump('bridge_control')]
        key 'K_LEFT' action [SetVariable('go', 0), SetVariable('gocount', -6), Jump('bridge_control')]
        key 'K_RIGHT' action [SetVariable('go', 1), SetVariable('gocount', 5), Jump('bridge_control')]
    elif gocount == 5:
        key 'pad_leftx_neg' action [SetVariable('go', 0), SetVariable('gocount', -7), Jump('bridge_control')]
        key 'pad_leftx_pos' action [SetVariable('go', 1), SetVariable('gocount', 6), Jump('bridge_control')]
        key 'K_LEFT' action [SetVariable('go', 0), SetVariable('gocount', -7), Jump('bridge_control')]
        key 'K_RIGHT' action [SetVariable('go', 1), SetVariable('gocount', 6), Jump('bridge_control')]
screen wallet():
    hbox xpos .6 ypos .65:
        imagebutton idle 'wallet' hover 'wallet' action [SetVariable('wallet', 1), Hide('wallet')]
    key 'pad_a_press' action [SetVariable('wallet', 1), Hide('wallet')]
    key 'K_o' action [SetVariable('wallet', 1), Hide('wallet')]
    if persistent.blind is True:
        key 'pad_leftx_neg' action [SetVariable('wallet', 1), Hide('wallet')]
        key 'K_LEFT' action [SetVariable('wallet', 1), Hide('wallet')]
        key 'pad_leftx_pos' action Return()
        key 'K_RIGHT' action Return()
    if persistent.controllers is not None:
        use a_press
screen anxiety():
    hbox xpos .459 ypos .87:
        imagebutton idle 'nebulizer' hover 'nebulizer' action Return()
    key 'pad_a_press' action Return()
    key 'K_o' action Return()
    if persistent.controllers is not None:
        use a_press
screen obdrawer():
    hbox xpos .1 ypos .74:
        if persistent.obdrawer is None:
            button background '#f7f7f7' xsize 680 ysize 282 action [SetField(persistent, 'obdrawer', True), Return()] at obalpha
            key 'pad_a_press' action [SetField(persistent, 'obdrawer', True), Return()]
            key 'K_o' action [SetField(persistent, 'obdrawer', True), Return()]
        else:
            button background '#f7f7f7' xsize 680 ysize 282 action Return() at obalpha
            key 'pad_a_press' action Return()
            key 'K_o' action Return()
    if persistent.controllers is not None:
        use a_press
screen holder():
    hbox ypos .743:
        imagebutton idle 'holder' hover 'holder' action Return()
    key 'pad_a_press' action Return()
    key 'K_o' action Return()
    if persistent.controllers is not None:
        use a_press
screen a_press():
    hbox xalign .99 yalign .99:
        add "gui/controllers/[persistent.controllers]/button_a.webp"
screen teddy():
    hbox xpos .53 ypos .53:
        imagebutton idle 'teddy' hover 'teddy' action [Hide('teddy'), Jump('teddy')]
    key 'pad_a_press' action [Hide('teddy'), Jump('teddy')]
    key 'K_o' action [Hide('teddy'), Jump('teddy')]
    if persistent.controllers is not None:
        use a_press
screen key_screen():
    if persistent.blind is True:
        key 'K_UP' action MainMenu()
        key 'K_DOWN' action QuickSave()
        key 'pad_lefty_neg' action MainMenu()
        key 'pad_lefty_pos' action QuickSave()
    else:
        if _preferences.afm_enable is True:
            key 'K_p' action [SetField(_preferences, 'afm_enable', False)]
            key 'pad_x_press' action [SetField(_preferences, 'afm_enable', False)]
        else:
            key 'K_p' action [SetField(_preferences, 'afm_enable', True), SetField(_preferences, 'afm_after_click', True)]
            key 'pad_x_press' action [SetField(_preferences, 'afm_enable', True), SetField(_preferences, 'afm_after_click', True)]
        key 'K_a' action [SetField(persistent, 'archives', True), ShowMenu('archives')]
        key 'pad_b_press' action [SetField(persistent, 'archives', True), ShowMenu('archives')]
        key 'K_c' action ShowMenu('preferences')
        key 'pad_y_press' action ShowMenu('preferences')
        key 'K_b' action ShowMenu('save')
        key 'K_q' action Quit()
screen part_clear():
    tag menu
    style_prefix "part_clear"
    use game_menu(_("{font=[gui.fontawesome]}{/font} Unlocked"), scroll="viewport"):
        vbox:
            if gp == 1:
                label _("{font=[gui.fontawesome]}{/font} Characters")
                hbox:
                    if progress == 1:
                        imagebutton idle 'arc_char_01' action [SetScreenVariable("char", "gayeon"), Show('characters')]
                        imagebutton idle 'arc_char_03' action [SetScreenVariable("char", "hyena"), Show('characters')]
                    if progress == 2:
                        imagebutton idle 'arc_char_06' action [SetScreenVariable("char", "interviewer"), Show('characters')]
                    if progress == 3:
                        imagebutton idle 'arc_char_02' action [SetScreenVariable("char", "yunwoo"), Show('characters')]
                    if progress == 4:
                        imagebutton idle 'arc_char_04' action [SetScreenVariable("char", "angel"), Show('characters')]
                    if progress ==12:
                        imagebutton idle 'arc_char_07' action [SetScreenVariable("char", "doctor"), Show('characters')]
                    if progress == 15 and persistent.obdrawer == True:
                        imagebutton idle 'arc_char_07_e' action [SetScreenVariable("char", "doctor"), Show('characters')]
                    if progress == 17:
                        imagebutton idle 'arc_char_05' action [SetScreenVariable("char", "taejin"), Show('characters')]
                    if progress == 20 and not sigiveup <= -1:
                        imagebutton idle 'arc_char_04_q' action [SetScreenVariable("char", "angel"), Show('characters')]
                    if progress == 25:
                        imagebutton idle 'arc_char_04_e' action [SetScreenVariable("char", "angel"), Show('characters')]
                        imagebutton idle 'arc_char_06_e' action [SetScreenVariable("char", "interviewer"), Show('characters')]
                null height (4 * gui.pref_spacing)
            if gc == 1:
                label _("{font=[gui.fontawesome]}{/font} Concept")
                hbox:
                    if progress == 2:
                        imagebutton idle 'arc_con_01' action [SetScreenVariable("concept", "concept01"), Show('concept')]
                    if progress == 7:
                        imagebutton idle 'arc_con_05' action [SetScreenVariable("concept", "concept05"), Show('concept')]
                    if progress == 11:
                        imagebutton idle 'arc_con_02' action [SetScreenVariable("concept", "concept02"), Show('concept')]
                        imagebutton idle 'arc_con_07' action [SetScreenVariable("concept", "concept07"), Show('concept')]
                    if progress == 14:
                        imagebutton idle 'arc_con_04' action [SetScreenVariable("concept", "concept04"), Show('concept')]
                    if progress == 20 and not sigiveup <= -1:
                        imagebutton idle 'arc_con_03' action [SetScreenVariable("concept", "concept03"), Show('concept')]
                    if progress == 21 and not sigiveup <= -1:
                        imagebutton idle 'arc_con_06' action [SetScreenVariable("concept", "concept06"), Show('concept')]
                    if progress == 23 and wallet == 0:
                        imagebutton idle 'arc_con_08' action [SetScreenVariable("concept", "concept08"), Show('concept')]
                    if progress == 25:
                        imagebutton idle 'arc_con_10' action [SetScreenVariable("concept", "concept10"), Show('concept')]
                        imagebutton idle 'arc_con_11' action [SetScreenVariable("concept", "concept11"), Show('concept')]
                        imagebutton idle 'arc_con_12' action [SetScreenVariable("concept", "concept12"), Show('concept')]
                null height (4 * gui.pref_spacing)
            if gd == 1:
                label _("{font=[gui.fontawesome]}{/font} Diary")
                hbox:
                    if progress == 15:
                        vbox:
                            hbox:
                                imagebutton idle 'arc_diary_01' action [SetScreenVariable("diary", "diary01"), Show('diary')]
                                imagebutton idle 'arc_diary_02' action [SetScreenVariable("diary", "diary02"), Show('diary')]
                                imagebutton idle 'arc_diary_03' action [SetScreenVariable("diary", "diary03"), Show('diary')]
                                imagebutton idle 'arc_diary_04' action [SetScreenVariable("diary", "diary04"), Show('diary')]
                            hbox:
                                imagebutton idle 'arc_diary_05' action [SetScreenVariable("diary", "diary05"), Show('diary')]
                                imagebutton idle 'arc_diary_06' action [SetScreenVariable("diary", "diary06"), Show('diary')]
                                imagebutton idle 'arc_diary_07' action [SetScreenVariable("diary", "diary07"), Show('diary')]
                                imagebutton idle 'arc_diary_08' action [SetScreenVariable("diary", "diary08"), Show('diary')]
                            hbox:
                                imagebutton idle 'arc_diary_09' action [SetScreenVariable("diary", "diary09"), Show('diary')]
                                imagebutton idle 'arc_diary_10' action [SetScreenVariable("diary", "diary10"), Show('diary')]
                                imagebutton idle 'arc_diary_11' action [SetScreenVariable("diary", "diary11"), Show('diary')]
                                imagebutton idle 'arc_diary_12' action [SetScreenVariable("diary", "diary12"), Show('diary')]
                            hbox:
                                imagebutton idle 'arc_diary_13' action [SetScreenVariable("diary", "diary13"), Show('diary')]
                                imagebutton idle 'arc_diary_14' action [SetScreenVariable("diary", "diary14"), Show('diary')]
                                imagebutton idle 'arc_diary_15' action [SetScreenVariable("diary", "diary15"), Show('diary')]
                    if progress == 17:
                        imagebutton idle 'arc_diary_16' action [SetScreenVariable("diary", "diary16"), Show('diary')]
                null height (4 * gui.pref_spacing)
            if gg == 1:
                label _("{font=[gui.fontawesome]}{/font} Gallery")
                hbox:
                    if progress == 2:
                        imagebutton idle 'arc_gall_01' action g.Action('frustration')
                        imagebutton idle 'arc_gall_02' action g.Action('vomiting')
                        imagebutton idle 'arc_gall_03' action g.Action('pusillanimous')
                    if progress == 4:
                        imagebutton idle 'arc_gall_04' action g.Action('that day we')
                    if progress == 6:
                        imagebutton idle 'arc_gall_05' action g.Action('fate')
                        imagebutton idle 'arc_gall_06' action g.Action('alleyway')
                        imagebutton idle 'arc_gall_07' action g.Action('moonlight')
                    if progress == 9:
                        imagebutton idle 'arc_gall_08' action g.Action('drunken')
                        imagebutton idle 'arc_gall_09' action g.Action('eternal happiness')
                    if progress == 10:
                        imagebutton idle 'arc_gall_10' action g.Action('despair')
                        imagebutton idle 'arc_gall_11' action g.Action('lean_gall')
                        imagebutton idle 'arc_gall_12' action g.Action('distortion')
                    if progress == 11:
                        imagebutton idle 'arc_gall_13' action g.Action('imf crisis')
                        imagebutton idle 'arc_gall_14' action g.Action('newspaper delivery')
                        imagebutton idle 'arc_gall_15' action g.Action('serving')
                    if progress == 13:
                        imagebutton idle 'arc_gall_16' action g.Action('kiss me')
                    if progress == 14:
                        imagebutton idle 'arc_gall_17' action g.Action('video_gall')
                    if progress == 15:
                        imagebutton idle 'arc_gall_18' action g.Action('self_gall')
                        if sigiveup <= -1:
                            imagebutton idle 'arc_gall_25' action g.Action('smoking')
                    if progress == 16:
                        imagebutton idle 'arc_gall_19' action g.Action('rip')
                    if progress == 17:
                        vbox:
                            hbox:
                                imagebutton idle 'arc_gall_20' action g.Action('masturbation')
                                imagebutton idle 'arc_gall_21' action g.Action('deep kiss')
                                imagebutton idle 'arc_gall_22' action g.Action('caress')
                                imagebutton idle 'arc_gall_23' action g.Action('fellatio')
                            hbox:
                                imagebutton idle 'arc_gall_24' action g.Action('riding')
                    if progress == 20 and not smoke == 1:
                        imagebutton idle 'arc_gall_25' action g.Action('smoking')
                    if progress == 21 and not sigiveup <= -1:
                        imagebutton idle 'arc_gall_26' action g.Action('bridge')
                    if progress == 22 and persistent.part22 is True:
                        imagebutton idle 'arc_gall_27' action g.Action('edge')
                    if progress == 23 and wallet == 0:
                        imagebutton idle 'arc_gall_28' action g.Action('corruption')
                    if progress == 24:
                        imagebutton idle 'arc_gall_29' action g.Action('doa')
                        imagebutton idle 'arc_gall_30' action g.Action('doa0')
                    if progress == 25:
                        imagebutton idle 'arc_gall_31' action g.Action('growing')
                        imagebutton idle 'arc_gall_32' action g.Action('nte')
                null height (4 * gui.pref_spacing)
            if gm == 1:
                label _("{font=[gui.fontawesome]}{/font} Music")
                hbox:
                    if progress == 1:
                        textbutton "Track 2. Sigh day" action mr.Play("bgm/Sigh day.opus")
                    if progress == 2:
                        textbutton "Track 3. Mare tranquillitatis" action mr.Play("bgm/Mare tranquillitatis.opus")
                        textbutton "Track 7. Unknown mist" action mr.Play("bgm/Unknown mist.opus")
                    if progress == 3:
                        textbutton "Track 4. CCCanon" action mr.Play("bgm/CCCanon.opus")
                    if progress == 4:
                        textbutton "Track 5. Let's game" action mr.Play("bgm/Let's game.opus")
                    if progress == 6:
                        textbutton "Track 6. Peace" action mr.Play("bgm/Peace.opus")
                    if progress == 8:
                        textbutton "Track 8. Lush garden" action mr.Play("bgm/Lush garden.opus")
                        textbutton "Track 9. Jormungandr" action mr.Play("bgm/Jormungandr.opus")
                    if progress == 9:
                        textbutton "Track 10. Nyx" action mr.Play("bgm/Nyx.opus")
                    if progress == 17:
                        textbutton "Track 11. Summit showdown" action mr.Play("bgm/Summit showdown.opus")
                    if progress == 20:
                        textbutton "Track 13. Sea of nectar" action mr.Play("bgm/Sea of nectar.opus")
                    if progress == 25:
                        textbutton "Track 12. Love song" action mr.Play("bgm/Love song.opus")
                null height (4 * gui.pref_spacing)
            if gr == 1:
                label _("{font=[gui.fontawesome]}{/font} Replay")
                hbox:
                    if progress == 1:
                        add 'part_01_sepia'
                    if progress == 2:
                        add 'part_02_sepia'
                    if progress == 3:
                        add 'part_03_sepia'
                    if progress == 4:
                        add 'part_04_sepia'
                    if progress == 6:
                        add 'part_05_sepia'
                    if progress == 7:
                        add 'part_07_sepia'
                    if progress == 8:
                        add 'part_08_sepia'
                    if progress == 9:
                        add 'part_09_sepia'
                    if progress == 10:
                        add 'part_10_sepia'
                    if progress == 11:
                        add 'part_11_sepia'
                    if progress == 12:
                        add 'part_12_sepia'
                    if progress == 13:
                        add 'part_13_sepia'
                    if progress == 14:
                        add 'part_14_sepia'
                    if progress == 17:
                        add 'part_17_sepia'
                    if progress == 20:
                        if not sigiveup <= -1:
                            add 'part_18_sepia'
                            add 'part_19_sepia'
                            add 'part_20_sepia'
                    if progress == 22 and persistent.part22 is True:
                        add 'part_22_sepia'
                    if progress == 24:
                        add 'part_24_sepia'
                    if progress == 25:
                        add 'part_25_sepia'
                null height (4 * gui.pref_spacing)
            vbox:
                label _("{font=[gui.fontawesome]}{/font} Total")
                if progress == 1:
                    text _("{font=[gui.fontawesome]}{/font} Characters +2")
                    text _("{font=[gui.fontawesome]}{/font} Music +1")
                if progress == 2:
                    text _("{font=[gui.fontawesome]}{/font} Characters +1")
                    text _("{font=[gui.fontawesome]}{/font} Concept +1")
                    text _("{font=[gui.fontawesome]}{/font} Gallery +3")
                    text _("{font=[gui.fontawesome]}{/font} Music +2")
                if progress == 3:
                    text _("{font=[gui.fontawesome]}{/font} Characters +1")
                    text _("{font=[gui.fontawesome]}{/font} Music +1")
                if progress == 4:
                    text _("{font=[gui.fontawesome]}{/font} Characters +1")
                    text _("{font=[gui.fontawesome]}{/font} Gallery +1")
                    text _("{font=[gui.fontawesome]}{/font} Music +1")
                if progress == 6:
                    text _("{font=[gui.fontawesome]}{/font} Gallery +3")
                    text _("{font=[gui.fontawesome]}{/font} Music +1")
                if progress == 7:
                    text _("{font=[gui.fontawesome]}{/font} Concept +1")
                if progress == 8:
                    text _("{font=[gui.fontawesome]}{/font} Music +2")
                if progress == 9:
                    text _("{font=[gui.fontawesome]}{/font} Gallery +2")
                    text _("{font=[gui.fontawesome]}{/font} Music +1")
                if progress == 10:
                    text _("{font=[gui.fontawesome]}{/font} Gallery +3")
                if progress == 11:
                    text _("{font=[gui.fontawesome]}{/font} Concept +2")
                    text _("{font=[gui.fontawesome]}{/font} Gallery +3")
                if progress == 12:
                    text _("{font=[gui.fontawesome]}{/font} Characters +1")
                if progress == 13:
                    text _("{font=[gui.fontawesome]}{/font} Gallery +1")
                if progress == 14:
                    text _("{font=[gui.fontawesome]}{/font} Concept +1")
                    text _("{font=[gui.fontawesome]}{/font} Gallery +1")
                if progress == 15:
                    if persistent.obdrawer == True:
                        text _("{font=[gui.fontawesome]}{/font} Characters +1")
                        text _("{font=[gui.fontawesome]}{/font} Diary +15")
                    if sigiveup <= -1:
                        text _("{font=[gui.fontawesome]}{/font} Gallery +2")
                    else:
                        text _("{font=[gui.fontawesome]}{/font} Gallery +1")
                if progress == 16:
                    text _("{font=[gui.fontawesome]}{/font} Gallery +1")
                if progress == 17:
                    text _("{font=[gui.fontawesome]}{/font} Characters +1")
                    if persistent.obdrawer == True:
                        text _("{font=[gui.fontawesome]}{/font} Diary +1")
                    text _("{font=[gui.fontawesome]}{/font} Gallery +5")
                    text _("{font=[gui.fontawesome]}{/font} Music +1")
                if progress == 20:
                    if not sigiveup <= -1:
                        text _("{font=[gui.fontawesome]}{/font} Characters +1")
                        text _("{font=[gui.fontawesome]}{/font} Concept +1")
                    if not smoke == 1:
                        text _("{font=[gui.fontawesome]}{/font} Gallery +1")
                    text _("{font=[gui.fontawesome]}{/font} Music +1")
                    if not sigiveup <= -1:
                        text _("{font=[gui.fontawesome]}{/font} Replay +3")
                if progress == 21 and sigiveup <= -1 or progress == 23:
                    if progress == 23 and wallet == 1:
                        pass
                    else:
                        text _("{font=[gui.fontawesome]}{/font} Concept +1")
                        text _("{font=[gui.fontawesome]}{/font} Gallery +1")
                if progress == 22 and persistent.part22 is True:
                    text _("{font=[gui.fontawesome]}{/font} Gallery +1")
                if progress == 24:
                    text _("{font=[gui.fontawesome]}{/font} Gallery +2")
                if progress == 25:
                    text _("{font=[gui.fontawesome]}{/font} Characters +2")
                    text _("{font=[gui.fontawesome]}{/font} Gallery +2")
                    text _("{font=[gui.fontawesome]}{/font} Music +1")
                if not progress == 15 and not progress == 16 and not progress == 20 and not progress == 21 and not progress == 23:
                    text _("{font=[gui.fontawesome]}{/font} Replay +1")
style part_clear_button_text is part_clear_text
style part_clear_text is gui_text:
    color gui.accent_color
screen archives():
    tag menu
    modal True
    $ cols = 2
    if persistent.dying is True:
        $ arc_diary = 16
    elif persistent.obdrawer is True:
        $ arc_diary = 15
    use game_menu(_("{font=[gui.fontawesome]}{/font} Archives"), scroll="viewport"):
        hbox:
            style_prefix "slider"
            vbox:
                label _("{font=[gui.fontawesome]}{/font} Characters")
                bar value persistent.char range 12
                label _("{font=[gui.fontawesome]}{/font} Diary")
                bar value arc_diary range 16
                label _("{font=[gui.fontawesome]}{/font} Music")
                bar value persistent.bgm range 13
            vbox:
                label _("{font=[gui.fontawesome]}{/font} Concept")
                bar value persistent.con range 12
                label _("{font=[gui.fontawesome]}{/font} Gallery")
                bar value persistent.gall range 32
                label _("{font=[gui.fontawesome]}{/font} Replay")
                bar value persistent.replay range 24
        null height (4 * gui.pref_spacing)
        label _("{font=[gui.fontawesome]}{/font} Medals")
        hbox spacing 20:
            if persistent.introduction is True:
                imagebutton idle '1m_gold' hover '1m_gold' action Start('esteregg_01') at menuback
            elif achievement.has('KNDW_DEMO'):
                imagebutton idle '1m_silver' hover '1m_silver' action Start('esteregg_01') at menuback
            elif persistent.part06 is True:
                add '1m_bronze'
            elif persistent.part03 is True:
                add '1m_copper'
            if persistent.development is True:
                imagebutton idle '2m_gold' hover '2m_gold' action Start('esteregg_02') at menuback
            elif achievement.has('KNDW_VIDEO'):
                imagebutton idle '2m_silver' hover '2m_silver' action Start('esteregg_02') at menuback
            elif persistent.part12 is True:
                add '2m_bronze'
            elif persistent.part10 is True:
                add '2m_copper'
            if persistent.turn is True:
                imagebutton idle '3m_gold' hover '3m_gold' action Start('esteregg_03') at menuback
            elif achievement.has('KNDW_MURDERER'):
                imagebutton idle '3m_silver' hover '3m_silver' action Start('esteregg_03') at menuback
            elif achievement.has('KNDW_DYING_MESSAGE'):
                add '3m_bronze'
            elif persistent.part15 is True:
                add '3m_copper'
            if persistent.conclusion is True:
                imagebutton idle '4m_gold' hover '4m_gold' action Start('esteregg_04') at menuback
            elif achievement.has('KNDW_SPONSOR'):
                imagebutton idle '4m_silver' hover '4m_silver' action Start('esteregg_04') at menuback
            elif achievement.has('KNDW_VOTERS'):
                add '4m_bronze'
            elif achievement.has('KNDW_MASTER'):
                add '4m_copper'
        null height (gui.pref_spacing)
        hbox spacing 20:
            if persistent.esteregg is True:
                imagebutton idle '5m_gold' hover '5m_gold' action Start('wimcj_001') at menuback
            elif achievement.has('KNDW_SPONSOR'):
                imagebutton idle '5m_silver' hover '5m_silver' action Start('wimcj_001') at menuback
            elif persistent.teddy is True:
                add '5m_bronze'
            elif persistent.dw2017 is True:
                add '5m_copper'
            if persistent.mahalath is True:
                imagebutton idle '6m_gold' hover '6m_gold' action Start('leannoth') at menuback
            elif persistent.esteregg is True:
                imagebutton idle '6m_silver' hover '6m_silver' action Start('leannoth') at menuback
            elif achievement.has('KNDW_SPONSOR'):
                add '6m_bronze'
            elif achievement.has('KNDW_MASTER'):
                add '6m_copper'
            if achievement.has('KNDW_MOD_PLAYER'):
                add '7m_gold'
            elif achievement.has('KNDW_DETECTIVE'):
                add '7m_silver'
            elif persistent.esteregg is True:
                add '7m_bronze'
            elif persistent.introduction is True and persistent.development is True and persistent.turn is True and persistent.conclusion is True:
                add '7m_copper'
            if achievement.has('KNDW_CREATOR') and achievement.has('KNDW_MOD_PLAYER') and achievement.has('KNDW_DETECTIVE'):
                add '8m_gold'
            elif achievement.has('KNDW_CREATOR'):
                add '8m_silver'
            elif achievement.has('KNDW_MOD_PLAYER'):
                add '8m_bronze'
            elif achievement.has('KNDW_SPONSOR'):
                add '8m_copper'
    key 'K_a' action [SetField(persistent, 'archives', None), Return()]
    key 'pad_b_press' action [SetField(persistent, 'archives', None), Return()]
screen blind_arc():
    tag menu
    add gui.main_menu_background
    vbox spacing 20:
        if blind_set == 1:
            default char = "gayeon"
            style_prefix "characters"
            if char == "gayeon":
                use gayeon
            elif char == "yunwoo":
                use yunwoo
            elif char == "hyena":
                use hyena
            elif char == "angel":
                use angel
            elif char == "taejin":
                use taejin
            elif char == "interviewer":
                use interviewer
            elif char == "doctor":
                use doctor
        elif blind_set == 2:
            default concept = "concept09"
            style_prefix "concept"
            if concept == "concept01":
                use concept01
            if concept == "concept02":
                use concept02
            if concept == "concept03":
                use concept03
            if concept == "concept04":
                use concept04
            if concept == "concept05":
                use concept05
            if concept == "concept06":
                use concept06
            if concept == "concept07":
                use concept07
            if concept == "concept08":
                use concept08
            if concept == "concept09":
                use concept09
            if concept == "concept10":
                use concept10
            if concept == "concept11":
                use concept11
            if concept == "concept12":
                use concept12
            if concept == "concept07" or concept == "concept08" or concept == "concept09" or concept == "concept10" or concept == "concept12":
                pass
            else:
                text _("Lee Yunseok -YGGDRASIL STUDIO")
        elif blind_set == 0:
            default diary = "diary01"
            style_prefix "concept"
            if persistent.obdrawer is None:
                label _("{font=[gui.fontawesome]}{/font} Find the diary in the room.")
            else:
                if diary == "diary01":
                    use diary01
                if diary == "diary02":
                    use diary02
                if diary == "diary03":
                    use diary03
                if diary == "diary04":
                    use diary04
                if diary == "diary05":
                    use diary05
                if diary == "diary06":
                    use diary06
                if diary == "diary07":
                    use diary07
                if diary == "diary08":
                    use diary08
                if diary == "diary09":
                    use diary09
                if diary == "diary10":
                    use diary10
                if diary == "diary11":
                    use diary11
                if diary == "diary12":
                    use diary12
                if diary == "diary13":
                    use diary13
                if diary == "diary14":
                    use diary14
                if diary == "diary15":
                    use diary15
                if diary == "diary16":
                    use diary16
        label _("Left arrow key: Previous, Right arrow key: Next.")
    key "game_menu" action [SetVariable('blind_set', None), Return()]
    key 'pad_b_press' action [SetVariable('blind_set', None), Return()]
    key 'K_UP' action [SetVariable('blind_set', None), Return()]
    key 'pad_lefty_neg' action [SetVariable('blind_set', None), Return()]
screen characters():
    tag menu
    default char = "gayeon"
    use game_menu(_("{font=[gui.fontawesome]}{/font} Characters"), scroll=If(renpy.variant("small"), true="viewport", false=None)):
        style_prefix "characters"
        vbox:
            hbox:
                textbutton _("Ga-yeon") action SetScreenVariable("char", "gayeon")
                if persistent.yunwoo is True:
                    textbutton _("Yunwoo") action SetScreenVariable("char", "yunwoo")
                if persistent.hyena is True:
                    textbutton _("Hye-na") action SetScreenVariable("char", "hyena")
                if persistent.eangel is True:
                    textbutton _("Seol-ah") action SetScreenVariable("char", "angel")
                elif persistent.staffq is True:
                    textbutton _("???") action SetScreenVariable("char", "angel")
                elif persistent.staff is True:
                    textbutton _("Staff") action SetScreenVariable("char", "angel")
                elif persistent.angel is True:
                    textbutton _("Clerk") action SetScreenVariable("char", "angel")
                if persistent.taejin is True:
                    textbutton _("Taejin") action SetScreenVariable("char", "taejin")
                if persistent.einterviewer is True:
                    textbutton _("Misun") action SetScreenVariable("char", "interviewer")
                elif persistent.interviewer is True:
                    textbutton _("Interviewer") action SetScreenVariable("char", "interviewer")
                if persistent.obdrawer is True:
                    textbutton _("Hyeongsik") action SetScreenVariable("char", "doctor")
                elif persistent.doctor is True:
                    textbutton _("Doctor") action SetScreenVariable("char", "doctor")
            if char == "gayeon":
                use gayeon
            elif char == "yunwoo":
                use yunwoo
            elif char == "hyena":
                use hyena
            elif char == "angel":
                use angel
            elif char == "taejin":
                use taejin
            elif char == "interviewer":
                use interviewer
            elif char == "doctor":
                use doctor
style characters_text is gui_text
style characters_vbox:
    xsize 780 spacing 23
style arc_mobile_text:
    size 42 color gui.interface_text_color
style arc_mobile_vbox is characters_vbox
screen gayeon():
    hbox:
        vbox:
            if renpy.variant("small"):
                style_prefix "arc_mobile"
            label _("{b}Choi Ga-yeon{/b}")
            text _("{b}Birth:{/b} April 19th, 1986")
            text _("{b}Blood Type:{/b} A(RH+)")
            text _("{b}Height / Weight:{/b} 165cm / 48kg")
            text _("{b}BWH:{/b} 81cm / 58cm / 86cm")
            if persistent.ending is True:
                text _("{b}Bio:{/b} Discouraged worker, Temporary absence from Health Administration of Yonsei University")
            else:
                text _("{b}Bio:{/b} Discouraged worker, Temporary absence from Health Administration of ○○ University")
            text _("{b}Certificates:{/b} 1st class Hospital Coordinator, Hospital Administrator")
            text _("{b}Likes:{/b} Bagels, Margherita pizza, Sweet rice bun")
            text _("{b}Dislikes:{/b} Capitalism, Doctors, Members of Parliament")
        if persistent.blind is True:
            key 'pad_leftx_neg' action [SetVariable('blind_set', None), Return()]
            key 'K_LEFT' action [SetVariable('blind_set', None), Return()]
            key 'pad_leftx_pos':
                if persistent.yunwoo is True:
                    action SetScreenVariable("char", "yunwoo")
                elif persistent.hyena is True:
                    action SetScreenVariable("char", "hyena")
            key 'K_RIGHT':
                if persistent.yunwoo is True:
                    action SetScreenVariable("char", "yunwoo")
                elif persistent.hyena is True:
                    action SetScreenVariable("char", "hyena")
        else:
            hbox:
                add 'gb'
screen yunwoo():
    hbox:
        vbox:
            if renpy.variant("small"):
                style_prefix "arc_mobile"
            label _("{b}Kim Yunwoo{/b}")
            text _("{b}Birth:{/b} January 19th, 1986")
            text _("{b}Blood Type:{/b} AB(RH+)")
            text _("{b}Height / Weight:{/b} 172cm / 58kg")
            if persistent.ending is True:
                text _("{b}Bio:{/b} Bassist of The Ghost Crying")
            else:
                text _("{b}Bio:{/b} Bassist of ○○")
            text _("{b}Likes:{/b} Bob Dylan, Choi Ga-yeon, Yu Jaeha")
            text _("{b}Dislikes:{/b} Auditions, Management, Soju")
        if persistent.blind is True:
            key 'pad_leftx_neg' action SetScreenVariable("char", "gayeon")
            key 'K_LEFT' action SetScreenVariable("char", "gayeon")
            key 'pad_leftx_pos' action SetScreenVariable("char", "hyena")
            key 'K_RIGHT' action SetScreenVariable("char", "hyena")
        else:
            hbox:
                add 'y_poker'
screen hyena():
    hbox:
        vbox:
            if renpy.variant("small"):
                style_prefix "arc_mobile"
            label _("{b}Choi Hye-na{/b}")
            text _("{b}Birth:{/b} June 17th, 1989")
            text _("{b}Blood Type:{/b} O(RH+)")
            text _("{b}Height / Weight:{/b} 168cm / 48kg")
            text _("{b}BWH:{/b} 92.5cm / 66cm / 92cm")
            if persistent.ending is True:
                text _("{b}Bio:{/b} Karaoke helper, Graduated in Tourism Food & Beverage of Korea Hotel Technical College")
            else:
                text _("{b}Bio:{/b} Karaoke helper, Graduated in Tourism Food & Beverage of ○○")
            text _("{b}Certificates:{/b} 2nd class Barista")
            text _("{b}Likes:{/b} Money, Photography, Ga-yeon, Drinking")
            text _("{b}Dislikes:{/b} Oryide, Sweet rice bun, Nightclub")
        if persistent.blind is True:
            key 'pad_leftx_neg':
                if persistent.yunwoo is True:
                    action SetScreenVariable("char", "yunwoo")
                else:
                    action SetScreenVariable("char", "gayeon")
            key 'K_LEFT':
                if persistent.yunwoo is True:
                    action SetScreenVariable("char", "yunwoo")
                else:
                    action SetScreenVariable("char", "gayeon")
            key 'pad_leftx_pos':
                if persistent.angel is True:
                    action SetScreenVariable("char", "angel")
                elif persistent.interviewer is True:
                    action SetScreenVariable("char", "interviewer")
            key 'K_RIGHT':
                if persistent.angel is True:
                    action SetScreenVariable("char", "angel")
                elif persistent.interviewer is True:
                    action SetScreenVariable("char", "interviewer")
        else:
            hbox:
                add 'h_smile'
screen angel():
    hbox:
        vbox:
            if renpy.variant("small"):
                style_prefix "arc_mobile"
            if persistent.eangel is True:
                label _("{b}Lee Seol-ah{/b}")
                text _("{b}Birth:{/b} December 7th, 1986")
                text _("{b}Died:{/b} October 3rd, 2006")
                text _("{b}Height / Weight:{/b} 158cm / 55kg")
                text _("{b}BWH:{/b} 89cm / 68.5cm / 85cm")
                text _("{b}Bio:{/b} Maid of Lauah")
                text _("{b}Certificates:{/b} Craftsman Piano Tuner")
                text _("{b}Likes:{/b} Ga-yeon, Herself, Papa, Taejin")
                text _("{b}Dislikes:{/b} Kelial, Mother, Tobacco, Truck")
            elif persistent.staffq is True:
                label "{b}???{/b}"
                text _("{font=[gui.fontawesome]}{/font} The information is unknown at this time.")
            elif persistent.staff is True:
                label _("{b}Staff{/b}")
                text _("{font=[gui.fontawesome]}{/font} The information is unknown at this time.")
            else:
                label _("{b}Clerk{/b}")
                text _("{font=[gui.fontawesome]}{/font} The information is unknown at this time.")
        if persistent.blind is True:
            key 'pad_leftx_neg' action SetScreenVariable("char", "hyena")
            key 'K_LEFT' action SetScreenVariable("char", "hyena")
            key 'pad_leftx_pos':
                if persistent.taejin is True:
                    action SetScreenVariable("char", "taejin")
                else:
                    action SetScreenVariable("char", "interviewer")
            key 'K_RIGHT':
                if persistent.taejin is True:
                    action SetScreenVariable("char", "taejin")
                else:
                    action SetScreenVariable("char", "interviewer")
        else:
            hbox:
                add 'e_poker'
screen taejin():
    hbox:
        vbox:
            if renpy.variant("small"):
                style_prefix "arc_mobile"
            label _("{b}Choi Taejin{/b}")
            text _("{b}Birth:{/b} March 28th, 1986")
            text _("{b}Blood Type:{/b} B(RH+)")
            text _("{b}Height / Weight:{/b} 182cm / 73kg")
            if persistent.ending is True:
                text _("{b}Bio:{/b} Lead Guitarist of The Ghost Crying, Graduated in Seoul Institute of the Arts")
            else:
                text _("{b}Bio:{/b} Lead Guitarist of ○○, Graduated in ○○")
            text _("{b}Certificates:{/b} Bachelor of Arts Degree in Gebrauchsmusik")
            text _("{b}Likes:{/b} Marylin Manson, NIN, Rammstein, Shin Junghyeon,\nShin Haechul")
            text _("{b}Dislikes:{/b} Eggplant, Ginger, Idol")
        if persistent.blind is True:
            key 'pad_leftx_neg' action SetScreenVariable("char", "angel")
            key 'K_LEFT' action SetScreenVariable("char", "angel")
            key 'pad_leftx_pos' action SetScreenVariable("char", "interviewer")
            key 'K_RIGHT' action SetScreenVariable("char", "interviewer")
        else:
            hbox:
                add 'band'
screen interviewer():
    hbox:
        vbox:
            if renpy.variant("small"):
                style_prefix "arc_mobile"
            if persistent.einterviewer is True:
                label _("{b}Park Misun{/b}")
                text _("{b}Birth:{/b} April 28th, 1974")
                text _("{b}Blood Type:{/b} O(RH+)")
                text _("{b}Height / Weight:{/b} 168cm / 47kg")
                text _("{b}BWH:{/b} 90cm / 63.8cm / 89cm")
                if persistent.ending is True:
                    text _("{b}Bio:{/b} Conductor of Business Management in Arno Restaurant franchise, Essayist, Graduated in SNU Business School")
                else:
                    text _("{b}Bio:{/b} Conductor of Business Management in Arno Restaurant franchise")
                text _("{b}Certificates:{/b} Doctor of Business Administration, Advanced level of TEPS, Special level of TESAT, Top level of MK TEST")
                text _("{b}Likes:{/b} Acoustic guitar, Challenge, Taejin, Writing")
                text _("{b}Dislikes:{/b} Electronic products, Game, Mantis, Sloth")
            else:
                label _("{b}Interviewer{/b}")
                text _("{b}Birth:{/b} Top Secret")
                text _("{b}Height / Weight:{/b} Top Secret")
                text _("{b}BWH:{/b} Top Secret")
                text _("{b}Bio:{/b} Conductor of Business Management in ○○")
        if persistent.blind is True:
            key 'pad_leftx_neg':
                if persistent.taejin is True:
                    action SetScreenVariable("char", "taejin")
                elif persistent.angel is True:
                    action SetScreenVariable("char", "angel")
                else:
                    action SetScreenVariable("char", "hyena")
            key 'K_LEFT':
                if persistent.taejin is True:
                    action SetScreenVariable("char", "taejin")
                elif persistent.angel is True:
                    action SetScreenVariable("char", "angel")
                else:
                    action SetScreenVariable("char", "hyena")
            if persistent.doctor is True:
                key 'pad_leftx_pos' action SetScreenVariable("char", "doctor")
                key 'K_RIGHT' action SetScreenVariable("char", "doctor")
        else:
            hbox:
                add 'i_poker'
screen doctor():
    hbox:
        vbox:
            if renpy.variant("small"):
                style_prefix "arc_mobile"
            if persistent.obdrawer is True:
                label _("{b}Park Hyeongsik{/b}")
                text _("{b}Birth:{/b} December 17th, 1979")
                text _("{b}Blood Type:{/b} AB(RH+)")
                text _("{b}Height / Weight:{/b} 172cm / 58kg")
                if persistent.ending is True:
                    text _("{b}Bio:{/b} Physician, Graduated in School of Medicine of Sungkyunkwan University")
                else:
                    text _("{b}Bio:{/b} Physician, Graduated in ○○")
                text _("{b}Certificates:{/b} Medical Licence")
                text _("{b}Likes:{/b} Fame, Money, Power")
                text _("{b}Dislikes:{/b} Capitalism, Members of Parliament, Soju")
            else:
                label _("{b}Doctor{/b}")
                text _("{b}Bio:{/b} Physician")
                text _("{font=[gui.fontawesome]}{/font} The information is unknown at this time.")
        if persistent.blind is True:
            key 'pad_leftx_neg' action SetScreenVariable("char", "interviewer")
            key 'K_LEFT' action SetScreenVariable("char", "interviewer")
            key 'pad_leftx_pos' action [SetVariable('blind_set', None), Return()]
            key 'K_RIGHT' action [SetVariable('blind_set', None), Return()]
        else:
            hbox:
                add 'arc_char_07_bg'
screen concept():
    tag menu
    default concept = "concept00"
    use game_menu(_("{font=[gui.fontawesome]}{/font} Concept"), scroll="viewport"):
        if concept == "concept00":
            grid 4 3 spacing 20 xoffset If(renpy.variant("small"), false=135):
                imagebutton idle 'arc_con_09_gray' hover 'arc_con_09' action SetScreenVariable("concept", "concept09")
                if persistent.con01 is None:
                    add 'con_lock'
                else:
                    imagebutton idle 'arc_con_01_gray' hover 'arc_con_01' action SetScreenVariable("concept", "concept01")
                if persistent.con05 is None:
                    add 'con_lock'
                else:
                    imagebutton idle 'arc_con_05_gray' hover 'arc_con_05' action SetScreenVariable("concept", "concept05")
                if persistent.con02 is None:
                    add 'con_lock'
                else:
                    imagebutton idle 'arc_con_02_gray' hover 'arc_con_02' action SetScreenVariable("concept", "concept02")
                if persistent.con07 is None:
                    add 'con_lock'
                else:
                    imagebutton idle 'arc_con_07_gray' hover 'arc_con_07' action SetScreenVariable("concept", "concept07")
                if persistent.con04 is None:
                    add 'con_lock'
                else:
                    imagebutton idle 'arc_con_04_gray' hover 'arc_con_04' action SetScreenVariable("concept", "concept04")
                if persistent.con03 is None:
                    add 'con_lock'
                else:
                    imagebutton idle 'arc_con_03_gray' hover 'arc_con_03' action SetScreenVariable("concept", "concept03")
                if persistent.con06 is None:
                    add 'con_lock'
                else:
                    imagebutton idle 'arc_con_06_gray' hover 'arc_con_06' action SetScreenVariable("concept", "concept06")
                if persistent.con08 is None:
                    add 'con_lock'
                else:
                    imagebutton idle 'arc_con_08_gray' hover 'arc_con_08' action SetScreenVariable("concept", "concept08")
                if persistent.ending is None:
                    add 'con_lock'
                    add 'con_lock'
                    add 'con_lock'
                else:
                    imagebutton idle 'arc_con_10_gray' hover 'arc_con_10' action SetScreenVariable("concept", "concept10")
                    imagebutton idle 'arc_con_11_gray' hover 'arc_con_11' action SetScreenVariable("concept", "concept11")
                    imagebutton idle 'arc_con_12_gray' hover 'arc_con_12' action SetScreenVariable("concept", "concept12")
        else:
            style_prefix "concept"
            vbox spacing 20:
                if concept == "concept01":
                    use concept01
                if concept == "concept02":
                    use concept02
                if concept == "concept03":
                    use concept03
                if concept == "concept04":
                    use concept04
                if concept == "concept05":
                    use concept05
                if concept == "concept06":
                    use concept06
                if concept == "concept07":
                    use concept07
                if concept == "concept08":
                    use concept08
                if concept == "concept09":
                    use concept09
                if concept == "concept10":
                    use concept10
                if concept == "concept11":
                    use concept11
                if concept == "concept12":
                    use concept12
                if concept == "concept07" or concept == "concept08" or concept == "concept09" or concept == "concept10" or concept == "concept12":
                    pass
                else:
                    text _("Lee Yunseok -YGGDRASIL STUDIO")
                textbutton _("{font=[gui.fontawesome]}{/font} Return") action SetScreenVariable("concept", "concept00")
style concept_text is gui_text
screen concept01():
    label _("Discouraged Worker")
    text _(" A discouraged worker is a person of legal employment age who is not actively seeking employment, or who can not find employment after long-term unemployment. This is usually because an individual has given up looking or has had no success in finding a job, hence the term \"discouraged\".\n\n{a=https://en.wikipedia.org/wiki/Discouraged_worker}Wikipedia{/a}\n\n Discouraged workers are classified as an economically inactive population and not included in the unemployment rate, although they are actually unemployed.\n\n And this artificially causes a decrease in the unemployment rate in official statistics, in spite of an actually higher unemployment rate. In the case of Korea, the Subsidiary Employment Index, which includes the not-calculated unemployed, was reported first in November, 2014, and accordingly, the hidden problems in Korea's employment-population ratio and discouraged workers have surfaced.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept09")
        key 'K_LEFT' action SetScreenVariable("concept", "concept09")
        if persistent.con05 is True:
            key 'pad_leftx_pos' action SetScreenVariable("concept", "concept05")
            key 'K_RIGHT' action SetScreenVariable("concept", "concept05")
screen concept02():
    label _("Reclusive Outsider")
    text _(" Reclusive outsider is the phenomenon of reclusive adolescents or adults who withdraw from social life, often seeking extreme degrees of isolation and confinement. The term reclusive outsider refers to both the sociological phenomenon in general as well as to people belonging to this societal group.\n\n{a=https://en.wikipedia.org/wiki/Hikikomori}Wikipedia{/a}\n\n Choi Ga-yeon, a heroine of \"Discouraged Workers\", suffered from depressive disorder because of the sudden firing from her job and breaking-up with her lover.\n\n In addition, with her continuous failure to get a job, her anxiety disorder symptoms only became worse. And she naturally has become a hikikomori(a person who becomes a recluse and gives up any social life) after she gave up trying to get a job.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept05")
        key 'K_LEFT' action SetScreenVariable("concept", "concept05")
        if persistent.con07 is True:
            key 'pad_leftx_pos' action SetScreenVariable("concept", "concept07")
            key 'K_RIGHT' action SetScreenVariable("concept", "concept07")
screen concept03():
    label _("Medical Referral")
    text _(" Generally, a medical referral is issued by a hospital when sending a patient to another hospital. Ga-yeon has received medical treatment from a psychiatrist since she was fired from the hospital where she was working as a coordinator. In spite of long treatment, her condition did not improve at all, and the hospital issued a medical referral to another hospital. But Ga-yeon refused the referral as she felt the psychiatrist gave up on her, and this made her fall into despair. So she didn't seek any more psychiatric treatment.\n\n Since many people still think negatively about seeking psychiatric treatment, and have unfavorable perceptions about those who seek it, often, people who need help with their problems, tend to avoid getting the help they need, both here in Korea and elsewhere in the world.\n\n Also in the case of Ga-yeon, she hasn't talked about it, regarding it as her embarrassing secret. The medical referral Yunwoo found in Ga-yeon's mailbox was actually a referral that Hye-na arranged for her.\n\n Actually, the description shown in the medical referral in the \"Ga-yeon and Yunwoo\" part of the story, is almost the same as the one commonly issued in a real hospital in Korea.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept04")
        key 'K_LEFT' action SetScreenVariable("concept", "concept04")
        if persistent.con06 is True:
            key 'pad_leftx_pos' action SetScreenVariable("concept", "concept06")
            key 'K_RIGHT' action SetScreenVariable("concept", "concept06")
screen concept04():
    label _("Anxiety Disorder")
    text _(" Anxiety disorders are a category of mental disorders characterized by feelings of anxiety and fear, where anxiety is a worry about future events and fear is a reaction to current events. These feelings may cause physical symptoms, such as a racing heart and shakiness.\n\n{a=https://en.wikipedia.org/wiki/Anxiety_disorder}Wikipedia{/a}\n\n My mother had suffered from panic disorder for almost eight years, and she used to complain of pain and hyperpnea in certain and sometimes new and unexpected situations(Hyperpnea is the need to breathe more deeply because the person experiencing it feels light headed or otherwise feels they need more oxygen for various reasons.).\n\n And someone whom I know had anxiety disorder, and she suffered from a tic disorder including repetitive eye blinking and apnea when she feels anxiety in those same kinds of situations. She was even very dependent on alcohol and showed symptoms of caffeine addiction as well. Standing by my mother's and her side, and watching their pain and experiencing it with them, I hoped to help set them free from those painful days. But as time went by, I found I was getting numb with their pain, and at that moment, I felt extremely ashamed as a human being.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept07")
        key 'K_LEFT' action SetScreenVariable("concept", "concept07")
        if persistent.con03 is True:
            key 'pad_leftx_pos' action SetScreenVariable("concept", "concept03")
            key 'K_RIGHT' action SetScreenVariable("concept", "concept03")
screen concept05():
    label _("Depressive Disorder")
    text _(" Depressive disorder is a mental disorder characterized by a pervasive and persistent low mood that is accompanied by low self-esteem and by a loss of interest or pleasure in normally enjoyable activities. The term \"depression\" is used in a number of different ways. It is often used to mean this syndrome but may refer to other mood disorders or simply to a low mood. Major depressive disorder is a disabling condition that adversely affects a person's family, work or school life, sleeping and eating habits, and general health.\n\n{a=https://en.wikipedia.org/wiki/Major_depressive_disorder}Wikipedia{/a}\n\n Choi Ga-yeon, a heroine of \"Discouraged Workers\", suffered from depressive disorder because of the sudden firing from her job and breaking-up with her lover. In addition, with her continuous failure to get a job, her anxiety disorder symptoms only became worse. And she naturally has become a hikikomori(a person who becomes a recluse and gives up any social life) after she gave up trying to get a job.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept01")
        key 'K_LEFT' action SetScreenVariable("concept", "concept01")
        if persistent.con02 is True:
            key 'pad_leftx_pos' action SetScreenVariable("concept", "concept02")
            key 'K_RIGHT' action SetScreenVariable("concept", "concept02")
screen concept06():
    label _("Bridge of the Life")
    text _(" \"Bridge of the life\" was actually a sort of attempt using advanced technological methods to prevent suicide. By trying to have a conversation with a pedestrian through hopeful words and changing their desperation into hope, the designers thought suicidal people might be encouraged not to end their lives, but, in the event that failed, there was still the traditional physical anti-suicide barrier. The sensors mounted on every section of the bridge detects the exact location of a pedestrian as she/he walks by and the bridge lights the hopeful word up in the right position for a pedestrian to read.\n\n The very first bridge of life opened on Mapo Bridge, Korea on September 26, 2012, and was sponsored by Seoul City and Samsung Life Insurance. Mapo Bridge was chosen as the first installation of this new technology because it has been notorious as the place with the highest suicide rate. And the second one opened on Hangang Bridge, Korea on November 5, 2013, sponsored by Korea Health Promotional Foundation.\n\n And the ad for \"Bridge of the life\" received 39 awards in the International Advertising Festival and obtained excellent advertising effects. But regardless of this successful record, the rate of suicides by death leap has steadily increased. According to statistics, installing closed circuit television on the public bridges was more helpful in preventing suicide jumps and rescuing suicide jumpers who actually did jump than the bridge of life technology.\n\n As a result of the Samsung Life Insurance's decision to discontinue their operational support for \"Bridge of the Life\" on Mapo Bridge in September 2015, the automatic detection sensor has not worked since December 1, 2015 and the website of Bridge of the Life was also closed.\n\n In fact, Hangang Bridge wasn't yet built at the time that the \"Discouraged workers\" story takes place. But in the game, it was set as a background to let Yunwoo try to think where Ga-yeon disappeared to.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept03")
        key 'K_LEFT' action SetScreenVariable("concept", "concept03")
        if persistent.con08 is True:
            key 'pad_leftx_pos' action SetScreenVariable("concept", "concept08")
            key 'K_RIGHT' action SetScreenVariable("concept", "concept08")
screen concept07():
    label _("IMF Crisis")
    text _(" The Asian financial crisis was a period of financial crisis that gripped much of East Asia beginning in July 1997 and raised fears of a worldwide economic meltdown due to financial contagion.\n\n The crisis started in Thailand with the financial collapse of the Thai baht after the Thai government was forced to float the baht due to lack of foreign currency to support its fixed exchange rate, cutting its peg to the U.S. dollar, after exhaustive efforts to support it in the face of a severe financial over-extension that was in part real estate driven.\n\n{a=https://en.wikipedia.org/wiki/1997_Asian_financial_crisis#South_Korea}Wikipedia{/a}\n\n At the time, Thailand had acquired a burden of foreign debt that made the country effectively bankrupt even before the collapse of its currency. As the crisis spread, most of Southeast Asia and Japan saw slumping currencies, devalued stock markets and other asset prices, and a precipitous rise in private debt.\n\n Indonesia, South Korea and Thailand were the countries most affected by the crisis. Hong Kong, Laos, Malaysia and the Philippines were also hurt by the slump. Brunei, China, Singapore, Taiwan and Vietnam were less affected, although all suffered from a loss of demand and confidence throughout the region.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept02")
        key 'K_LEFT' action SetScreenVariable("concept", "concept02")
        if persistent.con04 is True:
            key 'pad_leftx_pos' action SetScreenVariable("concept", "concept04")
            key 'K_RIGHT' action SetScreenVariable("concept", "concept04")
screen concept08():
    label _("Accident")
    text _(" \"Accident\" tells what happens after \"Epilogue\" which is the basic ending of \"Discouraged Workers\".\n\n Ga-yeon reached out her hand toward Yunwoo, but at that moment, she blacked out and fell off the bridge. And Yunwoo threw himself into the river to save her. A few days later, they rose to the surface, and one passerby's report told their deaths to the world.\n\n If Yunwoo hadn't found his wallet, Ga-yeon would die alone while he was haggling over the taxi fare.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept06")
        key 'K_LEFT' action SetScreenVariable("concept", "concept06")
        if persistent.ending is True:
            key 'pad_leftx_pos' action SetScreenVariable("concept", "concept10")
            key 'K_RIGHT' action SetScreenVariable("concept", "concept10")
screen concept09():
    label _("Prologue")
    text _(" As a hospital coordinator, Ga-yeon fell in love with a doctor at the hospital she was working in and they had an affair even though the doctor was a married man. When the director found out, she was fired. For over a year she tried to find another job, but her mental uneasiness eventually made her give up and she became a recluse.\n\n A year later, in the spring of 2013, her younger sister, Hye-na, and her first love Yunwoo come to her.\n\n A story about the dark side of today's youth and serious life events happening around Ga-yeon.")
    text "[config.name]"
    if persistent.blind is True:
        key 'pad_leftx_neg' action [SetVariable('blind_set', None), Return()]
        key 'K_LEFT' action [SetVariable('blind_set', None), Return()]
        if persistent.con01 is True:
            key 'pad_leftx_pos' action SetScreenVariable("concept", "concept01")
            key 'K_RIGHT' action SetScreenVariable("concept", "concept01")
screen concept10():
    label _("Flowery Mornings and Moonlit Nights")
    text _(" \"Flowery Mornings and Moonlit Nights\" is the true ending which assumes that Ga-yeon didn't faint and grabbed Yunwoo's hand in \"Epilogue\". Originally \"Discouraged Workers\" was intended to end with the \"Accident\" story as the true ending. But after deciding to release it in the market, this was chosen as the true ending.\n\n Ga-yeon finds the culprit who spread the video, with the help of Yunwoo, and reports him to the police. After that, she tries to find a job, but it's still not easy for her. Even some interviewers who know her, hurt her.\n\n Yunwoo just stays by her side and tries to protect her without saying anything, and Hye-na helps Ga-yeon to work part-time at the cafe where she's working. Ga-yeon works hard every day, grateful for being allowed to work there. One day, the cafe manager gives her a letter of recommendation from the general manager of the head office, and Ga-yeon gets an opportunity to have an interview for a large affiliated store run by the head office. And by chance, the interviewer she meets with for the job is her old boss, who during her schooldays, originally gave her the idea of her dream job being a restaurant manager. Ga-yeon passes the interview with ease, and finally, she starts to move towards her dream.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept08")
        key 'K_LEFT' action SetScreenVariable("concept", "concept08")
        key 'pad_leftx_pos' action SetScreenVariable("concept", "concept11")
        key 'K_RIGHT' action SetScreenVariable("concept", "concept11")
screen concept11():
    label _("Seohae Grand Bridge")
    text _(" A chain reaction collision, involving 29 vehicles, happened at 7:50am on October 3, 2006, Korean time, on Seohae Grand Bridge in South Korea. This collision happened due to a thick fog, and it left 12 people dead and about 50 injured. According to the investigation, the accident occurred not only because of bad weather, but also because some drivers were speeding as well as shoulder riding. But whatever the reason was, the damage was almost 4 billion won, which was the most awful and costly accident in Korean car insurance history.\n\n \"Lee Seol-ah\" is a fictitious character who died in this accident. This woman, who died at the age of 21, still in the flower of her youth, visits the world she used to live in after she died, and watches people whom she loved and shared friendships with. One day, she meets Ga-yeon who helped her in the past. To prevent her death, she decides to help Yunwoo.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept10")
        key 'K_LEFT' action SetScreenVariable("concept", "concept10")
        key 'pad_leftx_pos' action SetScreenVariable("concept", "concept12")
        key 'K_RIGHT' action SetScreenVariable("concept", "concept12")
screen concept12():
    label _("Red Dialogue Window")
    text _(" In \"Discouraged Workers\", a word box in red color is used to show the words and thoughts of Ga-yeon and a clerk Because when the basic scenario was developed, they are actually not alive.\n\n But when Ga-yeon is talking with her mom on the phone, the black box is used out of consideration for her mother.")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("concept", "concept11")
        key 'K_LEFT' action SetScreenVariable("concept", "concept11")
        key 'pad_leftx_pos' action [SetVariable('blind_set', None), Return()]
        key 'K_RIGHT' action [SetVariable('blind_set', None), Return()]
screen diary():
    tag menu
    default diary = "diary00"
    use game_menu(_("{font=[gui.fontawesome]}{/font} Diary"), scroll="viewport"):
        if persistent.obdrawer is None:
            label _("{font=[gui.fontawesome]}{/font} Find the diary in the room.")
        elif diary == "diary00":
            grid 4 4 spacing 20 xoffset If(renpy.variant("small"), false=135):
                imagebutton idle 'arc_diary_01_sepia' hover 'arc_diary_01' action SetScreenVariable("diary", "diary01")
                imagebutton idle 'arc_diary_02_sepia' hover 'arc_diary_02' action SetScreenVariable("diary", "diary02")
                imagebutton idle 'arc_diary_03_sepia' hover 'arc_diary_03' action SetScreenVariable("diary", "diary03")
                imagebutton idle 'arc_diary_04_sepia' hover 'arc_diary_04' action SetScreenVariable("diary", "diary04")
                imagebutton idle 'arc_diary_05_sepia' hover 'arc_diary_05' action SetScreenVariable("diary", "diary05")
                imagebutton idle 'arc_diary_06_sepia' hover 'arc_diary_06' action SetScreenVariable("diary", "diary06")
                imagebutton idle 'arc_diary_07_sepia' hover 'arc_diary_07' action SetScreenVariable("diary", "diary07")
                imagebutton idle 'arc_diary_08_sepia' hover 'arc_diary_08' action SetScreenVariable("diary", "diary08")
                imagebutton idle 'arc_diary_09_sepia' hover 'arc_diary_09' action SetScreenVariable("diary", "diary09")
                imagebutton idle 'arc_diary_10_sepia' hover 'arc_diary_10' action SetScreenVariable("diary", "diary10")
                imagebutton idle 'arc_diary_11_sepia' hover 'arc_diary_11' action SetScreenVariable("diary", "diary11")
                imagebutton idle 'arc_diary_12_sepia' hover 'arc_diary_12' action SetScreenVariable("diary", "diary12")
                imagebutton idle 'arc_diary_13_sepia' hover 'arc_diary_13' action SetScreenVariable("diary", "diary13")
                imagebutton idle 'arc_diary_14_sepia' hover 'arc_diary_14' action SetScreenVariable("diary", "diary14")
                imagebutton idle 'arc_diary_15_sepia' hover 'arc_diary_15' action SetScreenVariable("diary", "diary15")
                if persistent.dying is True:
                    imagebutton idle 'arc_diary_16_sepia' hover 'arc_diary_16' action SetScreenVariable("diary", "diary16")
                else:
                    add 'diary_lock'
        else:
            style_prefix "concept"
            vbox spacing 20:
                if diary == "diary01":
                    use diary01
                if diary == "diary02":
                    use diary02
                if diary == "diary03":
                    use diary03
                if diary == "diary04":
                    use diary04
                if diary == "diary05":
                    use diary05
                if diary == "diary06":
                    use diary06
                if diary == "diary07":
                    use diary07
                if diary == "diary08":
                    use diary08
                if diary == "diary09":
                    use diary09
                if diary == "diary10":
                    use diary10
                if diary == "diary11":
                    use diary11
                if diary == "diary12":
                    use diary12
                if diary == "diary13":
                    use diary13
                if diary == "diary14":
                    use diary14
                if diary == "diary15":
                    use diary15
                if diary == "diary16":
                    use diary16
                textbutton _("{font=[gui.fontawesome]}{/font} Return") action SetScreenVariable("diary", "diary00")
screen diary01():
    label _("My cool captain!")
    if persistent.blind is True:
        key 'pad_leftx_neg' action [SetVariable('blind_set', None), Return()]
        key 'K_LEFT' action [SetVariable('blind_set', None), Return()]
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary02")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary02")
    else:
        add 'diary01'
    text _(" It's been more than a month since I started working in a family restaurant. In the beginning, it was really hard to carry a tray and I even broke a few dishes. But now, I feel like I'm getting better and better. Sometimes, customers tip me as well, and also the other staff often praises my work. I'm especially good at…. hmmm…. well, it's too many to write them all down here! Later!\n\n However, the captain looks really cool. She's beautiful, smart, and also good at her work. Oh, she seems to be strong as well, as she usually carries heavy things by herself!\n\n I saw her carrying two metal trays stacked with dishes with just her two hands. It is hard even for men, but she's such a superwoman. How the hell can she do that? I hope I can do work as well as her someday.")
screen diary02():
    label _("My captain's tear")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary01")
        key 'K_LEFT' action SetScreenVariable("diary", "diary01")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary03")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary03")
    else:
        add 'diary02'
    text _(" Today the section chief of the head office visited the restaurant. I thought the chief would be a man, but she was a young woman. She came to our restaurant and called the captain to the locker room. She passed by me while I was working there, and I saw her nametag. And I found she has the same name as a famous comedian. Funny!\n\n As the captain was not in the hall, I tried to look for her, and when I opened the door of the locker room, she looked at me in surprise and turned her face hurriedly. And she said leave her alone for a while, forcing me out of the room. She was crying.\n\n Probably the section chief made her cry. That bitch! What did the captain do wrong? Hey, I'll get even with her!! Shit!")
screen diary03():
    label _("Went to see Yunwoo")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary02")
        key 'K_LEFT' action SetScreenVariable("diary", "diary02")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary04")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary04")
    else:
        add 'diary03'
    text _(" I went to Cheolwon, with Eunyoung to see Yunwoo today. I didn't realize it was that cold, but when I got off the bus, I was just shocked as it was literally freezing. It didn't snow, and the wind didn't blow, but cold air made even my eyes freeze. Eunyoung and I hurried into the visitor's room to wait for Yunwoo.\n\n A few minutes later, a soldier came in - actually I recognized that he was Yunwoo as soon as I saw him! And I got the giggles. His camouflage patterned muffler looked pretty cool, but his earmuffs reminded me of a once famous singer, and I couldn't stop laughing!\n\n I told him about that singer, and he got embarrassed. Eunyoung took his earmuffs away and danced, and all of us burst into laughter.\n\n However, since we said goodbye to Yunwoo, I've felt somewhat lonesome, and I still feel that way even as I'm writing this…. why do I feel this way?")
screen diary04():
    label _("I rejected him")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary03")
        key 'K_LEFT' action SetScreenVariable("diary", "diary03")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary05")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary05")
    else:
        add 'diary04'
    text _(" After I parted with him, and while I was coming home, I tried really hard to fight back tears. But when I arrived in my room, I just burst into tears. Why? Why was I so mean to him? I raged at him, and told him to quit music. Why the hell did I do that?\n\n Today he told me what I've really looked forward to hearing from him, but why…. why couldn't I accept him? And why did I hurt him? I can't stop crying….")
screen diary05():
    label _("As a friend")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary04")
        key 'K_LEFT' action SetScreenVariable("diary", "diary04")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary06")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary06")
    else:
        add 'diary05'
    text _(" I had a long conversation with Yunwoo today;\n\n You've just been discharged from the army, and I'm a student without a job. So what can we do now? You really think we can get married and start our home? Seriously? How?\n\n Besides, we're not romantically involved with each other. We're just friends. I think of you as my friend, and hope we could get along well with each other for a long time. That's all….\n\n I think I probably said it like that…. but of course it's not true that I think of him just as a friend, but…. To get back to our relationship as usual, I had to say it that way.\n\n I also said sorry that I hurt him.\n\n However, unexpectedly, it seemed he doesn't care about it. He said he was actually kidding when he asked me to marry him. And since I already refused his proposal anyway, there's nothing hard about getting along with me simply as a friend.\n\n What he said made me a little bit regretful, but anyway, we decided to leave as good friends as we've always been.")
screen diary06():
    label _("My days in hospital")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary05")
        key 'K_LEFT' action SetScreenVariable("diary", "diary05")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary07")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary07")
    else:
        add 'diary06'
    text _(" It's been almost a year since I started working in this hospital. I work as a coordinator of the hospital. I had my salary raised, and also I'm pretty satisfied with my job. My savings account with the balance which gets bigger and bigger makes me feel really happy.\n\n When I had to quit the university temporarily, I was just stunned. But now that I think about it, it was rather smart to do that, actually. Because of that choice, I was able to pay Hye-na's university tuition, without a loan.\n\n I'll save more money to send Mom and Daddy to travel on, and also support Hye-na until she gets married someday. Jeez, why is time passing so fast today? Until tomorrow, I'm going to bed!\n\n Ga-yeon, just keep it up as you've done so far!")
screen diary07():
    label _("Observing a doctor")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary06")
        key 'K_LEFT' action SetScreenVariable("diary", "diary06")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary08")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary08")
    else:
        add 'diary07'
    text _(" Oh, my god…. how could he look like him that much? His face, way of talking, character, and even that he can't hold liquor well…. everything is just like him. He reminds me of Yunwoo a lot. And it makes me feel sad. And this keeps bothering me so much. These days, I'm often trying to speak to him, or be around him. He also seems to be interested in me, and sometimes talks to me, or brings some snack or drink. He looks like a pretty good man.")
screen diary08():
    label _("His wife")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary07")
        key 'K_LEFT' action SetScreenVariable("diary", "diary07")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary09")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary09")
    else:
        add 'diary08'
    text _(" His wife visited the hospital. Though the Director and my lover prefer a simple and plain style, she dressed up too much, with luxurious dress and accessories. She looked just full of vanity. When I saw she's coquetting with him arm in arm, she really looked like an old fox. I can't imagine she's the Director's sister, and my lover's wife. She really makes me feel sick.\n\n When he and I were left alone because of night duty. he talked to me as if he was just working, because he knew we were being recorded on a CCTV.\n\n After finishing work, I got out of the hospital, and sat alone on the bench in front of the building. After a while, all lights were off in the hospital except one—Light from his office, coming through the blinds.")
screen diary09():
    label _("Farewell")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary08")
        key 'K_LEFT' action SetScreenVariable("diary", "diary08")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary10")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary10")
    else:
        add 'diary09'
    text _(" The director seemed to be trying hard not to hurt me, controlling his feelings. I understand he would feel betrayed as he has trusted me a lot, but he never swore at me at all, and treated me human to human. And now, I've finally realized what the hell I did. I felt really sorry for his wife, as she has never thought about this, and also felt sorry for the director who has always truly taken care of me. At the request of the Director, I decided to quit the hospital. I also said to him I would definitely break off my affair with the Doctor.\n\n After I packed up my stuff and got out of the hospital, I saw him running after me, but I just came out of the building and got into a taxi. In the running taxi, I just cried and cried. I could never see my colleagues there and the Director anymore…. and also him…. whom I made love with…. goodbye, everyone…. My greed has screwed up everything. Thank you all, and sorry….")
screen diary10():
    label _("I miss him")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary09")
        key 'K_LEFT' action SetScreenVariable("diary", "diary09")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary11")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary11")
    else:
        add 'diary10'
    text _(" Every single day, I cry, sleep, and wake from sleep, remember my good old days, especially with him, and then, cry, and fall asleep again. Beginning with a few days ago, I sometimes burst into laughter, and sometimes, burst into a fit of anger. I feel like I can't breathe well from time to time.\n\n I miss him. I miss him looking at me with a gentle smile. Thinking this makes me weepy, and it becomes hard to breathe. Also at this moment I'm writing this, I'm feeling really suffocated.")
screen diary11():
    label _("Sign")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary10")
        key 'K_LEFT' action SetScreenVariable("diary", "diary10")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary12")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary12")
    else:
        add 'diary11'
    text _(" Even though I had no interview today, I sat in front of my dressing table to put on makeup. But as soon as I saw my face, I was frightened, as it suddenly looked awful and disgusting. I fell backward, and managed to crawl to the bed. And I trembled and trembled. Then, I called Hye-na and begged her to save me.\n\n Soon, Hye-na came to my home, and I said to her I was probably going crazy, crying loudly in her arms. After I cried for a good while, I told her everything and taking her suggestion, I decided to see a doctor tomorrow. Hye-na is drinking a can of beer now.\n\n When I'm glancing at her, I feel my wrist, wrapped with bandages, is stinging.\n\n Okay, I'll finish today's diary here and go to bed after having some more conversations with Hye-na. Good night.")
screen diary12():
    label _("A lunatic")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary11")
        key 'K_LEFT' action SetScreenVariable("diary", "diary11")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary13")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary13")
    else:
        add 'diary12'
    text _(" Today, I visited a neuropsychiatric clinic, with Hye-na. I was pretty afraid to go there, but as I was with my sister, I could do it. The doctor asked me a number of things, from trivial questions to what is happening to me now and what I don't want to tell others as well.\n\n He also asked whether I have some physical problems, and I told him I hurt myself several times, and especially when I looked at my face yesterday, I was really frightened, as my eyes continuously blinked. The doctor asked me to have a medical checkup. So I filled out the questionnaire and had a blood test as well.\n\n And the result said I had 'anxiety disorder' and 'depressive disorder'. I asked the doctor if I was going to be a mental patient. But he said no.\n\n He just told me my condition and tick disorder would get better soon, if I try hard to improve my life pattern and steadily get counseling.")
screen diary13():
    label _("My friend, Eunju")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary12")
        key 'K_LEFT' action SetScreenVariable("diary", "diary12")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary14")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary14")
    else:
        add 'diary13'
    text _(" Today, I met Eunju. It's been a really long time since I've seen her. She used to be my best friend when we were high school students, but she is not single anymore. She said she's really worried as she hasn't lost any weight in spite of her steady diet since she gave birth to her baby. So I told her that she still looks good. Eunju worried about me saying I'm so bony, and she said to take her fat from her, shaking her potbelly. It was hilarious.\n\n Eunju has become a master of a Japanese fencing school. I think she probably heard about my situation from Hye-na, because she has never asked me about my job or marriage.\n\n She just kept talking about our school days, or her travel. Like other mamas, her voice was louder than it used to be, and also she speaks so fast Anyway, I'm happy she is having a good life.\n\n Ga-yeon, no more negative thinking! Okay?")
screen diary14():
    label _("Getting a job")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary13")
        key 'K_LEFT' action SetScreenVariable("diary", "diary13")
        key 'pad_leftx_pos' action SetScreenVariable("diary", "diary15")
        key 'K_RIGHT' action SetScreenVariable("diary", "diary15")
    else:
        add 'diary14'
    text _(" These days, I receive mental health treatment, and also try hard to get a job. I didn't want to close my installment savings account, but I did, to have some reserved money for myself and also give some of it to my parents. I can't stop sending money to my parents because I have to make them believe I live well without any problem as always.\n\n However, getting a new job is harder than I expected. Because I worked mostly in restaurants, I have failed several times already, although I had a number of interviews for general office jobs.\n\n Besides, I never wrote my mental health-related matter in the resume, but some interviewers seemed to recognize my problem, as my tick disorder appeared even during the interview.\n\n I'm trying really to keep the steam up, but…. I'm getting tired of living….")
screen diary15():
    label _("Rubbish and rubbish can")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary14")
        key 'K_LEFT' action SetScreenVariable("diary", "diary14")
        if persistent.dying is True:
            key 'pad_leftx_pos' action SetScreenVariable("diary", "diary16")
            key 'K_RIGHT' action SetScreenVariable("diary", "diary16")
    else:
        add 'diary15'
    text _(" I gave up. I gave up finding a new job, meeting people, receiving medical treatment, and everything. All are just useless. What I have now is…. only this tiny space. Where nothing happens unless I stir it.\n\n In spite of heaps of attempts to get a job, what I had was only frustration and discouragement. The hospital where I've received the treatment suggested I transfer to another hospital. Sometimes, the nebulizer which Hye-na presented me to soothe myself didn't work at all.\n\n I feel like my room is a rubbish can, and I'm just rubbish.")
screen diary16():
    label _("Dying message")
    if persistent.blind is True:
        key 'pad_leftx_neg' action SetScreenVariable("diary", "diary15")
        key 'K_LEFT' action SetScreenVariable("diary", "diary15")
        key 'pad_leftx_pos' action [SetVariable('blind_set', None), Return()]
        key 'K_RIGHT' action [SetVariable('blind_set', None), Return()]
    else:
        add 'diary16'
    text _(" Go die, you bitch. How dare you want to live on! You're such a hooker who tried to take another's husband! Why are you still alive? You know well what a useless thing you are. You're just a whore. Now are you going to cling to him, instead of your previous lover? You don't deserve to live anymore. Go away. Go away and die.\n\n Someone keeps whispering in my ears. Okay. Alright. Just stop it, please. Please. I'm sorry. I go and die now. So, please shut up!")
screen gallery():
    tag menu
    use game_menu(_("{font=[gui.fontawesome]}{/font} Gallery"), scroll="viewport"):
        grid 4 8:
            add g.make_button('frustration', 'arc_gall_01', hover_border='arc_gall_01', idle_border='arc_gall_01_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('vomiting', 'arc_gall_02', hover_border='arc_gall_02', idle_border='arc_gall_02_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('pusillanimous', 'arc_gall_03', hover_border='arc_gall_03', idle_border='arc_gall_03_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('that day we', 'arc_gall_04', hover_border='arc_gall_04', idle_border='arc_gall_04_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('fate', 'arc_gall_05', hover_border='arc_gall_05', idle_border='arc_gall_05_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('alleyway', 'arc_gall_06', hover_border='arc_gall_06', idle_border='arc_gall_06_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('moonlight', 'arc_gall_07', hover_border='arc_gall_07', idle_border='arc_gall_07_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('drunken', 'arc_gall_08', hover_border='arc_gall_08', idle_border='arc_gall_08_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('eternal happiness', 'arc_gall_09', hover_border='arc_gall_09', idle_border='arc_gall_09_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('despair', 'arc_gall_10', hover_border='arc_gall_10', idle_border='arc_gall_10_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('lean_gall', 'arc_gall_11', hover_border='arc_gall_11', idle_border='arc_gall_11_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('distortion', 'arc_gall_12', hover_border='arc_gall_12', idle_border='arc_gall_12_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('imf crisis', 'arc_gall_13', hover_border='arc_gall_13', idle_border='arc_gall_13_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('newspaper delivery', 'arc_gall_14', hover_border='arc_gall_14', idle_border='arc_gall_14_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('serving', 'arc_gall_15', hover_border='arc_gall_15', idle_border='arc_gall_15_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('kiss me', 'arc_gall_16', hover_border='arc_gall_16', idle_border='arc_gall_16_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('video_gall', 'arc_gall_17', hover_border='arc_gall_17', idle_border='arc_gall_17_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('self_gall', 'arc_gall_18', hover_border='arc_gall_18', idle_border='arc_gall_18_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('rip', 'arc_gall_19', hover_border='arc_gall_19', idle_border='arc_gall_19_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('masturbation', 'arc_gall_20', hover_border='arc_gall_20', idle_border='arc_gall_20_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('deep kiss', 'arc_gall_21', hover_border='arc_gall_21', idle_border='arc_gall_21_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('caress', 'arc_gall_22', hover_border='arc_gall_22', idle_border='arc_gall_22_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('fellatio', 'arc_gall_23', hover_border='arc_gall_23', idle_border='arc_gall_23_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('riding', 'arc_gall_24', hover_border='arc_gall_24', idle_border='arc_gall_24_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('smoking', 'arc_gall_25', hover_border='arc_gall_25', idle_border='arc_gall_25_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('bridge', 'arc_gall_26', hover_border='arc_gall_26', idle_border='arc_gall_26_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('edge', 'arc_gall_27', hover_border='arc_gall_27', idle_border='arc_gall_27_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('corruption', 'arc_gall_28', hover_border='arc_gall_28', idle_border='arc_gall_28_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('doa', 'arc_gall_29', hover_border='arc_gall_29', idle_border='arc_gall_29_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('doa0', 'arc_gall_30', hover_border='arc_gall_30', idle_border='arc_gall_30_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('growing', 'arc_gall_31', hover_border='arc_gall_31', idle_border='arc_gall_31_gray', ysize=358, padding=(0,0), margin=(0,0))
            add g.make_button('nte', 'arc_gall_32', hover_border='arc_gall_32', idle_border='arc_gall_32_gray', ysize=358, padding=(0,0), margin=(0,0))
screen gallery_navigation():
    text "[config.name]":
        style "gallery_title"
screen music_room():
    tag menu
    use game_menu(_("{font=[gui.fontawesome]}{/font} Music"), scroll=None):
        hbox spacing 100:
            if not renpy.variant("small"):
                vbox:
                    textbutton _("Track 1. Pandemic") action mr.Play("bgm/Pandemic.opus")
                    textbutton _("Track 2. Sigh day") action mr.Play("bgm/Sigh day.opus")
                    textbutton _("Track 3. Mare tranquillitatis") action mr.Play("bgm/Mare tranquillitatis.opus")
                    textbutton _("Track 4. CCCanon") action mr.Play("bgm/CCCanon.opus")
                    textbutton _("Track 5. Let's game") action mr.Play("bgm/Let's game.opus")
                    textbutton _("Track 6. Peace") action mr.Play("bgm/Peace.opus")
                    textbutton _("Track 7. Unknown mist") action mr.Play("bgm/Unknown mist.opus")
                    textbutton _("Track 8. Lush garden") action mr.Play("bgm/Lush garden.opus")
                    textbutton _("Track 9. Jormungandr") action mr.Play("bgm/Jormungandr.opus")
                    textbutton _("Track 10. Nyx") action mr.Play("bgm/Nyx.opus")
                    textbutton _("Track 11. Summit showdown") action mr.Play("bgm/Summit showdown.opus")
                    textbutton _("Track 12. Love song") action mr.Play("bgm/Love song.opus")
                    textbutton _("Track 13. Sea of nectar") action mr.Play("bgm/Sea of nectar.opus")
            else:
                vbox:
                    null width 0
            vbox:
                add 'fate' zoom .5 xalign .5
                null height (2 * gui.pref_spacing)
                vbox xalign .5:
                    if not persistent.controllers is None:
                        hbox:
                            button xsize 120:
                                vbox xalign 0.5:
                                    spacing 5
                                    imagebutton idle 'controller_config' action mr.Stop() at menuback:
                                        xalign 0.5
                                    textbutton ('{size=[gui.quick_button_text_size]}Stop{/size}') action mr.Stop() at menuback:
                                        xalign 0.5
                            button xsize 120:
                                vbox xalign 0.5:
                                    spacing 5
                                    imagebutton idle 'controller_shoulder_l' action mr.Previous() at menuback:
                                        xalign 0.5
                                    textbutton ('{size=[gui.quick_button_text_size]}Previous{/size}') action mr.Previous() at menuback:
                                        xalign 0.5
                            button xsize 120:
                                vbox xalign 0.5:
                                    spacing 5
                                    imagebutton idle 'controller_shoulder_r' action mr.Next() at menuback:
                                        xalign 0.5
                                    textbutton ('{size=[gui.quick_button_text_size]}Next{/size}') action mr.Next() at menuback:
                                        xalign 0.5
                            button xsize 120:
                                vbox xalign 0.5:
                                    spacing 5
                                    imagebutton idle 'controller_hide' action mr.ToggleSingleTrack() at menuback:
                                        xalign 0.5
                                    textbutton ('{size=[gui.quick_button_text_size]}Loop{/size}') action mr.ToggleSingleTrack() at menuback:
                                        xalign 0.5
                            button xsize 120:
                                vbox xalign 0.5:
                                    spacing 5
                                    imagebutton idle 'controller_skip' action mr.ToggleShuffle() at menuback:
                                        xalign 0.5
                                    textbutton ('{size=[gui.quick_button_text_size]}Shuffle{/size}') action mr.ToggleShuffle() at menuback:
                                        xalign 0.5
                    else:
                        hbox:
                            textbutton _("{font=[gui.fontawesome]}{/font} Stop") action mr.Stop()
                            textbutton _("{font=[gui.fontawesome]}{/font} Shuffle") action mr.ToggleShuffle()
                            textbutton _("{font=[gui.fontawesome]}{/font} Random") action mr.RandomPlay()
                            textbutton _("{font=[gui.fontawesome]}{/font} Loop") action mr.ToggleSingleTrack()
                            if renpy.variant("pc"):
                                textbutton _("{font=[gui.fontawesome]}{/font} Previous") action mr.Previous()
                                textbutton _("{font=[gui.fontawesome]}{/font} Next") action mr.Next()
                        if renpy.variant("small"):
                            null height (2 * gui.pref_spacing)
                            hbox xalign .5:
                                textbutton _("{font=[gui.fontawesome]}{/font} Previous") action mr.Previous()
                                textbutton _("{font=[gui.fontawesome]}{/font} Next") action mr.Next()
                        null height (2 * gui.pref_spacing)
                        hbox xalign .5:
                            textbutton _("{font=[gui.fontawesome]}{/font} Bandcamp") action OpenURL('https://yggdrasilstudio.bandcamp.com/album/discouraged-workers-ost')
                            textbutton _("{font=[gui.fontawesome]}{/font} Soundcloud") action OpenURL('https://soundcloud.com/arisae/sets/discouraged-workers-ost')
                            if persistent.steam is True:
                                if _renpysteam.dlc_installed(375160):
                                    textbutton _("{font=[gui.fontawesome]}{/font} Manual"):
                                        if _preferences.language == 'Korean':
                                            action OpenDirectory('Soundtrack/manual/discouraged_workers_ost_readme_ko.pdf')
                                        else:
                                            action OpenDirectory('Soundtrack/manual/discouraged_workers_ost_readme.pdf')
                                else:
                                    textbutton _("{font=[gui.fontawesome]}{/font} Add to cart") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 375160), Jump('dlc')]
        on "replace" action mr.Play()
        on "replaced" action Play("music", "bgm/Pandemic.opus")
        key 'hide_windows' action mr.ToggleSingleTrack()
        key 'rollforward' action mr.Next()
        key 'rollback' action mr.Previous()
        key 'toggle_skip' action mr.ToggleShuffle()
        key 'K_c' action mr.Stop()
        key 'pad_y_press' action mr.Stop()
screen replay():
    tag menu
    use game_menu(_("{font=[gui.fontawesome]}{/font} Replay"), scroll="viewport"):
        grid 4 5:
            if persistent.part01 is True:
                imagebutton idle 'part_01_sepia' hover 'part_01' action Replay('start')
            else:
                add 'lock'
            if persistent.part02 is True:
                imagebutton idle 'part_02_sepia' hover 'part_02' action Replay('mono0')
            else:
                add 'lock'
            if persistent.part03 is True:
                imagebutton idle 'part_03_sepia' hover 'part_03' action Replay('caffe')
            else:
                add 'lock'
            if persistent.part04 is True:
                imagebutton idle 'part_04_sepia' hover 'part_04' action Replay('shinchon')
            else:
                add 'lock'
            if persistent.part05 is True:
                imagebutton idle 'part_05_sepia' hover 'part_05' action Replay('food')
            else:
                add 'lock'
            if persistent.part07 is True:
                imagebutton idle 'part_07_sepia' hover 'part_07' action Replay('food1')
            else:
                add 'lock'
            if persistent.part08 is True:
                imagebutton idle 'part_08_sepia' hover 'part_08' action Replay('cheon')
            else:
                add 'lock'
            if persistent.part09 is True:
                imagebutton idle 'part_09_sepia' hover 'part_09' action Replay('hyena')
            else:
                add 'lock'
            if persistent.part10 is True:
                imagebutton idle 'part_10_sepia' hover 'part_10' action Replay('tears')
            else:
                add 'lock'
            if persistent.part11 is True:
                imagebutton idle 'part_11_sepia' hover 'part_11' action Replay('mono3')
            else:
                add 'lock'
            if persistent.part12 is True:
                imagebutton idle 'part_12_sepia' hover 'part_12' action Replay('hospital')
            else:
                add 'lock'
            if persistent.part13 is True:
                imagebutton idle 'part_13_sepia' hover 'part_13' action Replay('life')
            else:
                add 'lock'
            if persistent.part14 is True:
                imagebutton idle 'part_14_sepia' hover 'part_14' action Replay('discouraged')
            else:
                add 'lock'
            if persistent.part17 is True:
                imagebutton idle 'part_17_sepia' hover 'part_17' action Replay('love')
            else:
                add 'lock'
            if persistent.part18 is True:
                imagebutton idle 'part_18_sepia' hover 'part_18' action Replay('yunwoo0')
            else:
                add 'lock'
            if persistent.part19 is True:
                imagebutton idle 'part_19_sepia' hover 'part_19' action Replay('gayeon')
            else:
                add 'lock'
            if persistent.part20 is True:
                imagebutton idle 'part_20_sepia' hover 'part_20' action Replay('yunwoo2')
            else:
                add 'lock'
            if persistent.part22 is True:
                imagebutton idle 'part_22_sepia' hover 'part_22' action Replay('edge')
            else:
                add 'lock'
            if persistent.part24 is True:
                imagebutton idle 'part_24_sepia' hover 'part_24' action Replay('epilogue')
            else:
                add 'lock'
            if persistent.part25 is True:
                imagebutton idle 'part_25_sepia' hover 'part_25' action Replay('ending')
            else:
                add 'lock'
screen credits():
    tag menu
    default credits = "credits"
    use game_menu(_("{font=[gui.fontawesome]}{/font} Credits"), scroll="viewport"):
        vbox:
            hbox:
                textbutton _("{font=[gui.fontawesome]}{/font} Credits") action SetScreenVariable("credits", "credits")
                textbutton _("{font=[gui.fontawesome]}{/font} Authors") action SetScreenVariable("credits", "author")
                textbutton _("{font=[gui.fontawesome]}{/font} Photographers") action SetScreenVariable("credits", "photo")
            null height (4 * gui.pref_spacing)
            style_prefix "help"
            if credits == "credits":
                use credits_list
            if credits == "author":
                use authors
            if credits == "photo":
                use photographers
screen credits_list():
    vbox:
        spacing 23
        hbox:
            label _("Lee Yunseok")
            text _("Directing, Design, Programming, Music, Sound, Writing, UI Design, Background CG, Object Sprites, Packaging, Video, Website -From April 21, 2013")
        hbox:
            label _("chibilis studio")
            text _("Animation, Character Sprites, CG Sprites -From March 10, 2015")
        hbox:
            label _("Brian Connors")
            text _("English Translation Adviser -June 3, 2015~July 1, 2017")
        hbox:
            label _("Ga Younghee")
            text _("English Translator -April 11, 2015~June 10, 2016")
        hbox:
            label _("IVY")
            text _("Chinese Translator -July 25, 2016~February 10, 2018")
        hbox:
            label _("Roman Koledin")
            text _("Russian Translator -August 28, 2016~December 7, 2017")
        hbox:
            label _("Adam Patric Kratz")
            text _("Epilepsy Adviser -November 15, 2015~November 20, 2015")
        label _('{font=[gui.fontawesome]}{/font} {font=gui/fonts/Merienda-Regular.ttf}Project Gamer Japonés{/font}')
        hbox:
            label _("Oscar Ballona Centeno")
            text _("Project Leader in Spanish, Spanish Translator -From May 29, 2017")
        hbox:
            label _("AxelBodga")
            text _("Spanish Editor -From May 29, 2017")
        hbox:
            label _("Yisus")
            text _("Spanish Translator -From May 29, 2017")
        label _('{font=[gui.fontawesome]}{/font} Old Version')
        hbox:
            label _("YANG")
            text _("Male sprites, CG sprites -April 8, 2015~September 13, 2015")
        hbox:
            label _("Jeon Junsik")
            text _("Unofficial Demo Sprites -January 5, 2015~February 25, 2015")
        hbox:
            label _("Kyle Fawcett")
            text _("English Demo Translation Adviser -June 3, 2015~June 14, 2015")
    null height (4 * gui.pref_spacing)
    vbox:
        style_prefix "about"
        label _('{font=[gui.fontawesome]}{/font} Contributors')
        null height (2 * gui.pref_spacing)
        text _('ACOC, Aiman Sharul, Axel Mertes, Bgame, Brandon Tanimoto, Brian Connors, BRISAK Kim Doohyeon, cheif.choi, Choi Irang, Choi Jihye, cloture, Danielle Bell, Edward N Puckering, Gary King, Gwak Jaeryeol, Han Ihyeong, Hoe Namyoon, Hong Eunki, Hwang Daehoon, Hyojoon, James Emmerson, Jeong Dongwon, Jeong Wookjin, Jeong Yoonsoo, Jianmin Zhang,\nKarina Schulze, Keira Val\'Azr, Kim Hanseol, Kim Hyeoncheol, Kim Jaeseong, Kim Jeongwoong, Kim Myeongwook,\nLee Changki, Lee Eunji, Lee Gunhae, Lee Hyejin, Lee Jaewi, Light Twins, Lim Jisoo, Maddy Wootton,\nMarshall Proudfoot, Mirumu, Mojaeng, Oh Hyeonjun, Park Hyeonjun, Park JoonKoo, Rewind, Sander Tieleman, srwss, Sung Chanaul, YottaCho, Zerial.net')
        null height (4 * gui.pref_spacing)
        label _('{font=[gui.fontawesome]}{/font} Rooters')
        null height (2 * gui.pref_spacing)
        text _('Caz Woolley, Game Dev Robot, Gamsadev, Indie GameDev Bot, Indie Game Lover, Indie Games Devel, IndieVideoGames, Joachim Dimitri Jensen, Kim Kyeongtae, Kim Younghwan, Kurt Simon, Linda Lee King, Peter Christiansen, Sakimichi, Sebastian Haba, Spero Mcgee, The Indie Sloth, Vrachos, Xin Liu, Yu Shinhyeon')
        null height (4 * gui.pref_spacing)
        label _('{font=[gui.fontawesome]}{/font} Special Thanks To')
        null height (2 * gui.pref_spacing)
        text _("Christopher Rice, George Winston, Kim Sooyoung, Lee Illseong, Pixabay, Shin Haechul, So Reyeon, Tom Rothamel,\nValve Corporation")
        null height (4 * gui.pref_spacing)
screen authors():
    vbox:
        spacing 23
        hbox:
            label _("36play")
            text _("SamhyunyukgakVSTi")
        hbox:
            label _("Alex")
            text _("Some code improvement for Ren'Py jigsaw puzzle")
        hbox:
            label _("ASAN-SI")
            text _("YiSunShin")
        hbox:
            label _("Bitstream, Inc.")
            text _("DejaVuSans")
        hbox:
            label _("Dave Gandy")
            text _("Font Awesome")
        hbox:
            label _("Designzzz")
            text _("Circle Abstract Brushes")
        hbox:
            label _("Eduardo Tunni")
            text _("Merienda")
        hbox:
            label _("ephtracy")
            text _("MagicaVoxel")
        hbox:
            label _("Fontfabric")
            text _("Intro Cond")
        hbox:
            label _("freesfx.co.uk")
            text _("Slap sound effect")
        hbox:
            label _("Hanyang University")
            text _("OXVSTi")
        hbox:
            label _("Johnanth")
            text _("Button layout of a wireless Xbox 360 controller")
        hbox:
            label _("Jupiter Hadley")
            text _("Game Jolt Inspired Font")
        hbox:
            label _("Microsoft")
            text _("Xbox 360 Controller/Button asset pack")
        hbox:
            label _("Naver Corporation")
            text _("NanumFont")
        hbox:
            label _("PerpetualStudios")
            text _("Broken Glass Brushes - Eight")
        hbox:
            label _("SusanTheCat")
            text _("The original code for Ren'Py jigsaw puzzle")
        hbox:
            label _("The Android Open Source Project")
            text _("DroidSansFallback")
        hbox:
            label _("Tom Rothamel")
            text _("Ren'Py Visual Novel Engine")
        hbox:
            label _("Valve Corporation")
            text _("Steam, Steamworks")
        hbox:
            label _("Vic Fieger fonts")
            text _("Edo")
        hbox:
            label _("Zhuo Xiao Feng")
            text _("Shu Ti Fang Zhuo Xiao Feng Xing Cao Ti")
screen photographers():
    vbox:
        spacing 23
        hbox:
            label _("Bundang LineM")
            text _("Yeouinaru Station")
        hbox:
            label _("byongsu")
            text _("Hof")
        hbox:
            label _("Cunture PD\nLim Ye-seong")
            text _("SangsangMadang")
        hbox:
            label _("Ellif")
            text _("Familymart")
        hbox:
            label _("Jinho Jung")
            text _("Daehangno")
        hbox:
            label _("J o")
            text _("Osaka Dai-ichi Hotel Moderate Single Room")
        hbox:
            label _("Julie Facine")
            text _("Sanchon")
        hbox:
            label _("Joost Vanhoutte")
            text _("Korea Signs")
        hbox:
            label _("Lim Seongyeon")
            text _("Cafe")
        hbox:
            label _("Nagyman")
            text _("Festival world")
        hbox:
            label _("Official U.S. Navy Page")
            text _("Fort Belvoir Community Hospital")
        hbox:
            label _("Pixabay community")
            text _("Many public domain images")
        hbox:
            label _("Sangrila")
            text _("Guckkasten")
        hbox:
            label _("Subway06")
            text _("SMSC Line1 VVVF Inside")
        hbox:
            label _("TF-urban")
            text _("Sinchon street")
        hbox:
            label _("Trainer2a")
            text _("Jet Nubulizer")
        hbox:
            label _("Verizon Wireless")
            text _("Cellphone Shop")
screen downloadable():
    tag menu
    default downloadable = "dlc"
    use game_menu(_("{font=[gui.fontawesome]}{/font} DLC&MOD"), scroll="viewport"):
        vbox:
            hbox:
                textbutton _("DLC") action SetScreenVariable("downloadable", "dlc")
                textbutton _("MOD") action SetScreenVariable("downloadable", "mod")
            if downloadable == "dlc":
                use dlc
            if downloadable == "mod":
                use mod
    key 'K_p' action [SetField(persistent, 'downloadable', None), Return()]
    key 'pad_x_press'  action [SetField(persistent, 'downloadable', None), Return()]
screen dlc():
    default tt = Tooltip("")
    vbox:
        style_prefix "dlc"
        hbox:
            if _renpysteam.dlc_installed(404910):
                add '404910_header'
            else:
                add '404910_header_sepia'
            null width (2 * gui.pref_spacing)
            vbox:
                label _("Extras")
                hbox:
                    if _renpysteam.dlc_installed(404910):
                        textbutton _("{font=[gui.fontawesome]}{/font} Open") action OpenDirectory('Extras/')
                        textbutton _("{font=[gui.fontawesome]}{/font} Gift") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 404910), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Delete") action [SetField(persistent, 'dlc', 'delete'), SetVariable('dlc_key', 404910), Jump('dlc')]
                    else:
                        textbutton _("{font=[gui.fontawesome]}{/font} Install") action [SetField(persistent, 'dlc', 'install'), SetVariable('dlc_key', 404910), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Add to cart") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 404910), Jump('dlc')]
        null height (4 * gui.pref_spacing)
        hbox:
            if _renpysteam.dlc_installed(375160):
                add '375160_header'
            else:
                add '375160_header_sepia'
            null width (2 * gui.pref_spacing)
            vbox:
                label _("Original Sound Track")
                hbox:
                    if _renpysteam.dlc_installed(375160):
                        textbutton _("{font=[gui.fontawesome]}{/font} Open") action OpenDirectory('Soundtrack/')
                        textbutton _("{font=[gui.fontawesome]}{/font} Manual"):
                            if _renpysteam.get_current_game_language() == 'koreana':
                                action OpenDirectory('Soundtrack/manual/discouraged_workers_ost_readme_ko.pdf')
                            else:
                                action OpenDirectory('Soundtrack/manual/discouraged_workers_ost_readme.pdf')
                        textbutton _("{font=[gui.fontawesome]}{/font} Gift") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 375160), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Delete") action [SetField(persistent, 'dlc', 'delete'), SetVariable('dlc_key', 375160), Jump('dlc')]
                    else:
                        textbutton _("{font=[gui.fontawesome]}{/font} Install") action [SetField(persistent, 'dlc', 'install'), SetVariable('dlc_key', 375160), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Add to cart") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 375160), Jump('dlc')]
        null height (4 * gui.pref_spacing)
        hbox:
            if _renpysteam.dlc_installed(382390):
                add '382390_header'
            else:
                add '382390_header_sepia'
            null width (2 * gui.pref_spacing)
            vbox:
                label _("Digital Art Book")
                hbox:
                    if _renpysteam.dlc_installed(382390):
                        textbutton _("{font=[gui.fontawesome]}{/font} View") action OpenDirectory('Books/discouraged_workers_art_book.pdf')
                        textbutton _("{font=[gui.fontawesome]}{/font} Gift") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 382390), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Delete") action [SetField(persistent, 'dlc', 'delete'), SetVariable('dlc_key', 382390), Jump('dlc')]
                    else:
                        textbutton _("{font=[gui.fontawesome]}{/font} Install") action [SetField(persistent, 'dlc', 'install'), SetVariable('dlc_key', 382390), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Add to cart") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 382390), Jump('dlc')]
        null height (4 * gui.pref_spacing)
        hbox:
            if _renpysteam.dlc_installed(384650):
                add '384650_header'
            else:
                add '384650_header_sepia'
            null width (2 * gui.pref_spacing)
            vbox:
                label _("Digital Concept Book")
                hbox:
                    if _renpysteam.dlc_installed(384650):
                        textbutton _("{font=[gui.fontawesome]}{/font} View"):
                            if _renpysteam.get_current_game_language() == 'koreana':
                                action OpenDirectory('Books/discouraged_workers_concept_book_ko.pdf')
                            elif _renpysteam.get_current_game_language() == 'russian':
                                action OpenDirectory('Books/discouraged_workers_concept_book_ru.pdf')
                            elif _renpysteam.get_current_game_language() == 'schinese':
                                action OpenDirectory('Books/discouraged_workers_concept_book_zh.pdf')
                            elif _renpysteam.get_current_game_language() == 'spanish':
                                action OpenDirectory('Books/discouraged_workers_concept_book_es.pdf')
                            else:
                                action OpenDirectory('Books/discouraged_workers_concept_book.pdf')
                        textbutton _("{font=[gui.fontawesome]}{/font} Gift") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 384650), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Delete") action [SetField(persistent, 'dlc', 'delete'), SetVariable('dlc_key', 384650), Jump('dlc')]
                    else:
                        textbutton _("{font=[gui.fontawesome]}{/font} Install") action [SetField(persistent, 'dlc', 'install'), SetVariable('dlc_key', 384650), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Add to cart") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 384650), Jump('dlc')]
        null height (4 * gui.pref_spacing)
        hbox:
            if _renpysteam.dlc_installed(407760):
                add '407760_header'
            else:
                add '407760_header_sepia'
            null width (2 * gui.pref_spacing)
            vbox:
                label _("MOD Creator Development Kit")
                hbox:
                    if _renpysteam.dlc_installed(407760):
                        textbutton _("{font=[gui.fontawesome]}{/font} Open") action OpenDirectory(renpy.config.basedir + '/MCDK/')
                        textbutton _("{font=[gui.fontawesome]}{/font} Gift") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 407760), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Delete") action [SetField(persistent, 'dlc', 'delete'), SetVariable('dlc_key', 407760), Jump('dlc')]
                    else:
                        textbutton _("{font=[gui.fontawesome]}{/font} Install") action [SetField(persistent, 'dlc', 'install'), SetVariable('dlc_key', 407760), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Add to cart") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 407760), Jump('dlc')]
        null height (4 * gui.pref_spacing)
        hbox:
            if _renpysteam.dlc_installed(375161):
                add '375161_header'
            else:
                add '375161_header_sepia'
            null width (2 * gui.pref_spacing)
            vbox:
                label _("Tarot PNP Pack")
                hbox:
                    if _renpysteam.dlc_installed(375161):
                        textbutton _("{font=[gui.fontawesome]}{/font} Open"):
                            if _renpysteam.get_current_game_language() == 'koreana':
                                action OpenDirectory('Books/kndw_tarot_ko.pdf')
                            elif _renpysteam.get_current_game_language() == 'russian':
                                action OpenDirectory('Books/kndw_tarot_ru.pdf')
                            elif _renpysteam.get_current_game_language() == 'schinese':
                                action OpenDirectory('Books/kndw_tarot_zh.pdf')
                            elif _renpysteam.get_current_game_language() == 'spanish':
                                action OpenDirectory('Books/kndw_tarot_es.pdf')
                            elif _renpysteam.get_current_game_language() == 'english':
                                action OpenDirectory('Books/kndw_tarot.pdf')
                            else:
                                action OpenDirectory('Books/')
                        textbutton _("{font=[gui.fontawesome]}{/font} Gift") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 375161), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Delete") action [SetField(persistent, 'dlc', 'delete'), SetVariable('dlc_key', 375161), Jump('dlc')]
                    else:
                        textbutton _("{font=[gui.fontawesome]}{/font} Install") action [SetField(persistent, 'dlc', 'install'), SetVariable('dlc_key', 375161), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Add to cart") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 375161), Jump('dlc')]
        null height (4 * gui.pref_spacing)
        hbox:
            if _renpysteam.dlc_installed(558690):
                add '558690_header'
            else:
                add '558690_header_sepia'
            null width (2 * gui.pref_spacing)
            vbox:
                label _("Back to the Basic")
                hbox:
                    if _renpysteam.dlc_installed(558690):
                        textbutton _("{font=[gui.fontawesome]}{/font} Open") action OpenDirectory('BTTB/')
                        textbutton _("{font=[gui.fontawesome]}{/font} Gift") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 558690), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Delete") action [SetField(persistent, 'dlc', 'delete'), SetVariable('dlc_key', 558690), Jump('dlc')]
                    else:
                        textbutton _("{font=[gui.fontawesome]}{/font} Install") action [SetField(persistent, 'dlc', 'install'), SetVariable('dlc_key', 558690), Jump('dlc')]
                        textbutton _("{font=[gui.fontawesome]}{/font} Add to cart") action [SetField(persistent, 'dlc', 'buy'), SetVariable('dlc_key', 558690), Jump('dlc')]
        null height (4 * gui.pref_spacing)
style dlc_text:
    color gui.accent_color
screen mod():
    vbox:
        style_prefix "dlc"
        for i in range(0, mod_name_len):
            $ mitem = mod_name[i]
            $ mdesc = mod_desc[i]
            $ mlabel = mod_label[i]
            hbox:
                add mlabel
                null width (2 * gui.pref_spacing)
                vbox:
                    label _(mitem)
                    text _(mdesc)
                    hbox:
                        textbutton _("{font=[gui.fontawesome]}{/font} Start") action [SetField(persistent, 'downloadable', False), Start(mlabel)]
            null height (4 * gui.pref_spacing)
screen esteregg_01():
    tag menu
    add 'ester_1'
    add im.Scale("gui/puzzle/_puzzle_field.webp", img_width, img_height) pos(puzzle_field_offset, puzzle_field_offset)
    draggroup:
        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s-%s"%(i,j)
                $ my_x = i*int(active_area_size*x_scale_index)+puzzle_field_offset
                $ my_y = j*int(active_area_size*y_scale_index)+puzzle_field_offset
                drag:
                    drag_name name
                    child im.Scale("gui/puzzle/_blank_space.webp", int(active_area_size*x_scale_index), int(active_area_size*y_scale_index) )
                    draggable False
                    xpos my_x ypos my_y
        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s-%s-piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    dragged esteregg_01
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]
screen esteregg_02():
    tag menu
    add 'ester_2'
    draggroup:
        drag:
            drag_name "ester_polaroid_01"
            child "arc_gall_10"
            droppable False
            dragged esteregg_02
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_02"
            child "arc_gall_11"
            droppable False
            dragged esteregg_02
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_03"
            child "arc_gall_12"
            droppable False
            dragged esteregg_02
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_04"
            child "arc_gall_13"
            droppable False
            dragged esteregg_02
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_05"
            child "arc_gall_14"
            droppable False
            dragged esteregg_02
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_06"
            child "arc_gall_15"
            droppable False
            dragged esteregg_02
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_07"
            child "arc_gall_16"
            droppable False
            dragged esteregg_02
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_08"
            child "arc_gall_17"
            droppable False
            dragged esteregg_02
            xpos 1580 ypos 702
        drag:
            drag_name "ester_order_01"
            child "lock"
            draggable False
            xpos 290 ypos 172
        drag:
            drag_name "ester_order_02"
            child "lock"
            draggable False
            xpos 620 ypos 172
        drag:
            drag_name "ester_order_03"
            child "lock"
            draggable False
            xpos 950 ypos 172
        drag:
            drag_name "ester_order_04"
            child "lock"
            draggable False
            xpos 1280 ypos 172
        drag:
            drag_name "ester_order_05"
            child "lock"
            draggable False
            xpos 290 ypos 540
        drag:
            drag_name "ester_order_06"
            child "lock"
            draggable False
            xpos 620 ypos 540
        drag:
            drag_name "ester_order_07"
            child "lock"
            draggable False
            xpos 950 ypos 540
        drag:
            drag_name "ester_order_08"
            child "lock"
            draggable False
            xpos 1280 ypos 540
screen esteregg_03():
    tag menu
    add 'ester_3'
    add im.Scale("gui/puzzle/_puzzle_field.webp", img_width, img_height) pos(puzzle_field_offset, puzzle_field_offset)
    draggroup:
        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s-%s"%(i,j)
                $ my_x = i*int(active_area_size*x_scale_index)+puzzle_field_offset
                $ my_y = j*int(active_area_size*y_scale_index)+puzzle_field_offset
                drag:
                    drag_name name
                    child im.Scale("gui/puzzle/_blank_space.webp", int(active_area_size*x_scale_index), int(active_area_size*y_scale_index) )
                    draggable False
                    xpos my_x ypos my_y
        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s-%s-piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    dragged esteregg_01
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]
screen esteregg_04():
    tag menu
    add 'ester_4'
    draggroup:
        drag:
            drag_name "ester_polaroid_01"
            child "arc_gall_25"
            droppable False
            dragged esteregg_04
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_03"
            child "arc_gall_27"
            droppable False
            dragged esteregg_04
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_06"
            child "arc_gall_30"
            droppable False
            dragged esteregg_04
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_04"
            child "arc_gall_28"
            droppable False
            dragged esteregg_04
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_02"
            child "arc_gall_26"
            droppable False
            dragged esteregg_04
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_08"
            child "arc_gall_32"
            droppable False
            dragged esteregg_04
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_05"
            child "arc_gall_29"
            droppable False
            dragged esteregg_04
            xpos 1580 ypos 702
        drag:
            drag_name "ester_polaroid_07"
            child "arc_gall_31"
            droppable False
            dragged esteregg_04
            xpos 1580 ypos 702
        drag:
            drag_name "ester_order_01"
            child "lock"
            draggable False
            xpos 290 ypos 172
        drag:
            drag_name "ester_order_02"
            child "lock"
            draggable False
            xpos 620 ypos 172
        drag:
            drag_name "ester_order_03"
            child "lock"
            draggable False
            xpos 950 ypos 172
        drag:
            drag_name "ester_order_04"
            child "lock"
            draggable False
            xpos 1280 ypos 172
        drag:
            drag_name "ester_order_05"
            child "lock"
            draggable False
            xpos 290 ypos 540
        drag:
            drag_name "ester_order_06"
            child "lock"
            draggable False
            xpos 620 ypos 540
        drag:
            drag_name "ester_order_07"
            child "lock"
            draggable False
            xpos 950 ypos 540
        drag:
            drag_name "ester_order_08"
            child "lock"
            draggable False
            xpos 1280 ypos 540
screen wimcj_detail_001():
    tag menu
    add gui.main_menu_background
    style_prefix "main_menu"
    hbox xalign .5 yalign .5:
        vbox yalign .99:
            image 'trophy_57354' xalign .5
            null height 20
            label _('STORY')
            bar value AnimatedValue(value=1.0, range=1.0, delay=0.5, old_value=0.0)
            label _('SIZE')
            bar value AnimatedValue(value=0.2, range=1.0, delay=1.0, old_value=0.0)
            label _('TIME')
            bar value AnimatedValue(value=0.1, range=1.0, delay=1.5, old_value=1.0)
            label _('TRICK')
            bar value AnimatedValue(value=1.0, range=2.5, delay=3.0, old_value=0.0)
            hbox:
                style_prefix "return_button"
                textbutton _("{font=[gui.fontawesome]}{/font} Play") action Return()
                textbutton _("{font=[gui.fontawesome]}{/font} Return") action [mr.Stop(), MainMenu(confirm=False)]
        image 'wimcj_level_001'
screen wimcj_countdown():
    if wimcj_level == 1:
        timer 1 repeat True action If(wimcj_time > 30, true=SetVariable('wimcj_time', wimcj_time - 1), false=If(wimcj_time == 30, true=[Hide('wimcj_countdown'), Jump('wimcj_001_play')], false=If(wimcj_time > 10, true=SetVariable('wimcj_time', wimcj_time - 1), false=If(wimcj_time == 10, true=[Hide('wimcj_countdown'), Jump('wimcj_001_play')], false=If(wimcj_time > 0, true=SetVariable('wimcj_time', wimcj_time - 1), false=[Hide('wimcj_countdown'), Jump(wimcj_timer_jump)])))))
    else:
        timer 1 repeat True action If(wimcj_time > 0, true=SetVariable('wimcj_time', wimcj_time - 1), false=[Hide('wimcj_countdown'), Jump(wimcj_timer_jump)])
    if wimcj_time <= 9:
        text str(wimcj_time) color "#FF0000" font "gui/fonts/BrokenGlass.ttf" outlines[(1, "#000000cf", 0, 0)] size 256 at wimcj_timer_hurryup
    elif wimcj_time <= 29:
        text str(wimcj_time) color "#FF0000" font "gui/fonts/BrokenGlass.ttf" outlines[(1, "#000000cf", 0, 0)] size 256 at wimcj_timer_hurry
    else:
        text str(wimcj_time) xpos .01 ypos .01 color "#000" outlines[(1, "#ffffffcf", 0, 0)] font "gui/fonts/BrokenGlass.ttf" size 256 at wimcj_timer_normal
screen wimcj_level_nav():
    if renpy.variant("small"):
        textbutton '{font=[gui.fontawesome]}{/font}' text_color '#000' text_size 256 text_xalign .5 text_yalign .5 xsize 1920 ysize 128 background None hover_background 'wimcj_system_white' activate_sound 'se/wimcj_walk.opus' xalign .5 yalign 0:
            if wimcj_level == 1:
                if wimcj_level_001_move == 0:
                    action [SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 1:
                    action Jump('wimcj_001_play')
                if wimcj_level_001_move == 2:
                    action [SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 3:
                    action Jump('wimcj_001_play')
                if wimcj_level_001_move == 4:
                    action Jump('wimcj_001_play')
                if wimcj_level_001_move == 5:
                    action [SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 6:
                    action [SetVariable('wimcj_level_001_move', 15), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 7:
                    action Jump('wimcj_001_play')
                if wimcj_level_001_move == 8:
                    action [SetVariable('wimcj_level_001_move', 9), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 9:
                    action Jump('wimcj_001_play')
                if wimcj_level_001_move == 10:
                    action Jump('wimcj_001_play')
                if wimcj_level_001_move == 11:
                    action [SetVariable('wimcj_level_001_move', 3), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 12:
                    action [SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 13:
                    action [SetVariable('wimcj_level_001_move', 14), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 14:
                    action Jump('wimcj_001_play')
                if wimcj_level_001_move == 15:
                    action Jump('wimcj_001_play')
        textbutton '{font=[gui.fontawesome]}{/font}' text_color '#000' text_size 256 text_xalign .5 text_yalign .5 xsize 1920 ysize 128 background None hover_background 'wimcj_system_white' activate_sound 'se/wimcj_walk.opus' xalign .5 yalign .999:
            if wimcj_level == 1:
                if wimcj_level_001_move == 0:
                    action [SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 1:
                    action [SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 2:
                    action [SetVariable('wimcj_level_001_move', 0), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 3:
                    action [SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 4:
                    action [SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 5:
                    action [SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 6:
                    action [SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 7:
                    action [SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 8:
                    action [SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 9:
                    action [SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 10:
                    action [SetVariable('wimcj_level_001_move', 9), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 11:
                    action [SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 12:
                    action [SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 13:
                    action [SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 14:
                    action [SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 15:
                    action [SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        textbutton '{font=[gui.fontawesome]}{/font}' text_color '#000' text_size 256 text_xalign .5 text_yalign .5 xsize 128 ysize 1080 background None hover_background 'wimcj_system_white' activate_sound 'se/wimcj_walk.opus' xalign 0 yalign .5:
            if wimcj_level == 1:
                if wimcj_level_001_move == 0:
                    action [SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 1:
                    action [SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 2:
                    action [SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 3:
                    action [SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 4:
                    action [SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 5:
                    action [SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 6:
                    action [SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 7:
                    action [SetVariable('wimcj_level_001_move', 12), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 8:
                    action [SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 9:
                    action [SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 10:
                    action [SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 11:
                    action [SetVariable('wimcj_level_001_move', 0), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 12:
                    action [SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 13:
                    action [SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 14:
                    action [SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 15:
                    action [SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        textbutton '{font=[gui.fontawesome]}{/font}' text_color '#000' text_size 256 text_xalign .5 text_yalign .5 xsize 128 ysize 1080 background None hover_background 'wimcj_system_white' activate_sound 'se/wimcj_walk.opus' xalign .999 yalign .5:
            if wimcj_level == 1:
                if wimcj_level_001_move == 0:
                    action [SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 1:
                    action [SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 2:
                    action [SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 3:
                    action [SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 4:
                    action [SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 5:
                    action [SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 6:
                    action [SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 7:
                    action [SetVariable('wimcj_level_001_move', 13), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 8:
                    action [SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 9:
                    action [SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 10:
                    action [SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 11:
                    action [SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 12:
                    action [SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 13:
                    action [SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 14:
                    action [SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
                if wimcj_level_001_move == 15:
                    action [SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
    if wimcj_level == 1:
        if wimcj_level_001_move == 0:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 1:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 2:
            key 'K_UP' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 0), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 0), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 0), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 3:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 4:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 5:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 6:
            key 'K_UP' action [Play("sound", 'se/wimcj_kitchen.opus'), SetVariable('wimcj_level_001_move', 15), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_kitchen.opus'), SetVariable('wimcj_level_001_move', 15), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_kitchen.opus'), SetVariable('wimcj_level_001_move', 15), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 7:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 12), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 13), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 12), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 13), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 5), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 12), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 13), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 8:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 9), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 9), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 9), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 9:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 10), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 10:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 9), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 9), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 9), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_door.opus'), SetVariable('wimcj_level_001_move', 11), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 8), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 11:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 3), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 0), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 3), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 0), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 3), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 0), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 12:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 13:
            key 'K_UP' action [Play("sound", 'se/wimcj_kitchen.opus'), SetVariable('wimcj_level_001_move', 14), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_kitchen.opus'), SetVariable('wimcj_level_001_move', 14), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_kitchen.opus'), SetVariable('wimcj_level_001_move', 14), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 7), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 14:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 2), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        if wimcj_level_001_move == 15:
            key 'K_UP' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'K_DOWN' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_LEFT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'K_RIGHT' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_lefty_neg' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_lefty_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_neg' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_leftx_pos' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpup_press' action [Play("sound", 'se/wimcj_walk.opus'), Jump('wimcj_001_play')]
            key 'pad_dpdown_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 6), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpleft_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 4), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_dpright_press' action [Play("sound", 'se/wimcj_walk.opus'), SetVariable('wimcj_level_001_move', 1), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
screen wimcj_level_001():
    style_prefix 'wimcj_level_say'
    if wimcj_level_001_move == 0:
        add 'wimcj_level_001_01'
        if wimcj_time <= 29:
            text 'Help….'
        else:
            text 'Hmm….'
    if wimcj_level_001_move == 1:
        add 'wimcj_level_001_02'
        if wimcj_time <= 29:
            text '….'
        else:
            text 'My bed.'
    if wimcj_level_001_move == 2:
        add 'wimcj_level_001_03'
        if wimcj_time <= 29:
            text 'There is no plastic bag.'
        else:
            text 'There is no jam on the bookshelf.{w=.3} And toilet…?'
    if wimcj_level_001_move == 3:
        add 'wimcj_level_001_04'
        text '….'
    if wimcj_level_001_move == 4:
        add 'wimcj_level_001_05'
        if wimcj_time <= 29:
            text 'Help….'
        else:
            text 'My room is very small.'
    if wimcj_level_001_move == 5:
        add 'wimcj_level_001_06'
        if wimcj_time <= 29:
            text "It seems to be around…."
        else:
            text "It seems to be around.{w=.3} But it's not in the refrigerator."
    if wimcj_level_001_move == 6:
        add 'wimcj_level_001_07'
        if wimcj_time <= 29:
            text 'Help….'
        else:
            text 'I stare at my reflection in the mirror.{w=.3} Are you happy now?'
    if wimcj_level_001_move == 7:
        add 'wimcj_level_001_08'
        if wimcj_time <= 29:
            text "It's near."
        else:
            text 'The water coming out of well.'
    if wimcj_level_001_move == 8:
        add 'wimcj_level_001_13'
        text '….'
    if wimcj_level_001_move == 9:
        add 'wimcj_level_001_14'
        if wimcj_time <= 29:
            text '….'
        else:
            text "It's me."
    if wimcj_level_001_move == 10:
        add 'wimcj_level_001_15'
        if wimcj_time <= 29:
            text 'Please….'
        else:
            text '….'
    if wimcj_level_001_move == 11:
        add 'wimcj_level_001_16'
        if wimcj_time <= 29:
            text 'Somebody…, help me….'
        else:
            text 'My bed.'
    if wimcj_level_001_move == 12:
        add 'wimcj_level_001_09'
        if wimcj_time <= 29:
            text 'Not there!'
        else:
            text "It's a washing machine,{w=.3} and a gas stove."
    if wimcj_level_001_move == 13:
        add 'wimcj_level_001_10'
        if wimcj_time <= 29:
            text 'Open it!'
            key 'K_SPACE' action [Play("sound", 'se/wimcj_kitchen.opus'), SetVariable('wimcj_level_001_move', 14), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
            key 'pad_a_press' action [Play("sound", 'se/wimcj_kitchen.opus'), SetVariable('wimcj_level_001_move', 14), SetVariable('wimcj_time', wimcj_time - 1), Jump('wimcj_001_play')]
        else:
            text "I don't have any kitchen tools."
    if wimcj_level_001_move == 14:
        add 'wimcj_level_001_11'
        if wimcj_time <= 29:
            text 'Take out it!'
        else:
            text "It's a cat plastic bag."
        if wimcj_level_001_trick_1 == 1:
            imagebutton idle 'level_001_obj_001' action [Play("sound", 'se/wimcj_plastic_bag.opus'), Jump('wimcj_001_bag')] xpos 0.3937 ypos 0.362
            key 'K_SPACE' action [Play("sound", 'se/wimcj_plastic_bag.opus'), Jump('wimcj_001_bag')]
            key 'pad_a_press' action [Play("sound", 'se/wimcj_plastic_bag.opus'), Jump('wimcj_001_bag')]
        else:
            image 'level_001_obj_001' xpos 0.3937 ypos 0.362
    if wimcj_level_001_move == 15:
        add 'wimcj_level_001_12'
        text '….'
    if wimcj_time <= 29:
        add 'wimcj_system_gall_black'
    if wimcj_time <= 9:
        add 'wimcj_system_black'
    use wimcj_level_nav
    use wimcj_countdown
screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 9
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text
style skip_frame:
    ypos gui.skip_ypos background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile) padding gui.skip_frame_borders.padding
style skip_text:
    size gui.notify_text_size
style skip_triangle:
    font "gui/fonts/DejaVuSans.ttf"
screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text message
    timer 3.25 action Hide('notify')
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
style notify_frame is empty
style notify_text is gui_text
style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
style notify_text:
    size gui.notify_text_size
screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing
        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)
        else:
            use nvl_dialogue(dialogue)
        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"
    add SideImage() xalign 0.0 yalign 1.0
screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            fixed:
                yfit gui.nvl_height is None
                if d.who is not None:
                    text d.who:
                        id d.who_id
                text d.what:
                    id d.what_id
style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text
style nvl_window:
    xfill True yfill True background "gui/nvl.webp" padding gui.nvl_borders.padding
style nvl_entry:
    xfill True ysize gui.nvl_height
style nvl_label:
    xpos gui.nvl_name_xpos xanchor gui.nvl_name_xalign ypos gui.nvl_name_ypos yanchor 0.0 xsize gui.nvl_name_width min_width gui.nvl_name_width text_align gui.nvl_name_xalign
style nvl_dialogue:
    xpos gui.nvl_text_xpos xanchor gui.nvl_text_xalign ypos gui.nvl_text_ypos xsize gui.nvl_text_width min_width gui.nvl_text_width text_align gui.nvl_text_xalign layout ("subtitle" if gui.nvl_text_xalign else "tex") color gui.accent_color
style nvl_thought:
    xpos gui.nvl_thought_xpos xanchor gui.nvl_thought_xalign ypos gui.nvl_thought_ypos xsize gui.nvl_thought_width min_width gui.nvl_thought_width text_align gui.nvl_thought_xalign layout ("subtitle" if gui.nvl_text_xalign else "tex") color gui.accent_color
style nvl_button:
    properties gui.button_properties("nvl_button") xpos gui.nvl_button_xpos xanchor gui.nvl_button_xalign
style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
style pref_vbox:
    variant "medium" xsize 675
style window:
    variant "small" background "gui/phone/dialogue.webp"
style nvl_window:
    variant "small" background "gui/phone/nvl.webp"
style main_menu_frame:
    variant "small" background "gui/phone/overlay/main_menu.webp"
style game_menu_outer_frame:
    variant "small" background "gui/phone/overlay/game_menu.webp"
style game_menu_navigation_frame:
    variant "small" xsize 510
style game_menu_content_frame:
    variant "small" top_margin 0
style pref_vbox:
    variant "small" xsize 600
style slider_pref_vbox:
    variant "small" xsize None
style slider_pref_slider:
    variant "small" xsize 900
