init:
    image warning_ko = LiveComposite(
        (1920, 1080),
        (0, 0), Solid("#000"),
        (535, 540), im.Crop('demosprites01.png', (0, 1080, 869, 540))
        )
    image continue_ko = LiveComposite(
        (320, 320),
        (41, 32), Text('', style='awesome'),
        (85, 278), Text('이어서 읽기', style='mscreen')
        )
    image continueg_ko = LiveComposite(
        (320, 320),
        (41, 32), Text('', style='awesomeg'),
        (85, 278), Text('이어서 읽기', style='mscreeng')
        )
    image start_ko = LiveComposite(
        (320, 320),
        (51, 32), Text('', style='awesome'),
        (71, 278), Text('처음부터 읽기', style='mscreen')
        )
    image startg_ko = LiveComposite(
        (320, 320),
        (51, 32), Text('', style='awesomeg'),
        (71, 278), Text('처음부터 읽기', style='mscreeng')
        )
    image archives_ko = LiveComposite(
        (320, 320),
        (33, 32), Text('', style='awesome'),
        (85, 278), Text('기록 보관소', style='mscreen')
        )
    image archivesg_ko = LiveComposite(
        (320, 320),
        (33, 32), Text('', style='awesomeg'),
        (85, 278), Text('기록 보관소', style='mscreeng')
        )
    image credits_ko = LiveComposite(
        (320, 320),
        (58, 32), Text('', style='awesome'),
        (117, 278), Text('만든이', style='mscreen')
        )
    image creditsg_ko = LiveComposite(
        (320, 320),
        (58, 32), Text('', style='awesomeg'),
        (117, 278), Text('만든이', style='mscreeng')
        )
    image configration_ko = LiveComposite(
        (320, 320),
        (48, 32), Text('', style='awesome'),
        (103, 278), Text('환경설정', style='mscreen')
        )
    image configrationg_ko = LiveComposite(
        (320, 320),
        (48, 32), Text('', style='awesomeg'),
        (103, 278), Text('환경설정', style='mscreeng')
        )
    image close_ko = LiveComposite(
        (320, 320),
        (58, 32), Text('', style='awesome'),
        (100, 278), Text('책장 덮기', style='mscreen')
        )
    image closeg_ko = LiveComposite(
        (320, 320),
        (58, 32), Text('', style='awesomeg'),
        (100, 278), Text('책장 덮기', style='mscreeng')
        )
    image play_ko = LiveComposite(
        (200, 200),
        (32, 22), Text('', style='awesomeq'),
        (55, 174), Text('계속 읽기', style='qscreen')
        )
    image stop_ko = LiveComposite(
        (200, 200),
        (32, 22), Text('', style='awesomeq'),
        (45, 174), Text('잠깐 멈추기', style='qscreen')
        )
    image save_ko = LiveComposite(
        (200, 200),
        (43, 22), Text('', style='awesomeq'),
        (44, 174), Text('책갈피 꽂기', style='qscreen')
        )
    image config_ko = LiveComposite(
        (200, 200),
        (32, 22), Text('', style='awesomeq'),
        (58, 174), Text('환경설정', style='qscreen')
        )
    image arc_ko = LiveComposite(
        (200, 200),
        (24, 22), Text('', style='awesomeq'),
        (48, 174), Text('기록 보관소', style='qscreen')
        )
    image getchar_ko = LiveComposite (
        (379, 115),
        (0, 0), im.Rotozoom(im.Crop('demosprites01.png', (1950, 0, 759, 230)), 0, .5),
        (76, 35), Text('{b}등장인물 +1{/b}')
        )
    image getmusic_ko = LiveComposite (
        (379, 115),
        (0, 0), im.Rotozoom(im.Crop('demosprites01.png', (1950, 0, 759, 230)), 0, .5),
        (48, 35), Text('{b}음악 감상관 +1{/b}')
        )
    image getcon_ko = LiveComposite (
        (379, 115),
        (0, 0), im.Rotozoom(im.Crop('demosprites01.png', (1950, 0, 759, 230)), 0, .5),
        (76, 35), Text('{b}해설모음 +1{/b}')
        )
    image getgall_ko = LiveComposite (
        (379, 115),
        (0, 0), im.Rotozoom(im.Crop('demosprites01.png', (1950, 0, 759, 230)), 0, .5),
        (47, 35), Text('{b}미술 전시관 +1{/b}')
        )