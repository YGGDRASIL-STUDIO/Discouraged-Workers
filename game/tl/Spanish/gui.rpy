translate Spanish style main_menu_title:
    xalign .5 yoffset -700 size gui.title_text_size font gui.main_font
if renpy.variant("small"):
    translate Spanish style credits_text:
        font "gui/fonts/NanumBarunGothic.ttf"
    translate Spanish style thanks_text:
        yalign .9
translate Spanish python:
    gui.system_font = gui.text_font = gui.interface_text_font = gui.button_text_font  = "gui/fonts/Merienda-Regular.ttf"
    gui.main_font = "gui/fonts/Edo.ttf"
    gui.name_text_font = "gui/fonts/Merienda-Bold.ttf"
    gui.quick_hbox_xpos = .817
    gui.quick_hbox_ypos = .755
    config.name = "Trabajadores desanimados"
    config.window_title = u"Trabajadores desanimados"
    if renpy.variant("small"):
        config.translations["{font=[gui.fontawesome]}{/font} Basic Settings"] = u"{font=[gui.fontawesome]}{/font} básicos"
        config.translations["{font=[gui.fontawesome]}{/font} Main Menu"] = u"{font=[gui.fontawesome]}{/font} Menú"
        config.translations["{font=[gui.fontawesome]}{/font} Seen Text"] = u"{font=[gui.fontawesome]}{/font} Texto visto"
        config.translations["{font=[gui.fontawesome]}{/font} Mute All"] = u"{font=[gui.fontawesome]}{/font} Silencia"
        config.translations["{font=[gui.fontawesome]}{/font} Authors"] = u"{font=[gui.fontawesome]}{/font} Autores"
        config.translations['ACOC, Aiman Sharul, Axel Mertes, Bgame, Brandon Tanimoto, Brian Connors, BRISAK Kim Doohyeon, cheif.choi, Choi Irang, Choi Jihye, cloture, Danielle Bell, Edward N Puckering, Gary King, Gwak Jaeryeol, Han Ihyeong, Hoe Namyoon, Hong Eunki, Hwang Daehoon, Hyojoon, James Emmerson, Jeong Dongwon, Jeong Wookjin, Jeong Yoonsoo, Jianmin Zhang,\nKarina Schulze, Keira Val\'Azr, Kim Hanseol, Kim Hyeoncheol, Kim Jaeseong, Kim Jeongwoong, Kim Myeongwook,\nLee Changki, Lee Eunji, Lee Gunhae, Lee Hyejin, Lee Jaewi, Light Twins, Lim Jisoo, Maddy Wootton,\nMarshall Proudfoot, Mirumu, Mojaeng, Oh Hyeonjun, Park Hyeonjun, Park JoonKoo, Rewind, Sander Tieleman, srwss, Sung Chanaul, YottaCho, Zerial.net'] = u'ACOC, Aiman Sharul, Axel Mertes, Bgame, Brandon Tanimoto, Brian Connors,\nBRISAK Kim Doohyeon, cheif.choi, Choi Irang,\nChoi Jihye, cloture, Danielle Bell,\nEdward N Puckering, Gary King, Gwak Jaeryeol, Han Ihyeong, Hoe Namyoon, Hong Eunki,\nHwang Daehoon, Hyojoon, James Emmerson,\nJeong Dongwon, Jeong Wookjin,\nJeong Yoonsoo, Jianmin Zhang, Karina Schulze,\nKeira Val\'Azr, Kim Hanseol, Kim Hyeoncheol,\nKim Jaeseong, Kim Jeongwoong,\nKim Myeongwook, Lee Changki, Lee Eunji,\nLee Gunhae, Lee Hyejin, Lee Jaewi,\nLight Twins, Lim Jisoo, Maddy Wootton,\nMarshall Proudfoot, Mirumu, Mojaeng,\nOh Hyeonjun, Park Hyeonjun, Park JoonKoo,\nRewind, Sander Tieleman, srwss, Sung Chanaul,\nYottaCho, Zerial.net'
        config.translations['Caz Woolley, Game Dev Robot, Gamsadev, Indie GameDev Bot, Indie Game Lover, Indie Games Devel, IndieVideoGames, Joachim Dimitri Jensen, Kim Kyeongtae, Kim Younghwan, Kurt Simon, Linda Lee King, Peter Christiansen, Sakimichi, Sebastian Haba, Spero Mcgee, The Indie Sloth, Vrachos, Xin Liu, Yu Shinhyeon'] = u'Caz Woolley, Game Dev Robot, Gamsadev,\nIndie GameDev Bot, Indie Game Lover,\nIndie Games Devel, IndieVideoGames,\nJoachim Dimitri Jensen, Kim Kyeongtae,\nKim Younghwan, Kurt Simon, Linda Lee King,\nPeter Christiansen, Sakimichi, Sebastian Haba,\nSpero Mcgee, The Indie Sloth, Vrachos,\nXin Liu, Yu Shinhyeon'
        config.translations['Christopher Rice, George Winston, Kim Sooyoung, Lee Illseong, Pixabay, Shin Haechul, So Reyeon, Tom Rothamel,\nValve Corporation'] = u'Christopher Rice, George Winston,\nKim Sooyoung, Lee Illseong, Pixabay,\nShin Haechul, So Reyeon, Tom Rothamel,\nValve Corporation'
