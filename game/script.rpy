init python:
    import subprocess, sys, os, shutil, math, pygame_sdl2 as pygame
    class OpenDirectory(Action):
        def __init__(self, directory, absolute=False):
            if absolute:
                self.directory = directory
            else:
                self.directory = os.path.join(config.basedir, directory)
        def get_sensitive(self):
            return os.path.exists(self.directory)
        def __call__(self):
            try:
                directory = renpy.fsencode(self.directory)
                if renpy.windows:
                    os.startfile(directory)
                elif renpy.macintosh:
                    subprocess.Popen(["open", directory])
                else:
                    subprocess.Popen(["xdg-open", directory])
            except:
                pass
    class Shaker(object):
        anchors = {'top' : 0.0, 'center' : 0.5, 'bottom' : 1.0, 'left' : 0.0, 'right' : 1.0,}
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            self.start = [ self.anchors.get(i, i) for i in start ]
            self.dist = dist
            self.child = child
        def __call__(self, t, sizes):
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)
    def esteregg_01(drags, drop):
        if not drop:
            return
        p_x = drags[0].drag_name.split("-")[0]
        p_y = drags[0].drag_name.split("-")[1]
        t_x = drop.drag_name.split("-")[0]
        t_y = drop.drag_name.split("-")[1]
        a = []
        a.append(drop.drag_joined)
        a.append((drags[0], 3, 3))
        drop.drag_joined(a)
        if p_x == t_x and p_y == t_y:
            renpy.music.play("se/over.opus", channel="sound")
            my_x = int(int(p_x)*active_area_size*x_scale_index)-int(grip_size*x_scale_index)+puzzle_field_offset
            my_y = int(int(p_y)*active_area_size*y_scale_index)-int(grip_size*y_scale_index)+puzzle_field_offset
            drags[0].snap(my_x,my_y, delay=0.1)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True
            for i in range(0, grid_width):
                for j in range(0, grid_height):
                    if placedlist[i,j] == False:
                        return
            return True
        return
    def esteregg_02(drags, drop):
        if not drop:
            return
        store.ester_polaroid = drags[0].drag_name
        store.ester_order = drop.drag_name
        if ester_polaroid == 'ester_polaroid_01' and ester_order == 'ester_order_01':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(290, 172, delay=0)
            drags[0].draggable = False
            persistent.ester_order += 1
        elif ester_polaroid and ester_order == 'ester_order_01':
            drags[0].snap(290, 172, delay=0)
        if ester_polaroid == 'ester_polaroid_02' and ester_order == 'ester_order_02':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(620, 172, delay=0)
            drags[0].draggable = False
            persistent.ester_order += 1
        elif ester_polaroid and ester_order == 'ester_order_02':
            drags[0].snap(620, 172, delay=0)
        if ester_polaroid == 'ester_polaroid_03' and ester_order == 'ester_order_03':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(950, 172, delay=0)
            drags[0].draggable = False
            persistent.ester_order += 1
        elif ester_polaroid and ester_order == 'ester_order_03':
            drags[0].snap(950, 172, delay=0)
        if ester_polaroid == 'ester_polaroid_04' and ester_order == 'ester_order_04':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(1280, 172, delay=0)
            drags[0].draggable = False
            persistent.ester_order += 1
        elif ester_polaroid and ester_order == 'ester_order_04':
            drags[0].snap(1280, 172, delay=0)
        if ester_polaroid == 'ester_polaroid_05' and ester_order == 'ester_order_05':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(290, 540, delay=0)
            drags[0].draggable = False
            persistent.ester_order += 1
        elif ester_polaroid and ester_order == 'ester_order_05':
            drags[0].snap(290, 540, delay=0)
        if ester_polaroid == 'ester_polaroid_06' and ester_order == 'ester_order_06':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(620, 540, delay=0)
            drags[0].draggable = False
            persistent.ester_order += 1
        elif ester_polaroid and ester_order == 'ester_order_06':
            drags[0].snap(620, 540, delay=0)
        if ester_polaroid == 'ester_polaroid_07' and ester_order == 'ester_order_07':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(950, 540, delay=0)
            drags[0].draggable = False
            persistent.ester_order += 1
        elif ester_polaroid and ester_order == 'ester_order_07':
            drags[0].snap(950, 540, delay=0)
        if ester_polaroid == 'ester_polaroid_08' and ester_order == 'ester_order_08':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(1280, 540, delay=0)
            drags[0].draggable = False
            persistent.ester_order += 1
        elif ester_polaroid and ester_order == 'ester_order_08':
            drags[0].snap(1280, 540, delay=0)
        if persistent.ester_order == 8:
            return True
    def esteregg_03(drags, drop):
        if not drop:
            return
        p_x = drags[0].drag_name.split("-")[0]
        p_y = drags[0].drag_name.split("-")[1]
        t_x = drop.drag_name.split("-")[0]
        t_y = drop.drag_name.split("-")[1]
        a = []
        a.append(drop.drag_joined)
        a.append((drags[0], 3, 3))
        drop.drag_joined(a)
        if p_x == t_x and p_y == t_y:
            renpy.music.play("se/over.opus", channel="sound")
            my_x = int(int(p_x)*active_area_size*x_scale_index)-int(grip_size*x_scale_index)+puzzle_field_offset
            my_y = int(int(p_y)*active_area_size*y_scale_index)-int(grip_size*y_scale_index)+puzzle_field_offset
            drags[0].snap(my_x,my_y, delay=0.1)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True
            for i in range(0, grid_width):
                for j in range(0, grid_height):
                    if placedlist[i,j] == False:
                        return
            return True
        return
    def esteregg_04(drags, drop):
        if not drop:
            return
        store.ester_polaroid_last = drags[0].drag_name
        store.ester_order_last = drop.drag_name
        if ester_polaroid_last == 'ester_polaroid_01' and ester_order_last == 'ester_order_01':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(290, 172, delay=0)
            drags[0].draggable = False
            persistent.ester_last_order += 1
        elif ester_polaroid_last and ester_order_last == 'ester_order_01':
            drags[0].snap(290, 172, delay=0)
        if ester_polaroid_last == 'ester_polaroid_02' and ester_order_last == 'ester_order_02':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(620, 172, delay=0)
            drags[0].draggable = False
            persistent.ester_last_order += 1
        elif ester_polaroid_last and ester_order_last == 'ester_order_02':
            drags[0].snap(620, 172, delay=0)
        if ester_polaroid_last == 'ester_polaroid_03' and ester_order_last == 'ester_order_03':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(950, 172, delay=0)
            drags[0].draggable = False
            persistent.ester_last_order += 1
        elif ester_polaroid_last and ester_order_last == 'ester_order_03':
            drags[0].snap(950, 172, delay=0)
        if ester_polaroid_last == 'ester_polaroid_04' and ester_order_last == 'ester_order_04':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(1280, 172, delay=0)
            drags[0].draggable = False
            persistent.ester_last_order += 1
        elif ester_polaroid_last and ester_order_last == 'ester_order_04':
            drags[0].snap(1280, 172, delay=0)
        if ester_polaroid_last == 'ester_polaroid_05' and ester_order_last == 'ester_order_05':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(290, 540, delay=0)
            drags[0].draggable = False
            persistent.ester_last_order += 1
        elif ester_polaroid_last and ester_order_last == 'ester_order_05':
            drags[0].snap(290, 540, delay=0)
        if ester_polaroid_last == 'ester_polaroid_06' and ester_order_last == 'ester_order_06':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(620, 540, delay=0)
            drags[0].draggable = False
            persistent.ester_last_order += 1
        elif ester_polaroid_last and ester_order_last == 'ester_order_06':
            drags[0].snap(620, 540, delay=0)
        if ester_polaroid_last == 'ester_polaroid_07' and ester_order_last == 'ester_order_07':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(950, 540, delay=0)
            drags[0].draggable = False
            persistent.ester_last_order += 1
        elif ester_polaroid_last and ester_order_last == 'ester_order_07':
            drags[0].snap(950, 540, delay=0)
        if ester_polaroid_last == 'ester_polaroid_08' and ester_order_last == 'ester_order_08':
            renpy.music.play("se/over.opus", channel="sound")
            drags[0].snap(1280, 540, delay=0)
            drags[0].draggable = False
            persistent.ester_last_order += 1
        elif ester_polaroid_last and ester_order_last == 'ester_order_08':
            drags[0].snap(1280, 540, delay=0)
        if persistent.ester_last_order == 8:
            return True
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
        return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)
    def vibrate(duration):
        if persistent.vibrate:
            renpy.vibrate(duration)
    def controllers(old, new, current):
            current.update(old)
            current.update(new)
            return current
    def dlc(old, new, current):
            current.update(old)
            current.update(new)
            return current
    renpy.register_persistent('install', dlc)
    renpy.register_persistent('delete', dlc)
    renpy.register_persistent('buy', dlc)
    renpy.register_persistent('steam', controllers)
    renpy.register_persistent('xbox', controllers)
    renpy.register_persistent('ouya', controllers)
    achievement.register('KNDW_IDENTIFY', steam_stat='IDENTIFY', stat_max=10)
    achievement.register('KNDW_CONCEPT', steam_stat='CONCEPT', stat_max=13)
    achievement.register('KNDW_DIARY')
    achievement.register('KNDW_ART', steam_stat='ART', stat_max=32)
    achievement.register('KNDW_OST', steam_stat='OST', stat_max=13)
    achievement.register('KNDW_PROGRESS', steam_stat='PROGRESS', stat_max=25)
    achievement.register('KNDW_OBJECT', steam_stat='OBJECT', stat_max=10)
    achievement.register('KNDW_KILLER')
    achievement.register('KNDW_MASTER')
    achievement.register('KNDW_SPONSOR')
    achievement.register('KNDW_FRONTIER')
    achievement.register('KNDW_MASTER_FRONTIER')
    achievement.register('KNDW_START')
    achievement.register('KNDW_VOTERS')
    achievement.register('KNDW_GAMEOVER')
    achievement.register('KNDW_ACCIDENT')
    achievement.register('KNDW_DEMO')
    achievement.register('KNDW_ADULT', steam_stat='ADULT', stat_max=5)
    achievement.register('KNDW_LEFT', steam_stat='LEFT', stat_max=3)
    achievement.register('KNDW_RIGHT', steam_stat='RIGHT', stat_max=6)
    achievement.register('KNDW_MURDERER')
    achievement.register('KNDW_ONLOOKER')
    achievement.register('KNDW_WALLET')
    achievement.register('KNDW_HOLDER')
    achievement.register('KNDW_NEBULIZER')
    achievement.register('KNDW_DRAWER')
    achievement.register('KNDW_VIDEO')
    achievement.register('KNDW_DYING_MESSAGE')
    achievement.register('KNDW_RELEASE')
    achievement.register('KNDW_INTRODUCTION')
    achievement.register('KNDW_DEVELOPMENT')
    achievement.register('KNDW_TURN')
    achievement.register('KNDW_CONCLUSION')
    achievement.register('KNDW_DETECTIVE')
    achievement.register('KNDW_MOD_PLAYER')
    achievement.register('KNDW_CREATOR')
    d = Dissolve(1.0)
    d3 = Dissolve(3.0)
    d5 = Dissolve(0.5)
    dl = Dissolve(5.0)
    px = Pixellate(3.0, 10)
    px5 = Pixellate(3.0, 30)
    flash = Fade(0.1, 0.0, 1.0, color='#fff')
    flash3 = Fade(0.3, 0.0, 3.0, color='#fff')
    red = Fade(0.1, 0.0, 1.0, color='#ff0000')
    blind = ImageDissolve('images/blind.webp', time=1.0, ramplen=512)
    centerblind = ImageDissolve('images/centerblind.webp', time=3.0, ramplen=256)
    f = Fade(1.0, 0.0, 1.0)
    f3 = Fade(3.0, 0.0, 3.0)
    p = Character('Me', window_background = Image(im.MatrixColor(('gui/dialogue.webp'), im.matrix.colorize("#4c0000", "#000"))))
    h = Character('Hye-na')
    y = Character('Yunwoo')
    b = Character('Taejin')
    ga = Character('Ga-yeon')
    pp = ga.copy(window_background = Image(im.MatrixColor(('gui/dialogue.webp'), im.matrix.colorize("#4c0000", "#000"))))
    ex = p.copy('angelname', dynamic = True)
    pm = Character('Me')
    intern = Character('Interviewer')
    pa = Character('Misun')
    woo = Character(None)
    na = woo.copy(window_background = Image(im.MatrixColor(('gui/dialogue.webp'), im.matrix.colorize("#4c0000", "#000"))))
    system = Character('System')
    Shake = renpy.curry(_Shake)
    shock = Shake((0, 0, 0, 0), 1.0, dist=10)
    shock2 = Shake((0, 0, 0, 0), 3.0, dist=50)
    sicount = 0
    sigiveup = 0
    wallet = 0
    go = 1
    gocount = 0
    progress = 0
    arc_diary = 0
    gp = 0
    gc = 0
    gd = 0
    gg = 0
    gm = 0
    gr = 0
    smoke = 0
    dlc_key = 0
    blind_set = None
    wimcj_timer_range = 0
    wimcj_timer_jump = 0
    wimcj_level = 0
    wimcj_level_001_move = 0
    wimcj_level_001_trick_1 = 0
    wimcj_timer_hurryup = Shake((.01, .01, 0, 0), 10, dist=10)
    wimcj_timer_hurry = Shake((.01, .01, 0, 0), 20, dist=5)
    wimcj_timer_normal = Shake((.01, .01, 0, 0), 100, dist=1)
    mod_name_len = len(mod_name)
    mod_desc_len = len(mod_desc)
    mod_label_len = len(mod_label)
    if persistent.con is None:
        persistent.con = 1
    if persistent.gall is None:
        persistent.gall = 0
    if persistent.bgm is None:
        persistent.bgm = 1
    if persistent.char is None:
        persistent.char = 1
    if persistent.replay is None:
        persistent.replay = 0
    if persistent.ester_order is None:
        persistent.ester_order = 0
    if persistent.ester_last_order is None:
        persistent.ester_last_order = 0
    persistent.archives = False
    persistent.downloadable = False
label splashscreen:
    if persistent.opening is None:
        call screen default_language
    scene black
    if _preferences.language is None or _preferences.language == "Spanish":
        if persistent.blind is True:
            show expression Text("[gui.attention]\nThe episode is adult content. The program contains Violence, Blood, Strong Sexual Content, Nudity, Strong Language, Use of Tobacco, Alcohol Reference. Not recommended for Children, Seniors or Pregnant, Feeble-Minded Person.", yalign=.5, size=48, style="centered_text")
        else:
            show warning at truecenter
    else:
        show expression Text("[gui.attention]", yalign=.1, size=72)
        show expression Text("[gui.language]", yalign=.3, size=48, style="centered_text")
        show warning
    $ renpy.transition(Dissolve(1))
    if persistent.blind is True:
        pause 30
    else:
        $ renpy.pause(3, hard = True)
    scene black
    if not persistent.blind is True:
        $ renpy.transition(Dissolve(3))
        $ renpy.pause(3, hard = True)
    if persistent.opening is None:
        scene black
        show yggdrasil_logo at truecenter
        with d5
        pause 1
        scene sky
        show chibilis_logo at truecenter
        with d5
        pause 1
        scene white
        show renpy_logo at truecenter
        show expression Text("Created with Ren'Py Visual Novel Engine", yalign=.82, size=24, color="#404040")
        with d5
        pause 1
        scene black with d
        $ renpy.pause(1, hard = True)
        show born_balls at main_balls
        show expression Text("I never wanna be born human again, ever.", yalign=.5, size=48) as text onlayer overlay with dl
        with dl
        $ persistent.opening = True
    else:
        pass