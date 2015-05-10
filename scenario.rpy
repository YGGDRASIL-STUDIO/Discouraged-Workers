label start:
    show screen key_screen
    if persistent.gayeon is True:
        $ archives += 1
    if persistent.hyena is True:
        $ archives += 1
    if persistent.yunwoo is True:
        $ archives += 1
    if persistent.interviewer is True:
        $ archives += 1
    if persistent.angel is True:
        $ archives += 1
    if persistent.bgm02 is True:
        $ archives += 1
    if persistent.bgm03 is True:
        $ archives += 1
    if persistent.bgm04 is True:
        $ archives += 1
    if persistent.bgm05 is True:
        $ archives += 1
    if persistent.bgm06 is True:
        $ archives += 1
    if persistent.bgm07 is True:
        $ archives += 1
    if persistent.bgm08 is True:
        $ archives += 1
    if persistent.bgm09 is True:
        $ archives += 1
    if persistent.bgm10 is True:
        $ archives += 1
    if persistent.unlock_1 is True:
        $ archives += 1
    if persistent.unlock_2 is True:
        $ archives += 1
    stop music
    scene black with d
    $ show_quick_menu = False
    centered '{cps=15}Discouraged Workers{/cps}'
    centered '{cps=15}The one who wants to get a job,{w=.3} but gives up because it\'s impossible.{/cps}'
    pause 1
    scene dw
    show expression Text ('{color=#ff9000}{size=+64}A{/size}{/color}re you alright?', style='part', color='#fdc56c')
    if persistent.part01 is False:
        $ persistent.part01 = True
        $ archives += 1
    with dissolvee
    pause 3
    scene room with dissolvee
    $ show_quick_menu = True
    play sound 'se/bell.ogg'
    play music 'bgm/Sigh day.ogg' fadein 3
    if persistent.bgm02 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getmusic at get
            else:
                show getmusic_ko at get
        $ persistent.bgm02 = True
        $ archives += 1
    na 'A bell wakes me up.'
    na 'I open my eyes and pick up the cell phone to see the time.'
    na '8:45AM'
    if persistent.alarm is True:
        hide getmusic
        hide getmusic_ko
    play sound 'se/bell.ogg'
    na 'A bell rings again.'
    na 'It\'s quite annoying,{w=.3} but I get out of the bed and walk toward the door.'
    show p at pstand
    with d5
    if persistent.gayeon is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getchar at get
            else:
                show getchar_ko at get
        $ persistent.gayeon = True
        $ archives += 1
    p 'Who on earth is that,{w=.3} at this early morning…?'
    hide p
    with d5
    play sound 'se/open.ogg'
    na 'Scratching my head,{w=.3} I open the door.'
    if persistent.alarm is True:
        hide getchar
        hide getchar_ko
    show hy
    with d5
    h 'Surprise~!{w=.3} Ga-yeon!{w=.3} It\'s me!'
    if persistent.hyena is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getchar at get
            else:
                show getchar_ko at get
        $ persistent.hyena = True
        $ archives += 1
    na 'My sister,{w=.3} Hye-na,{w=.3} is standing here,{w=.3} greeting in the cheerful tone with her beautiful big smile.'
    na 'With a puzzled face,{w=.3} I say to her.'
    if persistent.alarm is True:
        hide getchar
        hide getchar_ko
    p 'Hye-na….{w=.3} What are you doing here?'
    h 'Well,{w=.3} while I was buying fresh bread,{w=.3} you just popped into my head!{w=.3} So I came to see you.'
    na 'As if she is emphasizing the last sentence, she leans forward towards to me.'
    na 'And she shows me a bag of breads.'
    na 'Breads in this early morning?'
    p 'Uh…,{w=.3} anyway come on in.'
    na 'I give way to her by moving aside so that she can enter the room.'
    play sound 'se/steb.ogg'
    na 'She grins at me, takes off her shoes,{w=.3} then strides across the room and sits by a small desk. '
    h 'Hey,{w=.3} I bought some bagels and sesame breads for you.{w=.3} Have some!'
    na 'She beckons me.'
    p 'Ah…,{w=.3} yes.'
    hide hy
    with d5
    play sound 'se/cup.ogg'
    na 'I take milk out of the fridge,{w=.3} and bring it to her with a cup.'
    na 'Sitting across from her,{w=.3} I pour milk into a cup and pass it to her.'
    na 'Taking a bite of the sesame bread,{w=.3} she stares at me.'
    na 'Then,{w=.3} she opens her mouth.'
    show hy
    with d5
    h 'Why don\'t you call these days?{w=.3} I heard even you haven\'t contacted mom and dad for a long time.'
    na 'After throwing several words,{w=.3} she\'s waiting for my answer.'
    na 'I put down my bread,{w=.3} and blink my eyes several times.{w=.3} Something is disturbing me in my mind.'
    p 'Well…,{w=.3} it\'s….'
    na 'I hesitate for a moment,{w=.3} because I don\'t know what to say.{w=.3} I just blink my eyes unconsciously.'
    h 'Do you have any idea how worried mom has been?{w=.3} She said you haven\'t called almost for three months.'
    p '….{w=.3}'
    na 'She puts down her bread and carefully asks to me.'
    hide hy
    show hs
    with d5
    h 'Was your phone cut off?'
    p '….{w=.3}'
    na 'Damn,{w=.3} I\'m so ashamed of myself.{w=.3} I can\'t even raise my head in front of my sister.'
    na 'I keep silence for a moment and just wiggle my fingers on the desk.'
    h 'Take it.'
    play sound 'se/envelope.ogg'
    na 'Then,{w=.3} she takes a white envelope out of her handbag and pokes it out to me.'
    p 'What\'s this?'
    na 'I take it and open to see what is in it.'
    na 'Then,{w=.3} I\'m so shocked by a ￦ 100,000 won check in the envelope.{w=.3} I give it back to her right away.'
    p 'What\'s this?{w=.3} Why you give it to me?'
    h 'I got paid.{w=.3} I just wanted to present something for you.'
    na 'Then,{w=.3} she gives me a smile,{w=.3} and continues to speak.'
    hide hs
    show hy
    with d5
    h 'Because you are not working now.{w=.3} I\'ll be happy if it\'s helpful to you.'
    na 'In contrast with her smiling face,{w=.3} I\'m very embarrassed.'
    na 'Needless to think,{w=.3} I say,{w=.3} scowling at her.'
    p 'No!{w=.3} I can\'t get this!'
    na 'Saying like this,{w=.3} I roughly shake my hands with the envelope.'
    na 'How come can I get money from my younger sister?{w=.3} I can\'t do!'
    hide hy
    show hs
    with d5
    h 'Look,{w=.3} you\'ve given too many things to me.{w=.3} And now,{w=.3} it\'s time for me to help you.{w=.3} Please.'
    na 'She replies with a little bit serious face.'
    play sound 'se/give.ogg'
    na 'And as if she is never going to take the envelope back,{w=.3} she covers it with her two hands and strongly gives it back to me.'
    p 'Hye-na…!{w=.5}'
    na 'I sign out.'
    hide hs
    show hw
    with d5
    h 'Take it.{w=.3} And please keep your chin up!{w=.3} It\'s not like you!'
    h 'Look,{w=.3} you are smart.{w=.3} You can do everything!{w=.3} Don\'t let anyone bring you down!'
    na 'With a strong voice,{w=.3} she tries to cheer me up.'
    na 'And soon,{w=.3} she smiles again and says to me.'
    hide hw
    show hy
    with d5
    h 'OK?{w=.3} Then,{w=.3} let\'s eat!'
    p '….{w=.3}'
    na 'I hesitate for a while.{w=.3} But soon,{w=.3} I decide to follow her.'
    p 'Um….{w=.3} Thank you.'
    na 'And with my answer,{w=.3} she nods her head and picks up the bread again.'
    na 'She\'s a good sister.{w=.3} My adorable and beautiful sister.'
    na 'Eating bread,{w=.3} we chat about the best bakery in the town,{w=.3} and that sort of things.'
    with f
    h 'So,{w=.3} Ga-yeon,{w=.3} don\'t forget to give mom a call!{w=.3} Okay?'
    na 'Saying like that,{w=.3} she tilts her head slightly to her right hand gesturing like a phone.'
    p 'Yeah.{w=.3} Take care,{w=.3} bye.'
    na 'Giving her a slight nod,{w=.3} I reply to her.'
    hide hy
    show hss
    with d5
    h 'Okay!{w=.3} Good bye~!'
    play sound 'se/rock.ogg'
    hide hss
    with d5
    play sound 'se/hsteb.ogg'
    pause 1
    na 'She opens the door with her right hand,{w=.3} waves goodbye to me,{w=.3} then leaves.'
    p 'Well…,{w=.3} you left so early.{w=.3} I hoped you had eaten all the breads with me,{w=.3} staying longer.'
    na 'When she goes out of sight,{w=.3} I say to myself,{w=.3} looking at the bag of bread.'
    na 'Then,{w=.3} I sit by the desk,{w=.3} and take the money out of the envelope which she left to me,{w=.3} then count it.'
    p 'My god….{w=.3} one million won….{w=.3} It\'s too much….'
    na 'I raise my head,{w=.3} and let out a sigh.'
    scene black with dissolvee
    $ show_quick_menu = False
    pause 1
    centered '{cps=15}Well,{w=.3} no matter how much she gave,{w=.3} you were going to take it anyway.{/cps}'
    centered '{cps=15}How could you refuse it?{/cps=15}'
label mono0:
    show screen key_screen
    scene dw
    show expression Text ('{color=#776e6e}{size=+64}M{/size}{/color}onologue', style='part', color='#b0aca5')
    if persistent.part02 is False:
        $ persistent.part02 = True
        $ archives += 1
    with dissolvee
    pause 3
    scene black with dissolvee
    pause 1
    centered '{cps=15}I\'m jobless.{/cps}'
    centered '{cps=15}I\'m twenty eight years old.{/cps}'
    centered '{cps=15}After graduation,{w=.3} some of my friends got a job,{w=.3} and some of them got married.{w=.3} And they have been living happily with their new family.{/cps}'
    centered '{cps=15}But I didn\'t finish the university,{/cps}'
    centered '{cps=15}and I\'m unemployed,{/cps}'
    centered '{cps=15}and I\'m still not married.{/cps}'
    centered '{cps=15}Well…,{w=.3} what\'s even worse is,{w=.3} I don\'t even have someone to go out with,{w=.3} like a boyfriend.{/cps}'
    centered '{cps=15}What a shame.{w=.3} Young,{w=.3} but indoors all day long.{/cps}'
    centered '{cps=15}How did it come to this?{/cps}'
    centered '{cps=15}At the end of long thinking,{w=.3} I just draw a sigh.{/cps}'
    stop music fadeout 3
label intern:
    show screen key_screen
    scene black with d
    show expression Text ('A year ago….', style='extext') at times with d3
    scene black with d3
    scene internr with d3
    $ show_quick_menu = True
    play music 'bgm/Mare tranquillitatis.ogg' fadein 3
    if persistent.bgm03 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getmusic at get
            else:
                show getmusic_ko at get
        $ persistent.bgm03 = True
        $ archives += 1
    na 'An interview room at a restaurant.{w=.3} Now I\'m standing in front of an interviewer.'
    na 'In spite of that many interview experiences,{w=.3} I\'m still so nervous.'
    if persistent.alarm is True:
        hide getmusic
        hide getmusic_ko
    pause 1
    show intern
    with d5
    intern 'Miss Choi Ga-Yeon?'
    if persistent.interviewer is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getchar at get
            else:
                show getchar_ko at get
        $ persistent.interviewer = True
        $ archives += 1
    na 'Sitting at the desk,{w=.3} she looks at me and my resume alternately,{w=.3} then,{w=.3} asks me.'
    na 'Unlike her appearance,{w=.3} her question is pretty sharp.'
    if persistent.alarm is True:
        hide getchar
        hide getchar_ko
    p 'Yes,{w=.3} ma\'am!'
    na 'Not to feel daunted,{w=.3} I answer in a loud voice.'
    intern 'What made you choose our company?'
    na 'Even while moving her left hand to pick up a paper cup and drinking water,{w=.3} she keep her eyes firmly fixed on me.'
    na 'I answer without hesitation.'
    p 'I had job counseling at the employment information center to get a job in the food service industry!'
    p 'And as they recommended your company,{w=.3} I actually visited once to look around!'
    p 'When I visited here,{w=.3} I was so touched by the staff\'s kind service.{w=.3} And it made me decide to apply for this company!'
    na 'After I finish my answer,{w=.3} she smiles contentedly and gives me another question,{w=.3} looking at the resume.'
    hide intern
    show intern1
    with d5
    intern 'Haha,{w=.3} did you?{w=.3} Well,{w=.3} you\'ve also worked as a coordinator at OO hospital,{w=.3} for two years?'
    p 'Yes!{w=.3} That\'s right!'
    intern 'And you have a class 1 qualification.{w=.3} Will you tell me why you quit there even though you\'ve worked for more than two years?'
    intern 'I\'m just wondering why you want to work in the food service industry,{w=.3} quitting such a nice job.'
    na 'In spite of her friendly gesture,{w=.3} I wince for a moment.'
    na 'If I tell her the truth,{w=.3} I will definitely fail to get a job here.'
    na 'I\'ve also had similar question at the previous interview,{w=.3} and whenever I was asked like that,{w=.3} I told a lie.'
    na 'And this time,{w=.3} I\'m going to tell a lie once again.'
    p 'After I graduated from high school,{w=.3} I worked at a family restaurant for a while until entering the University!'
    p 'And seeing a manager there,{w=.3} I dreamed of someday becoming a professional manager,{w=.3} just like her,{w=.3} in the food service industry!'
    p 'But at that time,{w=.3} I had to go to University.{w=.3} Then,{w=.3} while at school,{w=.3} my family budget became pretty hard,{w=.3} and I started to work at hospital!'
    p 'Working at the hospital,{w=.3} I was sick of doctors who didn\'t sincerely care for their patients.{w=.3} So I made up my mind to quit there,{w=.3} and today,{w=.3} I came here to do what I\'ve been looking forward!'
    na 'I finished my answer in a confident voice.{w=.3} She nods her head,{w=.3} and continues to throw questions.'
    intern 'Good.{w=.3} The job here will be much harder than your previous job.{w=.3} Are you ready for that?'
    na 'I immediately answer to her.'
    p 'Yes!{w=.3} I can do it!'
    intern 'Here\'s the last question.{w=.3} What do you think customer is?{w=.5}'
    na 'Geez.{w=.3} I didn\'t expect this.'
    na 'Okay,{w=.3} calm down.{w=.3} Arrange words first.'
    na 'In a moment,{w=.3} I\'m racking my brain to find out a right word.'
    na 'And I organize the words in my mind.'
    p 'I think,{w=.3} customer is like an old friend at home.'
    hide intern1
    show intern2
    with d5
    intern '{cps=10}An old friend at home…?{/cps}'
    na 'Making a disappointed face,{w=.3} the interviewer drags her chair forward and leans towards the table.'
    na 'Oh…,{w=.3} did I say something wrong?'
    na 'Okay,{w=.3} just push it.'
    p 'I have some friends back home I can\'t often get in touch because of my busy life.'
    p 'And they sometimes come over to meet me from a distance.'
    p 'Then,{w=.3} I welcome and dish up the dinner for my friend who comes over my place just to meet me,{w=.3} and then,{w=.3} my friend goes back to his or her place again.'
    p 'We don\'t know when we could meet again,{w=.3} but we promise in our mind to meet someday in the future again,{w=.3} with this good memory.'
    p 'I think,{w=.3} this is what customer is.{w=.5}'
    na 'God,{w=.3} what am I talking about?'
    na 'As soon as I finish my answer,{w=.3} I think the interview today is completely screwed up,{w=.3} and I reproach my tongue in my mind.'
    play sound 'se/file.ogg'
    hide intern2
    with d5
    na 'She puts my resume down,{w=.3} and clasps her hands together on the desk.'
    na 'Only moving a forefinger of her right hand up and down,{w=.3} she looks at her hands.'
    na 'I can\'t read her face.'
    show intern
    with d5
    intern 'Miss Choi Ga-Yeon.'
    p 'Yes,{w=.3} Yes!'
    na 'I\'m nervous about her calm voice.'
    na 'After a while,{w=.3} she stops moving her finger,{w=.3} raises her head,{w=.3} and says.'
    intern 'Customer can\'t be friend.{w=.3} But anyway,{w=.3} your answer was exactly to my taste.'
    hide intern
    show intern1
    with d5
    intern 'If possible,{w=.3} I want to bring you to the restaurant and train right away.'
    p 'Ah…!'
    na 'Oh my god!'
    na 'The interviewer says with a smile in her face,{w=.3} to me who is leaping for joy in my mind.'
    intern 'I\'d like to give you 10 out of 10.{w=.3} But as there are many experienced applicants,{w=.3} I can\'t be 100\% sure.'
    p 'Thank you!{w=.3} I\'ll do my best!'
    hide intern1
    stop music fadeout 3
label mono1:
    show screen key_screen
    scene black with d3
    $ show_quick_menu = False
    play music 'bgm/CCCanon.ogg' fadein 3
    if persistent.bgm04 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getmusic at get
            else:
                show getmusic_ko at get
        $ persistent.bgm04 = True
        $ archives += 1
    pause 1
    centered '{cps=15}It was my last interview to get a job.{/cps}'
    centered '{cps=15}But there\'s no call.{/cps}'
    if persistent.alarm is True:
        hide getmusic
        hide getmusic_ko
    centered '{cps=15}It always goes like this.{/cps}'
    centered '{cps=15}The interviewer always says there will be the good news.{/cps}'
    centered '{cps=15}And we will work together soon.{/cps}'
    centered '{cps=15}But every time,{w=.3} it ends up like this.{/cps}'
    centered '{cps=15}I\'m sick of everything.{/cps}'
    centered '{cps=15}I cried like a child,{w=.3} hitting my pillow in my small room.{/cps}'
    centered '{cps=15}I drank,{w=.3} and threw up holding on the toilet.{/cps}'
    centered '{cps=15}I was just lying in my bed,{w=.3} doing nothing but starling up at the ceiling.{/cps}'
    centered '{cps=15}I\'m sick of everything.{/cps}'
    centered '{cps=15}I am a loser.{/cps}'
    centered '{cps=10}I\'m a{/cps} {cps=5}discouraged worker.{/cps}{w=1}'
    if persistent.con01 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getcon at get
            else:
                show getcon_ko at get
        $persistent.con01 = True
        $ archives += 1
    pause 3
    if persistent.alarm is True:
        hide getcon
        hide getcon_ko
label gone:
    show screen key_screen
    scene room with d3
    $ show_quick_menu = True
    na 'Standing in front of the desk for a while,{w=.3} I get depressed.'
    na 'Looking down at Hye-na\'s breads for a while,{w=.3} I have tears in my eyes.'
    play sound 'se/water.ogg'
    na 'Sitting by the desk,{w=.3} I pour milk into a cup and take a sip of it.'
    na 'I bite off a small chunk of the sesame bread.'
    na 'Tears pour down {cps=5}my face.{/cps}'
label caffe:
    show screen key_screen
    scene dw
    show expression Text ('{color=#c938ff}{size=+64}D{/size}{/color}o you remember first love?', style='part', color='#e1aaf1')
    if persistent.part03 is False:
        $ persistent.part03 = True
        $ archives += 1
    with dissolvee
    pause 3
    scene caffe with dissolvee
    pause 1
    show yu
    with d5
    y 'Feel better?'
    p '….{w=.5}'
    y 'Hey,{w=.3} you are not a teenage girl.'
    na 'A man sitting across a table raises his hands and says teasingly.'
    p 'I know that.'
    na 'I mutter with a wry face.'
    na 'His name is Kim Yun-Woo.'
    if persistent.yunwoo is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getchar at get
            else:
                show getchar_ko at get
        $ persistent.yunwoo = True
        $ archives += 1
    na 'He and I are the same age,{w=.3} and we\'ve known each other since we were the high school students.'
    na 'In our school days,{w=.3} he used to be a strange boy,{w=.3} showing almost no change in his expression,{w=.3} like a poker face.{w=.3} But as time goes by,{w=.3} he hass changed little by little.'
    if persistent.alarm is True:
        hide getchar
        hide getchar_ko
    y 'No one would cry so pitifully like you,{w=.3} eating bread in a room.'
    na 'His face looks as if he\'s talking to a kid.'
    p 'You know what,{w=.3} you,{w=.3} who trespassed on the other\'s private space,{w=.3} are the bad one….'
    na 'Slurring my words,{w=.3} I avoid his eyes.'
    na 'It is a very strange day today.'
    na 'Hye-na suddenly came to me so early in the morning,{w=.3} and just after a while,{w=.3} Yun-woo appeared.'
    na 'Well….{w=.3} Anyway,{w=.3} what a sight.'
    na 'Why did he pop up abruptly,{w=.3} even at that moment?'
    y 'You know,{w=.3} I was frightened.{w=.3} The door was open,{w=.3} and a crying girl in a room was chewing her bread.'
    p 'So why did you come over here without a single word?{w=.3} It\'s your fault.'
    na 'I keep complaining.'
    y 'Your phone has been cut off because of the unpaid bills.{w=.3} So,{w=.3} what was I supposed to do but visit?'
    na 'You idiot.{w=.3} there is WiFi.'
    na 'Snapping at the chance,{w=.3} I bridle and have a dig at him.'
    p 'There\'s ○○.{w=.3} I can use it wherever WiFi is available.'
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    hide yu
    show yus with shock
    with d5
    y 'What?{w=.3} Are you kidding?'
    na 'Huh.{w=.3} how many faces does he have?'
    hide yus
    show yua
    with d5
    y 'Then,{w=.3} why haven\'t you contacted me so long?'
    na 'Supporting himself against his left elbow on the arm of the chair,{w=.3} he bends his body to the left and asks me.'
    p 'How could I contact you in such an embarrassing situation?'
    na 'This time,{w=.3} I answer to him,{w=.3} slightly whining.{w=.3} And he says with a smile.'
    hide yua
    show yu
    with d5
    y 'Dude,{w=0.3} you can\'t do like that to me.{w=.3} I thought you\'ve got nothing embarrassing to me.'
    p 'Well,{w=0.3} you are right.'
    na 'Replying briefly,{w=.3} I let out a sigh.'
    hide yu
    with d5
    na 'He\'s pretty a weird man.'
    na 'After graduating from high school,{w=.3} he joined the military,{w=.3} and after finished the military service,{w=.3} he has lived in a semi-basement room near Hongik University area.'
    na 'And only because he is into music,{w=.3} he hasn\'t got a job and just has played in a band so far.'
    na 'He looks like living in his own isolated world,{w=.3} far away from this world.'
    na 'He will never compromise with the principle of capitalism,{w=.3} but lives in his own way as he has done.'
    na 'When I was young,{w=.3} I thought that was cool.'
    na 'He seemed to be thoughtful and also was like an older brother.'
    na 'However,{w=.3} as soon as I went out to society after graduation,{w=.3} all these things seemed to be different.'
    na 'Yun-woo might be desperate,{w=.3} more than any others.'
    na 'Though he never lets it show to others,{w=.3} I vividly remember what he told me for the first time after he was discharged from the military service and his intense eyes at that moment.'
    show yu
    with d5
    y 'Hey,{w=0.3} come on.'
    p 'Eh,{w=0.3} why?'
    na 'Thinking about these stuff,{w=0.3} I answer to him.'
    y 'Your coffee is getting cold.{w=0.3} You know what,{w=0.3} cold coffee is like a lifeless life.'
    na 'I don\'t understand him as he sometimes says something like this,{w=0.3} weird thing.'
    p 'Uh-huh.'
    hide yu
    with d5
    na 'Anyway,{w=0.3} because I have nothing to say,{w=0.3} I just mumble the answer.'
    na 'Then,{w=0.3} I pick up a cup on the table and take a gulp of coffee.'
    na 'As soon as I put it down,{w=0.3} he also picks up a small glass and takes a sip.'
    na 'He likes espresso.{w=0.3} But I don\'t understand why he likes that sort of thing.'
    show yu
    with d5
    y 'Here,{w=0.3} have some bread.'
    na 'He cut off a bit of honey bread with his fork,{w=0.3} and holds it out to me.'
label shinchon:
    show screen key_screen
    scene dw
    show expression Text ('{color=#c938ff}{size=+64}S{/size}{/color}hin-Chon Street', style='part', color='#e1aaf1')
    if persistent.part04 is False:
        $ persistent.part04 = True
        $ archives += 1
    with dissolvee
    pause 3
    scene sin
    with dissolvee
    na 'Yunwoo takes me out to the street,{w=0.3} saying that he\'s going to refresh me.'
    na 'He walks at the right,{w=0.3} and I\'m at the left,{w=0.3} a little bit away from him.'
    na 'Though it\'s just in the middle of the day,{w=0.3} it\'s pretty crowded today.'
    show yus
    with d5
    y 'Is there something special today?{w=0.3} Why is it so crowded?'
    na 'Yunwoo doesn\'t look well.'
    p 'You don\'t like crowded area,{w=0.3} do you.'
    y 'Wow,{w=0.3} I don\'t feel well.'
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    na 'He answers to me.{w=0.3} He looks he\'s just about to throw up in a minute.'
    p 'My god!{w=0.3} Are you going to throw up here?'
    na 'I strongly shake his arms,{w=0.3} with surprise.'
    hide yus
    show yu
    with d5
    na 'Then he looks at me,{w=0.3} giggling.'
    y 'Haha,{w=0.3} it\'s just kidding.'
    na 'I make a pretty serious face,{w=0.3} and turn my head to the other side.'
    p 'It doesn\'t please me at all.'
    y 'There.{w=0.5}'
    na 'Regardless of my answer,{w=0.3} he speaks something and I instinctively turn my head to the way he shouts to.'
    p 'Huh?'
    hide yu
    with d5
    na 'He\'s pointing out somewhere with his finger.'
    na 'I try to find it,{w=.3} but because of his body,{w=.3} I can’t see.'
    na 'I grab his left arm and pull him towards me to secure a clear view.'
    na 'Well,{w=.3} it\'s better.{w=.3} Now I try to stick out my head more to see what his right hand is pointing out.'
    pause 2
    na 'That\'s a cellphone shop.'
    p 'What is that?{w=0.3}'
    p 'Um….{w=0.5}'
    show tdw
    with d
    pause 3
    na 'I\'m trying to ask him what he is going to do,{w=.3} lifting up my head.{w=.3} But soon,{w=.3} I stop.'
    na 'His eyes looking down at me and my eyes looking up at him are too close.'
    na 'Silence for a while.'
    y 'At the moment,{w=.3} time between us stops,{w=.3} while time of the world runs as it was before.'
    p '…!'
    hide tdw
    with d
    if persistent.unlock_1 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getgall at get
            else:
                show getgall_ko at get
        $ persistent.unlock_1 = True
        $ archives += 1
    na 'After a moment,{w=.3} I blink my eyes and take a step backward.'
    p 'Don\'t be stupid,{w=.3} so what?'
    if persistent.alarm is True:
        hide getgall
        hide getgall_ko
    na 'To get out of this awkward situation,{w=.3} I tell him like that.'
    na 'Then he gazes at me,{w=.3} and the shop,{w=.3} and tells.'
    show yu
    with d5
    y 'You said Hye-na gave you some money for the unpaid phone bill.{w=.3} Let\'s go and pay it now.'
    p 'No,{w=.3} later.{w=.3} I will go alone.'
    na 'Turning my head,{w=.3} I tell him in a feeble voice.'
    na 'Probably a clerk will say,{w=.3} like I\'ve got lots of bills in arrears,{w=.3} or something like that.'
    na 'And I don\'t want to show myself in such a shameful situation to Yunwoo.'
    y 'Come on.'
    na 'Then he cuts in and grabs my wrist,{w=0.3} then takes me to the shop.'
    p 'Hey!{w=0.3} I said no!'
    na 'I holler at him,{w=0.3} but he completely ignores.'
    na 'Though I\'m intensely trying to brace myself against him,{w=0.3} it\'s impossible to cope with him.'
    na 'I\'m almost dragged by him until getting to the shop.'
    stop music fadeout 3
label phone:
    show screen key_screen
    scene phone with f
    play music "bgm/Let's game.ogg" fadein 3
    show ex1 at right
    with d5
    if persistent.bgm05 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getmusic at get
            else:
                show getmusic_ko at get
        $ persistent.bgm05 = True
        $ archives += 1
    ex 'Come on in!{w=0.3} May I help you?{w=0.3} Want some new arrivals?{w=0.3} We\'ve got also many phones for a couple as well!'
    if persistent.alarm is True:
        hide getmusic
        hide getmusic_ko
    if persistent.angel is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getchar at get
            else:
                show getchar_ko at get
        $ persistent.angel = True
        $ archives += 1
    na 'A perky clerk welcomes us,{w=.3} coming out to the entrance of the shop.'
    hide ex1
    show exg at right
    show yu at left
    with d5
    y 'Well,{w=0.3} we will pay the bill.'
    if persistent.alarm is True:
        hide getchar
        hide getchar_ko
    hide yu
    show yug at left
    hide exg
    show ex1 at right
    with d5
    play sound 'se/clap1.ogg'
    ex 'Good~!{w=0.3} Come over here,{w=0.3} please.'
    na 'Then a woman clerk claps her hands and leads him to a table.'
    hide yug
    hide ex1
    with d5
    na 'Yunwoo talks with her,{w=0.3} sitting at a chair.{w=0.3} And I sit by the table behind them and gaze at him.'
    na 'He\'s dealing with my unpaid bills instead of me.'
    show ex1 at right
    with d5
    ex 'Okay,{w=0.3} done!{w=0.3} Anything else you need?'
    na 'After paying the bills,{w=0.3} she asks Yunwoo,{w=0.3} and he answers,{w=0.3} shaking his head.'
    hide ex1
    show exg at right
    show yu at left
    with d5
    y 'No,{w=0.3} thank you.'
    hide yu
    hide exg
    with d5
    na 'He comes to me,{w=0.3} and gestures to get out of there,{w=0.3} opening the door for me.'
    na 'So I get up and follow him.{w=0.3} At that time,{w=0.3} a clerk says something.'
    show ex1
    with d5
    ex 'Oh,{w=0.3} hey,{w=0.3} I think I saw you on the internet?'
    p 'Hum…?'
    na 'When I\'m about to turn my head to her,{w=0.3} Yunwoo puts his hand around my shoulder all of a sudden and pushes me out.'
    hide ex1
    show yu
    with d5
    y 'Let\'s get out of here,{w=0.3} Ga-yeon.'
    p 'Wa…,{w=0.3} wait!{w=0.3} What are you doing?'
    stop music fadeout 3
    scene sin with f
    play music 'bgm/Sigh day.ogg' fadein 3
    na 'He leads me out of the shop.'
    na 'And then,{w=0.3} putting his hand on my shoulder,{w=0.3} we continue to walk through the crowd.'
    p 'Hey,{w=0.3} Yunwoo!'
    na 'Led by him for a while,{w=0.3} I say to him.'
    na 'But he just ignores me and just keeps walking forward.'
    na 'He doesn\'t look very well.{w=0.5}'
label food:
    show screen key_screen
    scene dw
    show expression Text ('{color=#c938ff}{size=+64}S{/size}{/color}ad lunch', style='part', color='#e1aaf1')
    if persistent.part05 is False:
        $ persistent.part05 = True
        $ archives += 1
    with dissolvee
    pause 3
    scene food with dissolvee
    show yu
    with d5
    y 'You know that,{w=.3} pudding rather than praise?{w=0.3} Let\'s go grab a bite.{w=0.3} I haven\'t had a bite all day.'
    na 'After we enter a restaurant,{w=0.3} he looks slightly better.'
    na 'I ask him with curiosity.'
    p 'Why did you do like that?{w=0.3} She said I seemed familiar to her.'
    na 'Then he raises his left hand and massages the back of his neck.{w=0.3} And with annoyed look on his face,{w=0.3} he says.'
    y 'It\'s obvious she was trying to sell something like phone accessories.'
    na 'Well…,{w=0.3} I don\'t think so.'
    na 'Thinking for a while,{w=0.3} I just stop thinking,{w=0.3} and change the talk to another subject.'
    p 'By the way,{w=0.3} aren\'t you going to get married?'
    p 'You know,{w=0.3} we\'re already twenty eight.{w=0.3} You are going to die a bachelor.'
    na 'With a wry smile,{w=0.3} he says.'
    y 'So will you marry me?{w=0.3} I don\'t want to die alone.'
    na 'It makes me embarrassed.{w=0.3} After a bit of silence,{w=0.3} I say to him.'
    p 'If you want to feed me,{w=0.3} you\'d better make a lot of money.'
    y 'All right!{w=0.3} I\'ll pull my socks up.'
    na 'He says like a joke.'
    na 'Then,{w=0.3} I respond to his joke,{w=0.3} speaking bluntly.'
    p 'Of course,{w=0.3} you should.{w=0.3} You can\'t even imagine who I am.{w=0.3} I totally deserve it.'
    y 'Wow,{w=0.3} how lucky I am!'
    hide yu
    with d5
    na 'After his words,{w=0.3} I get lost in thought for a moment.'
    na 'Yeah,{w=0.3} you can\'t even imagine who I am.'
    na 'I don\'t deserve to marry a good guy,{w=0.3} like you.'
    na 'I\'m…,{w=0.3} such a slut.'
    na 'Ha,{w=0.3} I get so depressed.'
    na 'Change the subject.'
    p 'So,{w=0.3} how\'s your band?{w=0.3} Everything is fine?'
    na 'I ask,{w=0.3} staring at him.'
    show yu
    with d5
    y 'Yes,{w=0.3} now we\'ve got four permanent stages on weekends.'
    y 'Besides,{w=0.3} on weekdays we have six stages to play a day from 7PM to 1AM.'
    p 'Wow~,{w=0.3} you are going to be rich soon!'
    na 'I don\'t know why,{w=0.3} but I say to him,{w=0.3} a little bit excited by what he said.'
    na 'Then,{w=0.3} he adds,{w=0.3} with a slightly boastful face.'
    y 'Well,{w=0.3} actually we\'re also invited to a rock festival,{w=0.3} which is going to be held in two months.'
    p 'My god!{w=0.3} Are you serious?{w=0.3} Good for you!'
    na 'I touch his shoulder with my right hand,{w=0.3} even before I knew it.'
    na 'Then he draws up his chair forward,{w=0.3} and continues.'
    y 'So I want you to do something for me.{w=0.3} I remember you used to paint a picture with a computer program when you were in high school,{w=0.3} didn\'t you?'
    p 'Uh?{w=0.3} You say ○○?'
    na 'I recall the name and say it to him.'
    na 'And with my answer,{w=0.3} he claps his hands cheerfully and comes to the point.'
    play sound 'se/clap.ogg'
    y 'Yes,{w=0.3} you\'re right!{w=0.3} So this weekend,{w=0.3} we have our sole concert,{w=0.3} and we need a poster and pamphlet for it.'
    y 'If you don\'t mind,{w=0.3} will you do it for me?{w=0.3} Of course I will pay you.'
    na 'After he finishes,{w=0.3} I nod my head and agree to him.'
    p 'It is no problem.'
    na 'Then,{w=0.3} he turns his body and scrabbles around in his bag hung on the chair.'
    y 'So,{w=0.3} what we need is….'
    na 'He continues to talk,{w=0.3} taking out photos of his band members to insert in the poster.'
    na 'After a while,{w=0.3} the dishes are served and we continue talk about it,{w=0.3} having our meal.'
    stop music fadeout 3
label mono2:
    show screen key_screen
    scene dw
    show expression Text ('{color=#776e6e}{size=+64}M{/size}{/color}onologue', style='part', color='#b0aca5')
    if persistent.part06 is False:
        $ persistent.part06 = True
        $ archives += 1
    with dissolvee
    pause 3
    play music 'bgm/Peace.ogg' fadein 3
    scene black with dissolvee
    if persistent.bgm06 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getmusic at get
            else:
                show getmusic_ko at get
        $ persistent.bgm06 = True
        $ archives += 1
    $ show_quick_menu = False
    centered '{cps=15}I and Yunwoo.{/cps}'
    if persistent.alarm is True:
        hide getmusic
        hide getmusic_ko
    centered '{cps=15}In high school,{w=0.3} Yunwoo was a pretty mysterious boy.{/cps}'
    centered '{cps=15}He used to be such an isolated guy hard to get close to,{w=0.3} with an invisible barrier which never allowed others to enter.{/cps}'
    centered '{cps=15}He was taciturn and quiet.{w=0.3} Sometimes,{w=0.3} in the middle of class,{w=0.3} he just went out to the schoolyard to write music.{/cps}'
    centered '{cps=15}I was even surprised he was able to graduate from high school despite that many absences.{/cps}'
    centered '{cps=15}However,{w=.3} what made me and this sort of guy became friends was his younger sister.{/cps}'
    centered '{cps=15}He has a sister two years younger than him.{/cps}'
    centered '{cps=15}One night,{w=.3} I helped a junior student bullied by several girls at her age in a dark alleyway.{/cps}'
    centered '{cps=15}I took her to her home,{w=.3} trying to comfort her,{w=.3} and surprisingly,{w=.3} there was Yunwoo at home.{/cps}'
    centered '{cps=15}Yes,{w=.3} she was Yunwoo\'s younger sister.{/cps}'
    centered '{cps=15}At home,{w=.3} there were only Yunwoo and his sister living together.{w=.3} And at that night,{w=.3} he was in anxiety,{w=.3} worrying about his sister.{/cps}'
    centered '{cps=15}Yunwoo said {b}"Thank you"{/b} to me,{w=.3} with his warmest smile.{/cps}'
    centered '{cps=15}And he took me to my home,{w=.3} saying it was too late for a girl to go home alone.{/cps}'
    centered '{cps=15}As the way to my home was quite far from his house,{w=.3} we talked a lot about many things.{/cps}'
    centered '{cps=15}That night,{w=.3} the moon was unusually bright,{w=.3} and the stars were beautifully twinkling more than any other nights.{/cps}'
    centered '{cps=15}Our story has begun since then.{/cps}'
    pause 1
label food1:
    show screen key_screen
    scene dw
    show expression Text ('{color=#c938ff}{size=+64}C{/size}{/color}alm afternoon', style='part', color='#e1aaf1')
    if persistent.part07 is False:
        $ persistent.part07 = True
        $ archives += 1
    with dissolvee
    pause 3
    scene food with dissolvee
    $ show_quick_menu = True
    show yu
    with d5
    y 'What are you thinking about?'
    p 'Oh,{w=0.3} no.{w=0.3} Nothing.'
    na 'He interrupts my thinking and I answer to him,{w=0.3} starting to eat again.'
    y 'Hey,{w=0.3} I\'ve got something to show you.'
    na 'He says to me,{w=0.3} as if he has been waiting for this moment.'
    p 'Huh?{w=0.3} What\'s that?'
    na 'I ask him what it is,{w=0.3} and he moves his hand to the right pocket of his pants.'
    na 'Then,{w=0.3} with a grin,{w=0.3} he takes his cell phone out of his pocket.'
    na 'His fingers seem to be busy pressing somethings on the phone in his hands,{w=0.3} and soon,{w=0.3} he holds it out to me.'
    y 'Look,{w=0.3} isn\'t it so cute?'
    na 'I take his phone and look at the display.'
    na 'On the phone,{w=0.3} there is an adorable sleeping baby.'
    p 'Oh my god,{w=0.3} oh my god….{w=0.3} Who\'s this?{w=0.3} So adorable!'
    na 'Holding his phone in my hands,{w=0.3} I ask him with wonder.'
    y 'Eunyoung\'s baby.'
    na 'Without much thinking upon what he said,{w=0.3} I gaze at his face once,{w=0.3} then,{w=0.3} at the phone,{w=0.3} and finally,{w=0.3} I figure out what happened.'
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    p '{size=+10}Oh my goooood!{w=0.3} This is Eunyoung\'s baby?{/size}'
    na 'I\'m very surprised.{w=0.3} She\'s already has a child?'
    na 'It\'s been only a year -{w=0.3} no,{w=0.3} less than a year since she got married.{w=0.3} But how come!'
    y 'You know what,{w=0.3} when she married,{w=0.3} she was three months pregnant.'
    na 'I\'m extremely surprised with that news,{w=0.3} Looking at me,{w=.3} Yunwoo continuess with a giggle.'
    p 'Uh….{w=0.3} I never knew that.'
    na 'Eunyoung is Yunwoo\'s younger sister.'
    na 'She married at this time last year.{w=0.3} Well,{w=0.3} I didn\'t ever hear about this when I was at her wedding.'
    na 'Wow…,{w=0.3} she gave birth to this lovely baby.'
    y 'Why the long face?'
    na 'I just shake my head several times,{w=0.3} and then tell him.'
    p 'No,{w=0.3} nothing.{w=0.3} Just…,{w=0.3} it\'s just unbelievable.'
    p 'You know,{w=0.3} it seems like just yesterday that she wore a school uniform.'
    y 'Do you?{w=0.3} So do I.'
    y 'That little girl became a woman,{w=0.3} got married,{w=0.3} and gave birth to a baby.{w=0.3} It\'s just unbelievable.'
    hide yu
    with d5
    na 'Saying like this,{w=0.3} he raises his arms and locks his fingers behind his head.'
    na 'Again,{w=0.3} I gaze at a baby on the phone,{w=0.3} and touch it with a finger.'
    na 'Looking at a number of pictures of the baby,{w=0.3} something hollow grows bigger and bigger inside me.'
    na 'I know in this situation,{w=0.3} I\'m supposed to congratulate him.{w=0.3} However,{w=0.3} I can\'t help but look back on my reality.'
    na 'If I had married,{w=0.3} I would also have a baby now like her.'
    stop music fadeout 3
    na 'If I had married him at that time….'
    na 'Suddenly,{w=0.3} tears well up in my eyes.'
    show yus
    with px
    y 'Jeez,{w=0.3} what\'s wrong with you,{w=0.3} Ga-yeon!'
label says:
    show screen key_screen
    scene cheon with px5
    play music 'bgm/Unknown mist.ogg' fadein 3
    if persistent.bgm07 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getmusic at get
            else:
                show getmusic_ko at get
        $ persistent.bgm07 = True
        $ archives += 1
    play sound 'se/waterfall.ogg'
    pause 1
    na 'He looks very embarrassed by me,{w=0.3} and immediately takes me out of the restaurant.'
    if persistent.alarm is True:
        hide getmusic
        hide getmusic_ko
    na 'Like he says,{w=.3} it would be better if taking a walk for a while.{w=0.3} And we walk along the street quite a while, and reach the Cheonggyecheon Stream.'
    na 'While sitting by the stream,{w=0.3} I become pretty calm.'
    na 'Both of us are just gazing at flowing stream.'
    p 'I\'m sorry….{w=.5}'
    na 'I\'m hesitant for a moment with shame,{w=0.3} then carefully start to talk to him.'
    show yu
    with d5
    y 'No.{w=.3} However,{w=.3} it seems you have depression.'
    p 'Well…,{w=.3} I think so,{w=.3} too.'
    y 'Since when?{w=.5}'
    play sound 'se/canopen.ogg'
    hide yu
    with d5
    na 'He asks me,{w=.5} handing over a canned coffee.'
    na 'I receive it and take a sip of coffee.{w=.5} Then,{w=.5} I had it in both my hands and put on the top of my knees.{w=.5} Staring at flowing stream,{w=.5} I answer to him.'
    p 'It\'s been quite a long time - probably Since I stopped looking around for a job.'
    show yus
    with d5
    y 'It\'s been almost a year!'
    na 'He roars in a rough voice.'
    p '{size=-2}Yes,{w=.3} you\'re right….{/size}{w=.3}'
    na 'Looking down at a can in my hands,{w=.3} I mumble in a hollow voice.'
    y 'Why didn\'t you go to a doctor!'
    na 'His voice goes up.{w=.3} He gets angry with me.'
    play sound 'se/can.ogg'
    na 'My hands holding a can become slightly tightened.'
    na 'I feel something surging up in my mind.'
    na 'Calm.{w=.3} Calm down.'
    na 'No,{w=.3} don\'t.{w=.3} I shouldn’t behave shamefully in front of him,{w=.3} anymore.{w=.3}'
    na 'Then,{w=.3} I loosen my hands tightly holding a can.'
    na 'And I raise my head,{w=.3} turn to him,{w=.3} and say.'
    p 'I\'m alright,{w=.3} anyway.{w=.3} You\'ve come to save me.{w=1}'
    y '….{w=1}'
    hide yus
    show yu
    with d5
    y '….{w=1}'
    stop music fadeout 3
    scene dw
    show expression Text ('{color=#c938ff}{size=+64}Q{/size}{/color}uestionable {color=#ff9000}{size=+64}F{/size}{/color}{color=#fdc56c}eelings{/color}', style='part', color='#e1aaf1')
    if persistent.part08 is False:
        $ persistent.part08 = True
        $ archives += 1
    with dissolvee
    pause 3
    scene cheon with dissolvee
    play music 'bgm/Lush garden.ogg' fadein 3
    if persistent.bgm08 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getmusic at get
            else:
                show getmusic_ko at get
        $ persistent.bgm08 = True
        $ archives += 1
    play sound 'se/waves.ogg'
    na 'Even before we know,{w=.3} we are completely absorbed in chatting,{w=.3} putting our feet in flowing stream.'
    p 'It\'s been a really long time to come here with you.'
    if persistent.alarm is True:
        hide getmusic
        hide getmusic_ko
    show yu
    with d5
    y 'Yes,{w=.3} the last time we visited here was when you were a university student.{w=.3} It was almost six years ago.'
    p 'Six years?{w=0.3} My god,{w=0.3} I\'m going to be a grandma in a blink.'
    na 'Leaning back with my hands on the ground and disturbing the flow of the stream by moving my knees back and forth,{w=0.3} I say to him.'
    y 'That\'s just the way time goes.{w=.3} Time is the next scariest thing to human.'
    na 'Now,{w=.3} he clasps his hands behind his head and lies down on the ground.'
    na 'Looking down at him on the ground,{w=.3} I just agree to him.'
    p 'Yes,{w=.3} I think you are right.'
    y 'Oh,{w=.3} by the way,{w=.3} you know what?'
    p 'Huh?{w=.5}'
    na 'He gets up blinking his eyes,{w=.3} as if something comes into his mind.'
    hide yu
    show yua
    with d5
    y 'I think I saw Hye-na in the Hongik Uni. area several days ago,{w=.3} at dawn.'
    stop music fadeout 3
    p 'You saw Hye-na at dawn?'
    na 'I ponder about what he said.'
    na 'I heard Hye-na works near the Daehangno area.'
    na 'But there\'s no reason she stays there that late?'
    play music 'bgm/Jormungandr.ogg' fadein 3
    if persistent.bgm09 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getmusic at get
            else:
                show getmusic_ko at get
        $ persistent.bgm09 = True
        $ archives += 1
    p 'Aren\'t you mistaking another girl?'
    na 'I ask him again,{w=.3} tilting my head with a puzzled look.'
    if persistent.alarm is True:
        hide getmusic
        hide getmusic_ko
    y 'Well,{w=.3} also I was not sure first,{w=.3} but it\'s right,{w=.3} it was Hye-na.'
    y 'I tried to say hello to her,{w=.3} but as she was with a man in a suit,{w=.3} I just passed by her.{w=.3} I think she didn\'t see me.'
    p 'A man in a suit…?{w=.3} She\'s going out with some guy?'
    na 'I say lightly to him.'
    na 'But as he continues to explain about Hye-na that night,{w=.3} I feel something is going wrong.'
    y 'But she looked awkward….{w=.3} like a…,{w=.3} hmm….{w=.3} what should I….'
    y 'Actually a guy she walked together arm in arm looked slightly old.'
    p 'What?{w=1}'
    p 'Are you sure of that?'
    y 'Yes,{w=.3} I felt something strange.'
    p 'What did she wear?'
    na 'Saying like that,{w=.3} I turn to him.'
    y 'It was like- she was like,{w=.3} she went clubbing that night.'
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    p '{size=+10}No way!{w=.3} It\'s Hye-na!{w=0.3} She\'s not that sort of girl!{/size}'
    na 'I can\'t believe it!{w=.3} Don\'t be ridiculous!'
    na 'I just holler at him and turn my head away.'
    na 'It\'s bullshit!'
    na 'What does he take my sister for?'
    y 'Hey,{w=0.3} don\'t be upset.{w=0.3} Also I think it can\'t be.'
    y 'But she\'s your sister.{w=0.3} That\'s why I\'m telling you this.'
    na 'She was in such a dress,{w=0.3} with an old guy?{w=0.3} Why?'
    na 'No!{w=0.3} It\'s just bullshit.{w=0.3} Hye-na is not that sort of girl.'
    na 'This can\'t happen.{w=0.3} It mustn\'t happen.'
    na 'I think over and over,{w=0.3} blinking my eyes unconsciously.'
    p '{size=+10}I gotta to see her!{/size}'
    na 'I turn my head and say to Yunwoo,{w=0.3} staring at him.'
    p 'First of all,{w=0.3} I will find out where she works now,{w=0.3} and go there.'
    na 'While talking to him,{w=0.3} I continuously blink my eyes.'
    p 'Yunwoo,{w=0.3} you know many people around that area.{w=0.3} Please find people who saw Hye-na.'
    y 'But they don\'t know who she is.'
    p 'Hye-na is popular among guys,{w=0.3} and also she likes posting her photos on her blog.{w=0.3} So it will be easy to find her,{w=0.3} by using it.'
    y 'I don\'t think it would be that easy as you think,{w=0.3} but anyway,{w=0.3} I\'ll try.{w=0.3} And what are you going to do?'
    p 'I will call Hye-na and go to where she works.'
    p 'Then,{w=0.3} after having a conversation with her,{w=0.3} I will find out what she\'s doing,{w=0.3} whom she meets.'
    p 'If necessary,{w=.3} I will also stake out her.'
    y 'Okay.{w=.3} There\'ll be nothing wrong on her.'
    na 'A girl he saw shouldn\'t be Hye-na.'
label hyena:
    show screen key_screen
    scene dw
    show expression Text ('{color=#ff9000}{size=+64}C{/size}{/color}ircumstances', style='part', color='#fdc56c')
    if persistent.part09 is False:
        $ persistent.part09 = True
        $ archives += 1
    with dissolvee
    pause 3
    scene roomn with dissolvee
    na 'I still got enough time to deal with Yunwoo\'s design stuffs.'
    na 'At the moment,{w=.3} the most important thing to me is Hye-na.'
    play sound 'se/dial1.ogg'
    na 'As soon as I get back home,{w=.3} I call right away Hye-na.'
    na 'If she\'s working in a cafe,{w=.3} she would be still working.'
    play sound 'se/dial1.ogg'
    pause 2
    h 'Ga-yeon~!{w=.3} You finally call me!{w=.3} Have you met Yunwoo?'
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    p 'What?{w=1}'
    na 'As her unexpected question flusters me,{w=.3} I hesitate in speaking for a while.'
    p 'Yes,{w=.3} after I met him and got back home,{w=.3} I\'m calling you.'
    na 'Was it both of your plan to visit me today?'
    na 'Are they worried about me?{w=0.3} That\'s why they\'re doing like this?'
    na 'I know you worry about me,{w=0.3} and I\'m thankful for that,{w=0.3} but Hye-na.'
    p 'Are you busy now?'
    h 'No,{w=0.3} I\'m going to close the cafe soon.{w=0.3} Actually now I\'m filling the napkin boxes.{w=0.3} It\'s okay,{w=0.3} I\'m available now.'
    na 'She answers in relaxed tones.'
    na 'Listening to the way she talks,{w=0.3} I can see she is working now.'
    na 'Until I tell her the main point,{w=0.3} I double check,{w=0.3} having several short conversations with her.'
    p 'All right.{w=.3} So what did you say where you are working now?'
    h 'Me?{w=.3} Daehangno!{w=.3} It\'s a cafe – OO,{w=0.3} near the Exit 4 of Hyehwa Station.'
    h 'Did you already forget that?'
    p 'Oh,{w=.3} sorry.{w=.3} My memory isn\'t as good as before.'
    h 'Geez,{w=.3} you can\'t be!{w=.3} You are still young!'
    p 'Yes,{w=.3} you\'re right.{w=.3} Anyway,{w=.3} are you available after work?'
    h 'After work?{w=.3} Yes,{w=.3} sure,{w=.3} but why?{w=.3} What\'s wrong with you?'
    p 'No,{w=.3} let\'s go for a beer tonight.{w=.3} It\'s been a long time since we have a beer together.'
    h 'It sounds great.{w=.3} Also I wanted to have a beer with you.'
    p 'Okay,{w=.3} then I\'ll go over there now.'
    h 'Good!{w=.3} See you soon!'
    p 'Okay,{w=.3} bye.{w=1}'
    play sound 'se/dialoff.ogg'
    pause 1
    p 'Hye-na,{w=.3} I believe in you.'
    na 'I whisper at the phone,{w=.3} though it\'s already hung up.'
    na 'After putting my phone down,{w=.3} I think for a while about her privacy,{w=.3} her boyfriend,{w=.3} and all that sorts of things.'
    na 'I should lead the conversation naturally.'
    stop music fadeout 3
    na 'Letting out a short sigh,{w=.3} I get up and prepare to go out.'
    play music 'bgm/Nyx.ogg' fadein 3
    scene hofg with dissolvee
    if persistent.bgm10 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getmusic at get
            else:
                show getmusic_ko at get
        $ persistent.bgm10 = True
        $ archives += 1
    na 'My sister.{w=.5}'
    na 'Hye-na.{w=.5}'
    na 'What\'s going on around her….{w=.5}'
    if persistent.alarm is True:
        hide getmusic
        hide getmusic_ko
    pause 1
    h 'Ga-yeon~!'
    scene hof with dissolvee
    na 'I\'m deeply absorbed in thought for a while sitting alone by the table,{w=.3} and then,{w=.3} with Hye-na\'s voice,{w=.3} I turn my head to her.'
    show hy
    h 'I\'m sorry,{w=.3} the last customer stayed too long.'
    na 'She comes to my seat,{w=.3} waving her hand.'
    p 'No,{w=.3} no worry.{w=.3} Have a seat here.'
    h 'Hey,{w=.3} Ga-yeon,{w=.3} the interior design here is so cool,{w=.3} isn\'t it?'
    p 'Yes,{w=.3} I was so suprised!'
    h 'I like here.{w=.3} It looks posh and is not that noisy unlike other places.'
    p 'Yes,{w=.3} it seems cool.'
    na 'I make agreeable responses to her,{w=.3} admiring the pub.'
    na 'You know,{w=.3} Hye-na,{w=.3} your smile looks so pure.'
    hide hy
    show hss
    with f
    h 'It\'s really been a long long time to have a drink with you.'
    p 'Yeah,{w=.3} you\'re right.{w=.3} I feel great today.'
    h 'So,{w=.3} Ga-yeon,{w=.3} why don\'t you try to get over little by little?{w=.3} If out of work too long,{w=.3} you will forget everything.'
    na 'At the instant,{w=.3} it makes me gasp.'
    na 'It\'s been two years,{w=.3} since I became jobless.'
    na 'How longer do I have to be isolated in this way?'
    na 'No,{w=.3} it\'s not isolation.'
    na 'I\'ve just given up.'
    na 'Then,{w=.3} could I start again?'
    na 'Would there be any place where I\'m allowed to belong?'
    pause 1
    na 'Dropping my eyes,{w=.3} I\'m hesitant for a while.'
    na 'Later - Not now.'
    na 'Thinking like that,{w=.3} I raise my head again and look at Hye-na with a faint smile.'
    p 'You\'re right.{w=.3} I\'m not going to remain in this way.'
    p 'I\'ll challenge again.{w=.3} Will you root for me?'
    h 'Of course!{w=.3} I know you\'ve troubled a lot because of me so far!'
    p 'No,{w=.3} don\'t say like that!{w=.3} I can do anything for my adorable sister,{w=.3} Hye-na.'
    h 'Eww….{w=.3} Ga-yeon,{w=.3} stop,{w=.3} I got goose bumps.'
    hide hss
    with d5
    pause 1
    na 'Chortling with glee,{w=.3} I and she enjoy talking quite a while,'
    na 'about lots of happenings that we had while we haven\'t had a conversation,'
    na 'our parents in a small city,'
    na 'our childhood memories,'
    na 'and hot celebrities.'
    na 'And from now on,{w=.3} about what we have to talk.{w=1}'
    p 'Hye-na,{w=.3} do you have someone to go out with now?{w=.3} You\'re supposed to prepare for marriage,{w=.3} aren\'t you.'
    show hy
    with d5
    h 'Ga-yeon,{w=.3} how can I marry earlier than you!{w=.3} I don\'t leave you alone!'
    na 'Shaking her hands from side to side and smiling broadly,{w=.3} she says with her loosened tongue.'
    p 'Then you don\'t have a boyfriend?'
    na 'I say to her,{w=.3} inclining forward towards her with an interested look and staring at her eyes.'
    na 'Then,{w=.3} she rolls her eyes for a moment,{w=.3} and opens her lips gently gazing at me.'
    hide hy
    show hss
    with d5
    h 'I{w=.3} {size=+3}want{/size}{w=.5} {size=+6}to{/size}{w=.5} {size=+9}have{/size}{w=.5} {size=+12}one!{/size}{w=.5}'
    hide hss
    with d5
    play sound 'se/knocked.ogg'
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    p 'Hye-na?{w=.5} HYE-NA!!'
    na 'She got drunk too much.{w=.3} All of a sudden,{w=.3} she just blacks out and collapses against the table.'
    na 'Did you drink that much?'
    na 'I still have lots of things to ask….'
    na 'Well,{w=.3} I\'d better call Yunwoo.'
    na 'Thinking like that,{w=.3} I\'m just about to stand up.{w=.3} And at that moment,{w=.3} I hear Hye-na\'s small voice.'
    h 'Not today.{w=.3} I\'m so happy today as I met my sister.'
    scene hofshock with red
    h 'Honey,{w=.3} you have to pay me first.'
    h 'I drank too much today.{w=.3} If we…,{w=.3} I might throw up.'
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    h 'Do you like me?{w=1}'
    scene black with d
    $ show_quick_menu = False
    centered '{cps=15}{size=+5}What are you saying now?{/size}{/cps}'
    play sound 'se/flash.ogg'
    scene roomg with flash
    show hssg
    h 'Surprise~! Ga-yeon! It\'s me!'
    stop sound
    play sound 'se/flash.ogg'
    with flash
    h 'I got paid. I just wanted to present something for you.'
    hide hssg
    show hwg
    h 'Look, you are smart. You can do everything! Don\'t let anyone bring you down!'
    stop sound
    play sound 'se/flash.ogg'
    scene photo
    with flash
    if persistent.unlock_2 is False:
        if persistent.alarm is True:
            if persistent.korean is False:
                show getgall at get
            else:
                show getgall_ko at get
        $ persistent.unlock_2 = True
        $ archives += 1
    pause 1
    scene black
    with flash
    show expression Text ('Choi Hye-Na', style='extext') onlayer overlay as text with d3
    if persistent.alarm is True:
        hide getgall
        hide getgall_ko
    stop music fadeout 3
    with f3
    scene dw
    show expression Text ('{color=#776e6e}{size=+64}G{/size}{/color}ame {color=#776e6e}{size=+64}O{/size}{/color}ver', style='part', color='#b0aca5')
    with dissolvee
    pause 3
    return