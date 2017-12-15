screen default_language():
    tag menu
    modal True
    default tt = Tooltip("")
    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 3
    use game_menu(_("{font=[gui.fontawesome]}{/font} Basic Settings"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                vbox:
                    style_prefix "radio"
                    label _("{font=[gui.fontawesome]}{/font} Language")
                    textbutton ("{font=gui/fonts/NanumBarunGothic.ttf}English{/font}") action Language(None)
                    textbutton ("{font=gui/fonts/NanumBarunGothic.ttf}한국어{/font}") action Language('Korean')
                    textbutton ("{font=gui/fonts/NanumBarunGothic.ttf}Русский{/font}") action Language('Russian')
                    textbutton ("{font=gui/fonts/Merienda-Regular.ttf}Español{/font}") action Language('Spanish')
                    textbutton ("{font=gui/fonts/DroidSansFallback.ttf}{s}简体中文{/s}{/font}") #action Language('Chinese')
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("{font=[gui.fontawesome]}{/font} Controller")
                        textbutton _("{font=[gui.fontawesome]}{/font} Disable") action SetField(persistent, 'controllers', None) hovered tt.Action(_("Do not display any Controller images."))
                        textbutton _("{font=[gui.fontawesome]}{/font} Steam Controller") action SetField(persistent, 'controllers', 'steam') hovered tt.Action(_("Display the Steam Controller images."))
                        textbutton _("{font=[gui.fontawesome]}{/font} General Gamepad") action SetField(persistent, 'controllers', 'xbox') hovered tt.Action(_("Display the Xbox Controller images."))
                        textbutton _("{font=[gui.fontawesome]}{/font} {s}OUYA Controller{/s}")# action SetField(persistent, 'controllers', 'ouya') hovered tt.Action(_("Display the OUYA Controller images."))
                    # If the Steam can't sync your granted achievements, remove the sharp(#) in bottom three lines and run the Discouraged Workers, click the Sync with Steam.
                    #vbox:
                        #label _("{font=[gui.fontawesome]}{/font} Steamworks")
                        #textbutton _("{font=[gui.fontawesome]}{/font} Sync with Steam") action Jump('sync')
                    # If you want to reset all progress, remove the sharp(#) in bottom three lines and run the Discouraged Workers, click the reset all. This will removes all saves and persistents, Steam achievements.
                    #vbox:
                        #label _("{font=[gui.fontawesome]}{/font} Reset all")
                        #textbutton _("{font=[gui.fontawesome]}{/font} Reset all") action Jump('reset')
                if renpy.variant("mobile"):
                    vbox:
                        style_prefix "radio"
                        label _("{font=[gui.fontawesome]}{/font} Vibrate")
                        textbutton _("{font=[gui.fontawesome]}{/font} Enable") action SetField(persistent, 'vibrate', True)
                        textbutton _("{font=[gui.fontawesome]}{/font} Disable") action SetField(persistent, 'vibrate', None)
            null height (4 * gui.pref_spacing)
            hbox:
                box_wrap True
                vbox:
                    style_prefix "radio"
                    label _("{font=[gui.fontawesome]}{/font} Tic disorder")
                    textbutton _("{font=[gui.fontawesome]}{/font} Enable") action SetField(persistent, 'tic', True) hovered tt.Action(_("This will activate Ga-yeon's tic disorder."))
                    textbutton _("{font=[gui.fontawesome]}{/font} Disable") action SetField(persistent, 'tic', None) hovered tt.Action(_("This will deactivate Ga-yeon's tic disorder."))
                vbox:
                    style_prefix "radio"
                    label _("{font=[gui.fontawesome]}{/font} Epilepsy-friendly")
                    textbutton _("{font=[gui.fontawesome]}{/font} Enable") action SetField(persistent, 'epilepsy', True) hovered tt.Action(_("This will disable some screen effects for people who have epilepsy or similar photosensitive disorders."))
                    textbutton _("{font=[gui.fontawesome]}{/font} Disable") action SetField(persistent, 'epilepsy', None)
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("{font=[gui.fontawesome]}{/font} Blind-friendly")
                        textbutton _("{font=[gui.fontawesome]}{/font} Enable") action [SetField(_preferences, 'self_voicing', True), SetField(persistent, 'blind', True)] hovered tt.Action(_("This will activate the blind-friendly features with the self-voicing feature."))
                        textbutton _("{font=[gui.fontawesome]}{/font} Disable") action [SetField(_preferences, 'self_voicing', False), SetField(persistent, 'blind', None)] hovered tt.Action(_("This will disable the blind-friendly features."))
            null height (4 * gui.pref_spacing)
            label tt.value