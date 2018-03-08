screen default_language():
    tag menu
    modal True
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
                    textbutton ("{font=gui/fonts/Merienda-Regular.ttf}Español(Beta){/font}") action Language('Spanish')
                    textbutton ("{font=gui/fonts/DroidSansFallback.ttf}简体中文{/font}") action Language('Chinese')
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("{font=[gui.fontawesome]}{/font} Controller")
                        textbutton _("{font=[gui.fontawesome]}{/font} Disable") action SetField(persistent, 'controllers', None) tooltip _("Do not display any Controller images.")
                        textbutton _("{font=[gui.fontawesome]}{/font} Steam Controller") action SetField(persistent, 'controllers', 'steam') tooltip _("Display the Steam Controller images.")
                        textbutton _("{font=[gui.fontawesome]}{/font} General Gamepad") action SetField(persistent, 'controllers', 'xbox') tooltip _("Display the Xbox Controller images.")
                        textbutton _("{font=[gui.fontawesome]}{/font} {s}OUYA Controller{/s}")# action SetField(persistent, 'controllers', 'ouya') tooltip _("Display the OUYA Controller images.")
                    if persistent.opening is True:
                        vbox:
                            if persistent.steam is True:
                                label _("{font=[gui.fontawesome]}{/font} Steamworks")
                                textbutton _("{font=[gui.fontawesome]}{/font} Sync with Steam") action Jump('sync') tooltip _("This will sync your missing Steam Achievements from sync error with Steam.")
                                textbutton _("{font=[gui.fontawesome]}{/font} Reset Achievements") action Jump('rmsteam') tooltip _("This will reset your Steam Achievements progress.")
                            label _("{font=[gui.fontawesome]}{/font} Reset")
                            textbutton _("{font=[gui.fontawesome]}{/font} Persistent") action Jump('reset') tooltip _("This will delete your local persistent data.")
                            textbutton _("{font=[gui.fontawesome]}{/font} Reset all") action Jump('resetall') tooltip _("This will reset all your progress, including local persistent and saved data, and Steam Achievements")
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
                    textbutton _("{font=[gui.fontawesome]}{/font} Enable") action SetField(persistent, 'tic', True) tooltip _("This will activate Ga-yeon's tic disorder.")
                    textbutton _("{font=[gui.fontawesome]}{/font} Disable") action SetField(persistent, 'tic', None) tooltip _("This will deactivate Ga-yeon's tic disorder.")
                vbox:
                    style_prefix "radio"
                    label _("{font=[gui.fontawesome]}{/font} Epilepsy-friendly")
                    textbutton _("{font=[gui.fontawesome]}{/font} Enable") action SetField(persistent, 'epilepsy', True) tooltip _("This will disable some screen effects for people who have epilepsy or similar photosensitive disorders.")
                    textbutton _("{font=[gui.fontawesome]}{/font} Disable") action SetField(persistent, 'epilepsy', None)
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("{font=[gui.fontawesome]}{/font} Blind-friendly")
                        textbutton _("{font=[gui.fontawesome]}{/font} Enable") action [SetField(_preferences, 'self_voicing', True), SetField(persistent, 'blind', True), SetMixer('music', 0.5), SetField(_preferences, "video_image_fallback", True)] tooltip _("This will activate the blind-friendly features with the self-voicing feature.")
                        textbutton _("{font=[gui.fontawesome]}{/font} Disable") action [SetField(_preferences, 'self_voicing', False), SetField(persistent, 'blind', None), SetMixer('music', 1.0), SetField(_preferences, "video_image_fallback", False)] tooltip _("This will disable the blind-friendly features.")
            null height (4 * gui.pref_spacing)
            label GetTooltip()
