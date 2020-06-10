translate Russian style main_menu_title:
    xalign .5 yoffset -700 size gui.title_text_size - 10 font gui.main_font
if renpy.variant("small"):
    translate Russian style credits_text:
        font "gui/fonts/NanumBarunGothic.ttf"
    translate Russian style thanks_text:
        yalign .85
translate Russian python:
    gui.system_font = gui.text_font = gui.interface_text_font = gui.button_text_font = "gui/fonts/DejaVuSans.ttf"
    gui.main_font = "gui/fonts/IntroCondBlackFree.otf"
    gui.name_text_font = "gui/fonts/DejaVuSans-Bold.ttf"
    gui.quick_hbox_xpos = .809
    config.name = "Отчаявшиеся работники"
    config.window_title = u"Отчаявшиеся работники"
    if renpy.variant("small"):
        config.translations["{font=[gui.fontawesome]}{/font} Basic Settings"] = u"{font=[gui.fontawesome]}{/font} Основы"
        config.translations["{font=[gui.fontawesome]}{/font} Main Menu"] = u"{font=[gui.fontawesome]}{/font} Меню"
        config.translations["{font=[gui.fontawesome]}{/font} Seen Text"] = u"{font=[gui.fontawesome]}{/font} Прочтённых"
        config.translations["{font=[gui.fontawesome]}{/font} Mute All"] = u"{font=[gui.fontawesome]}{/font} Без звука"
        config.translations["{font=[gui.fontawesome]}{/font} Authors"] = u"{font=[gui.fontawesome]}{/font} Авторское"
        config.translations['ACOC, Aiman Sharul, Axel Mertes, Bgame, Brandon Tanimoto, Brian Connors, BRISAK Kim Doohyeon, cheif.choi, Choi Irang, Choi Jihye, cloture, Danielle Bell, Edward N Puckering, Gary King, Gwak Jaeryeol, Han Ihyeong, Hoe Namyoon, Hong Eunki, Hwang Daehoon, Hyojoon, James Emmerson, Jeong Dongwon, Jeong Wookjin, Jeong Yoonsoo, Jianmin Zhang,\nKarina Schulze, Keira Val\'Azr, Kim Hanseol, Kim Hyeoncheol, Kim Jaeseong, Kim Jeongwoong, Kim Myeongwook,\nLee Changki, Lee Eunji, Lee Gunhae, Lee Hyejin, Lee Jaewi, Light Twins, Lim Jisoo, Maddy Wootton,\nMarshall Proudfoot, Mirumu, Mojaeng, Oh Hyeonjun, Park Hyeonjun, Park JoonKoo, Rewind, Sander Tieleman, srwss, Sung Chanaul, YottaCho, Zerial.net'] = u'ACOC, Aiman Sharul, Axel Mertes, Bgame, Brandon Tanimoto, Brian Connors,\nBRISAK Kim Doohyeon, cheif.choi, Choi Irang,\nChoi Jihye, cloture, Danielle Bell,\nEdward N Puckering, Gary King, Gwak Jaeryeol, Han Ihyeong, Hoe Namyoon, Hong Eunki,\nHwang Daehoon, Hyojoon, James Emmerson,\nJeong Dongwon, Jeong Wookjin, Jeong Yoonsoo,\nJianmin Zhang, Karina Schulze, Keira Val\'Azr,\nKim Hanseol, Kim Hyeoncheol, Kim Jaeseong,\nKim Jeongwoong, Kim Myeongwook,\nLee Changki, Lee Eunji, Lee Gunhae,\nLee Hyejin, Lee Jaewi, Light Twins, Lim Jisoo,\nMaddy Wootton, Marshall Proudfoot, Mirumu,\nMojaeng, Oh Hyeonjun, Park Hyeonjun,\nPark JoonKoo, Rewind, Sander Tieleman, srwss,\nSung Chanaul, YottaCho, Zerial.net'
        config.translations['Caz Woolley, Game Dev Robot, Gamsadev, Indie GameDev Bot, Indie Game Lover, Indie Games Devel, IndieVideoGames, Joachim Dimitri Jensen, Kim Kyeongtae, Kim Younghwan, Kurt Simon, Linda Lee King, Peter Christiansen, Sakimichi, Sebastian Haba, Spero Mcgee, The Indie Sloth, Vrachos, Xin Liu, Yu Shinhyeon'] = u'Caz Woolley, Game Dev Robot, Gamsadev, Indie GameDev Bot, Indie Game Lover,\nIndie Games Devel, IndieVideoGames,\nJoachim Dimitri Jensen, Kim Kyeongtae,\nKim Younghwan, Kurt Simon, Linda Lee King,\nPeter Christiansen, Sakimichi, Sebastian Haba,\nSpero Mcgee, The Indie Sloth, Vrachos,\nXin Liu, Yu Shinhyeon'
        config.translations['Christopher Rice, George Winston, Kim Sooyoung, Lee Illseong, Pixabay, Shin Haechul, So Reyeon, Tom Rothamel,\nValve Corporation'] = u'Christopher Rice, George Winston,\nKim Sooyoung, Lee Illseong, Pixabay,\nShin Haechul, So Reyeon, Tom Rothamel,\nValve Corporation'
    gui.language = "В соответствии с Федеральным законом № 436-ФЗ от 29.12.2010 данная игра содержит сцены:\n\nСамоубийства, употребления алкоголя и табачных изделий, нецензурной лексики, порнографии"
