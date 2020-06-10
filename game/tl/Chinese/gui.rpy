if renpy.variant("small"):
    translate Chinese style credits_text:
        font "gui/fonts/NanumBarunGothic.ttf"
    translate Chinese style thanks_text:
        yalign .9
translate Chinese python:
    gui.system_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = "gui/fonts/DroidSansFallback.ttf"
    gui.main_font = "gui/fonts/ShuTiFangZhuoXiaoFengXingCaoTi.ttf"
    gui.quick_hbox_ypos = .765
    config.name = "失望失业者"
    config.window_title = u"失望失业者"
    if renpy.variant("small"):
        config.translations["{font=[gui.fontawesome]}{/font} Basic Settings"] = u"{font=[gui.fontawesome]}{/font} 基本设置"
        config.translations["{font=[gui.fontawesome]}{/font} Seen Text"] = u"{font=[gui.fontawesome]}{/font} 看过"
        config.translations["{font=[gui.fontawesome]}{/font} Mute All"] = u"{font=[gui.fontawesome]}{/font} 声音关"
        config.translations["{font=[gui.fontawesome]}{/font} Authors"] = u"{font=[gui.fontawesome]}{/font} 版权所有者"
        config.translations['ACOC, Aiman Sharul, Axel Mertes, Bgame, Brandon Tanimoto, Brian Connors, BRISAK Kim Doohyeon, cheif.choi, Choi Irang, Choi Jihye, cloture, Danielle Bell, Edward N Puckering, Gary King, Gwak Jaeryeol, Han Ihyeong, Hoe Namyoon, Hong Eunki, Hwang Daehoon, Hyojoon, James Emmerson, Jeong Dongwon, Jeong Wookjin, Jeong Yoonsoo, Jianmin Zhang,\nKarina Schulze, Keira Val\'Azr, Kim Hanseol, Kim Hyeoncheol, Kim Jaeseong, Kim Jeongwoong, Kim Myeongwook,\nLee Changki, Lee Eunji, Lee Gunhae, Lee Hyejin, Lee Jaewi, Light Twins, Lim Jisoo, Maddy Wootton,\nMarshall Proudfoot, Mirumu, Mojaeng, Oh Hyeonjun, Park Hyeonjun, Park JoonKoo, Rewind, Sander Tieleman, srwss, Sung Chanaul, YottaCho, Zerial.net'] = u'ACOC, Aiman Sharul, Axel Mertes, Bgame,\nBrandon Tanimoto, Brian Connors,\nBRISAK Kim Doohyeon, cheif.choi, Choi Irang,\nChoi Jihye, cloture, Danielle Bell,\nEdward N Puckering, Gary King, Gwak Jaeryeol,\nHan Ihyeong, Hoe Namyoon, Hong Eunki,\nHwang Daehoon, Hyojoon, James Emmerson,\nJeong Dongwon, Jeong Wookjin, Jeong Yoonsoo,\nJianmin Zhang, Karina Schulze, Keira Val\'Azr,\nKim Hanseol, Kim Hyeoncheol, Kim Jaeseong,\nKim Jeongwoong, Kim Myeongwook,\nLee Changki, Lee Eunji, Lee Gunhae, Lee Hyejin,\nLee Jaewi, Light Twins, Lim Jisoo, Maddy Wootton,\nMarshall Proudfoot, Mirumu, Mojaeng,\nOh Hyeonjun, Park Hyeonjun, Park JoonKoo,\nRewind, Sander Tieleman, srwss, Sung Chanaul,\nYottaCho, Zerial.net'
        config.translations['Caz Woolley, Game Dev Robot, Gamsadev, Indie GameDev Bot, Indie Game Lover, Indie Games Devel, IndieVideoGames, Joachim Dimitri Jensen, Kim Kyeongtae, Kim Younghwan, Kurt Simon, Linda Lee King, Peter Christiansen, Sakimichi, Sebastian Haba, Spero Mcgee, The Indie Sloth, Vrachos, Xin Liu, Yu Shinhyeon'] = u'Caz Woolley, Game Dev Robot, Gamsadev,\nIndie GameDev Bot, Indie Game Lover,\nIndie Games Devel, IndieVideoGames,\nJoachim Dimitri Jensen, Kim Kyeongtae,\nKim Younghwan, Kurt Simon, Linda Lee King,\nPeter Christiansen, Sakimichi, Sebastian Haba,\nSpero Mcgee, The Indie Sloth, Vrachos, Xin Liu,\nYu Shinhyeon'
        config.translations['Christopher Rice, George Winston, Kim Sooyoung, Lee Illseong, Pixabay, Shin Haechul, So Reyeon, Tom Rothamel,\nValve Corporation'] = u"Christopher Rice, George Winston, Kim Sooyoung, Lee Illseong, Pixabay, Shin Haechul, So Reyeon,\nTom Rothamel, Valve Corporation"
    gui.language = "此故事禁止未成年人观看。不建议儿童(青少年)、老弱者或者孕妇、身心较弱者观看。\n这个节目包含以下内容。\n\n性、菸酒、不當言語"
