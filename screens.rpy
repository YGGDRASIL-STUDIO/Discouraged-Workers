screen say:
    default side_image = None
    default two_window = False
    if not two_window:
        window:
            id "window"
            has vbox:
                style "say_vbox"
            if who:
                text who id "who"
            text what id "what"
    else:
        vbox:
            style "say_two_window_vbox"
            if who:
                window:
                    style "say_who_window"
                    text who:
                        id "who"
            window:
                id "window"
                has vbox:
                    style "say_vbox"
                text what id "what"
    if side_image:
        add side_image xalign 0.0 yalign 1.0
    else:
        add SideImage() xalign 0.0 yalign 1.0
    if show_quick_menu:
        use quick_menu
screen choice:
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5
        vbox:
            style "menu"
            spacing 2
            for caption, action, chosen in items:
                if action:
                    button:
                        action action
                        style "menu_choice_button"
                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"
screen nvl:
    window:
        style "nvl_window"
        has vbox:
            style "nvl_vbox"
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if who is not None:
                    text who id who_id
                text what id what_id
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"
    add SideImage() xalign 0.0 yalign 1.0
    use quick_menu
screen main_menu:
    tag menu
    add 'dw'
    if persistent.korean is False:
        hbox xalign 0.5 yalign 0.05:
            imagebutton idle 'continueg' hover 'continue' hover_background "#f7f7f7" action ShowMenu('load') at menuback
            imagebutton idle 'startg' hover 'start' hover_background "#f7f7f7" action Start() at menuback
            imagebutton idle 'archivesg' hover 'archives' hover_background "#f7f7f7" action ShowMenu('archives') at menuback
        hbox xalign 0.5 yalign 0.5:
            imagebutton idle 'creditsg' hover 'credits' hover_background "#f7f7f7" action ShowMenu('credits') at menuback
            imagebutton idle 'configrationg' hover 'configration' hover_background "#f7f7f7" action ShowMenu('preferences') at menuback
            imagebutton idle 'closeg' hover 'close' hover_background "#f7f7f7" action Quit(confirm=False) at menuback
    else:
        hbox xalign 0.5 yalign 0.05:
            imagebutton idle 'continueg_ko' hover 'continue_ko' hover_background "#f7f7f7" action ShowMenu('load') at menuback
            imagebutton idle 'startg_ko' hover 'start_ko' hover_background "#f7f7f7" action Start() at menuback
            imagebutton idle 'archivesg_ko' hover 'archives_ko' hover_background "#f7f7f7" action ShowMenu('archives') at menuback
        hbox xalign 0.5 yalign 0.5:
            imagebutton idle 'creditsg_ko' hover 'credits_ko' hover_background "#f7f7f7" action ShowMenu('credits') at menuback
            imagebutton idle 'configrationg_ko' hover 'configration_ko' hover_background "#f7f7f7" action ShowMenu('preferences') at menuback
            imagebutton idle 'closeg_ko' hover 'close_ko' hover_background "#f7f7f7" action Quit(confirm=False) at menuback
screen file_picker():
    add 'dw'
    hbox yalign .2:
        style_group "pref"
        for i in range(1):
            textbutton "{font=fontawesome.ttf}{/font} Bookmark" action FilePage(i)
        textbutton "{font=fontawesome.ttf}{/font} Auto" action FilePage("auto")
        textbutton "{font=fontawesome.ttf}{/font} Previous" action FilePagePrevious()
        textbutton "{font=fontawesome.ttf}{/font} Next" action FilePageNext()
    $ columns = 3
    $ rows = 1
    grid columns rows:
        transpose True
        xfill True
        yalign .4
        for i in range(1, columns * rows + 1):
            button top_padding 10:
                action FileAction(i)
                xfill True
                has vbox
                add FileScreenshot(i)
                $ file_time = FileTime(i, empty=_("Empty Slot."))
                text "{font=fontawesome.ttf}{/font} [file_time!t]"
                key "save_delete" action FileDelete(i)
    vbox yalign .7:
        style_group "pref"
        textbutton "{font=fontawesome.ttf}{/font} Return" action Return()
screen save:
    tag menu
    use file_picker()
    key 'K_b' action Return()
screen load:
    tag menu
    use file_picker()
    key 'K_b' action Return()
screen rtcommon:
    hbox yalign .7:
        style_group "arc"
        textbutton "{font=fontawesome.ttf}{/font} Return" action Return()
screen crecommon:
    tag menu
    add 'dw'
    hbox yalign .1:
        style_group "arcc"
        textbutton "{font=fontawesome.ttf}{/font} Credits" action ShowMenu('credits')
        textbutton "{font=fontawesome.ttf}{/font} Authorship" action ShowMenu('authorship')
        textbutton "{font=fontawesome.ttf}{/font} Sponsor" action ShowMenu('sponsor')
        textbutton "{font=fontawesome.ttf}{/font} Supporter" action ShowMenu('supporter')
screen credits:
    tag menu
    use crecommon
    use sns
    use rtcommon
    vbox yalign .25:
        style_group "arcc"
        spacing 10
        text "{b}Lee Yunseok{/b}: Directing, Design, Programming, Music, Sound, TA, Writing, Packaging, Video, Website -April 21, 2013"
        text "{b}YANG{/b}: Male sprites, CG sprites -April 8, 2015"
        text "{b}Ga Younghee{/b}: English Translator -April 11, 2015"
        text "{b}chibilis studio{/b}: Female sprites, CG sprite-Eternal Happiness -March 10~April 6, 2015"
        text "{b}Jeon Junsik{/b}: Unofficial demo sprites -January 05~February 25, 2015"
    vbox yalign .43:
        style_group "arcc"
        spacing 20
        label '{font=fontawesome.ttf}{/font} Special Thanks to'
        text "{b}Kim Sooyoung, Lee Illseong, Tom Rothamel, Christopher rice, Reyeon, Pixabay, George Winston, AND YOU{/b}"
screen authorship:
    tag menu
    use crecommon
    vbox yalign .2:
        style_group "arcc"
        spacing 5
        label '{font=fontawesome.ttf}{/font} Authorship by'
        text 'NanumFont by Naver Corporation, Font Awesome by Dave Gandy'
        text 'Flag set by Nordic Factory, Dialogue window by Vitachii sozaikan'
    vbox yalign .4:
        style_group "arcc"
        spacing 5
        label '{font=fontawesome.ttf}{/font} Actual Photos by'
        text 'Cafe by Monorail Coffee, Cheonggyecheon by lyu1388'
        text 'Festival world by Nagyman, Hof by byongsu'
        text 'Sanchon by Julie Facine, One room by J o'
        text 'Phone market by happydsdesign, Sinchon street by TF-urban'
    vbox yalign .6:
        style_group "arcc"
        label '{font=fontawesome.ttf}{/font} You can check detail, please view the Help-Credits.'
    hbox yalign .7:
        style_group "arc"
        if persistent.korean is False:
            textbutton "{font=fontawesome.ttf}{/font} Help" action OpenURL("http://yggdrasil-studio.github.io/Discouraged-Workers/README_demo.html")
        else:
            textbutton "{font=fontawesome.ttf}{/font} Help" action OpenURL("http://yggdrasil-studio.github.io/Discouraged-Workers/README_demo_ko.html")
        textbutton "{font=fontawesome.ttf}{/font} Return" action Return()
screen sponsor:
    tag menu
    use crecommon
    use rtcommon
    vbox yalign .4:
        style_group "arcc"
        spacing 10
        text '{b}ACOC, AV Media Lab, Axel Mertes,{/b}'
        text '{b}Brandon Tanimoto, Gwak Jaeryeol, Hong Eunki,{/b}'
        text '{b}Jeong Dongwon, Jeong Wookjin, Kim Hyeoncheol,{/b}'
        text '{b}Kim Myeongwook, Lee Gunhae, Lee Hyejin,{/b}'
        text '{b}Mojaeng, Oh Hyeonjun, Rewind{/b}'
screen supporter:
    tag menu
    use crecommon
    use rtcommon
    vbox yalign .4:
        style_group "arcc"
        spacing 10
        text '{b}Caz Woolley, Indie GameDev Bot, Indie Game Lover,{/b}'
        text '{b}Indie Games Devel, IndieVideoGames, Joachim Dimitri Jensen,{/b}'
        text '{b}Kim Kyeongtae, Kim Younghwan, Kurt Simon,{/b}'
        text '{b}Linda Lee King, Peter Christiansen, Sakimichi,{/b}'
        text '{b}Sebastian Haba, Spero Mcgee, The Indie Sloth,{/b}'
        text '{b}Vrachos, Xin Liu, Yu Shinhyeon{/b}'
screen preferences:
    tag menu
    add 'dw'
    #hbox yalign .1:
    #    style_group "arc"
    #    label "{font=fontawesome.ttf}{/font} Language"
    #hbox yalign .16:
    #    style_group "pref"
    #    spacing 10
    #    textbutton "English" action [Language(None), SetField(persistent, 'korean', False)]
    #    textbutton "한국어" action [Language('Korean'), SetField(persistent, 'korean', True)]
    hbox yalign .24:
        style_group "arc"
        label "{font=fontawesome.ttf}{/font} Volume"
    hbox yalign .30:
        style_group "pref"
        spacing 10
        textbutton "{font=fontawesome.ttf}{/font} Mute" action [Preference("music mute", "toggle"), Preference("sound mute", "toggle")]
        textbutton "{font=fontawesome.ttf}{/font} Min" action [Preference("music volume", 0.2), Preference("sound volume", 0.2)]
        textbutton "{font=fontawesome.ttf}{/font} Medium" action [Preference("music volume", 0.5), Preference("sound volume", 0.5)]
        textbutton "{font=fontawesome.ttf}{/font} Big" action [Preference("music volume", 0.7), Preference("sound volume", 0.7)]
        textbutton "{font=fontawesome.ttf}{/font} Max" action [Preference("music volume", 1.0), Preference("sound volume", 1.0)]
    hbox yalign .38:
        style_group "arc"
        label "{font=fontawesome.ttf}{/font} Archives alarm"
    hbox yalign .44:
        style_group "pref"
        spacing 10
        textbutton "{font=fontawesome.ttf}{/font} On" action SetField(persistent, 'alarm', True)
        textbutton "{font=fontawesome.ttf}{/font} Off" action SetField(persistent, 'alarm', False)
    hbox yalign .7:
        style_group "pref"
        spacing 10
        if persistent.korean is False:
            textbutton "{font=fontawesome.ttf}{/font} Help" action OpenURL("http://yggdrasil-studio.github.io/Discouraged-Workers/README_demo.html")
        else:
            textbutton "{font=fontawesome.ttf}{/font} Help" action OpenURL("http://yggdrasil-studio.github.io/Discouraged-Workers/README_demo_ko.html")
        textbutton "{font=fontawesome.ttf}{/font} Main" action MainMenu()
        textbutton "{font=fontawesome.ttf}{/font} Return" action Return()
        textbutton "{font=fontawesome.ttf}{/font} Quit" action Quit()
    key 'K_c' action Return()
screen yesno_prompt:
    modal True
    add 'dw'
    hbox yalign .3:
        style_group "pref"
        label _(message)
    hbox yalign .5:
        style_group "arc"
        spacing 100
        textbutton "{font=fontawesome.ttf}{/font} Yes" action yes_action
        textbutton "{font=fontawesome.ttf}{/font} No" action no_action
screen quick_menu:
    if persistent.korean is False:
        vbox xalign .0 yalign .9:
            imagebutton action ShowMenu('archives') idle 'arc' hover 'arc' at menuback
            imagebutton action ShowMenu('preferences') idle 'config' hover 'config' at menuback
        vbox xalign .99 yalign .9:
            imagebutton action Preference('auto-forward', 'toggle') idle 'play' hover 'play' selected_idle 'stop' selected_hover 'stop' at menuback
            imagebutton action ShowMenu('save') idle 'save' hover 'save' at menuback
    else:
        vbox xalign .0 yalign .9:
            imagebutton action ShowMenu('archives') idle 'arc_ko' hover 'arc_ko' at menuback
            imagebutton action ShowMenu('preferences') idle 'config_ko' hover 'config_ko' at menuback
        vbox xalign .99 yalign .9:
            imagebutton action Preference('auto-forward', 'toggle') idle 'play_ko' hover 'play_ko' selected_idle 'stop_ko' selected_hover 'stop_ko' at menuback
            imagebutton action ShowMenu('save') idle 'save_ko' hover 'save_ko' at menuback
    hbox xalign .5 yalign .9:
            bar value archives range 28 xmaximum 300 ymaximum 30
screen arccommon:
    tag menu
    add 'dw'
    hbox yalign .1:
        style_group "arc"
        textbutton "{font=fontawesome.ttf}{/font} Characters" action ShowMenu('characters')
        textbutton "{font=fontawesome.ttf}{/font} Concept" action ShowMenu('concept')
        textbutton "{font=fontawesome.ttf}{/font} Diary" action ShowMenu('diary')
        textbutton "{font=fontawesome.ttf}{/font} Gallery" action ShowMenu('gallery')
        textbutton "{font=fontawesome.ttf}{/font} Music" action ShowMenu('music_room')
screen sns:
    tag menu
    hbox yalign .59 xalign .5:
        spacing 10
        imagebutton idle 'steamg' hover 'steam' action OpenURL('http://steamcommunity.com/sharedfiles/filedetails/?id=399374348') at menuback
        if persistent.korean is False:
            imagebutton idle 'homeg' hover 'home' action OpenURL('https://yggdrasil-studio.github.io/Discouraged-Workers') at menuback
        else:
            imagebutton idle 'homeg' hover 'home' action OpenURL('https://yggdrasil-studio.github.io/Discouraged-Workers/index_ko.html') at menuback
        imagebutton idle 'facebookg' hover 'facebook' action OpenURL('https://www.facebook.com/YGGDRASILSTUDIO') at menuback
        imagebutton idle 'twitterg' hover 'twitter' action OpenURL('https://twitter.com/STUDIOYGGDRASIL') at menuback
        imagebutton idle 'googleg' hover 'google' action OpenURL('https://plus.google.com/111690235848207359251') at menuback
        imagebutton idle 'androidg' hover 'android' action OpenURL('https://play.google.com/store/apps/details?id=kr.indiegame.dw') at menuback
screen archives:
    tag menu
    use arccommon
    use rtcommon
    hbox xalign .5 yalign .35:
        add 'photos'
    key 'K_a' action Return()
screen arcbcommon:
    tag menu
    hbox yalign .7:
        style_group "arc"
        textbutton "{font=fontawesome.ttf}{/font} Return" action ShowMenu('archives')
screen characters:
    tag menu
    use arccommon
    use rtcommon
    if persistent.gayeon is False:
        hbox yalign .63:
            style_group "arc"
            label "{font=fontawesome.ttf}{/font} Unknown the information."
        hbox xalign .5 yalign .3:
             add 'photos'
    else:
        hbox ypos .16 xalign .5:
            style_group "arc"
            if persistent.interviewer is True:
                imagebutton idle 'intern' at arc_chars hover 'intern' action ShowMenu('interviewer')
            else:
                add 'intern' at arc_char
            if persistent.yunwoo is True:
                imagebutton idle 'yu' at arc_chars hover 'yu' action ShowMenu('yunwoo')
            else:
                add 'yu' at arc_char
            imagebutton idle 'p' at arc_chars hover 'p' action ShowMenu('gayeon')
            if persistent.hyena is True:
                imagebutton idle 'hy' at arc_chars hover 'hy' action ShowMenu('hyena')
            else:
                add 'hy' at arc_char
            if persistent.angel is True:
                imagebutton idle 'ex1' at arc_chars hover 'ex1' action ShowMenu('angel')
            else:
                add 'ex1' at arc_char
screen charbcommon:
    tag menu
    hbox yalign .7:
        style_group "arc"
        textbutton "{font=fontawesome.ttf}{/font} Return" action ShowMenu('characters')
screen gayeon:
    tag menu
    use arccommon
    use charbcommon
    hbox xalign .8 ypos .16:
        add 'p' at arc_char
    hbox xpos .1 ypos .2:
        vbox:
            style_group "arcu"
            spacing 10
            label "{b}Choi Ga-Yeon{/b}"
            text "{b}Birth:{/b} April 19th, 1986"
            text "{b}Blood Type:{/b} A(RH+)"
            text "{b}Height / Weight:{/b} 165cm / 48kg"
            text "{b}BWH:{/b} 81cm / 58cm / 86cm"
            text "{b}Bio:{/b} Discouraged worker / Leave of absence from\nHealth Administration of ○○ University"
            text "{b}Certificates:{/b} 1st class hospital coordinator / Hospital administrator"
            text "{b}Favorite:{/b} Begel, Margherita pizza, Sweet rice bun"
            text "{b}Dislike:{/b} Capitalism, Doctor, Member of parliament"
screen hyena:
    tag menu
    use arccommon
    use charbcommon
    button background '#fff' xpos .265 ypos .15 xsize 1410 ysize 554
    hbox xalign .8 ypos .16:
        add 'hy' at arc_char
    hbox xpos .1 ypos .2:
        vbox:
            style_group "arcu"
            spacing 10
            label "{b}Choi Hye-Na{/b}"
            text "{b}Birth:{/b} June 17th, 1989"
            text "{b}Blood Type:{/b} O(RH+)"
            text "{b}Height / Weight:{/b} 168cm / 48kg"
            text "{b}BWH:{/b} 92.5cm / 66cm / 92cm"
            text "{b}Bio:{/b} Karaoke helper / Graduated in Tourism Food & Beverage of ○○"
            text "{b}Certificates:{/b} 2nd class Barista"
            text "{b}Favorite:{/b} Money, Photography, Older sister, Drinking"
            text "{b}Dislike:{/b} Oryide, Sweet rice bun, Nightclub"
screen angel:
    tag menu
    use arccommon
    use charbcommon
    button background '#fff' xpos .265 ypos .15 xsize 1410 ysize 554
    hbox xalign .8 ypos .16:
        add 'ex1' at arc_char
    hbox xpos .1 ypos .2:
        vbox:
            style_group "arcu"
            spacing 10
            label "{b}Staff{/b}"
            text "Not available on the demo."
screen interviewer:
    tag menu
    use arccommon
    use charbcommon
    button background '#fff' xpos .265 ypos .15 xsize 1410 ysize 554
    hbox xalign .8 ypos .16:
        add 'intern' at arc_char
    hbox xpos .1 ypos .2:
        vbox:
            style_group "arcu"
            spacing 10
            label "{b}Interviewer{/b}"
            text "Not available on the demo."
screen yunwoo:
    tag menu
    use arccommon
    use charbcommon
    button background '#fff' xpos .265 ypos .15 xsize 1410 ysize 554
    hbox xalign .8 ypos .16:
        add 'yu' at arc_char
    hbox xpos .1 ypos .2:
        vbox:
            style_group "arcu"
            spacing 10
            label "{b}Kim Yun-Woo{/b}"
            text "{b}Birth:{/b} January 19th, 1986"
            text "{b}Blood Type:{/b} AB(RH+)"
            text "{b}Height / Weight:{/b} 172cm / 58kg"
            text "{b}Bio:{/b} Bassist of ○○"
            text "{b}Favorite:{/b} Bob Dylan, Choi Ga-Yeon, Yu Jae-Ha"
            text "{b}Dislike:{/b} Audition, Management, Soju"
screen music_room:
    tag menu
    add 'dw'
    use arccommon
    use rtcommon
    hbox yalign .16:
        style_group "pref"
        textbutton "Track 1. Pandemic"
        textbutton "Track 2. Sigh day" action mr.Play("bgm/Sigh day.ogg")
    hbox yalign .22:
        style_group "pref"
        textbutton "Track 3. Mare tranquillitatis" action mr.Play("bgm/Mare tranquillitatis.ogg")
        textbutton "Track 4. CCCanon" action mr.Play("bgm/CCCanon.ogg")
    hbox yalign .28:
        style_group "pref"
        textbutton "Track 5. Let's game" action mr.Play("bgm/Let's game.ogg")
        textbutton "Track 6. Peace" action mr.Play("bgm/Peace.ogg")
    hbox yalign .34:
        style_group "pref"
        textbutton "Track 7. Unknown mist" action mr.Play("bgm/Unknown mist.ogg")
        textbutton "Track 8. Lush garden" action mr.Play("bgm/Lush garden.ogg")
    hbox yalign .4:
        style_group "pref"
        textbutton "Track 9. Jormungandr" action mr.Play("bgm/Jormungandr.ogg")
        textbutton "Track 10. Nyx" action mr.Play("bgm/Nyx.ogg")
    hbox yalign .46:
        style_group "pref"
        textbutton "Track 11. Summit showdown"
        textbutton "Track 12. Love song" action mr.Play("bgm/Love song.ogg")
    hbox yalign .52:
        style_group "pref"
        textbutton "Track 13. Sea of nectar"
        textbutton "{font=fontawesome.ttf}{/font} Stop" action mr.Stop()
    hbox yalign .58:
        style_group "pref"
        textbutton "{font=fontawesome.ttf}{/font} Shuffle" action mr.ToggleShuffle()
        textbutton "{font=fontawesome.ttf}{/font} Loop" action mr.ToggleSingleTrack()
    hbox yalign .64:
        style_group "pref"
        textbutton "{font=fontawesome.ttf}{/font} Previous" action mr.Previous()
        textbutton "{font=fontawesome.ttf}{/font} Next" action mr.Next()
    on "replace" action mr.Play()
    on "replaced" action Play("music", "bgm/Love song.ogg")
screen concept:
    tag menu
    use arccommon
    use rtcommon
    if persistent.korean is False:
        hbox yalign .4:
            style_group "arc"
            label "{font=fontawesome.ttf}{/font} Please wait for the next update."
    else:
        hbox yalign .16:
            style_group "pref"
            if persistent.con01 is False:
                textbutton "Discouraged worker"
            else:
                textbutton "Discouraged worker" action Show('concept01')
            textbutton "Reclusive outsider"
        hbox yalign .22:
            style_group "pref"
            textbutton "Medical referral"
            textbutton "Anxiety disorder"
        hbox yalign .28:
            style_group "pref"
            textbutton "Depressive disorder"
            textbutton "Bridge of the life"
        hbox yalign .34:
            style_group "pref"
            textbutton "IMF Crisis"
            textbutton "Accident"
        hbox yalign .4:
            style_group "pref"
            textbutton "Prologue" action Show('concept09')
            textbutton "Epilogue"
        hbox yalign .46:
            style_group "pref"
            textbutton "Flowery mornings and moonlit nights"
            textbutton "Mahalath leannoth"
        hbox yalign .52:
            style_group "pref"
            textbutton "Seohae grand bridge"
            textbutton "Red dialogue window"
screen conbcommon:
    tag menu
    hbox yalign .7:
        style_group "arc"
        textbutton "{font=fontawesome.ttf}{/font} Return" action ShowMenu('concept')
screen concept01:
    tag menu
    use arccommon
    use conbcommon
    vbox ypos .16 xpos .083 xsize 1600:
        style_group "arcu"
        spacing 20
        label "{b}Discouraged worker{/b}"
        text " discouraged worker is a person of legal employment age who is not actively seeking employment or who does not find employment after long-term unemployment. This is usually because an individual has given up looking or has had no success in finding a job, hence the term \"discouraged\"."
        text "https://en.wikipedia.org/wiki/Discouraged_worker"
screen concept09:
    tag menu
    use arccommon
    use conbcommon
    vbox ypos .16 xpos .083 xsize 1600:
        style_group "arcu"
        spacing 20
        label "{b}Prologue{/b}"
        text " A hospital coordinator, Ga-Yeon, fell in love with a doctor at the hospital she was working in and they had an affair even though the doctor was a married man. But when the director found out, she was fired. For over a year she tried to find another job, but her mental uneasiness eventually made her give up and she became a recluse."
        text " A year later, in the spring of 2013, her younger sister, Hye-Na, and her first love Yun-Woo come to her."
        text " A story about the dark side of today’s youth and pretty serious everyday life happening around Ga-Yeon."
        text " Discouraged Workers"
screen diary:
    tag menu
    use arccommon
    use rtcommon
    hbox yalign .4:
        style_group "arc"
        label "{font=fontawesome.ttf}{/font} Not available on the demo."
screen gallery:
    tag menu
    use arccommon
    use rtcommon
    grid 2 1:
        transpose True
        yalign .25 xalign .5
        if persistent.unlock_1 is False:
            button xsize 768 ysize 432:
                add 'lock'
        else:
            add g.make_button("that day we", "tdws")
        if persistent.unlock_2 is False:
            button xsize 768 ysize 432:
                add 'lock'
        else:
            add g.make_button("eternal happiness", "photos")
screen default_language:
    add 'dw'
    hbox xalign .5 yalign .2:
        style_group "pref"
        label "{font=fontawesome.ttf}{/font} Select your language."
    hbox xalign .5 yalign .4:
        imagebutton idle 'usg' hover 'us' hover_background "#f7f7f7" selected_idle 'us' selected_hover 'us' action [Language(None), SetField(persistent, 'korean', False)]
        imagebutton idle 'krg' hover 'kr' hover_background "#f7f7f7" selected_idle 'kr' selected_hover 'kr' action [Language('Korean'), SetField(persistent, 'korean', True)]
    hbox xalign .5 yalign .7:
        style_group "pref"
        textbutton "{font=fontawesome.ttf}{/font} Complete Select Language." action Return()
screen key_screen:
    key 'K_a' action ShowMenu('archives')
    key 'K_c' action ShowMenu('preferences')
    key 'K_b' action ShowMenu('save')
    key 'K_p' action Preference('auto-forward', 'toggle')
    if persistent.alarm is True:
        key 'K_n' action SetField(persistent, 'alarm', False)
    else:
        key 'K_n' action SetField(persistent, 'alarm', True)