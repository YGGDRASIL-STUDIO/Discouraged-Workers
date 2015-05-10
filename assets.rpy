init:
    image caffe = im.Crop('demosprites00.jpg', (0, 0, 1920, 1080))
    image cheon = im.Crop('demosprites00.jpg', (1920, 0, 1920, 1080))
    image food = im.Crop('demosprites00.jpg', (3840, 0, 1920, 1080))
    image hof = im.Crop('demosprites00.jpg', (1920, 1080, 1920, 1080))
    image internr = im.Crop('demosprites00.jpg', (5760, 1080, 1920, 1080))
    image phone = im.Crop('demosprites00.jpg', (0, 1080, 1920, 1080))
    image room = im.Crop('demosprites00.jpg', (5760, 0, 1920, 1080))
    image sin = im.Crop('demosprites00.jpg', (7680, 0, 1920, 1080))
    image hofg = im.Grayscale(im.Crop('demosprites00.jpg', (1920, 1080, 1920, 1080)))
    image roomg = im.Grayscale(im.Crop('demosprites00.jpg', (5760, 0, 1920, 1080)))
    image hofshock = im.MatrixColor(im.Crop('demosprites00.jpg', (1920, 1080, 1920, 1080)), im.matrix.tint(1,0,0))
    image roomn = im.MatrixColor(im.Crop('demosprites00.jpg', (5760, 0, 1920, 1080)), im.matrix.tint(.2,.2,.4))
    image dialoguer = im.MatrixColor(im.Crop('demosprites01.png', (1950, 0, 759, 230)), im.matrix.colorize('#4c0000', '#000'))
    image dialogue = im.Crop('demosprites01.png', (1950, 0, 759, 230))
    image usg = im.Grayscale(im.Crop('demosprites01.png', (1950, 230, 320, 320)))
    image krg = im.Grayscale(im.Crop('demosprites01.png', (2270, 230, 320, 320)))
    image us = im.Crop('demosprites01.png', (1950, 230, 320, 320))
    image kr = im.Crop('demosprites01.png', (2270, 230, 320, 320))
    image p = im.Crop('demosprites01.png', (0, 0, 650, 1080))
    image photom = im.Crop('demosprites02.png', (0, 0, 1280, 720))
    image tdw = im.Crop('demosprites02.png', (1280, 0, 1600, 1080))
    image home = Text('', style='awesomea')
    image facebook = Text('', style='awesomea')
    image twitter = Text('', style='awesomea')
    image google = Text('', style='awesomea')
    image steam = Text('', style='awesomea')
    image ios = Text('', style='awesomea')
    image android = Text('', style='awesomea', ypos=-.05)
    image homeg = Text('', style='awesomeag')
    image facebookg = Text('', style='awesomeag')
    image twitterg = Text('', style='awesomeag')
    image googleg = Text('', style='awesomeag')
    image steamg = Text('', style='awesomeag')
    image iosg = Text('', style='awesomeag')
    image androidg = Text('', style='awesomeag', ypos=-.05)
    image warning = LiveComposite(
        (1920, 1080),
        (0, 0), Solid("#000"),
        (767, 540), im.Crop('demosprites01.png', (914, 1080, 386, 540))
        )
    image intern = im.Composite(
        (650, 1080),
        (0, 0), im.Crop('demosprites01.png', (650, 0, 650, 1080)),
        (191, 182), im.Crop('demosprites01.png', (2690, 1280, 256, 256))
        )
    image intern2 = im.Composite(
        (650, 1080),
        (0, 0), im.Crop('demosprites01.png', (650, 0, 650, 1080)),
        (191, 178), im.Crop('demosprites01.png', (2690, 1792, 256, 256))
        )
    image intern1 = im.Composite(
        (650, 1080),
        (0, 0), im.Crop('demosprites01.png', (650, 0, 650, 1080)),
        (191, 173), im.Crop('demosprites01.png', (2690, 1536, 256, 256))
        )
    image exg = im.Composite(
        (650, 1080),
        (0, 0), im.Grayscale(im.Crop('demosprites01.png', (1300, 0, 650, 1080))),
        (198, 190), im.Grayscale(im.Crop('demosprites01.png', (2946, 1792, 256, 256)))
        )
    image yuag = im.Composite(
        (750, 1080),
        (17, 0), im.Grayscale(im.Crop('demosprites01.png', (3207, 0, 750, 1080))),
        (243, 162), im.Grayscale(im.Crop('demosprites01.png', (2946, 1280, 256, 256)))
        )
    image yusg = im.Composite(
        (750, 1080),
        (17, 0), im.Grayscale(im.Crop('demosprites01.png', (3207, 0, 750, 1080))),
        (243, 162), im.Grayscale(im.Crop('demosprites01.png', (2946, 1536, 256, 256)))
        )
    image yug = im.Composite(
        (750, 1080),
        (17, 0), im.Grayscale(im.Crop('demosprites01.png', (3207, 0, 750, 1080))),
        (243, 161), im.Grayscale(im.Crop('demosprites01.png', (2946, 1024, 256, 256)))
        )
    image hssg = im.Composite(
        (650, 1080),
        (12, 0), im.Grayscale(im.Crop('demosprites01.png', (1950, 1080, 650, 1080))),
        (200, 202), im.Grayscale(im.Crop('demosprites01.png', (2946, 256, 256, 256)))
        )
    image hsg = im.Composite(
        (650, 1080),
        (12, 0), im.Grayscale(im.Crop('demosprites01.png', (1950, 1080, 650, 1080))),
        (200, 195), im.Grayscale(im.Crop('demosprites01.png', (2946, 512, 256, 256)))
        )
    image hwg = im.Composite(
        (650, 1080),
        (12, 0), im.Grayscale(im.Crop('demosprites01.png', (1950, 1080, 650, 1080))),
        (199, 203), im.Grayscale(im.Crop('demosprites01.png', (2946, 768, 256, 256)))
        )
    image hyg = im.Composite(
        (650, 1080),
        (12, 0), im.Grayscale(im.Crop('demosprites01.png', (1950, 1080, 650, 1080))),
        (201, 195), im.Grayscale(im.Crop('demosprites01.png', (2946, 0, 256, 256)))
        )
    image hy = im.Composite(
        (650, 1080),
        (12, 0), im.Crop('demosprites01.png', (1950, 1080, 650, 1080)),
        (201, 195), im.Crop('demosprites01.png', (2946, 0, 256, 256))
        )
    image hs = im.Composite(
        (650, 1080),
        (12, 0), im.Crop('demosprites01.png', (1950, 1080, 650, 1080)),
        (200, 195), im.Crop('demosprites01.png', (2946, 512, 256, 256))
        )
    image hw = im.Composite(
        (650, 1080),
        (12, 0), im.Crop('demosprites01.png', (1950, 1080, 650, 1080)),
        (199, 203), im.Crop('demosprites01.png', (2946, 768, 256, 256))
        )
    image hss = im.Composite(
        (650, 1080),
        (12, 0), im.Crop('demosprites01.png', (1950, 1080, 650, 1080)),
        (200, 202), im.Crop('demosprites01.png', (2946, 256, 256, 256))
        )
    image yu = im.Composite(
        (750, 1080),
        (17, 0), im.Crop('demosprites01.png', (3207, 0, 750, 1080)),
        (243, 161), im.Crop('demosprites01.png', (2946, 1024, 256, 256))
        )
    image yua = im.Composite(
        (750, 1080),
        (17, 0), im.Crop('demosprites01.png', (3207, 0, 750, 1080)),
        (243, 162), im.Crop('demosprites01.png', (2946, 1280, 256, 256))
        )
    image yus = im.Composite(
        (750, 1080),
        (17, 0), im.Crop('demosprites01.png', (3207, 0, 750, 1080)),
        (243, 162), im.Crop('demosprites01.png', (2946, 1536, 256, 256))
        )
    image ex1 = im.Composite(
        (650, 1080),
        (0, 0), im.Crop('demosprites01.png', (1300, 0, 650, 1080)),
        (198, 190), im.Crop('demosprites01.png', (2946, 1792, 256, 256))
        )
    image photo = LiveComposite(
        (1920, 1080),
        (0, 0), Solid("#000"),
        (320, 180), im.Crop('demosprites02.png', (0, 0, 1280, 720))
        )
    image photos = LiveComposite(
        (768, 432),
        (0, 0), im.Rotozoom(im.Crop('demosprites02.png', (0, 0, 1280, 720)), 0, .6)
        )
    image photog = LiveComposite(
        (1920, 1080),
        (0, 0), im.Rotozoom(im.Crop('demosprites02.png', (0, 0, 1280, 720)), 0, 1.5)
        )
    image tdwg = LiveComposite(
        (1920, 1080),
        (0, 0), im.Crop('demosprites00.jpg', (7680, 0, 1920, 1080)),
        (50, 0), im.Crop('demosprites02.png', (1280, 0, 1600, 1080))
        )
    image tdws = LiveComposite(
        (768, 432),
        (0, 0), im.Rotozoom(im.Crop('demosprites00.jpg', (7680, 0, 1920, 1080)), 0, .4),
        (20, 0), im.Rotozoom(im.Crop('demosprites02.png', (1280, 0, 1600, 1080)), 0, .4)
        )
    image dw = LiveComposite(
        (1920, 1080),
        (0, 0), Solid("#fff"),
        (420, 820), im.Rotozoom(im.Crop('demosprites01.png', (2816, 0, 130, 1080)), -90, 1),
        (775, 995), Text('ⓒ YGGDRASIL STUDIO', style='systext')
        )
    image renpy = LiveComposite(
        (1920, 1080),
        (0, 0), Solid("#fff"),
        (705, 150), im.Rotozoom(im.Crop('demosprites01.png', (1955, 550, 780, 510)), -90, 1),
        (670, 995), Text('Powered by Ren\'Py visual novel engine', style='systext')
        )
    image continue = LiveComposite(
        (320, 320),
        (41, 32), Text('', style='awesome'),
        (85, 278), Text('Bookmark', style='mscreen')
        )
    image continueg = LiveComposite(
        (320, 320),
        (41, 32), Text('', style='awesomeg'),
        (85, 278), Text('Bookmark', style='mscreeng')
        )
    image start = LiveComposite(
        (320, 320),
        (51, 32), Text('', style='awesome'),
        (65, 278), Text('Start reading', style='mscreen')
        )
    image startg = LiveComposite(
        (320, 320),
        (51, 32), Text('', style='awesomeg'),
        (65, 278), Text('Start reading', style='mscreeng')
        )
    image archives = LiveComposite(
        (320, 320),
        (33, 32), Text('', style='awesome'),
        (98, 278), Text('Archives', style='mscreen')
        )
    image archivesg = LiveComposite(
        (320, 320),
        (33, 32), Text('', style='awesomeg'),
        (98, 278), Text('Archives', style='mscreeng')
        )
    image credits = LiveComposite(
        (320, 320),
        (58, 32), Text('', style='awesome'),
        (108, 278), Text('Credits', style='mscreen')
        )
    image creditsg = LiveComposite(
        (320, 320),
        (58, 32), Text('', style='awesomeg'),
        (108, 278), Text('Credits', style='mscreeng')
        )
    image configration = LiveComposite(
        (320, 320),
        (48, 32), Text('', style='awesome'),
        (70, 278), Text('Configration', style='mscreen')
        )
    image configrationg = LiveComposite(
        (320, 320),
        (48, 32), Text('', style='awesomeg'),
        (70, 278), Text('Configration', style='mscreeng')
        )
    image close = LiveComposite(
        (320, 320),
        (58, 32), Text('', style='awesome'),
        (53, 278), Text('Close the book', style='mscreen')
        )
    image closeg = LiveComposite(
        (320, 320),
        (58, 32), Text('', style='awesomeg'),
        (53, 278), Text('Close the book', style='mscreeng')
        )
    image play = LiveComposite(
        (200, 200),
        (32, 22), Text('', style='awesomeq'),
        (80, 174), Text('Play', style='qscreen')
        )
    image stop = LiveComposite(
        (200, 200),
        (32, 22), Text('', style='awesomeq'),
        (66, 174), Text('Pause', style='qscreen')
        )
    image save = LiveComposite(
        (200, 200),
        (43, 22), Text('', style='awesomeq'),
        (44, 174), Text('Bookmark', style='qscreen')
        )
    image config = LiveComposite(
        (200, 200),
        (32, 22), Text('', style='awesomeq'),
        (32, 174), Text('Configration', style='qscreen')
        )
    image arc = LiveComposite(
        (200, 200),
        (24, 22), Text('', style='awesomeq'),
        (54, 174), Text('Archives', style='qscreen')
        )
    image lock = LiveComposite(
        (768, 432),
        (261, 41), Text('', style='gall')
        )
    image getchar = LiveComposite (
        (379, 115),
        (0, 0), im.Rotozoom(im.Crop('demosprites01.png', (1950, 0, 759, 230)), 0, .5),
        (41, 35), Text('{b}Characters +1{/b}')
        )
    image getmusic = LiveComposite (
        (379, 115),
        (0, 0), im.Rotozoom(im.Crop('demosprites01.png', (1950, 0, 759, 230)), 0, .5),
        (95, 35), Text('{b}Music +1{/b}')
        )
    image getcon = LiveComposite (
        (379, 115),
        (0, 0), im.Rotozoom(im.Crop('demosprites01.png', (1950, 0, 759, 230)), 0, .5),
        (69, 35), Text('{b}Concept +1{/b}')
        )
    image getgall = LiveComposite (
        (379, 115),
        (0, 0), im.Rotozoom(im.Crop('demosprites01.png', (1950, 0, 759, 230)), 0, .5),
        (83, 35), Text('{b}Gallery +1{/b}')
        )
    transform get:
        xalign .99 yalign 0
        alpha 0
        linear .5 alpha 1
        linear 1
        linear .5 alpha 0
    transform pstand:
        xalign .494
    transform times:
        xalign .45 yalign .5
        linear 3 xalign .5
    transform menuback:
        on hover:
            linear .5 alpha 0
            linear .5 alpha 1
        on selected_hover:
            linear .5 alpha 0
            linear .5 alpha 1
    transform arc_char:
        zoom .5 alpha .7
    transform arc_chars:
        zoom .5
    $ mr = MusicRoom(fadeout=1.0)
    $ mr.add("bgm/Sigh day.ogg")
    $ mr.add("bgm/Mare tranquillitatis.ogg")
    $ mr.add("bgm/CCCanon.ogg")
    $ mr.add("bgm/Let's game.ogg")
    $ mr.add("bgm/Peace.ogg")
    $ mr.add("bgm/Unknown mist.ogg")
    $ mr.add("bgm/Lush garden.ogg")
    $ mr.add("bgm/Jormungandr.ogg")
    $ mr.add("bgm/Nyx.ogg")
    $ mr.add("bgm/Love song.ogg", always_unlocked=True)
    $ g = Gallery()
    $ g.button("that day we")
    $ g.condition("persistent.unlock_1")
    $ g.image("tdwg")
    $ g.button("eternal happiness")
    $ g.condition("persistent.unlock_2")
    $ g.image("photog")