init python:
    import math
    class Shaker(object):
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
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
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
        return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)
    def vibrate(duration):
        if persistent.vibrate:
            renpy.vibrate(duration)
    if persistent.opening is None:
        persistent.opening = False
    if persistent.vibrate is None:
        persistent.vibrate = True
    if persistent.alarm is None:
        persistent.alarm = True
    if persistent.korean is None:
        persistent.korean = False
    if persistent.gayeon is None:
        persistent.gayeon = False
    if persistent.hyena is None:
        persistent.hyena = False
    if persistent.yunwoo is None:
        persistent.yunwoo = False
    if persistent.interviewer is None:
        persistent.interviewer = False
    if persistent.angel is None:
        persistent.angel = False
    if persistent.bgm02 is None:
        persistent.bgm02 = False
    if persistent.bgm03 is None:
        persistent.bgm03 = False
    if persistent.bgm04 is None:
        persistent.bgm04 = False
    if persistent.bgm05 is None:
        persistent.bgm05 = False
    if persistent.bgm06 is None:
        persistent.bgm06 = False
    if persistent.bgm07 is None:
        persistent.bgm07 = False
    if persistent.bgm08 is None:
        persistent.bgm08 = False
    if persistent.bgm09 is None:
        persistent.bgm09 = False
    if persistent.bgm10 is None:
        persistent.bgm10 = False
    if persistent.part01 is None:
        persistent.part01 = False
    if persistent.part02 is None:
        persistent.part02 = False
    if persistent.part03 is None:
        persistent.part03 = False
    if persistent.part04 is None:
        persistent.part04 = False
    if persistent.part05 is None:
        persistent.part05 = False
    if persistent.part06 is None:
        persistent.part06 = False
    if persistent.part07 is None:
        persistent.part07 = False
    if persistent.part08 is None:
        persistent.part08 = False
    if persistent.part09 is None:
        persistent.part09 = False
    if persistent.con01 is None:
        persistent.con01 = False
    if persistent.unlock_1 is None:
        persistent.unlock_1 = False
    if persistent.unlock_2 is None:
        persistent.unlock_2 = False
    d = Dissolve(1.0)
    d3 = Dissolve(3.0)
    d5 = Dissolve(0.5)
    dl = Dissolve(5.0)
    px = Pixellate(3.0, 10)
    px5 = Pixellate(3.0, 30)
    flash = Fade(0.1, 0.0, 1.0, color='#fff')
    red = Fade(0.1, 0.0, 1.0, color='#ff0000')
    dissolvee = ImageDissolve(im.Crop('demosprites00.jpg', (7680, 1080, 1920, 1080)), time = 1.0, ramplen = 512)
    f = Fade(1.0, 0.0, 1.0)
    f3 = Fade(3.0, 0.0, 3.0)
    p = Character('Me', window_background = Frame('dialoguer', 0, 0))
    h = Character('Hye-Na')
    y = Character('Yun-Woo')
    ex = p.copy('Staff')
    exx = p.copy('???')
    pm = Character('Me')
    intern = Character('Interviewer')
    yme = Character('Me')
    woo = Character(None)
    na = woo.copy(window_background = Frame('dialoguer', 0, 0))
    Shake = renpy.curry(_Shake)
    shock = Shake((0, 0, 0, 0), 1.0, dist=10)
    shock2 = Shake((0, 0, 0, 0), 3.0, dist=50)
    archives = 2
label splashscreen:
    if persistent.korean is False:
        show warning
    else:
        show warning_ko
    show expression Text ('WARNING', yalign=.12, size=72, color="#fff")
    show expression Text ('This game contains Suggestive Themes, Alcohol Reference', yalign=.3, color='#fff', text_align=.5)
    $ renpy.transition(Dissolve(1))
    $ renpy.pause(5, hard = True)
    if persistent.opening is False:
        scene renpy
        with pixellate
        pause 5
        scene black
        $ renpy.transition(Dissolve(1))
        $ renpy.pause(1, hard = True)
        show expression Text ("I never wanna be born human again, ever.", yalign=.5, size=48) onlayer overlay as text with dl
        with dl
        $ persistent.opening=True
    else:
        pass