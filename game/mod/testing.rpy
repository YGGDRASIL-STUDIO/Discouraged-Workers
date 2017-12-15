init:
    image blahblah = 'mod/testing/testing_header.webp'
    $ mod_name.append("testing")
    $ mod_desc.append("1st MOD is testing")
    $ mod_label.append("blahblah")
label blahblah:
    show screen key_screen
    stop music
    $ show_quick_menu = True
    play music 'bgm/Love song.opus' fadein 3
    scene wall
    show g_smile
    ga "Hello?{w=.3} Long time no see.{w=.3} I am Choi Ga-yeon."
    ga "I am called here with the command '{b}show g_smile{/b}'."
    ga "Before that,{w=.3} the {b}wall background{/b} was called behind me with the command '{b}scene wall{/b}'."
    ga "My character name is {b}ga{/b}.{w=.3} It has the name '{b}Ga-yeon{/b}' and {b}black dialogue window{/b}."
    ga "{size=+10}To summarize:{/size}"
    ga "label blahblah:\n{space=50}scene wall\n{space=50}show g_smile\n{space=50}ga \"my dialogue.\""
    ga "{b}Discouraged Workers{/b} is created with {b}Ren\'Py Visual Novel Engine{/b}.{w=.3} So I suggest that you check the {a=https://www.renpy.org/doc/html/index.html}{color=#fff}Ren\'Py Documentation{/color}{/a},{w=.3} with {a=https://github.com/YGGDRASIL-STUDIO/Discouraged-Workers/wiki}{color=#fff}Discouraged Workers Wiki{/color}{/a}."
    ga "Thank you for coming to see me,{w=.3} and I hope you do not hate me."
    ga "Then I hope see you again next time in {b}YOUR MOD{/b}.{w=.3} Good bye."
    stop music fadeout 3
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