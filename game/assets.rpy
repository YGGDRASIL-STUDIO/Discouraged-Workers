init:
    image yggdrasil_logo = "gui/yggdrasil_logo.webp"
    image chibilis_logo = "gui/chibilis_logo.webp"
    image renpy_logo = "gui/renpy_logo.webp"
    image main_menu = "gui/overlay/main_menu.webp"
    image game_menu = 'gui/overlay/game_menu.webp'
    image born_balls = SnowBlossom("gui/overlay/main_ball.webp", count=50, yspeed=(100, 200))
    image controller_play:
        "gui/controllers/[persistent.controllers]/button_x.webp", size(89, 89)
    if persistent.controllers == "ouya":
        image controller_save:
            "gui/controllers/[persistent.controllers]/button_x.webp", size(89, 89)
    else:
        image controller_save:
            "gui/controllers/[persistent.controllers]/button_start.webp", size(89, 89)
    image controller_skip:
        "gui/controllers/[persistent.controllers]/trigger_r_click.webp", size(89, 89)
    image controller_hide:
        "gui/controllers/[persistent.controllers]/trigger_l_click.webp", size(89, 89)
    image controller_arc:
        "gui/controllers/[persistent.controllers]/button_b.webp", size(89, 89)
    image controller_config:
        "gui/controllers/[persistent.controllers]/button_y.webp", size(89, 89)
    image controller_shoulder_l:
        "gui/controllers/[persistent.controllers]/shoulder_l.webp", size(89, 89)
    image controller_shoulder_r:
        "gui/controllers/[persistent.controllers]/shoulder_r.webp", size(89, 89)
    image part_01:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_01.webp', xpos .06 ypos .056
        contains:
            Text('{i}Are you alright?{/i}', style='arc_text'), xpos .06 ypos .845
    image part_01_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_01.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Are you alright?{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_02:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_02.webp', xpos .06 ypos .056
        contains:
            Text('{i}Monologue{/i}', style='arc_text'), xpos .06 ypos .845
    image part_02_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_02.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Monologue{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_03:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Scale('images/bread.webp', 280, 280), xpos .06 ypos .056
        contains:
            Text('{i}Do you remember?{/i}', style='arc_text'), xpos .06 ypos .845
    image part_03_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia(im.Scale('images/bread.webp', 280, 280)), xpos .06 ypos .056
        contains:
            Text('{i}Do you remember?{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_04:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_04.webp', xpos .06 ypos .056
        contains:
            Text('{i}Shin-Chon Street{/i}', style='arc_text'), xpos .06 ypos .845
    image part_04_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_04.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Shin-Chon Street{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_05:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_05.webp', xpos .06 ypos .056
        contains:
            Text('{i}Sad lunch{/i}', style='arc_text'), xpos .06 ypos .845
    image part_05_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_05.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Sad lunch{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_06:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_07.webp', xpos .06 ypos .056
        contains:
            Text('{i}Monologue{/i}', style='arc_text'), xpos .06 ypos .845
    image part_06_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_07.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Monologue{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_07:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_05.webp', xpos .06 ypos .056
        contains:
            Text('{i}Calm afternoon{/i}', style='arc_text'), xpos .06 ypos .845
    image part_07_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_05.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Calm afternoon{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_08:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_08.webp', xpos .06 ypos .056
        contains:
            Text('{size=-5}{i}Questionable feelings{/i}{/size}', style='arc_text'), xpos .06 ypos .845
    image part_08_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_08.webp'), xpos .06 ypos .056
        contains:
            Text('{size=-5}{i}Questionable feelings{/i}{/size}', style='arc_text_gray'), xpos .06 ypos .845
    image part_09:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_01.webp', xpos .06 ypos .056
        contains:
            Text('{i}Circumstances{/i}', style='arc_text'), xpos .06 ypos .845
    image part_09_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_01.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Circumstances{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_10:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_12.webp', xpos .06 ypos .056
        contains:
            Text('{i}Distortion{/i}', style='arc_text'), xpos .06 ypos .845
    image part_10_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_12.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Distortion{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_11:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_11.webp', xpos .06 ypos .056
        contains:
            Text('{i}Monologue{/i}', style='arc_text'), xpos .06 ypos .845
    image part_11_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_11.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Monologue{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_12:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_12.webp', xpos .06 ypos .056
        contains:
            Text('{i}Broken heart{/i}', style='arc_text'), xpos .06 ypos .845
    image part_12_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_12.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Broken heart{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_13:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_11.webp', xpos .06 ypos .056
        contains:
            Text('{i}How alive are you?{/i}', style='arc_text'), xpos .06 ypos .845
    image part_13_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_11.webp'), xpos .06 ypos .056
        contains:
            Text('{i}How alive are you?{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_14:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_17.webp', xpos .06 ypos .056
        contains:
            Text('{i}Grasping reality{/i}', style='arc_text'), xpos .06 ypos .845
    image part_14_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_17.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Grasping reality{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_15:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_18.webp', xpos .06 ypos .056
        contains:
            Text('{i}Self-inflicted{/i}', style='arc_text'), xpos .06 ypos .845
    image part_15_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_18.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Self-inflicted{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_16:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_19.webp', xpos .06 ypos .056
        contains:
            Text('{i}R.I.P{/i}', style='arc_text'), xpos .06 ypos .845
    image part_16_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_19.webp'), xpos .06 ypos .056
        contains:
            Text('{i}R.I.P{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_17:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_21.webp', xpos .06 ypos .056
        contains:
            Text('{i}Madness{/i}', style='arc_text'), xpos .06 ypos .845
    image part_17_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_21.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Madness{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_18:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_18.webp', xpos .06 ypos .056
        contains:
            Text('{i}Yunwoo\'s view{/i}', style='arc_text'), xpos .06 ypos .845
    image part_18_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_18.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Yunwoo\'s view{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_19:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_11.webp', xpos .06 ypos .056
        contains:
            Text('{i}Ga-yeon\'s view{/i}', style='arc_text'), xpos .06 ypos .845
    image part_19_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_11.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Ga-yeon\'s view{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_20:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_20.webp', xpos .06 ypos .056
        contains:
            Text('{size=-5}{i}Ga-yeon and Yunwoo{/i}{/size}', style='arc_text'), xpos .06 ypos .845
    image part_20_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_part_20.webp'), xpos .06 ypos .056
        contains:
            Text('{size=-5}{i}Ga-yeon and Yunwoo{/i}{/size}', style='arc_text_gray'), xpos .06 ypos .845
    image part_21:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_26.webp', xpos .06 ypos .056
        contains:
            Text('{i}Bridge of the life{/i}', style='arc_text'), xpos .06 ypos .845
    image part_21_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_26.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Bridge of the life{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_22:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_27.webp', xpos .06 ypos .056
        contains:
            Text('{i}Edge of the world{/i}', style='arc_text'), xpos .06 ypos .845
    image part_22_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_27.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Edge of the world{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_23:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_28.webp', xpos .06 ypos .056
        contains:
            Text('{i}Accident{/i}', style='arc_text'), xpos .06 ypos .845
    image part_23_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_28.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Accident{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_24:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_29.webp', xpos .06 ypos .056
        contains:
            Text('{i}Epilogue{/i}', style='arc_text'), xpos .06 ypos .845
    image part_24_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_29.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Epilogue{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image part_25:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_31.webp', xpos .06 ypos .056
        contains:
            Text('{i}Flowery & moonlit{/i}', style='arc_text'), xpos .06 ypos .845
    image part_25_sepia:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Sepia('images/arc_gall_31.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Flowery & moonlit{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_char_01:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_11.webp', xpos .06 ypos .056
        contains:
            Text('{i}Choi Ga-yeon{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_02:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_18.webp', xpos .06 ypos .056
        contains:
            Text('{i}Kim Yunwoo{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_03:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_char_03.webp', xpos .06 ypos .056
        contains:
            Text('{i}Choi Hye-na{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_04_e:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_char_04_a.webp', xpos .06 ypos .056
        contains:
            Text('{i}Lee Seol-ah{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_04_q:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_20.webp', xpos .06 ypos .056
        contains:
            Text('{i}???{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_04:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_char_04.webp', xpos .06 ypos .056
        contains:
            Text('{i}Clerk{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_05:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_char_05.webp', xpos .06 ypos .056
        contains:
            Text('{i}Choi Taejin{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_06_e:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_char_06.webp', xpos .06 ypos .056
        contains:
            Text('{i}Park Misun{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_06:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_char_06.webp', xpos .06 ypos .056
        contains:
            Text('{i}Interviewer{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_07_e:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_12.webp', xpos .06 ypos .056
        contains:
            Text('{i}Park Hyeongsik{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_char_07:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_part_12.webp', xpos .06 ypos .056
        contains:
            Text('{i}Doctor{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_01:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_01.webp', xpos .06 ypos .056
        contains:
            Text('{i}Frustration{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_01_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_01.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Frustration{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_02:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_02.webp', xpos .06 ypos .056
        contains:
            Text('{i}Vomiting{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_02_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_02.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Vomiting{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_03:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_03.webp', xpos .06 ypos .056
        contains:
            Text('{i}Pusillanimous{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_03_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_03.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Pusillanimous{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_04:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_04.webp', xpos .06 ypos .056
        contains:
            Text('{i}That day we{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_04_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_04.webp'), xpos .06 ypos .056
        contains:
            Text('{i}That day we{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_05:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_05.webp', xpos .06 ypos .056
        contains:
            Text('{i}Fate{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_05_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_05.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Fate{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_06:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_06.webp', xpos .06 ypos .056
        contains:
            Text('{i}Courage{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_06_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_06.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Courage{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_07:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_07.webp', xpos .06 ypos .056
        contains:
            Text('{i}Moonlight{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_07_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_07.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Moonlight{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_08:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_08.webp', xpos .06 ypos .056
        contains:
            Text('{i}Drunken{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_08_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_08.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Drunken{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_09:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_09.webp', xpos .06 ypos .056
        contains:
            Text('{i}Eternal happiness{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_09_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_09.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Eternal happiness{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_10:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_10.webp', xpos .06 ypos .056
        contains:
            Text('{i}Despair{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_10_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_10.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Despair{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_11:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_11.webp', xpos .06 ypos .056
        contains:
            Text('{i}Lean{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_11_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_11.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Lean{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_12:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_12.webp', xpos .06 ypos .056
        contains:
            Text('{i}Distortion{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_12_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_12.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Distortion{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_13:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_13.webp', xpos .06 ypos .056
        contains:
            Text('{i}IMF Crisis{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_13_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_13.webp'), xpos .06 ypos .056
        contains:
            Text('{i}IMF Crisis{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_14:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_14.webp', xpos .06 ypos .056
        contains:
            Text('{k=-.8}{i}Newspaper delivery{/i}{/k}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_14_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_14.webp'), xpos .06 ypos .056
        contains:
            Text('{k=-.8}{i}Newspaper delivery{/i}{/k}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_15:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_15.webp', xpos .06 ypos .056
        contains:
            Text('{i}Serving{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_15_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_15.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Serving{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_16:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_16.webp', xpos .06 ypos .056
        contains:
            Text('{i}Kiss me{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_16_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_16.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Kiss me{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_17:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_17.webp', xpos .06 ypos .056
        contains:
            Text('{i}Video{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_17_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_17.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Video{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_18:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_18.webp', xpos .06 ypos .056
        contains:
            Text('{i}Self-inflicted{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_18_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_18.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Self-inflicted{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_19:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_19.webp', xpos .06 ypos .056
        contains:
            Text('{i}R.I.P{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_19_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_19.webp'), xpos .06 ypos .056
        contains:
            Text('{i}R.I.P{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_20:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_20.webp', xpos .06 ypos .056
        contains:
            Text('{i}Masturbation{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_20_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_20.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Masturbation{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_21:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_21.webp', xpos .06 ypos .056
        contains:
            Text('{i}Deep kiss{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_21_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_21.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Deep kiss{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_22:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_22.webp', xpos .06 ypos .056
        contains:
            Text('{i}Caress{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_22_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_22.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Caress{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_23:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_23.webp', xpos .06 ypos .056
        contains:
            Text('{i}Fellatio{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_23_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_23.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Fellatio{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_24:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_24.webp', xpos .06 ypos .056
        contains:
            Text('{i}Riding style{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_24_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_24.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Riding style{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_25:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_25.webp', xpos .06 ypos .056
        contains:
            Text('{i}Smoking{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_25_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_25.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Smoking{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_26:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_26.webp', xpos .06 ypos .056
        contains:
            Text('{i}Bridge of the life{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_26_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_26.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Bridge of the life{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_27:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_27.webp', xpos .06 ypos .056
        contains:
            Text('{i}Edge of the world{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_27_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_27.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Edge of the world{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_28:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_28.webp', xpos .06 ypos .056
        contains:
            Text('{i}Corruption{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_28_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_28.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Corruption{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_29:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_29.webp', xpos .06 ypos .056
        contains:
            Text('{i}Epilogue{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_29_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_29.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Epilogue{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_30:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_30.webp', xpos .06 ypos .056
        contains:
            Text('{i}Dead or Alive{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_30_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_30.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Dead or Alive{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_31:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_31.webp', xpos .06 ypos .056
        contains:
            Text('{i}Growing{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_31_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_31.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Growing{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_gall_32:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            'images/arc_gall_32.webp', xpos .06 ypos .056
        contains:
            Text('{i}Not the end{/i}', style='arc_text'), xpos .06 ypos .845
    image arc_gall_32_gray:
        size(320, 358)
        contains:
            'gui/polaroid.webp'
        contains:
            im.Grayscale('images/arc_gall_32.webp'), xpos .06 ypos .056
        contains:
            Text('{i}Not the end{/i}', style='arc_text_gray'), xpos .06 ypos .845
    image arc_con_01:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" A discouraged worker is a person of legal employment age who is not actively seeking employment, or who can not find employment after long-term unemployment. This is usually because an individual has given up looking or has had no success in finding a job, hence the term \"discouraged\".\n\n Discouraged workers are classified as an...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_02:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" Reclusive outsider is the phenomenon of reclusive adolescents or adults who withdraw from social life, often seeking extreme degrees of isolation and confinement. The term reclusive outsider refers to both the sociological phenomenon in general as well as to people belonging to this societal group.\n\n Choi Ga-yeon, a heroine of \"Discouraged Workers\", suffered from depressive...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_03:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" Generally, a medical referral is issued by a hospital when sending a patient to another hospital. Ga-yeon has received medical treatment from a psychiatrist since she was fired from the hospital where she was working as a coordinator. In spite of long treatment, her condition did not improve at all, and the hospital issued a medical referral to another hospital. But Ga-yeon...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_04:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" Anxiety disorders are a category of mental disorders characterized by feelings of anxiety and fear, where anxiety is a worry about future events and fear is a reaction to current events. These feelings may cause physical symptoms, such as a racing heart and shakiness.\n\n My mother had suffered from panic disorder for almost eight years...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_05:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" Depressive disorder is a mental disorder characterized by a pervasive and persistent low mood that is accompanied by low self-esteem and by a loss of interest or pleasure in normally enjoyable activities. The term \"depression\" is used in a number of different ways. It is often used to mean this syndrome but may refer to other mood disorders or simply to a...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_06:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" \"Bridge of the life\" was actually a sort of attempt using advanced technological methods to prevent suicide. By trying to have a conversation with a pedestrian through hopeful words and changing their desperation into hope, the designers thought suicidal people might be encouraged not to end their lives, but, in the event that failed, there was still the traditional physical...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_07:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" The Asian financial crisis was a period of financial crisis that gripped much of East Asia beginning in July 1997 and raised fears of a worldwide economic meltdown due to financial contagion.\n\n The crisis started in Thailand with the financial collapse of the Thai baht after the Thai government was forced to float the baht due to lack of foreign currency to support...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_08:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" \"Accident\" tells what happens after \"Epilogue\" which is the basic ending of \"Discouraged Workers\".\n\n Ga-yeon reached out her hand toward Yunwoo, but at that moment, she blacked out and fell off the bridge. And Yunwoo threw himself into the river to save her. A few days later, they rose to the surface, and one passerby's report told their deaths to the world...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_09:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" As a hospital coordinator, Ga-yeon fell in love with a doctor at the hospital she was working in and they had an affair even though the doctor was a married man. When the director found out, she was fired. For over a year she tried to find another job, but her mental uneasiness eventually made her give up and she became a recluse...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_10:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" \"Flowery Mornings and Moonlit Nights\" is the true ending which assumes that Ga-yeon didn't faint and grabbed Yunwoo's hand in \"Epilogue\". Originally \"Discouraged Workers\" was intended to end with the \"Accident\" story as the true ending. But after deciding to release it in the market, this was chosen as the true ending.\n\n Ga-yeon finds the culprit who spread the video...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_11:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" A chain reaction collision, involving 29 vehicles, happened at 7:50am on October 3, 2006, Korean time, on Seohae Grand Bridge in South Korea. This collision happened due to a thick fog, and it left 12 people dead and about 50 injured. According to the investigation, the accident occurred not only because of bad weather, but also because some drivers were speeding as well as shoulder riding...", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_12:
        size(253, 358)
        contains:
            'gui/parchment.webp'
        contains:
            Text(" In \"Discouraged Workers\", a word box in red color is used to show the words and thoughts of Ga-yeon and a clerk Because when the basic scenario was developed, they are actually not alive.\n\n But when Ga-yeon is talking with her mom on the phone, the black box is used out of consideration for her mother.", style="arc_text_small"), xpos .0791 ypos .0838
    image arc_con_01_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" A discouraged worker is a person of legal employment age who is not actively seeking employment, or who can not find employment after long-term unemployment. This is usually because an individual has given up looking or has had no success in finding a job, hence the term \"discouraged\".\n\n Discouraged workers are classified as an...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_02_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" Reclusive outsider is the phenomenon of reclusive adolescents or adults who withdraw from social life, often seeking extreme degrees of isolation and confinement. The term reclusive outsider refers to both the sociological phenomenon in general as well as to people belonging to this societal group.\n\n Choi Ga-yeon, a heroine of \"Discouraged Workers\", suffered from depressive...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_03_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" Generally, a medical referral is issued by a hospital when sending a patient to another hospital. Ga-yeon has received medical treatment from a psychiatrist since she was fired from the hospital where she was working as a coordinator. In spite of long treatment, her condition did not improve at all, and the hospital issued a medical referral to another hospital. But Ga-yeon...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_04_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" Anxiety disorders are a category of mental disorders characterized by feelings of anxiety and fear, where anxiety is a worry about future events and fear is a reaction to current events. These feelings may cause physical symptoms, such as a racing heart and shakiness.\n\n My mother had suffered from panic disorder for almost eight years...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_05_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" Depressive disorder is a mental disorder characterized by a pervasive and persistent low mood that is accompanied by low self-esteem and by a loss of interest or pleasure in normally enjoyable activities. The term \"depression\" is used in a number of different ways. It is often used to mean this syndrome but may refer to other mood disorders or simply to a...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_06_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" \"Bridge of the life\" was actually a sort of attempt using advanced technological methods to prevent suicide. By trying to have a conversation with a pedestrian through hopeful words and changing their desperation into hope, the designers thought suicidal people might be encouraged not to end their lives, but, in the event that failed, there was still the traditional physical...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_07_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" The Asian financial crisis was a period of financial crisis that gripped much of East Asia beginning in July 1997 and raised fears of a worldwide economic meltdown due to financial contagion.\n\n The crisis started in Thailand with the financial collapse of the Thai baht after the Thai government was forced to float the baht due to lack of foreign currency to support...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_08_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" \"Accident\" tells what happens after \"Epilogue\" which is the basic ending of \"Discouraged Workers\".\n\n Ga-yeon reached out her hand toward Yunwoo, but at that moment, she blacked out and fell off the bridge. And Yunwoo threw himself into the river to save her. A few days later, they rose to the surface, and one passerby's report told their deaths to the world...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_09_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" As a hospital coordinator, Ga-yeon fell in love with a doctor at the hospital she was working in and they had an affair even though the doctor was a married man. When the director found out, she was fired. For over a year she tried to find another job, but her mental uneasiness eventually made her give up and she became a recluse...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_10_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" \"Flowery Mornings and Moonlit Nights\" is the true ending which assumes that Ga-yeon didn't faint and grabbed Yunwoo's hand in \"Epilogue\". Originally \"Discouraged Workers\" was intended to end with the \"Accident\" story as the true ending. But after deciding to release it in the market, this was chosen as the true ending.\n\n Ga-yeon finds the culprit who spread the video...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_11_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" A chain reaction collision, involving 29 vehicles, happened at 7:50am on October 3, 2006, Korean time, on Seohae Grand Bridge in South Korea. This collision happened due to a thick fog, and it left 12 people dead and about 50 injured. According to the investigation, the accident occurred not only because of bad weather, but also because some drivers were speeding as well as shoulder riding...", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_con_12_gray:
        size(253, 358)
        contains:
            im.Grayscale('gui/parchment.webp')
        contains:
            Text(" In \"Discouraged Workers\", a word box in red color is used to show the words and thoughts of Ga-yeon and a clerk Because when the basic scenario was developed, they are actually not alive.\n\n But when Ga-yeon is talking with her mom on the phone, the black box is used out of consideration for her mother.", style="arc_text_small_gray"), xpos .0791 ypos .0838
    image arc_diary_01:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" It's been more than a month since I started working in a family restaurant. In the beginning, it was really hard to carry a tray and I even broke a few dishes. But now, I feel like I'm getting better and better. Sometimes, customers tip me as well, and also the other staff often praises my work. I'm especially good at…. hmmm…. well, it's too many to write them all down here! Later...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_02:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" Today the section chief of the head office visited the restaurant. I thought the chief would be a man, but she was a young woman. She came to our restaurant and called the captain to the locker room. She passed by me while I was working there, and I saw her nametag. And I found she has the same name as a famous comedian. Funny...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_03:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" I went to Cheolwon, with Eunyoung to see Yunwoo today. I didn't realize it was that cold, but when I got off the bus, I was just shocked as it was literally freezing. It didn't snow, and the wind didn't blow, but cold air made even my eyes freeze. Eunyoung and I hurried into the visitor's room to wait for Yunwoo.\n\n A few minutes later...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_04:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" After I parted with him, and while I was coming home, I tried really hard to fight back tears. But when I arrived in my room, I just burst into tears. Why? Why was I so mean to him? I raged at him, and told him to quit music. Why the hell did I do that?\n\n Today he told me what I've really looked forward to hearing from him, but why…. why couldn't I accept him...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_05:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" I had a long conversation with Yunwoo today;\n\n You've just been discharged from the army, and I'm a student without a job. So what can we do now? You really think we can get married and start our home? Seriously? How?\n\n Besides, we're not romantically involved with each other. We're just...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_06:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" It's been almost a year since I started working in this hospital. I work as a coordinator of the hospital. I had my salary raised, and also I'm pretty satisfied with my job. My savings account with the balance which gets bigger and bigger makes me feel really happy.\n\n When I had to quit the university temporarily, I was just stunned. But now that I...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_07:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" Oh, my god…. how could he look like him that much? His face, way of talking, character, and even that he can't hold liquor well…. everything is just like him. He reminds me of Yunwoo a lot. And it makes me feel sad. And this keeps bothering me so much. These days, I'm often trying to speak to him, or be around him. He also seems to be interested in me, and sometimes talks to me...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_08:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" His wife visited the hospital. Though the Director and my lover prefer a simple and plain style, she dressed up too much, with luxurious dress and accessories. She looked just full of vanity. When I saw she's coquetting with him arm in arm, she really looked like an old fox. I can't imagine she's the Director's sister, and my lover's wife. She really makes me feel sick...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_09:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" The director seemed to be trying hard not to hurt me, controlling his feelings. I understand he would feel betrayed as he has trusted me a lot, but he never swore at me at all, and treated me human to human. And now, I've finally realized what the hell I did. I felt really sorry for his wife, as she has never thought about this, and also felt sorry for the director who has always truly taken...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_10:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" Every single day, I cry, sleep, and wake from sleep, remember my good old days, especially with him, and then, cry, and fall asleep again. Beginning with a few days ago, I sometimes burst into laughter, and sometimes, burst into a fit of anger. I feel like I can't breathe well from time to time.\n\n I miss him. I miss him looking at me with a gentle smile...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_11:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" Even though I had no interview today, I sat in front of my dressing table to put on makeup. But as soon as I saw my face, I was frightened, as it suddenly looked awful and disgusting. I fell backward, and managed to crawl to the bed. And I trembled and trembled. Then, I called Hye-na and begged her to save me.\n\n Soon, Hye-na came to my...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_12:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" Today, I visited a neuropsychiatric clinic, with Hye-na. I was pretty afraid to go there, but as I was with my sister, I could do it. The doctor asked me a number of things, from trivial questions to what is happening to me now and what I don't want to tell others as well.\n\n He also asked whether I have some physical problems, and I told him I hurt myself...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_13:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" Today, I met Eunju. It's been a really long time since I've seen her. She used to be my best friend when we were high school students, but she is not single anymore. She said she's really worried as she hasn't lost any weight in spite of her steady diet since she gave birth to her baby. So I told her that she still looks good. Eunju worried about me saying I'm so bony, and she said to take her fat...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_14:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" These days, I receive mental health treatment, and also try hard to get a job. I didn't want to close my installment savings account, but I did, to have some reserved money for myself and also give some of it to my parents. I can't stop sending money to my parents because I have to make them believe I live well without any problem as always...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_15:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" I gave up. I gave up finding a new job, meeting people, receiving medical treatment, and everything. All are just useless. What I have now is…. only this tiny space. Where nothing happens unless I stir it.\n\n In spite of heaps of attempts to get a job, what I had was only frustration and discouragement. The hospital where I've...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_16:
        size(253, 358)
        contains:
            'gui/diary.webp'
        contains:
            Text(" Go die, you bitch. How dare you want to live on! You're such a hooker who tried to take another's husband! Why are you still alive? You know well what a useless thing you are. You're just a whore. Now are you going to cling to him, instead of your previous lover? You don't deserve to live anymore. Go away. Go away and die.\n\n Someone keeps whispering...", style="arc_diary_small"), xpos .0474 ypos .1955
    image arc_diary_01_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" It's been more than a month since I started working in a family restaurant. In the beginning, it was really hard to carry a tray and I even broke a few dishes. But now, I feel like I'm getting better and better. Sometimes, customers tip me as well, and also the other staff often praises my work. I'm especially good at…. hmmm…. well, it's too many to write them all down here! Later...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_02_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" Today the section chief of the head office visited the restaurant. I thought the chief would be a man, but she was a young woman. She came to our restaurant and called the captain to the locker room. She passed by me while I was working there, and I saw her nametag. And I found she has the same name as a famous comedian. Funny...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_03_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" I went to Cheolwon, with Eunyoung to see Yunwoo today. I didn't realize it was that cold, but when I got off the bus, I was just shocked as it was literally freezing. It didn't snow, and the wind didn't blow, but cold air made even my eyes freeze. Eunyoung and I hurried into the visitor's room to wait for Yunwoo.\n\n A few minutes later...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_04_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" After I parted with him, and while I was coming home, I tried really hard to fight back tears. But when I arrived in my room, I just burst into tears. Why? Why was I so mean to him? I raged at him, and told him to quit music. Why the hell did I do that?\n\n Today he told me what I've really looked forward to hearing from him, but why…. why couldn't I accept him...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_05_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" I had a long conversation with Yunwoo today;\n\n You've just been discharged from the army, and I'm a student without a job. So what can we do now? You really think we can get married and start our home? Seriously? How?\n\n Besides, we're not romantically involved with each other. We're just...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_06_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" It's been almost a year since I started working in this hospital. I work as a coordinator of the hospital. I had my salary raised, and also I'm pretty satisfied with my job. My savings account with the balance which gets bigger and bigger makes me feel really happy.\n\n When I had to quit the university temporarily, I was just stunned. But now that I...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_07_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" Oh, my god…. how could he look like him that much? His face, way of talking, character, and even that he can't hold liquor well…. everything is just like him. He reminds me of Yunwoo a lot. And it makes me feel sad. And this keeps bothering me so much. These days, I'm often trying to speak to him, or be around him. He also seems to be interested in me, and sometimes talks to me...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_08_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" His wife visited the hospital. Though the Director and my lover prefer a simple and plain style, she dressed up too much, with luxurious dress and accessories. She looked just full of vanity. When I saw she's coquetting with him arm in arm, she really looked like an old fox. I can't imagine she's the Director's sister, and my lover's wife. She really makes me feel sick...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_09_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" The director seemed to be trying hard not to hurt me, controlling his feelings. I understand he would feel betrayed as he has trusted me a lot, but he never swore at me at all, and treated me human to human. And now, I've finally realized what the hell I did. I felt really sorry for his wife, as she has never thought about this, and also felt sorry for the director who has always truly taken...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_10_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" Every single day, I cry, sleep, and wake from sleep, remember my good old days, especially with him, and then, cry, and fall asleep again. Beginning with a few days ago, I sometimes burst into laughter, and sometimes, burst into a fit of anger. I feel like I can't breathe well from time to time.\n\n I miss him. I miss him looking at me with a gentle smile...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_11_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" Even though I had no interview today, I sat in front of my dressing table to put on makeup. But as soon as I saw my face, I was frightened, as it suddenly looked awful and disgusting. I fell backward, and managed to crawl to the bed. And I trembled and trembled. Then, I called Hye-na and begged her to save me.\n\n Soon, Hye-na came to my...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_12_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" Today, I visited a neuropsychiatric clinic, with Hye-na. I was pretty afraid to go there, but as I was with my sister, I could do it. The doctor asked me a number of things, from trivial questions to what is happening to me now and what I don't want to tell others as well.\n\n He also asked whether I have some physical problems, and I told him I hurt myself...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_13_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" Today, I met Eunju. It's been a really long time since I've seen her. She used to be my best friend when we were high school students, but she is not single anymore. She said she's really worried as she hasn't lost any weight in spite of her steady diet since she gave birth to her baby. So I told her that she still looks good. Eunju worried about me saying I'm so bony, and she said to take her fat...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_14_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" These days, I receive mental health treatment, and also try hard to get a job. I didn't want to close my installment savings account, but I did, to have some reserved money for myself and also give some of it to my parents. I can't stop sending money to my parents because I have to make them believe I live well without any problem as always...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_15_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" I gave up. I gave up finding a new job, meeting people, receiving medical treatment, and everything. All are just useless. What I have now is…. only this tiny space. Where nothing happens unless I stir it.\n\n In spite of heaps of attempts to get a job, what I had was only frustration and discouragement. The hospital where I've...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image arc_diary_16_sepia:
        size(253, 358)
        contains:
            im.Sepia('gui/diary.webp')
        contains:
            Text(" Go die, you bitch. How dare you want to live on! You're such a hooker who tried to take another's husband! Why are you still alive? You know well what a useless thing you are. You're just a whore. Now are you going to cling to him, instead of your previous lover? You don't deserve to live anymore. Go away. Go away and die.\n\n Someone keeps whispering...", style="arc_diary_small_sepia"), xpos .0474 ypos .1955
    image walletnot:
        size(759, 153)
        contains:
            im.Rotozoom('gui/dialogue.webp', 0, .395)
        contains:
            Text('{b}Find Your Wallet{/b}', style='extext'), xalign .5 yalign .5
    image anxiety:
        size(759, 153)
        contains:
            im.Rotozoom('gui/dialogue.webp', 0, .395)
        contains:
            Text('{b}Find the Nebulizer{/b}', style='extext'), xalign .5 yalign .5
    image knife:
        size(759, 153)
        contains:
            im.Rotozoom('gui/dialogue.webp', 0, .395)
        contains:
            Text('{b}Find a Cutter Knife{/b}', style='extext'), xalign .5 yalign .5
    image drawer:
        size(759, 153)
        contains:
            im.Rotozoom('gui/dialogue.webp', 0, .395)
        contains:
            Text('{b}Open the Drawer{/b}', style='extext'), xalign .5 yalign .5
    image 404910_header_sepia = im.Sepia('images/404910_header.webp')
    image 375160_header_sepia = im.Sepia('images/375160_header.webp')
    image 375161_header_sepia = im.Sepia('images/375161_header.webp')
    image 382390_header_sepia = im.Sepia('images/382390_header.webp')
    image 384650_header_sepia = im.Sepia('images/384650_header.webp')
    image 407760_header_sepia = im.Sepia('images/407760_header.webp')
    image 558690_header_sepia = im.Sepia('images/558690_header.webp')
    image arc_char_07_bg = im.Flip('images/dr.webp', horizontal=True)
    image dialoguer = im.MatrixColor(('gui/dialogue.webp'), im.matrix.colorize("#4c0000", "#000"))
    image lock = Composite((320, 358), (0, 0), 'gui/polaroid.webp', (57, 12), Text('', style='awegall'))
    image con_lock = Composite((253, 358), (0, 0), im.Grayscale('gui/parchment.webp'), (24, 22), Text('', style='awearc'))
    image diary_lock = Composite((253, 358), (0, 0), im.Sepia('gui/diary.webp'), (24, 52), Text('', style='awearc'))
    image ending = Movie(fps=60, channel='video', play='images/ending.webm', image='images/ending.webp', layer='screens')
    image girl_walk = Movie(fps=60, channel='video', play='images/girl.webm', mask_channel='mask', image='images/girl.webp', side_mask=True, layer='screens')
    image girl_walk_flip = Movie(fps=60, channel='video', play='images/girl_hflip.webm', mask_channel='mask', image='leftgirl', side_mask=True, layer='screens')
    image shoes = Composite((1920, 1080), (420, -75), 'images/shoes.webp', (0, 0), 'images/circle.webp')
    image leftgirl = im.Flip('images/girl.webp', horizontal=True)
    image bshock = '#ff00004c'
    image night = '#0000d04c'
    image white = '#ffffff'
    image sky = '#4aafef'
    image dim = '#0008'
    image tdw_sepia = Composite((1920, 1080), (0, 0), im.Sepia('images/sin.webp'), (600, 0), im.Sepia('images/tdw.webp'))
    image slap_sepia = Composite((1920, 1080), (0, 0), im.Sepia('images/room.webp'), (600, 0), im.Sepia('images/slap.webp'))
    image deep_sepia = Composite((1920, 1080), (0, 0), im.Sepia('images/room.webp'), (800, 0), im.Sepia('images/deepkiss.webp'))
    image alleyway_gall = Composite((1920, 1080), (0, 0), 'images/alleyway.webp', (241, 0), 'images/alleyway_1.webp')
    image lean_gall = Composite((1920, 1080), (0, 0), 'images/post1.webp', (900, 0), 'images/lean.webp')
    image dw2017_0 = 'images/doa_1.webp'
    image dw2017_1 = 'images/doa.webp'
    image dw2017_2 = 'images/doa_2.webp'
    image dw2017_3 = 'images/doa_3.webp'
    image photop = 'images/photo.webp'
    if achievement.has('KNDW_SPONSOR') and persistent.esteregg is True:
        image video = Composite((1920, 1080), (0,0), 'images/hospital.webp', (0, 0), 'images/video.webp')
        image video_play = Movie(fps=60, channel='video', play='images/video.webm', image='video', layer='screens')
        image y_dakimakura_1 = Composite((1920, 5760), (0,0), 'images/y_dakimakura_1.webp', (816, 1793), 'images/y_dakimakura_uncensored.webp')
        image riding0 = Composite((1920, 2226), (0,0), 'images/riding_0_mask.webp', (893, 1587), 'images/riding_0_uncensored.webp')
        image riding1 = Movie(fps=60, channel='video', play='images/riding_1.webm', image='riding0', layer='screens')
        image riding2 = Movie(fps=60, channel='video', play='images/riding_2.webm', image='riding0', layer='screens')
        image riding3 = Movie(fps=60, channel='video', play='images/riding_3.webm', image='riding0', layer='screens')
        image fellatio =  Composite((2289, 1080), (0,0), 'images/fellatio.webp', (1222, 535), 'images/fellatio_uncensored.webp')
    else:
        image video = Composite((1920, 1080), (0,0), 'images/hospital.webp', (0, 0), 'images/video.webp', (260, 870), 'images/video_mask.webp')
        image video_play = Movie(fps=60, channel='video', play='images/video_mask.webm', image='video', layer='screens')
        image riding0 = 'images/riding_0_mask.webp'
        image riding1 = Movie(fps=60, channel='video', play='images/riding_1_mask.webm', image='riding_0_mask', layer='screens')
        image riding2 = Movie(fps=60, channel='video', play='images/riding_2_mask.webm', image='riding_0_mask', layer='screens')
        image riding3 = Movie(fps=60, channel='video', play='images/riding_3_mask.webm', image='riding_0_mask', layer='screens')
    image mas_1:
        contains:
            'video_play', video_divide_0
        contains:
            AlphaMask('images/masturbation_1.webp', mask='images/divide_mask.webp'), trueright
        contains:
            'divide', center
    image mas_2:
        contains:
            'video_play', video_divide_1
        contains:
            AlphaMask('images/masturbation_2.webp', mask='images/divide_mask.webp'), trueright
        contains:
            'divide', center
    image mas_3:
        contains:
            'video_play', video_divide_2
        contains:
            AlphaMask('images/masturbation_3.webp', mask='images/divide_mask.webp'), trueright
        contains:
            'divide', center
    image doa_1:
        contains:
            'images/doa_yunwoo_1.webp', topleft
        contains:
            AlphaMask('images/doa_gayeon_1.webp', mask='images/divide_mask.webp'), trueright
        contains:
            'divide', center
    image doa_2:
        contains:
            'images/doa_yunwoo_1.webp', topleft
        contains:
            AlphaMask('images/doa_gayeon_2.webp', mask='images/divide_mask.webp'), trueright
        contains:
            'divide', center
    image doa_3:
        contains:
            'images/doa_yunwoo_2.webp', topleft
        contains:
            AlphaMask('images/doa_gayeon_1.webp', mask='images/divide_mask.webp'), trueright
        contains:
            'divide', center
    image doa_4:
        contains:
            'images/doa_yunwoo_2.webp', topleft
        contains:
            AlphaMask('images/doa_gayeon_3.webp', mask='images/divide_mask.webp'), trueright
        contains:
            'divide', center
    image doa_5:
        contains:
            'images/doa_yunwoo_2.webp', topleft
        contains:
            AlphaMask('images/doa_gayeon_2.webp', mask='images/divide_mask.webp'), trueright
        contains:
            'divide', center
    image caress:
        'images/caress.webp', zoom 1.24 xalign .6 yalign .5
    image caress0:
        contains:
            'images/caress.webp', xpos -.23 yalign .7 zoom 1.24
        contains:
            'circle'
    image caress1:
        im.Rotozoom((Composite((1550, 1500), (0, 0), 'images/caress.webp', (951, 612), 'images/caress1.webp')), 0, 1.24), xalign .6 yalign .5
    image self_gall:
        im.Crop('images/self.webp', 0, 0, 1920, 1080), yalign .4
    image photo:
        'images/photo.webp', truecenter
    image rooml:
        contains:
            'images/room.webp'
        contains:
            'images/rooml.webp', xpos .782 ypos .106
    image gb_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/gb.webp')
    image g_angry:
        size(650, 1080)
        contains:
            'images/gb.webp'
        contains:
            'images/ga.webp', xpos .3077 ypos .1546
    image g_angry_gray:
        size(650, 1080)
        contains:
            im.Grayscale('images/gb.webp')
        contains:
            im.Grayscale('images/ga.webp'), xpos .3077 ypos .1546
    image g_angry_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/gb.webp')
        contains:
            im.Sepia('images/ga.webp'), xpos .3077 ypos .1546
    image g_question:
        size(650, 1080)
        contains:
            'images/gb.webp'
        contains:
            'images/gq.webp', xpos .3077 ypos .1546
    image g_question_gray:
        size(650, 1080)
        contains:
            im.Grayscale('images/gb.webp')
        contains:
            im.Grayscale('images/gq.webp'), xpos .3077 ypos .1546
    image g_question_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/gb.webp')
        contains:
            im.Sepia('images/gq.webp'), xpos .3077 ypos .1546
    image g_shock:
        size(650, 1080)
        contains:
            'images/gb.webp'
        contains:
            'images/gs_1.webp', xpos .3077 ypos .1546
    image g_shock_gray:
        size(650, 1080)
        contains:
            im.Grayscale('images/gb.webp')
        contains:
            im.Grayscale('images/gs_1.webp'), xpos .3077 ypos .1546
    image g_shock_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/gb.webp')
        contains:
            im.Sepia('images/gs_1.webp'), xpos .3077 ypos .1546
    image g_smile:
        size(650, 1080)
        contains:
            'images/gb.webp'
        contains:
            'images/gs.webp', xpos .3077 ypos .1546
    image g_smile_gray:
        size(650, 1080)
        contains:
            im.Grayscale('images/gb.webp')
        contains:
            im.Grayscale('images/gs.webp'), xpos .3077 ypos .1546
    image g_smile_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/gb.webp')
        contains:
            im.Sepia('images/gs.webp'), xpos .3077 ypos .1546
    image g_tear:
        size(650, 1080)
        contains:
            'images/gb.webp'
        contains:
            'images/gt.webp', xpos .3077 ypos .1546
    image g_tear_gray:
        size(650, 1080)
        contains:
            im.Grayscale('images/gb.webp')
        contains:
            im.Grayscale('images/gt.webp'), xpos .3077 ypos .1546
    image g_tear_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/gb.webp')
        contains:
            im.Sepia('images/gt.webp'), xpos .3077 ypos .1546
    image h_question:
        size(662, 1080)
        contains:
            'images/hb.webp'
        contains:
            'images/hq.webp', xalign .48 yalign .24
    image h_question_gray:
        size(662, 1080)
        contains:
            im.Grayscale('images/hb.webp')
        contains:
            im.Grayscale('images/hq.webp'), xalign .48 yalign .24
    image h_question_sepia:
        size(662, 1080)
        contains:
            im.Sepia('images/hb.webp')
        contains:
            im.Sepia('images/hq.webp'), xalign .48 yalign .24
    image h_tear:
        size(662, 1080)
        contains:
            'images/hb.webp'
        contains:
            'images/ht.webp', xalign .48 yalign .26
    image h_tear_gray:
        size(662, 1080)
        contains:
            im.Grayscale('images/hb.webp')
        contains:
            im.Grayscale('images/ht.webp'), xalign .48 yalign .26
    image h_tear_sepia:
        size(662, 1080)
        contains:
            im.Sepia('images/hb.webp')
        contains:
            im.Sepia('images/ht.webp'), xalign .48 yalign .26
    image h_opinion:
        size(662, 1080)
        contains:
            'images/hb.webp'
        contains:
            'images/ho.webp', xalign .48 yalign .26
    image h_opinion_gray:
        size(662, 1080)
        contains:
            im.Grayscale('images/hb.webp')
        contains:
            im.Grayscale('images/ho.webp'), xalign .48 yalign .26
    image h_opinion_sepia:
        size(662, 1080)
        contains:
            im.Sepia('images/hb.webp')
        contains:
            im.Sepia('images/ho.webp'), xalign .48 yalign .26
    image h_poker:
        size(662, 1080)
        contains:
            'images/hb.webp'
        contains:
            'images/hp.webp', xalign .48 yalign .26
    image h_poker_gray:
        size(662, 1080)
        contains:
            im.Grayscale('images/hb.webp')
        contains:
            im.Grayscale('images/hp.webp'), xalign .48 yalign .26
    image h_poker_sepia:
        size(662, 1080)
        contains:
            im.Sepia('images/hb.webp')
        contains:
            im.Sepia('images/hp.webp'), xalign .48 yalign .26
    image h_laugh:
        size(662, 1080)
        contains:
            'images/hb.webp'
        contains:
            'images/hl.webp', xalign .48 yalign .26
    image h_laugh_gray:
        size(662, 1080)
        contains:
            im.Grayscale('images/hb.webp')
        contains:
            im.Grayscale('images/hl.webp'), xalign .48 yalign .26
    image h_laugh_sepia:
        size(662, 1080)
        contains:
            im.Sepia('images/hb.webp')
        contains:
            im.Sepia('images/hl.webp'), xalign .48 yalign .26
    image h_smile:
        size(662, 1080)
        contains:
            'images/hb.webp'
        contains:
            'images/hs.webp', xalign .48 yalign .26
    image h_smile_gray:
        size(662, 1080)
        contains:
            im.Grayscale('images/hb.webp')
        contains:
            im.Grayscale('images/hs.webp'), xalign .48 yalign .26
    image h_smile_sepia:
        size(662, 1080)
        contains:
            im.Sepia('images/hb.webp')
        contains:
            im.Sepia('images/hs.webp'), xalign .48 yalign .26
    image i_poker:
        size(654, 1080)
        contains:
            'images/ib.webp'
        contains:
            'images/ip.webp', xalign .473 yalign .25
    image i_poker_gray:
        size(654, 1080)
        contains:
            im.Grayscale('images/ib.webp')
        contains:
            im.Grayscale('images/ip.webp'), xalign .473 yalign .25
    image i_poker_sepia:
        size(654, 1080)
        contains:
            im.Sepia('images/ib.webp')
        contains:
            im.Sepia('images/ip.webp'), xalign .473 yalign .25
    image i_smile:
        size(654, 1080)
        contains:
            'images/ib.webp'
        contains:
            'images/is.webp', xalign .493 yalign .24
    image i_smile_gray:
        size(654, 1080)
        contains:
            im.Grayscale('images/ib.webp')
        contains:
            im.Grayscale('images/is.webp'), xalign .493 yalign .24
    image i_smile_sepia:
        size(654, 1080)
        contains:
            im.Sepia('images/ib.webp')
        contains:
            im.Sepia('images/is.webp'), xalign .493 yalign .24
    image i_think:
        size(654, 1080)
        contains:
            'images/ib.webp'
        contains:
            'images/it.webp', xalign .492 yalign .25
    image i_think_gray:
        size(654, 1080)
        contains:
            im.Grayscale('images/ib.webp')
        contains:
            im.Grayscale('images/it.webp'), xalign .492 yalign .25
    image i_think_sepia:
        size(654, 1080)
        contains:
            im.Sepia('images/ib.webp')
        contains:
            im.Sepia('images/it.webp'), xalign .492 yalign .25
    image e_laugh:
        size(650, 1080)
        contains:
            'images/eb.webp'
        contains:
            'images/el.webp', xalign .499 yalign .24
    image e_think:
        size(650, 1080)
        contains:
            'images/eb.webp'
        contains:
            'images/et.webp', xalign .5 yalign .26
    image e_question:
        size(650, 1080)
        contains:
            'images/eb.webp'
        contains:
            'images/eq.webp', xalign .5 yalign .25
    image e_poker:
        size(650, 1080)
        contains:
            'images/eb.webp'
        contains:
            'images/ep.webp', xalign .5 yalign .26
    image e_laugh_gray:
        size(650, 1080)
        contains:
            im.Grayscale('images/eb.webp')
        contains:
            im.Grayscale('images/el.webp'), xalign .499 yalign .24
    image e_think_gray:
        size(650, 1080)
        contains:
            im.Grayscale('images/eb.webp')
        contains:
            im.Grayscale('images/et.webp'), xalign .5 yalign .26
    image e_question_gray:
        size(650, 1080)
        contains:
            im.Grayscale('images/eb.webp')
        contains:
            im.Grayscale('images/eq.webp'), xalign .5 yalign .25
    image e_poker_gray:
        size(650, 1080)
        contains:
            im.Grayscale('images/eb.webp')
        contains:
            im.Grayscale('images/ep.webp'), xalign .5 yalign .26
    image e_laugh_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/eb.webp')
        contains:
            im.Sepia('images/el.webp'), xalign .499 yalign .24
    image e_think_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/eb.webp')
        contains:
            im.Sepia('images/et.webp'), xalign .5 yalign .26
    image e_question_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/eb.webp')
        contains:
            im.Sepia('images/eq.webp'), xalign .5 yalign .25
    image e_poker_sepia:
        size(650, 1080)
        contains:
            im.Sepia('images/eb.webp')
        contains:
            im.Sepia('images/ep.webp'), xalign .5 yalign .26
    image y_smile:
        size(793, 1080)
        contains:
            'images/yb.webp'
        contains:
            'images/ys.webp', xalign .4245 yalign .214
    image y_think:
        size(793, 1080)
        contains:
            'images/yb.webp'
        contains:
            'images/yt.webp', xalign .4245 yalign .214
    image y_question:
        size(793, 1080)
        contains:
            'images/yb.webp'
        contains:
            'images/yq.webp', xalign .4245 yalign .214
    image y_poker:
        size(793, 1080)
        contains:
            'images/yb.webp'
        contains:
            'images/yp.webp', xalign .4245 yalign .214
    image y_angry:
        size(793, 1080)
        contains:
            'images/yb.webp'
        contains:
            'images/ya.webp', xalign .4245 yalign .214
    image y_smile_gray:
        size(793, 1080)
        contains:
            im.Grayscale('images/yb.webp')
        contains:
            im.Grayscale('images/ys.webp'), xalign .4245 yalign .214
    image y_think_gray:
        size(793, 1080)
        contains:
            im.Grayscale('images/yb.webp')
        contains:
            im.Grayscale('images/yt.webp'), xalign .4245 yalign .214
    image y_question_gray:
        size(793, 1080)
        contains:
            im.Grayscale('images/yb.webp')
        contains:
            im.Grayscale('images/yq.webp'), xalign .4245 yalign .214
    image y_poker_gray:
        size(793, 1080)
        contains:
            im.Grayscale('images/yb.webp')
        contains:
            im.Grayscale('images/yp.webp'), xalign .4245 yalign .214
    image y_angry_gray:
        size(793, 1080)
        contains:
            im.Grayscale('images/yb.webp')
        contains:
            im.Grayscale('images/ya.webp'), xalign .4245 yalign .214
    image y_smile_sepia:
        size(793, 1080)
        contains:
            im.Sepia('images/yb.webp')
        contains:
            im.Sepia('images/ys.webp'), xalign .4245 yalign .214
    image y_think_sepia:
        size(793, 1080)
        contains:
            im.Sepia('images/yb.webp')
        contains:
            im.Sepia('images/yt.webp'), xalign .4245 yalign .214
    image y_question_sepia:
        size(793, 1080)
        contains:
            im.Sepia('images/yb.webp')
        contains:
            im.Sepia('images/yq.webp'), xalign .4245 yalign .214
    image y_poker_sepia:
        size(793, 1080)
        contains:
            im.Sepia('images/yb.webp')
        contains:
            im.Sepia('images/yp.webp'), xalign .4245 yalign .214
    image y_angry_sepia:
        size(793, 1080)
        contains:
            im.Sepia('images/yb.webp')
        contains:
            im.Sepia('images/ya.webp'), xalign .4245 yalign .214
    image dr:
        'images/dr.webp', xalign .4
    image dr_sepia:
        im.Sepia('images/dr.webp')
    image part24_sepia:
        im.Sepia('images/part24.webp'), trueright
    image band:
        'images/band.webp', xalign .455
    image photog:
        'images/photo.webp', zoom 1.5
    image despair:
        contains:
            'black'
        contains:
            'images/despair.webp'
            xalign .43
    image self3:
        contains:
            'images/self3.webp', xpos .403 ypos .5
    image wall_gayeon_sigh:
        contains:
            'images/wall_gayeon_sigh.webp', xalign .35
    image wall_gayeon_glaring:
        contains:
            'images/wall_gayeon_glaring.webp', xalign .35
    image wall_gayeon_normal:
        contains:
            'images/wall_gayeon_normal.webp', xalign .35
    image wall_gayeon_side:
        contains:
            'images/wall_gayeon_side.webp', xalign .35
    image wall_yunwoo:
        contains:
            'images/wall_yunwoo.webp', xalign .65
    image wall_yunwoo_side:
        contains:
            'images/wall_yunwoo_side.webp', xalign .65
    image wall_sepia:
        contains:
            im.Sepia('images/wall_gayeon_normal.webp'), xalign .6
        contains:
            im.Sepia('images/wall_yunwoo.webp'), xalign .9
    image baby:
        'images/baby.webp'
        yalign .22 xalign .5
    image bread:
        'images/bread.webp'
        yalign .15 xalign .5
    image canned:
        'images/canned.webp'
        yalign .08 xalign .5
    image envelope:
        'images/envelope.webp'
        yalign .17 xalign .5
    image glasses:
        'images/glasses.webp'
        yalign .22 xalign .5
    image diary:
        'images/diary.webp'
        yalign .16 xalign .5
    image blink1:
        '#000'
        alpha 0
        linear .5 alpha 1
        linear .5 alpha 0
        linear .2 alpha 1
        linear .4 alpha 0
        pause 1
        linear .2 alpha 1
        linear .2 alpha 0
        linear .2 alpha 1
        linear .2 alpha 0
        linear .2 alpha 1
        linear .2 alpha 0
    image blink2:
        '#000'
        alpha 0
        linear .2 alpha 1
        linear .2 alpha 0
        linear .2 alpha 1
        linear .2 alpha 0
        linear .2 alpha 1
        linear .2 alpha 0
        pause 1
        linear .5 alpha 1
        linear .5 alpha 0
        pause 1
        linear .2 alpha 1
        linear .2 alpha 0
        linear .2 alpha 1
        linear .2 alpha 0
        linear .2 alpha 1
        linear .2 alpha 0
        pause 1
        repeat
    image blink3:
        '#000'
        alpha 0
        linear .2 alpha 1
        linear .2 alpha 0
        repeat
    transform times:
        xalign .45 yalign .5
        linear 3 xalign .5
    transform menuback:
        on selected_hover:
            linear .5 alpha 0
            linear .5 alpha 1
        on hover:
            linear .5 alpha 0
            linear .5 alpha 1
    transform obalpha:
        alpha 0
    transform obnebu:
        xpos .46 ypos .865
    transform left:
        xalign .2
    transform right:
        xalign .8
    transform main_balls:
        yzoom -1
    transform part_polaroid:
        xalign .1 yalign .5 alpha 0
        linear 3 rotate -5 alpha 1
    transform story_polaroid:
        yalign .5 alpha 0
        linear 3 alpha 1
    transform trueright:
        xalign 1.003 zoom 1.001
    transform video1:
        zoom 2 topright
    transform video2:
        zoom 2 xalign .5 yalign .8
    transform video3:
        zoom 2 left yalign .99
    transform video_divide_0:
        xpos -.325
    transform video_divide_1:
        xpos -.325
        linear 3 xpos -.25
    transform video_divide_2:
        xpos -.25
        linear 3 xpos -.1
    transform unlocked_center:
        zoom .2 truecenter
        linear .2 zoom 1.2
        linear .1 zoom 1
    transform unlocked_two_left:
        zoom .2 truecenter
        linear .2 zoom 1.2 xalign .4
        linear .1 zoom 1
    transform unlocked_two_right:
        zoom .2 truecenter
        linear .2 zoom 1.2 xalign .6
        linear .1 zoom 1
    transform unlocked_three_left:
        zoom .2 truecenter
        linear .2 zoom 1.2 xalign .3
        linear .1 zoom 1
    transform unlocked_three_right:
        zoom .2 truecenter
        linear .2 zoom 1.2 xalign .7
        linear .1 zoom 1
    transform unlocked_four_left:
        zoom .2 truecenter
        linear .2 zoom 1.2 xalign .2
        linear .1 zoom 1
    transform unlocked_four_right:
        zoom .2 truecenter
        linear .2 zoom 1.2 xalign .8
        linear .1 zoom 1
    transform unlocked_five_left:
        zoom .2 truecenter
        linear .2 zoom 1.2 xalign .1
        linear .1 zoom 1
    transform unlocked_five_right:
        zoom .2 truecenter
        linear .2 zoom 1.2 xalign .9
        linear .1 zoom 1
    transform unlocked_text:
        xalign .5 yalign .7 alpha 0
        pause .3
        alpha  1
        pause .1
        linear .5 yalign .65 alpha 0
    transform spread(child):
        contains:
            child
        contains:
            child
            yalign .2
            linear 1 yalign .175 zoom 1.5 alpha 0
    transform masturbation_gall:
        top
        linear 3 yalign .28
        linear 3 yalign .33
        linear 3 yalign .7
        linear 3 yalign .75
        linear 3 center
        linear 3 yalign .8
        linear 3 yalign .75
        linear 3 yalign .38
        linear 3 yalign .33
        linear 3 top
        repeat
    transform pusillanimous_gall:
        top
        linear 3 yalign .15
        linear 3 yalign .2
        linear 3 yalign .4
        linear 3 yalign .45
        linear 3 center
        linear 3 yalign .5
        linear 3 yalign .45
        linear 3 yalign .25
        linear 3 yalign .2
        linear 3 top
        repeat
    transform gray(child):
        im.Grayscale(child)
    transform sepia(child):
        im.Sepia(child)
    transform blur(child):
        contains:
            child
            alpha 1.0
        contains:
            child
            alpha 0.2 xoffset -3
        contains:
            child
            alpha 0.2 xoffset 3
        contains:
            child
            alpha 0.2 yoffset -3
        contains:
            child
            alpha 0.2 yoffset 3
    transform zoom_blur(child):
        contains:
            child
            alpha 1.0
        contains:
            child
            alpha 0.2 zoom 1.015
        contains:
            child
            alpha 0.2 zoom 1.010
        contains:
            child
            alpha 0.2 zoom 0.995
        contains:
            child
            alpha 0.2 zoom 0.990
    transform bridge_right:
        xalign .0
        linear 60 xalign .99
        repeat
    transform bridge_left:
        xalign .99
        linear 60 xalign .0
        repeat
    transform caress:
        center
        linear 5 yalign .2
        linear 3 top
        linear 5 yalign .8
        linear 3 center
        repeat
    transform fallatio:
        xalign .99
        linear 5 xalign .0
        linear 5 xalign .5
    transform bottomtotop:
        center
        linear 10 top
        linear 10 center
        repeat
    transform toptobottom:
        top
        linear 10 center
        linear 10 top
        repeat
    transform y_daki0:
        top
        linear 3 yalign .15
        linear 3 yalign .2
    transform y_daki1:
        yalign .2
        linear 3 yalign .35
        linear 3 yalign .4
        linear 3 center
        linear 3 yalign .45
        linear 3 yalign .4
        linear 3 zoom 2 yalign .4
    transform y_daki2:
        yalign .4
        linear 5 yalign .15
    transform y_daki3:
        yalign .35
        linear 1 yalign .4
    transform fellatio:
        xalign .0
        linear 5 xalign .99
        linear 5 xalign .0
        repeat
    transform fell:
        center
        linear .5 top
        linear 3 yalign .273
    transform leannoth_t(child):
        contains:
            child
            center
            pause 1
            top
            pause 1
            truecenter
            pause 1
            yalign .3
            pause 1
            yalign .7
            pause 1
    $ g = Gallery()
    $ g.locked_button = 'lock'
    $ g.navigation = True
    $ g.button('that day we')
    $ g.condition('persistent.unlock_1==True')
    $ g.image('sin', 'tdw')
    $ g.button('eternal happiness')
    $ g.condition('persistent.unlock_2==True')
    $ g.image('photog')
    $ g.button('despair')
    $ g.condition('persistent.unlock_3==True')
    $ g.image('despair')
    $ g.button('lean_gall')
    $ g.condition('persistent.unlock_4==True')
    $ g.image('lean_gall', 'night')
    $ g.button('imf crisis')
    $ g.condition('persistent.unlock_5==True')
    $ g.image('imf', 'circle')
    $ g.button('newspaper delivery')
    $ g.condition('persistent.unlock_6==True')
    $ g.image('delivery')
    $ g.button('kiss me')
    $ g.condition('persistent.unlock_7==True')
    $ g.image('post', 'kissme', 'night')
    $ g.button('video_gall')
    $ g.condition('persistent.unlock_8==True')
    $ g.image('video')
    $ g.transform(video1)
    $ g.image('video')
    $ g.transform(video2)
    $ g.image('video')
    $ g.transform(video3)
    $ g.image('video_play')
    $ g.button('deep kiss')
    $ g.condition('persistent.unlock_10==True')
    $ g.image('room', 'deepkiss')
    $ g.button('smoking')
    $ g.condition('persistent.unlock_12==True')
    $ g.image('smoking')
    $ g.button('self_gall')
    $ g.condition('persistent.unlock_13==True')
    $ g.image('self_gall')
    $ g.button('bridge')
    $ g.condition('persistent.unlock_14==True')
    $ g.image('bridge_gall')
    $ g.image('ending')
    $ g.condition('persistent.ending==True')
    $ g.button('growing')
    $ g.condition('persistent.unlock_15==True')
    $ g.image('wall', 'wall_gayeon_sigh', 'wall_yunwoo')
    $ g.image('wall', 'wall_gayeon_glaring', 'wall_yunwoo')
    $ g.image('wall', 'wall_gayeon_side', 'wall_yunwoo')
    $ g.image('wall', 'wall_gayeon_side', 'wall_yunwoo_side')
    $ g.button('frustration')
    $ g.condition('persistent.unlock_16==True')
    $ g.image('frustration', 'circle')
    $ g.button('vomiting')
    $ g.condition('persistent.unlock_17==True')
    $ g.image('vomiting', 'circle')
    $ g.button('pusillanimous')
    $ g.condition('persistent.unlock_18==True')
    $ g.image('pusillanimous', 'circle')
    $ g.button('corruption')
    $ g.condition('persistent.unlock_19==True')
    $ g.image('corruption')
    $ g.button('rip')
    $ g.condition('persistent.unlock_20==True')
    $ g.image('rip')
    $ g.button('moonlight')
    $ g.condition('persistent.unlock_21==True')
    $ g.image('moonlight3')
    $ g.image('moonlight0')
    $ g.image('moonlight1')
    $ g.image('moonlight2')
    $ g.button('fate')
    $ g.condition('persistent.unlock_22==True')
    $ g.image('fate')
    $ g.button('distortion')
    $ g.condition('persistent.unlock_23==True')
    $ g.image('room', 'slap')
    $ g.button('drunken')
    $ g.condition('persistent.unlock_24==True')
    $ g.image('hof', 'drunken')
    $ g.button('alleyway')
    $ g.condition('persistent.unlock_25==True')
    $ g.image('alleyway_gall', 'night')
    $ g.button('masturbation')
    $ g.condition('persistent.unlock_9==True')
    $ g.image('mas_1')
    $ g.image('mas_2')
    $ g.image('mas_3')
    $ g.button('caress')
    $ g.condition('persistent.unlock_11==True')
    $ g.image('caress')
    $ g.transform(caress)
    $ g.image('caress1')
    $ g.transform(caress)
    $ g.button('fellatio')
    $ g.condition('persistent.unlock_11==True')
    $ g.image('y_dakimakura_0')
    $ g.transform(toptobottom)
    $ g.image('y_dakimakura_1')
    $ g.transform(toptobottom)
    $ g.image('y_dakimakura_2')
    $ g.image('fellatio')
    $ g.transform(fellatio)
    $ g.button('riding')
    $ g.condition('persistent.unlock_11==True')
    $ g.image('riding1')
    $ g.transform(bottomtotop)
    $ g.image('riding2')
    $ g.transform(bottomtotop)
    $ g.image('riding3')
    $ g.transform(bottomtotop)
    $ g.button('serving')
    $ g.condition('persistent.unlock_26==True')
    $ g.image('serving')
    $ g.button('edge')
    $ g.condition('persistent.unlock_27==True')
    $ g.image('shoes')
    $ g.image('eotw0')
    $ g.transform(zoom_blur)
    $ g.image('eotw0')
    $ g.image('eotw1')
    $ g.transform(zoom_blur)
    $ g.image('eotw1')
    $ g.image('eotw1')
    $ g.transform(zoom_blur)
    $ g.button('doa')
    $ g.condition('persistent.unlock_28==True')
    $ g.image('doa_1')
    $ g.image('doa_2')
    $ g.image('doa_5')
    $ g.image('doa_3')
    $ g.image('doa_4')
    $ g.button('doa0')
    $ g.condition('persistent.unlock_29==True')
    $ g.image('dw2017_0')
    $ g.transform(fell)
    $ g.image('dw2017_1')
    $ g.image('dw2017_2')
    $ g.image('dw2017_3')
    $ g.condition('persistent.unlock_30==True')
    $ g.button('nte')
    $ g.condition('persistent.unlock_31==True')
    $ g.image('nte')
    $ g.transition = Dissolve(1.0)
    $ mr = MusicRoom(fadeout=1.0)
    $ mr.add('bgm/Pandemic.opus', always_unlocked=True)
    $ mr.add('bgm/Sigh day.opus')
    $ mr.add('bgm/Mare tranquillitatis.opus')
    $ mr.add('bgm/CCCanon.opus')
    $ mr.add("bgm/Let's game.opus")
    $ mr.add('bgm/Peace.opus')
    $ mr.add('bgm/Unknown mist.opus')
    $ mr.add('bgm/Lush garden.opus')
    $ mr.add('bgm/Jormungandr.opus')
    $ mr.add('bgm/Nyx.opus')
    $ mr.add('bgm/Summit showdown.opus')
    $ mr.add('bgm/Love song.opus')
    $ mr.add('bgm/Sea of nectar.opus')
    image wimcj_system_black = '#0000007f'
    image wimcj_system_black_deep = '#000000b2'
    image wimcj_system_gall_black = '#0000003f'
    image wimcj_system_white = '#ffffff19'
    image wimcj_system_level_white = '#ffffff7f'
    image wimcj_system_comment = Text('', font='gui/fonts/fontawesome.ttf', size=256)
    image wimcj_system_comment_black = Text('', font='gui/fonts/fontawesome.ttf', size=256, color='#000')
    image wimcj_system_comment0 = Text('', font='gui/fonts/fontawesome.ttf', size=256)
    image wimcj_system_comment0_black = Text('', font='gui/fonts/fontawesome.ttf', size=256, color='#000')
    image wimcj_system_hungry = Composite((256, 256), (0, 0), 'wimcj_system_comment0_flip', (80, 70), Text('', font='gui/fonts/fontawesome.ttf', size=128))
    image wimcj_system_bulb = Composite((256, 256), (0, 0), 'wimcj_system_comment0_flip', (140, 70), Text('', font='gui/fonts/fontawesome.ttf', size=128))
    image wimcj_system_bulb_black = Composite((256, 256), (0, 0), 'wimcj_system_comment0_black_flip', (90, 70), Text('', font='gui/fonts/fontawesome.ttf', color='#000', size=128))
    image wimcj_system_question = Composite((256, 256), (0, 0), 'wimcj_system_comment0', (88, 70), Text('', font='gui/fonts/fontawesome.ttf', size=128))
    image wimcj_system_question_black = Composite((256, 256), (0, 0), 'wimcj_system_comment0_black', (88, 70), Text('', font='gui/fonts/fontawesome.ttf', size=128, color='#000'))
    image wimcj_system_comment_flip = Transform('wimcj_system_comment', xzoom=-1.0)
    image wimcj_system_comment_black_flip = Transform('wimcj_system_comment_black', xzoom=-1.0)
    image wimcj_system_comment0_flip = Transform('wimcj_system_comment0', xzoom=-1.0)
    image wimcj_system_comment0_black_flip = Transform('wimcj_system_comment0_black', xzoom=-1.0)
    image wimcj_cafe_sepia = im.Sepia('images/wimcj_cafe.webp')
    image wimcj_voxel_0001_sepia = im.Sepia('images/wimcj_voxel_0001.webp')
    image wimcj_voxel_0002_sepia = im.Sepia('images/wimcj_voxel_0002.webp')
    image wimcj_voxel_0003_sepia = im.Sepia('images/wimcj_voxel_0003.webp')
    image wimcj_voxel_0005_sepia = im.Sepia('images/wimcj_voxel_0005.webp')
    image wimcj_voxel_0006_sepia = im.Sepia('images/wimcj_voxel_0006.webp')
    image wimcj_level_001_02_sepia = im.Sepia('images/wimcj_level_001_02.webp')
    image wimcj_level_001_small = im.Scale('images/wimcj_level_001.webp', 380, 320)
    image wimcj_sys_radar = Text('!ON RADAR!', style='wimcj_large_message', color='#00ff00', outlines=[(1, "#000000cf", 0, 0)], xalign=.5, yalign=.5)
    image wimcj_sys_start = Text('!START!', style='wimcj_large_message', outlines=[(1, "#000000cf", 0, 0)], xalign=.5, yalign=.5)
    image wimcj_sys_warning = Text('!WARNING!', style='wimcj_large_message', color='#ff0000', outlines=[(1, "#000000cf", 0, 0)], xalign=.5, yalign=.5)
    image trophy_57354 = im.Scale('images/trophy_57354.webp', 256, 256)
    transform wimcj_sys_center:
        linear .5 alpha 1
        linear .5 alpha 0
        repeat
    transform wimcj_emoticons:
        linear .2 rotate -30
        linear .2 rotate 30
        linear .2 rotate -30
        linear .2 rotate 30
        linear .2 rotate 0
