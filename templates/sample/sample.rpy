init:
    image label_publishedfileid = 'publishedfileid_header.webp'
    $ mod_name.append("your_mod_name")
    $ mod_desc.append("your_mod_description")
    $ mod_label.append("label_publishedfileid")
label label_publishedfileid:
    show screen key_screen
    stop music
    $ show_quick_menu = True# edit True to False if your dialogues will show to centered.
    # write your story below.
    
    
    
    # end your mod
    if not achievement.has('KNDW_MOD_PLAYER'):
        scene main_menu
        show gradiant
        with blind
        show expression Text("[gui.unlocked]", style='unlocked_title') as text at spread
        pause 1
        show expression '7m_gold' at unlocked_center
        $ achievement.grant('KNDW_MOD_PLAYER')
        pause 1.5
        scene main_menu with blind
    return