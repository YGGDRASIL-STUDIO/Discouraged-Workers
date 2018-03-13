label start:
    show screen key_screen
    stop music
    if not _in_replay:
        scene black with d
        $ show_quick_menu = False
        centered "Discouraged Workers"
        centered "People who want to get jobs,{w=.3} but give up because it's impossible."
        pause 1
    $ progress += 1
    if not persistent.blind is True:
        scene room at sepia
        show h_smile_sepia at right
        show expression 'part_01_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part01]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part01]', style='centered_text')
    pause 3
    scene black with d
    if persistent.blind is True:
        scene room with blind
    elif persistent.dw2017 is True and persistent.teddy is None:
        scene room
        show screen teddy
        with blind
    else:
        scene room with blind
    $ show_quick_menu = True
    $ save_name = "[gui.part01]"
    play sound 'se/bell.opus'
    play music 'bgm/Sigh day.opus' fadein 3
    na "The doorbell rings and wakes me up."
    na "I open my eyes and pick up the cell phone to see the time."
    na "8:45 a.m."
    play sound 'se/bell.opus'
    na "The doorbell rings again."
    na "It's quite annoying,{w=.3} but I get out of bed and walk toward the door."
    show gb
    with d5
    p "Who on earth is that,{w=.3} so early in the morning…?"
    hide gb
    with d5
    play sound 'se/open.opus'
    na "Scratching my head,{w=.3} I open the door."
    show h_smile
    with d5
    h "Surprise~!{w=.3} Ga-yeon!{w=.3} It's me!"
    na "My sister,{w=.3} Hye-na,{w=.3} cheerfully greets me with her beautiful big smile."
    na "With a puzzled look,{w=.3} I say to her."
    p "Hye-na….{w=.3} What are you doing here?"
    h "Well,{w=.3} while I was buying fresh bread,{w=.3} you just popped into my head!{w=.3} So I came to see you."
    na "And to emphasize the last sentence,{w=.3} she leans forward towards me."
    na "And she shows me a bag full of bread."
    na "Bread so early in the morning?"
    p "Uh…,{w=.3} anyway come on in."
    na "I move away from the doorway so she can enter the room."
    play sound 'se/step.opus'
    na "She grins at me,{w=.3} takes off her shoes,{w=.3} then strides across the room and sits by a small desk. "
    h "Hey,{w=.3} I bought some bagels and sesame buns for you.{w=.3} Have some!"
    na "She beckons me."
    p "Ah…,{w=.3} yes."
    hide h_smile
    with d5
    play sound 'se/cup.opus'
    na "Taking the milk out of the fridge,{w=.3} I bring it to her with a cup. "
    na "Sitting across from her,{w=.3} I pour the milk into the cup and pass it to her."
    na "Taking a bite of her sesame bread,{w=.3} she stares at me."
    na "Then,{w=.3} she opens her mouth."
    show h_smile
    with d5
    h "Why haven't you called me for so long?{w=.3} I heard that you haven't called Mom and Dad for a long time either."
    na "After blurting out those words,{w=.3} she's waiting for my answer."
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        show blink1 with d5
    na "Putting down my bread and blinking several times,{w=.3} something is disturbing me."
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        hide blink1 with d5
    p "Well…,{w=.3} it's…."
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        show blink1 with d5
    na "I hesitate for a moment,{w=.3} because I don't know what to say.{w=.3} I just blink my eyes unconsciously."
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        hide blink1 with d5
    h "Do you have any idea how worried Mom has been?{w=.3} She said you haven't called in almost three months."
    p "….{w=.3}"
    na "She puts down her bread and carefully asks me."
    hide h_smile
    show h_poker
    with d5
    h "Was your phone cut off?"
    p "….{w=.3}"
    na "Damn,{w=.3} I'm so ashamed of myself.{w=.3} I can't even raise my head in front of my sister."
    na "I keep silent for a moment and just drum my fingers on the desk."
    h "Take it."
    hide h_poker
    show envelope
    with d5
    play sound 'se/envelope.opus'
    na "Then,{w=.3} she takes a white envelope out of her handbag and holds it out to me."
    p "What's this?"
    na "I take it and open to see what's inside."
    na "Then,{w=.3} I'm so shocked by a ￦ 100,000 check in the envelope.{w=.3} I give it back to her right away."
    hide envelope
    with d5
    p "What's this?{w=.3} Why are you giving it to me?"
    show h_poker
    with d5
    h "I got paid.{w=.3} I just wanted to give you a present."
    na "Then,{w=.3} she gives me a smile,{w=.3} and continues to speak."
    hide h_poker
    show h_smile
    with d5
    h "Because you are not working now.{w=.3} I'll be happy if it's helpful to you."
    na "In contrast with her smiling face,{w=.3} I'm very embarrassed."
    na "Needless to say,{w=.3} I exclaim,{w=.3} scowling at her."
    p "No!{w=.3} I can't take this!"
    na "Saying this,{w=.3} I shake my hands and the envelope."
    na "How can I take money from my little sister?{w=.3} I can't do that."
    hide h_smile
    show h_poker
    with d5
    h "Look,{w=.3} you've given too many things to me.{w=.3} And now,{w=.3} it's time for me to help you.{w=.3} Please."
    na "She replies with a slightly serious expression on her face."
    play sound 'se/give.opus'
    na "And as if she were going to take the envelope back,{w=.3} she covers it with her two hands,{w=.3} and strongly gives it back to me."
    p "Hye-na…!{w=.5}"
    na "I stop talking and look away from Hye-na,{w=.3} just staring off into the distance."
    hide h_poker
    show h_opinion
    with d5
    h "Take it.{w=.3} And please keep your chin up!{w=.3} It's not like you!"
    h "Look,{w=.3} you are smart.{w=.3} You can do anything!{w=.3} Don't let anyone bring you down!"
    na "With a strong voice,{w=.3} she tries to cheer me up."
    na "And soon,{w=.3} she smiles again and says to me,"
    hide h_opinion
    show h_smile
    with d5
    h "OK?{w=.3} Then,{w=.3} let's eat!"
    p "….{w=.3}"
    na "I hesitate for awhile.{w=.3} But soon,{w=.3} I decide to follow her."
    p "Um….{w=.3} Thank you."
    na "And with my answer,{w=.3} she nods her head and picks up her bread again."
    na "She's a good sister.{w=.3} My adorable and beautiful sister."
    na "Eating bread,{w=.3} we chat about best bakery in the town,{w=.3} and those sorts of things."
    with f
    h "So,{w=.3} Ga-yeon,{w=.3} don't forget to give Mom a call!{w=.3} Okay?"
    na "And while saying that,{w=.3} she tilts her head slightly to her right hand,{w=.3} where her thumb and fingers are arranged to look like a phone."
    na "Giving her a slight nod,{w=.3} I reply to her."
    p "Yeah.{w=.3} Take care,{w=.3} bye."
    hide h_smile
    show h_laugh
    with d5
    h "Okay!{w=.3} Good bye~!"
    play sound 'se/rock.opus'
    hide h_laugh
    with d5
    play sound 'se/hstep.opus'
    pause 1
    na "She opens the door with her right hand,{w=.3} waves goodbye to me,{w=.3} then leaves."
    p "Well…,{w=.3} you left so soon.{w=.3} I hoped you would have stayed longer and eaten all the bread with me."
    na "I say to myself,{w=.3} looking at the bag of bread,{w=.3} while she walks away and out of my sight."
    na "Then,{w=.3} I sit by the desk,{w=.3} and open the envelope Hye-na gave me again.{w=.3} Wait,{w=.3} there's more than one check in it!{w=.3} I look at the individual checks in the envelope and count them…."
    p "My god….{w=.3} There's ten checks in here…,{w=.3} one million won….{w=.3} It's too much…."
    na "I raise my head,{w=.3} and let out a sigh."
    scene black with blind
    $ show_quick_menu = False
    pause 1
    centered "Well,{w=.3} no matter how much she gave,{w=.3}\nyou were going to take it anyway."
    centered "How could you refuse it?"
    $ renpy.end_replay()
    if persistent.part01 is None:
        $ persistent.bgm02 = True
        $ persistent.hyena = True
        $ persistent.bgm += 1
        $ persistent.char += 1
        $ persistent.replay += 1
        $ achievement.grant('KNDW_START')
        $ achievement.grant('KNDW_RELEASE')
        $ achievement.progress('KNDW_PROGRESS', 1)
        $ achievement.progress('KNDW_IDENTIFY', 2)
        $ achievement.progress('KNDW_OBJECT', 1)
        $ achievement.progress('KNDW_OST', 2)
        if not persistent.blind is True:
            call unlocked
label mono0:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene room at sepia
        show gb_sepia at right
        show expression 'part_02_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part02]', style='part_title')
        with d
        pause 3
    else:
        scene black
        show expression Text ('[gui.part02]', style='centered_text')
    scene black with d
    pause 1
    $ progress += 1
    $ save_name = "Monologue"
    $ show_quick_menu = False
    centered "I'm jobless."
    centered "I'm twenty eight years old."
    centered "After graduation,{w=.3} some of my friends got jobs,{w=.3} and some of them got married.{w=.3} And they have been living happily with their new families."
    centered "But I didn't finish university,"
    centered "and I'm unemployed,"
    centered "and I'm still not married."
    centered "Well…,{w=.3} what's even worse is,{w=.3}\nI don't even have a boyfriend to go out with."
    centered "What a shame.{w=.3} I'm too young to stay cooped up indoors all day long."
    centered "How did this happen?"
    centered "After thinking for a long time,{w=.3} I just draw a sigh."
    stop music fadeout 3
label intern:
    scene black with d
    show expression Text ('A year ago….', style='extext') at times with d3
    scene black with d3
    scene internr with d3
    $ show_quick_menu = True
    $ save_name = "A year ago…."
    play music 'bgm/Mare tranquillitatis.opus' fadein 3
    na "An interview room at a restaurant.{w=.3} I'm standing in front of the interviewer."
    na "In spite of many interview experiences,{w=.3} I'm still so nervous."
    pause 1
    show i_poker
    with d5
    intern "Miss Choi Ga-yeon?"
    na "Sitting at the desk,{w=.3} she looks at me and my resume alternately.{w=.3} Then,{w=.3} she asked me."
    na "Just like her appearance,{w=.3} her question is pretty sharp."
    p "Yes,{w=.3} ma'am!"
    na "Undaunted,{w=.3} I answer without hesitation and in a loud voice."
    intern "What made you choose our company?"
    na "Even as she picked up a paper cup filled with water and drank some,{w=.3} she kept her eyes firmly fixed on me."
    na "I answer without hesitation."
    p "I had job counseling at the employment information center.{w=.3} They suggested I get a job in the food service industry."
    p "And they recommended your company.{w=.3} I visited once to look around!"
    p "When I visited,{w=.3} I was touched by the staff's kind service.{w=.3} So,{w=.3} I decide to apply for a job here!"
    na "After I finish my answer,{w=.3} she smiles contentedly and asks me another question,{w=.3} while also looking at my resume."
    hide i_poker
    show i_smile
    with d5
    intern "Haha,{w=.3} did you?{w=.3} Well,{w=.3} you've also worked as a coordinator at OO hospital,{w=.3} for two years?"
    p "Yes!{w=.3} That's right!"
    intern "And you have a class 1 qualification as a hospital coordinator.{w=.3} Will you tell me why you quit,{w=.3} even though you've worked there for more than two years?"
    intern "I'm just wondering why you want to work in the food service industry,{w=.3} instead of continuing to work as a skilled hospital coordinator?"
    na "In spite of her friendly manner,{w=.3} I winced for a moment…."
    na "If I tell her the truth,{w=.3} I will definitely fail to get a job here."
    na "I've also had similar questions at the previous interviews,{w=.3} and whenever I was asked,{w=.3} I lied."
    na "And this time,{w=.3} I'm going to tell a lie again."
    p "After I graduated from high school,{w=.3} I worked at a family restaurant for a while,{w=.3} until entering university."
    p "And after seeing the manager there,{w=.3} I dreamt of someday becoming a professional manager,{w=.3} just like her,{w=.3} in the food service industry!"
    p "But I had to go to university.{w=.3} Then,{w=.3} while at school,{w=.3} my family budget became tight,{w=.3} and I started to work at the hospital!"
    p "Working at the hospital,{w=.3} I became sick of doctors who didn't sincerely care for their patients.{w=.3} So I decided to quit,{w=.3} and today I look forward to change."
    na "I finished my answer in a confident voice.{w=.3} She nods her head,{w=.3} and continues to ask questions."
    intern "Good.{w=.3} The job here will be much harder than your previous job.{w=.3} Are you ready for that?"
    na "I answered her immediately."
    p "Yes!{w=.3} I can do it!"
    intern "Here's my last question.{w=.3} What do you think a customer is?{w=.5}"
    na "Geez.{w=.3} I didn't expect this."
    na "Okay,{w=.3} calm down.{w=.3} Arrange words first."
    na "For a moment,{w=.3} I rack my brain to find the right words."
    na "And I organize the words in my mind."
    p "I think,{w=.3} a customer is like an old friend at home."
    hide i_smile
    show i_think
    with d5
    intern "{cps=10}An old friend at home…?{/cps}{w=1}"
    na "Making a disappointed face,{w=.3} the interviewer pulls her chair forward and leans towards the table."
    na "Oh…,{w=.3} did I say something wrong?"
    na "Ok,{w=.3} let me try to explain further."
    p "I have some friends back home that I can't get in touch with often because of my busy life."
    p "And sometimes they visit me from far away."
    p "Then,{w=.3} I welcome them and dish up dinner for my friends…,{w=.3} then,{w=.3} my friends go back to their houses far away."
    p "We don't know when we will meet again,{w=.3} but we promise each other to meet someday in the future,{w=.3} with these good memories."
    p "That is what a customer is to me.{w=.5}"
    na "God,{w=.3} what am I talking about?"
    na "As soon as I finish that answer,{w=.3} I think the interview today is completely screwed up,{w=.3} and I mentally reproach my tongue."
    play sound 'se/file.opus'
    hide i_think
    with d5
    na "She puts my resume down,{w=.3} and clasps her hands together on the desk."
    na "Only moving the forefinger of her right hand up and down,{w=.3} she looks down at her hands."
    na "I can't read her face."
    show i_poker
    with d5
    intern "Miss Choi Ga-yeon."
    p "Yes,{w=.3} yes!"
    na "I'm nervous about her calm voice."
    na "After a while,{w=.3} she stops moving her forefinger,{w=.3} looks up at me,{w=.3} and says."
    intern "Customers can't be friends.{w=.3} But I personally think your answer was perfect."
    hide i_poker
    show i_smile
    with d5
    intern "If possible,{w=.3} I want to begin training you right away."
    p "Ah…!"
    na "Oh my god!"
    na "The interviewer says with a smile on her face,{w=.3} to me,{w=.3} who is leaping for joy in my mind."
    intern "I give you 10 out of 10 for your interview.{w=.3} But as there are many experienced applicants,{w=.3} I can't be 100%% certain yet that you are the best person for the job."
    p "Thank you!{w=.3} If you do hire me,{w=.3} I'll do my best!"
    stop music fadeout 3
    scene black with d3
label mono1:
    scene room with d3
    play music 'bgm/Unknown mist.opus' fadein 3
    pause 1
    $ save_name = "I'm sick of everything."
    na "That was my last interview."
    na "But there was no call."
    na "It always went like that."
    na "The interviewer always says there will be good news."
    na "And that we will work together soon."
    na "But every time,{w=.3} it ends up like this."
    scene black
    show frustration
    show circle
    with d3
    na "I'm sick of everything."
    na "I cried like a child,{w=.3} hitting my pillow in frustration,{w=.3} in my small room."
    hide frustration
    hide circle
    show vomiting
    show circle
    with d3
    na "I drank,{w=.3} and threw up holding the toilet."
    hide vomiting
    hide circle
    show pusillanimous
    show circle
    with d3
    na "I was just lying in my bed,{w=.3} doing nothing but staring up at the ceiling."
    na "I'm sick of everything."
    na "I am a loser."
    na "{cps=15}I'm a discouraged worker.{/cps}{w=1}"
    pause 3
label gone:
    scene room with f3
    na "Standing in front of the desk for a while,{w=.3} I get depressed."
    na "Looking down at Hye-na's breads for a while,{w=.3} I still have tears in my eyes."
    play sound 'se/water.opus'
    na "Sitting by the desk,{w=.3} I pour the milk into my cup and take a sip of it."
    na "I bite off a small chunk of the sesame bread."
    na "{cps=15}Tears pour down {/cps}{cps=5}my face.{/cps}{w=1}"
    stop music fadeout 3
    $ renpy.end_replay()
    if persistent.part02 is None:
        $ persistent.bgm03 = True
        $ persistent.bgm07 = True
        $ persistent.interviewer = True
        $ persistent.con01 = True
        $ persistent.unlock_16 = True
        $ persistent.unlock_17 = True
        $ persistent.unlock_18 = True
        $ persistent.bgm += 2
        $ persistent.char += 1
        $ persistent.con += 1
        $ persistent.gall += 3
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 2)
        $ achievement.progress('KNDW_IDENTIFY', 3)
        $ achievement.progress('KNDW_CONCEPT', 2)
        $ achievement.progress('KNDW_ART', 3)
        $ achievement.progress('KNDW_OST', 4)
        if not persistent.blind is True:
            call unlocked
label caffe:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene caffe at sepia
        show y_smile_sepia at right
        show expression 'part_03_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part03]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part03]', style='centered_text')
    pause 3
    scene black with d
    $ progress += 1
    scene caffe with blind
    pause 1
    $ save_name = "Do you remember first love?"
    $ show_quick_menu = True
    play music 'bgm/CCCanon.opus' fadein 3
    show y_smile
    with d5
    y "Feel better?"
    p "….{w=.5}"
    y "Hey,{w=.3} you're not a teenager anymore."
    na "A man sitting across my table says teasingly while raising his hands."
    p "I know that."
    na "I mutter with a wry face."
    na "His name is Kim Yunwoo."
    na "He and I are the same age,{w=.3} and we've known each other since we were high school students."
    na "During high school,{w=.3} I always thought he was a strange boy who never showed any emotion and who always had a poker face.{w=.3} But as time went by,{w=.3} he gradually changed little by little."
    y "No one would cry so pitifully like you,{w=.3} eating bread in a room."
    na "His face looks as if he were talking to a kid."
    p "You know what,{w=.3} you are the bad guy,{w=.3} coming into my place uninvited."
    na "Slurring my words,{w=.3} I avoid his eyes."
    na "Today is a very strange day."
    na "Hye-na came over unexpectedly so early in the morning,{w=.3} and soon after she left,{w=.3} Yunwoo appeared too."
    na "Well….{w=.3} Anyway,{w=.3} what a sight."
    na "Why did he appear so abruptly now?"
    y "You know,{w=.3} I was surprised.{w=.3} Your door was open,{w=.3} and a crying girl was eating her bread alone inside."
    p "So why did you come over here without telling me you were coming?{w=.3} It's your fault."
    na "I grumble to him."
    y "Your phone has been cut off because of the unpaid bills.{w=.3} So,{w=.3} what was I supposed to do but visit?"
    na "You idiot.{w=.3} There is WiFi."
    na "Snapping at the chance,{w=.3} I bridle,{w=.3} and take a dig at Yunwoo."
    p "There's ○○.{w=.3} I can use it wherever there is free WiFi."
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    hide y_smile
    show y_question with shock
    with d5
    y "What?{w=.3} Are you kidding?"
    na "Huh,{w=.3} why is he being so insincere?"
    hide y_question
    show y_think
    with d5
    y "Then,{w=.3} why haven't you talked to me for so long?"
    na "Supporting himself against his left elbow on the arm of the chair,{w=.3} he bends his body to the left and asks me."
    p "How could I contact you when I am in such an embarrassing situation?"
    na "I replied,{w=.3} whining slightly.{w=.3} And he says with a smile."
    hide y_think
    show y_smile
    with d5
    y "Dude,{w=0.3} that's not true.{w=.3} Our relationship is special."
    p "Well,{w=0.3} you are right."
    na "And with that,{w=.3} I breathe a sigh."
    hide y_smile
    with d5
    na "Yunwoo is a pretty weird man."
    na "After graduating from high school,{w=.3} he joined the military,{w=.3} and since he was discharged,{w=.3} he's been living in a semi-basement room near Hongik University."
    na "And because he loves music so much,{w=.3} he hasn't had any job and just plays in his band."
    na "Yunwoo is living in his own isolated world,{w=.3} far away from others outside of his band."
    na "Yunwoo doesn't compromise with the principle of capitalism.{w=.3} And lives in his own way.{w=.3} Happiness is much more important than money to him."
    na "When I was young,{w=.3} I thought that was cool."
    na "He was so thoughtful and felt like an older brother to me."
    na "However,{w=.3} as soon as I began my life as an adult in society,{w=.3} everything seemed to be different."
    na "Yunwoo might be more desperate than many other people."
    na "Though he never shows this side of him to others,{w=.3} I vividly remember what he said after he was discharged from the military.{w=.3} His eyes were so intense at the moment he first told me…."
    show y_smile
    with d5
    y "Hey,{w=0.3} come on."
    p "Eh,{w=0.3} what?"
    na "Thinking about this stuff,{w=0.3} I say to him."
    y "Your coffee is getting cold.{w=0.3} Cold coffee is like an empty life."
    na "I don't understand Yunwoo when he sometimes says weird things like this."
    p "Uh-huh."
    hide y_smile
    with d5
    na "Anyway,{w=0.3} because I have nothing to say,{w=0.3} I just mumble an answer to him."
    na "Then,{w=0.3} I pick up my cup on the table,{w=.3} and take a gulp of coffee."
    na "As soon as I put my coffee cup down,{w=0.3} Yunwoo picks up his small demitasse cup and takes a sip."
    na "He likes espresso.{w=0.3} But I don't understand why he likes that sort of thing."
    show y_smile
    with d5
    y "Here,{w=0.3} have some bread."
    hide y_smile
    show bread
    with d5
    na "Yunwoo cut off a bit of honey bread with his fork,{w=0.3} and held it out for me to take."
    $ renpy.end_replay()
    if persistent.part03 is None:
        $ persistent.yunwoo = True
        $ persistent.bgm04 = True
        $ persistent.bgm += 1
        $ persistent.char += 1
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 3)
        $ achievement.progress('KNDW_IDENTIFY', 4)
        $ achievement.progress('KNDW_OST', 5)
        $ achievement.progress('KNDW_OBJECT', 2)
        if not persistent.blind is True:
            call unlocked
label shinchon:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene sin at sepia
        show tdw_sepia
        show expression 'part_04_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part04]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part04]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    scene sin with blind
    $ save_name = "Shin-Chon Street"
    $ show_quick_menu = True
    na "Yunwoo takes me outside on the street,{w=0.3} saying that I need fresh air."
    na "He's walking on my right,{w=0.3} and I on his left,{w=0.3} a little bit away from him."
    na "Even though it's only midday now,{w=0.3} it's still pretty crowded here today."
    show y_think
    with d5
    y "Is there something special going on today?{w=0.3} Why is it so crowded?"
    na "Yunwoo doesn't look well."
    p "You don't like crowded areas,{w=0.3} do you?"
    y "Wow,{w=0.3} I don't feel well."
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    na "He looks like he's just about to throw up any minute now."
    p "My god!{w=0.3} Are you going to throw up here?"
    na "Surprised,{w=.3} I strongly shake his arms."
    hide y_think
    show y_smile
    with d5
    na "Then he looks at me,{w=0.3} giggling."
    y "Haha,{w=0.3} I'm just kidding."
    na "I give Yunwoo a serious look,{w=0.3} and turn my head to look away from him."
    p "It doesn't please me at all."
    y "There it is,{w=.3} Ga-yeon.{w=0.5}"
    na "I don't think Yunwoo even heard my comment about his joke.{w=.3} And I instinctively turn my head in the direction that he is looking."
    p "Huh?"
    hide y_smile
    with d5
    na "He is pointing over to the right."
    na "I try to see what Yunwoo is pointing at.{w=.3} But because he's blocking my view in that direction,{w=.3} I can't see what it is."
    na "I grab Yunwoo's left arm,{w=.3} and pull him towards me to get a clear view."
    na "That's better.{w=.3} I crane my neck to see what he is pointing at."
    pause 1
    na "It is a cell phone shop."
    p "Ok.{w=0.3} So what?"
    p "Um….{w=0.5}"
    show tdw
    with d
    pause 3
    na "Raising my head to look at him,{w=.3} I start to ask Yunwoo what he is going to do.{w=.3} But then,{w=.3} I stop."
    na "Yunwoo looks down at me,{w=.3} and I look up at him.{w=.3} Our eyes lock.{w=.3} Soon,{w=.3} I realize that we are too close."
    na "We are silent for a while."
    y "Right now,{w=.3} time between us stops.{w=.3} While time for the rest of the world continues as it was before."
    p "…!"
    hide tdw
    with d
    na "After a moment,{w=.3} I blink my eyes and take a step backward."
    p "Don't be stupid,{w=.3} so what?"
    na "I say to Yunwoo,{w=.3} mostly to end the awkward silence between us."
    na "Then Yunwoo gazes at me,{w=.3} and the shop,{w=.3} and says,"
    show y_smile
    with d5
    y "You said Hye-na gave you some money for your unpaid phone bill.{w=.3} Let's go and pay it now."
    p "No,{w=.3} later.{w=.3} I'll go alone."
    na "Turning my head,{w=.3} I answered in a feeble voice."
    na "The clerk will probably say that I've got a lot of past-due bills or something like that."
    na "And I don't want Yunwoo to see me in such a shameful situation."
    y "Come on."
    na "Then he grabs my wrist by his hand,{w=0.3} and pulls me towards the shop."
    p "Hey!{w=0.3} I said no!"
    na "I holler at Yunwoo,{w=0.3} but he completely ignores me."
    na "Although I try to resist him,{w=.3} it is futile."
    na "Then we arrive at the shop,{w=.3} and he practically has to drag me inside."
    stop music fadeout 3
label phone:
    scene phone with f
    play music "bgm/Let's game.opus" fadein 3
    show e_laugh at right
    with d5
    $ angelname = 'Clerk'
    ex "Come on in!{w=0.3} May I help you?{w=.3} Want to see our newest phone models?{w=0.3} We have many phones for couples as well!"
    na "A perky clerk welcomes us,{w=.3} coming out to the entrance of the shop."
    hide e_laugh
    show e_laugh_gray at right
    show y_smile at left
    with d5
    y "Hello,{w=0.3} we'd like to pay a phone bill."
    hide y_smile
    show y_smile_gray at left
    hide e_laugh_gray
    show e_laugh at right
    with d5
    play sound 'se/clap1.opus'
    ex "Good~!{w=0.3} Come over here,{w=0.3} please."
    na "Then,{w=.3} the woman claps her hands and leads Yunwoo to a table."
    hide y_smile_gray
    hide e_laugh
    with d5
    na "Yunwoo sits in a chair across from her and talks.{w=.3} And I sit by the table behind them and gaze at Yunwoo the entire time."
    na "He's dealing with my unpaid bills for me."
    show e_laugh at right
    with d5
    ex "Okay,{w=0.3} done!{w=0.3} Anything else you need?"
    na "She asks Yunwoo,{w=0.3} and he answers by shaking his head."
    hide e_laugh
    show e_laugh_gray at right
    show y_smile at left
    with d5
    y "No,{w=0.3} thank you."
    hide y_smile
    hide e_laugh_gray
    with d5
    na "He comes over to me and gestures that we should leave,{w=0.3} opening the door for me."
    na "So I get up and follow him.{w=.3} Then,{w=.3} the clerk says something,"
    show e_laugh
    with d5
    ex "Oh,{w=0.3} hey,{w=0.3} you look familiar,{w=.3} have I seen you on the internet?"
    p "Hum…?"
    na "As I am about to turn around,{w=0.3} Yunwoo suddenly puts his arm around my shoulder and guides me out."
    hide e_laugh
    show y_smile
    with d5
    y "Let's get out of here,{w=0.3} Ga-yeon."
    p "Wa…,{w=0.3} wait!{w=0.3} What are you doing?"
    stop music fadeout 3
    scene sin with f
    play music 'bgm/Sigh day.opus' fadein 3
    na "He pushes me out of the shop."
    na "With his hand still on my shoulder,{w=0.3} we start to walk through the crowd."
    p "Hey,{w=0.3} Yunwoo!"
    na "After being led by him for a while,{w=0.3} I said to him."
    na "But he ignores me and keeps walking forward."
    na "He does not look well.{w=0.5}"
    $ renpy.end_replay()
    if persistent.part04 is None:
        $ persistent.angel = True
        $ persistent.unlock_1 = True
        $ persistent.bgm05 = True
        $ persistent.bgm += 1
        $ persistent.char += 1
        $ persistent.gall += 1
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 4)
        $ achievement.progress('KNDW_IDENTIFY', 5)
        $ achievement.progress('KNDW_ART', 4)
        $ achievement.progress('KNDW_OST', 6)
        if not persistent.blind is True:
            call unlocked
label food:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene food at sepia
        show gb_sepia at right
        show expression 'part_05_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part05]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part05]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    scene food with blind
    show y_smile
    with d5
    $ save_name = "Sad lunch"
    $ show_quick_menu = True
    y "You know the old saying,{w=.3} \"Pudding rather than praise?\"{w=0.3} Let's go grab something to eat.{w=0.3} I haven't had a bite all day."
    na "After we enter a restaurant,{w=0.3} he looks slightly better."
    na "I venture to ask him."
    p "Why did you rush me out of that shop?{w=0.3} The clerk said I looked familiar."
    na "He raises his left hand and massages the back of his neck.{w=0.3} And with an annoyed look,{w=0.3} he says,"
    y "She was obviously trying to sell something like phone accessories."
    na "Well…,{w=0.3} I don't think so."
    na "I thought about that for a while,{w=0.3} and then decide to change the topic since things were starting to feel awkward."
    p "By the way,{w=0.3} aren't you going to get married?"
    p "You know,{w=0.3} you're already twenty eight.{w=0.3} You are going to die a bachelor."
    na "With a wry smile,{w=0.3} he says,"
    y "So,{w=.3} will you marry me?{w=0.3} I don't want to die alone."
    na "His comment makes me blush.{w=0.3} After an awkward silence,{w=0.3} I say to him,"
    p "If you want to feed me,{w=0.3} you'd better make a lot of money."
    y "All right!{w=0.3} I'll pull my socks up."
    na "He says it like it's a joke."
    na "Then,{w=0.3} I respond to his joke,{w=0.3} speaking bluntly."
    p "Of course,{w=0.3} you should.{w=0.3} You can't imagine who I am."
    y "Wow,{w=0.3} lucky me."
    hide y_smile
    with d5
    na "After this conversation between us,{w=0.3} I get lost in thought for a moment."
    na "Yeah,{w=0.3} you can't even imagine who I am."
    na "I don't deserve to marry a good guy,{w=0.3} like you."
    na "I'm…,{w=0.3} such a slut."
    na "Ha,{w=0.3} I get so depressed."
    na "Let's change the subject."
    p "So,{w=0.3} how's your band?{w=0.3} Is everything alright?"
    na "I ask,{w=0.3} staring at him."
    show y_smile
    with d5
    y "Yes,{w=0.3} we've got four permanent stages on weekends."
    y "And,{w=0.3} on weekdays we have six stages to play at between 7 in the evening and 1 in the morning."
    p "Wow~,{w=0.3} you are going to be rich soon!"
    na "I don't know why I told him that,{w=0.3} but I am a little bit excited."
    na "Then,{w=0.3} he adds,{w=0.3} with a slightly boastful expression."
    y "Well,{w=0.3} we're also invited to a rock festival,{w=0.3} which'll be held in two months."
    p "My god!{w=0.3} Are you serious?{w=0.3} Good for you!"
    na "And before even realizing what I'm doing,{w=.3} I touch his shoulder with my right hand."
    na "Then he slides his chair closer to me,{w=0.3} and continues."
    y "So I want you to do something for me.{w=0.3} Aren't you good with computer programs that help you paint pictures?{w=.3} Didn't you do that in high school?"
    p "Uh?{w=0.3} You say ○○?"
    na "I recall the name and say it to him."
    na "And with my answer,{w=0.3} he claps his hands cheerfully and comes to the point."
    play sound 'se/clap.opus'
    y "Yes,{w=0.3} that's it!{w=0.3} So this weekend,{w=0.3} we have our only concert,{w=0.3} and we need a poster and pamphlet for it."
    y "If you don't mind,{w=0.3} will you do it for me?{w=0.3} Of course I will pay you."
    na "After he finishes,{w=0.3} I nod my head and agree to do his poster and pamphlet job."
    p "Sure,{w=.3} no problem."
    na "Then,{w=0.3} he turns around and rummages around in his bag hung on the chair."
    y "So,{w=0.3} what we need is…."
    na "He continues to talk,{w=0.3} taking out photos of his band members to put on the poster."
    scene sanchon with d5
    na "After a while,{w=0.3} the dishes are served,{w=0.3} and we eat,{w=.3} and continue to talk about the band's poster and pamphlet for the concert."
    stop music fadeout 3
label mono2:
    scene black with d3
    $ progress += 1
    $ save_name = "Monologue"
    play music 'bgm/Peace.opus' fadein 3
    pause 1
    scene fate with d
    na "Yunwoo and I."
    na "In high school,{w=0.3} Yunwoo was a pretty mysterious guy."
    na "He used to be such a loner,{w=0.3} and hard to get close to.{w=.3} He seemed to put up an invisible barrier,{w=.3} and he never allowed others inside."
    na "He was taciturn and quiet.{w=0.3} Sometimes,{w=0.3} in the middle of class,{w=0.3} he just went out to the schoolyard to write music."
    na "I was surprised that he was even able to graduate with so many absences."
    scene alleyway
    show night
    with d
    na "However,{w=.3} what got me through his invisible barrier was his little sister."
    na "He has a sister,{w=.3} two years younger than him."
    scene alleyway_gall
    show night
    with d5
    na "One night,{w=.3} I helped another student that was being bullied in a dark alleyway,{w=.3} by several girls that were about the same age."
    na "I took her home,{w=.3} trying to comfort her on the way there.{w=.3} Surprisingly,{w=.3} Yunwoo was at her house."
    na "Yes,{w=.3} she was Yunwoo's younger sister."
    na "At home,{w=.3} there were only Yunwoo and his sister living alone,{w=.3} and that night,{w=.3} he was very anxious,{w=.3} worrying about his sister."
    scene moonlight0 with d
    na "Yunwoo said,{w=.3} {b}\"Thank you\"{/b} to me,{w=.3} with his warmest smile."
    scene moonlight1 with d
    na "And he took me home,{w=.3} saying it was too late for a girl to go home alone."
    scene moonlight2 with d
    na "As my home was quite far from his,{w=.3} we talked a lot during the trip."
    scene moonlight with d3
    na "That night,{w=.3} the moon was unusually bright,{w=.3} and the stars were beautiful and twinkling more than any other night I've watched them."
    na "Our story began that night…."
    pause 1
    $ renpy.end_replay()
    if persistent.part05 is None:
        $ persistent.bgm06 = True
        $ persistent.unlock_22 = True
        $ persistent.unlock_25 = True
        $ persistent.unlock_21 = True
        $ persistent.bgm += 1
        $ persistent.gall += 3
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 6)
        $ achievement.progress('KNDW_ART', 7)
        $ achievement.progress('KNDW_OST', 7)
        if not persistent.blind is True:
            call unlocked
label food1:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene food at sepia
        show y_smile_sepia at right
        show expression 'part_07_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part07]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part07]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    scene food with blind
    show y_smile
    with d5
    $ save_name = "Calm afternoon"
    $ show_quick_menu = True
    y "What are you thinking about?"
    p "Oh,{w=0.3} no.{w=0.3} Nothing."
    na "I reply to Yunwoo.{w=.3} My train of thought interrupted,{w=.3} I start to eat again."
    y "Hey,{w=0.3} I've got something to show you."
    na "He says to me,{w=0.3} as if he has been waiting for this moment."
    p "Huh?{w=0.3} What is it?"
    na "As I ask him what it is,{w=0.3} and he moves his hand to the right pocket of his pants."
    na "Then,{w=0.3} with a grin,{w=0.3} he takes his cell phone out of his pocket."
    na "His fingers seem to be busy pressing buttons on his phone,{w=0.3} and soon,{w=0.3} he holds it out for me to see."
    y "Look,{w=0.3} isn't she so cute?"
    hide y_smile
    with d5
    na "I take his phone and look at it."
    show baby
    with d5
    na "On the phone,{w=0.3} there is an adorable sleeping baby."
    p "Oh my god,{w=0.3} oh my god….{w=0.3} Whose is this?{w=0.3} So adorable!"
    na "Holding his phone in my hands,{w=0.3} I ask him with wonder."
    hide baby
    show y_smile
    with d5
    y "Eunyoung's baby."
    na "Not thinking much about what he had just said,{w=0.3} I look at Yunwoo,{w=0.3} then back at the phone,{w=0.3} and finally,{w=0.3} I figure out what happened."
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    p "{size=+10}Oh my goooood!{w=0.3} This is Eunyoung's baby?{/size}"
    na "I'm very surprised.{w=0.3} She already has a child?"
    na "It's only been a year -{w=0.3} no,{w=0.3} less than a year since she got married.{w=0.3} But how come?"
    y "You know what,{w=0.3} when she married,{w=0.3} she was already three months pregnant."
    na "Yunwoo says with a giggle and looks at my reaction.{w=.3} I'm extremely surprised by that."
    p "Uh….{w=0.3} I never knew that."
    na "Eunyoung is Yunwoo's younger sister."
    na "She married at around this time last year.{w=0.3} I didn't hear about this when I was at her wedding."
    na "Wow…,{w=0.3} she gave birth to this lovely baby."
    y "Why the long face?"
    na "I just shake my head several times,{w=0.3} and then tell him."
    p "No,{w=0.3} nothing.{w=0.3} Just…,{w=0.3} it's just unbelievable."
    p "You know,{w=0.3} it seems like just yesterday that she wore a school uniform."
    y "Yeah,{w=.3} only yesterday."
    y "That little girl became a woman,{w=0.3} got married,{w=0.3} and gave birth to a baby.{w=0.3} It's just unbelievable."
    hide y_smile
    with d5
    na "Having said that,{w=0.3} Yunwoo raises his arms and locks his fingers behind his head."
    na "Again,{w=0.3} I gaze at the baby's picture on the phone,{w=0.3} and touch it with my finger."
    na "Looking at a number of pictures of the baby,{w=0.3} something hollow grows inside of me."
    na "I know in this situation I'm supposed to congratulate him.{w=0.3} However,{w=0.3} I can't help but look at my own reality."
    na "If I had married,{w=0.3} I would also have a baby now like Eunyoung."
    stop music fadeout 3
    na "If I had married him at that time…."
    na "Suddenly,{w=0.3} tears well up in my eyes."
    show y_question
    with px
    y "Jeez,{w=0.3} what's wrong with you,{w=0.3} Ga-yeon!"
label says:
    scene cheon with px5
    play music 'bgm/Unknown mist.opus' fadein 3
    play sound 'se/waterfall.opus'
    pause 1
    na "He seemed to be embarrassed at what I had done,{w=0.3} and immediately takes me out of the restaurant."
    na "Yunwoo suggested we take a walk.{w=0.3} We walk along the streets quite a while,{w=.3} before reaching Cheonggyecheon Stream."
    na "While sitting by the stream,{w=0.3} I calm down."
    na "Both of us are just gazing at the flowing stream."
    p "I'm sorry….{w=.5}"
    na "Feeling ashamed,{w=.3} I hesitate at first.{w=.3} But I slowly and carefully start to talk to Yunwoo again."
    show y_smile
    with d5
    y "No.{w=.3} But it seems you are depressed."
    p "Well…,{w=.3} I think so as well."
    y "Since when?{w=.5}"
    hide y_smile
    show canned
    with d5
    play sound 'se/canopen.opus'
    na "He asks me,{w=.5} handing me a can of coffee."
    hide canned
    with d5
    na "I take the can from Yunwoo and take a sip of coffee.{w=.3} I hold the can in my hands and rest it on my knees.{w=.3} Staring at the flowing stream,{w=.3} I say to him,"
    p "It's been quite a while.{w=.3} Probably since I stopped looking for a job."
    show y_angry
    with d5
    y "It's been almost a year!"
    na "He roars in a rough voice."
    p "{size=-2}Yes,{w=.3} you're right….{/size}{w=.3}"
    na "I mumble in a hollow voice while looking down at the can in my hands."
    y "Why didn't you go to a doctor?!"
    na "His voice goes up.{w=.3} He is starting to get angry with me."
    play sound 'se/can.opus'
    na "My hands tighten their grip on the can of coffee I'm holding as I hear Yunwoo's words."
    na "I feel something surging up inside of me."
    na "Calm.{w=.3} Calm down."
    na "No,{w=.3} don't.{w=.3} I shouldn't behave shamefully in front of him,{w=.3} anymore.{w=.3}"
    na "Then I relax a bit,{w=.3} and loosen my grip on the coffee can."
    na "I raise my head,{w=.3} turn to him,{w=.3} and say,"
    p "I'm alright.{w=.3} Anyway,{w=.3} you've come to save me.{w=1}"
    y "….{w=1}"
    hide y_angry
    show y_smile
    with d5
    y "….{w=1}"
    stop music fadeout 3
    $ renpy.end_replay()
    if persistent.part07 is None:
        $ persistent.con05 = True
        $ persistent.con += 1
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 7)
        $ achievement.progress('KNDW_CONCEPT', 3)
        $ achievement.progress('KNDW_OBJECT', 4)
        if not persistent.blind is True:
            call unlocked
label cheon:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene cheon at sepia
        show h_smile_sepia at right
        show expression 'part_08_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part08]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part08]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    $ save_name = "Questionable feelings"
    $ show_quick_menu = True
    scene cheon with blind
    play music 'bgm/Lush garden.opus' fadein 3
    play sound 'se/waves.opus'
    na "Before I know it,{w=.3} Yunwoo and I are completely absorbed in conversation and putting our feet in the flowing stream."
    p "It's been a really long time since we've been here together,{w=.3} Yunwoo."
    show y_smile
    with d5
    y "Yes,{w=.3} the last time we were here was when you were a university student.{w=.3} That was almost six years ago."
    p "Six years?{w=0.3} My god,{w=0.3} I'm going to be a grandma in a blink."
    na "Leaning back on my hands on the ground,{w=.3} and with my legs in the stream,{w=.3} I move my knees back and forth to create ripples in the water.{w=.3} I said to Yunwoo,"
    y "That's just the way time is.{w=.3} I think the scariest thing in life is being human,{w=.3} and the second scariest is time."
    na "Now,{w=.3} he clasps his hands behind his head and lies down on the ground."
    na "Looking down at him on the ground,{w=.3} I just agree with him."
    p "Yes,{w=.3} I think you're right."
    y "Oh,{w=.3} by the way,{w=.3} you know what?"
    p "Huh?{w=.5}"
    na "Yunwoo gets up,{w=.3} blinking his eyes.{w=.3} He looks like he just remembered something he wanted to tell me."
    hide y_smile
    show y_think
    with d5
    y "I think I saw Hye-na in the Hongik University area several days ago,{w=.3} at dawn."
    stop music fadeout 3
    p "You saw Hye-na at dawn?"
    na "I ponder what Yunwoo just told me."
    na "Hye-na told me that she works near the Daehangno area."
    na "She wouldn't have a reason to be in the Hongik University area so late."
    play music 'bgm/Jormungandr.opus' fadein 3
    p "Are you sure you didn't see some other girl who just looked like Hye-na?"
    na "I ask him,{w=.3} tilting my head sideways with a puzzled look."
    y "Well,{w=.3} I was not sure at first.{w=.3} But then I got a closer look,{w=.3} and it was definitely Hye-na."
    y "I was about to say hello to her,{w=.3} but she was with a well dressed man,{w=.3} so I just walked past her without saying anything.{w=.3} I don't think she saw me."
    p "A man in a suit…?{w=.3} She's going out with some guy?"
    na "I ask in an unconcerned tone."
    na "But as he continues to tell me what he saw,{w=.3} I feel something is wrong."
    y "But she looked awkward…,{w=.3} like a…,{w=.3} hmm…,{w=.3} what should I…."
    y "Actually,{w=.3} they had their arms together.{w=.3} And he looked a bit older."
    p "What?{w=1}"
    p "Are you sure?"
    y "Yes,{w=.3} I felt something strange."
    p "What was she wearing?"
    na "I ask Yunwoo,{w=.3} and turn to look at him with a concerned look on my face."
    y "It looked like…,{w=.3} well,{w=.3} it looked like she had gone clubbing that night."
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    p "{size=+10}No way!{w=.3} It's Hye-na!{w=0.3} She's not that sort of girl!{/size}"
    na "I can't believe it!{w=.3} Don't be ridiculous!"
    na "I just holler at him and turn my head away."
    na "That's bullshit!"
    na "What kind of person does he take my sister for?"
    y "Hey,{w=0.3} don't be upset with me.{w=0.3} I can't believe it either."
    y "I am telling you this because she is your sister."
    na "She was in a skimpy dress,{w=0.3} with an old guy?{w=0.3} Why?"
    na "No!{w=0.3} That's just bullshit.{w=0.3} Hye-na is not that sort of girl."
    na "This can't happen.{w=0.3} It mustn't happen."
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        show blink2  with d5
    na "I think it over,{w=0.3} blinking my eyes unconsciously."
    p "{size=+10}I gotta go see her!{/size}"
    na "I say as I turn my head to Yunwoo and stare at him."
    p "First of all,{w=0.3} I will find out where she works,{w=.3} and go visit her."
    na "While talking to him,{w=0.3} I continuously blink my eyes."
    p "Yunwoo,{w=0.3} you know many people that live in that area.{w=0.3} Please see if you can find people who saw her."
    y "But they don't know who she is."
    p "Hye-na is popular among guys,{w=0.3} and also she likes posting her photos on her blog.{w=0.3} So it will be easy to find her,{w=0.3} by using it."
    y "I don't think it will be as easy as you believe.{w=0.3} But I'll try anyway.{w=0.3} What are you going to do?"
    p "I will call Hye-na and go to where she works."
    p "Then,{w=0.3} after talking with her,{w=0.3} I will find out what she's doing,{w=0.3} and who she is meeting."
    p "And,{w=.3} if needed,{w=.3} I will follow her."
    y "OK.{w=.3} I hope that what we are assuming is wrong,{w=.3} and that she is fine."
    na "I hope the girl Yunwoo saw wasn't Hye-na."
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        hide blink2 with d5
    $ renpy.end_replay()
    if persistent.part08 is None:
        $ persistent.bgm08 = True
        $ persistent.bgm09 = True
        $ persistent.bgm += 2
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 8)
        $ achievement.progress('KNDW_OST', 9)
        if not persistent.blind is True:
            call unlocked
label hyena:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene room at sepia
        show h_smile_sepia at right
        show expression 'part_09_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part09]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part09]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    $ save_name = "Circumstances"
    $ show_quick_menu = True
    scene room
    show night
    with blind
    na "I'll work on Yunwoo's poster and pamphlet later."
    na "Right now,{w=.3} my concern is Hye-na."
    play sound 'se/dial1.opus'
    na "When I got back home,{w=.3} I called Hye-na immediately."
    na "If Hye-na still works at the cafe,{w=.3} she would still be working right now."
    play sound 'se/dial1.opus'
    pause 2
    h "Ga-yeon~!{w=.3} You finally called me!{w=.3} Did you see Yunwoo today?"
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    p "What?{w=1}"
    na "I was surprised by her asking me about Yunwoo.{w=.3} Flustered, I stay silent for a few seconds before answering her."
    p "Yes,{w=.3} he visited me today,{w=.3} and now that I'm back home,{w=.3} I'm calling you."
    na "Did Hye-na and Yunwoo plan to visit me on the same day?"
    na "Are both Hye-na and Yunwoo worried about me?{w=.3} Is that why they both visited me today?"
    na "I know you worry about me,{w=0.3} and I'm thankful for that,{w=0.3} but Hye-na."
    p "Are you busy now?"
    h "No,{w=0.3} I'm going to close the cafe soon.{w=0.3} Right now I'm filling the napkin boxes.{w=0.3} It's okay,{w=0.3} I'm available now."
    na "She answers in a relaxed tone."
    na "Judging by the way she is talking,{w=0.3} I can tell she is working."
    na "I chat with Hye-na for a few minutes before bringing up why I called."
    p "All right.{w=.3} So,{w=.3} where was it you said you were working?"
    h "Me?{w=.3} Daehangno district!{w=.3} It's a cafe – OO,{w=0.3} near Hyehwa Station on Line 4."
    h "Have you already forgotten?"
    p "Oh,{w=.3} sorry.{w=.3} My memory isn't as good as it used to be."
    h "Geez,{w=.3} that can't be!{w=.3} You're still young!"
    p "Yes,{w=.3} you're right.{w=.3} Anyway,{w=.3} can I visit you after work?"
    h "After work?{w=.3} Yes,{w=.3} sure,{w=.3} but why?{w=.3} What's wrong?"
    p "Nothing!{w=.3} Just thought we should go for a beer tonight.{w=.3} It's been so long since we've had a beer together."
    h "That sounds great.{w=.3} I'm looking forward to it."
    p "Okay,{w=.3} then I'll go over there now."
    h "Good!{w=.3} See you soon!"
    p "Okay,{w=.3} bye.{w=1}"
    play sound 'se/dialoff.opus'
    pause 1
    p "Hye-na,{w=.3} I believe in you."
    na "I whisper into the phone,{w=.3} even though Hye-na has already hung up."
    na "After putting the phone down,{w=.3} I think for a while about Hye-na,{w=.3} her privacy,{w=.3} her boyfriend and how she has been."
    na "When I meet Hye-na,{w=.3} I should talk to her casually."
    stop music fadeout 3
    na "Letting out a short sigh,{w=.3} I get up and prepare to go out."
    play music 'bgm/Nyx.opus' fadein 3
    scene hof at gray with blind
    na "My sister.{w=.5}"
    na "Hye-na.{w=.5}"
    na "What's going on with her…?{w=.5}"
    pause 1
    h "Ga-yeon~!"
    scene hof with blind
    na "I was absorbed in thought,{w=.3} sitting alone in the bar.{w=.3} Then,{w=.3} hearing Hye-na's voice,{w=.3} I turned to face her."
    show h_smile
    h "I'm sorry!{w=.3} The last customer didn't want to leave!"
    na "Hye-na waves at me,{w=.3} and comes over and sits at my table."
    p "No,{w=.3} no worries.{w=.3} Have a seat here."
    h "Hey,{w=.3} Ga-yeon,{w=.3} the interior design here is so cool,{w=.3} isn't it?"
    p "Yes,{w=.3} I was surprised at how amazing it is."
    h "I like it here.{w=.3} It looks posh and is not that noisy,{w=.3} unlike other places I've been."
    p "Yes,{w=.3} it seems cool."
    na "We chat a bit more about the pub."
    na "You know,{w=.3} Hye-na.{w=.3} You really do have a beautiful smile."
    hide h_smile
    show h_laugh
    with f
    h "It's been a really long time since we've had a drink together."
    p "Yeah,{w=.3} you're right.{w=.3} I feel great today."
    h "So,{w=.3} Ga-yeon,{w=.3} why can't you at least try to get a job?{w=.3} If you're out of work for too long,{w=.3} you will forget your training.{w=.3} Making it hard to get one."
    na "I swallow hard,{w=.3} and gasp listening to Hye-na's question."
    na "It's been two years since I became jobless."
    na "How much longer can I be isolated?"
    na "No,{w=.3} it's not isolation."
    na "I've just given up."
    na "So,{w=.3} could I start looking for another job again?"
    na "Is there anyone who would hire me?{w=.3} Is there anywhere I can work and belong?"
    pause 1
    na "Dropping my eyes,{w=.3} I hesitate to respond to Hye-na's question."
    na "Later,{w=.3} not now."
    na "So with that thought in mind,{w=.3} I raise my head and look Hye-na in the eye,{w=.3} and with a faint smile."
    p "You're right.{w=.3} I'm not going to remain jobless for much longer."
    p "I'll start looking for a job again.{w=.3} Will you root for me and wish me luck?"
    h "Of course!{w=.3} And I know that you've suffered greatly because of me!"
    p "No,{w=.3} don't talk like that!{w=.3} I would do anything for my adorable little sister,{w=.3} Hye-na."
    h "Eww….{w=.3} Ga-yeon,{w=.3} please stop,{w=.3} I got goose bumps."
    hide h_laugh
    with d5
    pause 1
    na "Laughing and giggling with glee,{w=.3} Hye-na and I keep talking for quite a while.{w=.3} We're both having a good time."
    na "We talk about all the things we have done and seen since we have been apart."
    na "Our parents living in their small town…."
    na "Our childhood memories…,"
    na "and hot celebrities."
    na "But now,{w=.3} I decide it's time to talk to her about what I came here for.{w=1}"
    p "Hye-na,{w=.3} do you have a steady boyfriend now?{w=.3} Shouldn't you be thinking about getting married soon?"
    show h_smile
    with d5
    h "Ga-yeon,{w=.3} how can I marry before you?{w=.3} I can't leave you alone!"
    na "Hye-na says,{w=.3} while emphatically shaking her hands from side to side,{w=.3} smiling broadly and flailing her hands in the air.{w=.3} It's clear she has been drinking and it has loosened her tongue a bit."
    p "Then you don't have a boyfriend?"
    na "I say to her while staring into her eyes.{w=.3} I slowly creep forward in my chair towards her."
    na "Then,{w=.3} she rolls her eyes for a moment,{w=.3} and opens her lips,{w=.3} gently gazing at me."
    hide h_smile
    show h_laugh
    with d5
    h "I{w=.3} {size=+3}want{/size}{w=.5} {size=+6}to{/size}{w=.5} {size=+9}have{/size}{w=.5} {size=+12}one!{/size}{w=.5}"
    hide h_laugh
    with d5
    play sound 'se/knocked.opus'
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    p "Hye-na?{w=.5} Hye-na!!"
    show drunken
    na "Hye-na drank too much.{w=.3} Suddenly,{w=.3} she just blacks out and collapses against the table."
    na "Did you drink that much,{w=.3} Hye-na?"
    na "I still have lots of questions to ask…."
    na "Well,{w=.3} I'd better call Yunwoo."
    na "With that thought in mind,{w=.3} I start to stand up.{w=.3} And,{w=.3} just then,{w=.3} I hear Hye-na's small voice."
    h "Not today.{w=.3} I'm so happy today as I got to see my sister."
    show bshock
    if persistent.epilepsy is True:
        with d
    else:
        with red
    h "Honey,{w=.3} you have to pay me first."
    h "I drank too much today.{w=.3} If I do fellatio today,{w=.3} I might throw up."
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    h "Do you like my body?{w=1}"
    scene black with d
    $ show_quick_menu = False
    centered "{size=+5}What are you saying now?{/size}"
    play sound 'se/flash.opus'
    scene room at gray with flash
    show h_laugh_gray
    $ show_quick_menu = True
    h "Surprise~! Ga-yeon! It's me!"
    stop sound
    play sound 'se/flash.opus'
    with flash
    h "I got paid. I just wanted to give you a present."
    hide h_laugh_gray
    show h_opinion_gray
    h "Look, you are smart. You can do anything! Don't let anyone bring you down!"
    stop sound
    play sound 'se/flash.opus'
    scene black
    show photo
    if persistent.epilepsy is True:
        with d5
    else:
        with flash
    scene black
    if persistent.epilepsy is True:
        with d5
    else:
        $ renpy.transition(flash)
    $ renpy.pause(.5, hard = True)
    show expression Text ('Choi Hye-na', style='extext')
    $ renpy.transition(Dissolve(3))
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(f3)
    $ renpy.pause(3, hard = True)
    stop music fadeout 3
    $ renpy.end_replay()
    if persistent.part09 is None:
        $ persistent.unlock_24 = True
        $ persistent.unlock_2 = True
        $ persistent.bgm10 = True
        $ persistent.bgm += 1
        $ persistent.gall += 2
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 9)
        $ achievement.progress('KNDW_ART', 9)
        $ achievement.progress('KNDW_OST', 10)
        $ achievement.grant('KNDW_DEMO')
        $ achievement.grant('KNDW_FRONTIER')
        if not persistent.blind is True:
            call unlocked
label tears:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        show slap_sepia
        show expression 'part_10_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part10]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part10]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    $ save_name = "Distortion"
    $ show_quick_menu = True
    scene room
    show night
    with blind
    play music 'bgm/Sigh day.opus' fadein 3
    na "Yunwoo came quickly,{w=.3} as soon as he received my call.{w=.3} And we took Hye-na back to my room via taxi.{w=.3} Once inside,{w=.3} Yunwoo carried her to my bed."
    p "Sorry for calling you at this late hour."
    show y_smile
    with d5
    y "No,{w=.3} don't worry.{w=.3} The concert had already ended when you called."
    p "But you must be so exhausted….{w=.3} Sorry for disturbing you."
    y "It's fine.{w=.3} Don't worry about me,{w=.3} Ga-yeon.{w=.3} You rest.{w=.3} You must be tired after walking around all day long."
    na "He says to me tenderly."
    p "Okay,{w=.3} I'm going to bed."
    y "Good.{w=.3} Then,{w=.3} good night.{w=.3} Bye."
    hide y_smile
    with d5
    na "He waves his hand briefly,{w=.3} then turns around and opens the door."
    na "Yunwoo,{w=.3} what am I supposed to do?"
    na "I thought to myself."
    na "My poor Hye-na….{w=.3} What should I do for her?"
    na "He gazes at me for a while with an apprehensive glance,{w=.3} then closes the door silently."
    scene despair
    with d3
    na "At that moment,{w=.3} I burst into tears."
    na "And I collapse on the ground,{w=.3} clasping the door handle."
    na "Don't go."
    na "I'm so exhausted and everything around me is just so hard."
    na "I feel like I'm falling into a bottomless pit that will never end."
    na "My whole body begins to shake,{w=.3} I'm trembling like a leaf."
    na "I start to sob with deep sorrow,{w=.3} covering my mouth with my hands."
    stop music fadeout 3
    na "I need you."
    play sound 'se/open.opus'
    scene post
    show night
    with d5
    pause 3
    play sound 'se/run.opus'
    na "And before I know it,{w=.3} I run out of my room into the hallway."
    na "There is Yunwoo walking down the stairs."
    na "I rush towards him,{w=.3} and hug him from behind."
    scene lean_gall
    show night
    with d3
    pause 1
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('"Don\'t look back."', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(dl)
    $ renpy.pause(5, hard = True)
    show expression Text ('"Just stay like this for a minute,{w=.3} please."', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(dl)
    $ renpy.pause(5, hard = True)
    play music 'bgm/Sigh day.opus' fadein 3
    scene room with dl
    play sound 'se/boiling.opus'
    na "I lift the lid off the pot,{w=.3} steam rises in a large cloud.{w=.3} The contents of the pot are bubbling and boiling furiously."
    na "Using a fist-sized ladle,{w=.3} hung on the shelf next to my silvery sink,{w=.3} I scoop our a bit of the seaweed soup.{w=.3} The soup is a beautiful black and green color."
    na "I blow carefully over the soup in the ladle to cool it,{w=.3} and then taste it."
    na "It tastes just right."
    play sound 'se/washing.opus'
    na "I wash the ladle in the sink,{w=.3} hang it up back on the shelf,{w=.3} and then,{w=.3} cover the pot."
    na "I blink several times to keep tears from coming."
    na "I sigh for a moment,{w=.3} and then turn around to wake Hye-na up."
    show h_laugh
    with d5
    h "Thanks,{w=.3} Ga-yeon!"
    hide h_laugh
    with d5
    na "She says in a cheerful voice.{w=.3} Then Hye-na picks up the spoon and chopsticks."
    na "I gaze at Hye-na eating her meal hungrily."
    na "Then I become sad again,{w=.3} thinking about this bright girl….{w=0.3}"
    na "It's all because of me.{w=0.3} I shouldn't have quit the hospital."
    na "No…,{w=.3} I shouldn't have loved that guy in the hospital."
    show h_smile
    with d5
    h "Ga-yeon,{w=.3} what are you doing?"
    p "Oh,{w=.3} sorry.{w=.3} I was just thinking about something."
    na "Tears well up in my eyes."
    na "To avoid her eyes,{w=.3} I look up the ceiling and blink several times to calm myself down."
    p "Hye-na.{w=0.5}"
    h "Um?{w=.3} Why are you?"
    na "It seems she doesn't remember what she said last night."
    p "Who is that guy you called honey last night?"
    h "Honey?{w=.3} What do you…, {w=.3}{nw}"
    hide h_smile
    show h_question
    extend "mean…?"
    na "She speaks vaguely,{w=.3} with a slightly startled face."
    p "Don't even think about lying to me."
    p "I know you met him in Hongik University area.{w=.3} Who's that guy?"
    na "Making a serious face,{w=.3} I ask her again strongly."
    hide h_question
    show h_poker
    with d5
    h "I don't understand what you're saying now….{w=.3} What's wrong with you,{w=.3} Ga-yeon…."
    na "She asks back,{w=.3} but with a quivering voice.{w=.3} Then,{w=.3} she slowly puts down her spoon and chopsticks and turns her head."
    pause 1
    p "{size=+10}Answer me!{w=.3} Who is that guy!?{/size}{nw}"
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    extend "{w=.5}{nw}"
    hide h_poker
    show h_question
    with shock
    na "I loudly browbeat Hye-na and she cowers in fear and is surprised by my intense interrogation."
    na "With anger,{w=.3} I lash out at her."
    p "{size=+10}What the hell are you doing these days?!{/size}{nw}"
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    extend "{w=.5}{nw}"
    hide h_question
    show h_tear
    with shock
    h "{size=+5}Then,{w=.3} what was I supposed to do?!{/size}"
    p "…!{w=1}"
    na "She yells out in a tearful voice."
    na "Then she continues,{w=.3} letting out her pent-up anger."
    h "It's been two years since you quit your job!"
    h "I know you've continued to send money to Mom and Dad and had to stop putting money away into savings."
    h "Now,{w=.3} I had to do whatever I could to earn money.{w=.3} So you could do whatever you wanted to do."
    h "But,{w=.3} I was going to stop it when you get a job again!"
    h "But there really isn't much work I can do!{w=.3} Unlike you,{w=.3} Ga-yeon!"
    h "To be honest,{w=.3} you may remember that I was working as a waitress at the cafe.{w=.3} But that was so long ago,{w=.3} I hardly remember working there."
    if not _preferences.language == 'Korean' and not _preferences.language == 'Chinese':
        h "When you didn't have a job for so long,{w=.3} I got a job as a karaoke hostess.{w=.3} But it's been a long time since I've been a karaoke hostess too."
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    p "What?{w=.3} A hostess?!"
    na "I'm just so shocked by her sudden confession.{w=.3} My sister is a hostess?"
    na "No – it's just bullshit.{w=.3} I don't believe it.{w=.3} Why….{w=.3} Why is this happening to me?"
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        show blink2  with d5
    na "Feeling dizzy,{w=.3} I blink my eyes erratically."
    na "I'm speechless….{w=.3} Hye-na continues her explanations…."
    h "The basic pay is good,{w=.3} and that guy comes to see me whenever I work there.{w=.3} And he's a tipper."
    h "He said he likes me.{w=.3} So now,{w=.3} we go out together.{w=.3} We go to the movies and do many other things together just like any ordinary couple."
    h "And because he asked me to,{w=.3} I just quit working at the Karaoke.{w=.3} Now he pays me regularly to be his companion."
    h "Is what I'm doing really so bad?{w=.3} I've met a nice guy who likes me,{w=.3} and he gives me money."
    h "Ga-yeon,{w=.3} you've always been so nice.{w=.3} Even when we were just kids."
    if not _preferences.language == 'Korean' and not _preferences.language == 'Chinese':
        h "Do you remember that?{w=.3} When you were still in middle school,{w=.3} you always gave me things,{w=.3} paid for with your part-time work.{w=.3} When Dad,{w=.3} who was sick,{w=.3} couldn't…."
    h "You even paid my tuition for all four years of university,{w=.3} even though you couldn't really afford it!"
    h "Ga-yeon,{w=.3} I just wanted to help you now!"
    na "I've been silently listening to Hye-na up to now.{w=.3} But,{w=.3} with her last comment about wanting to help me,{w=.3} I shout at her…."
    p "Did you think I would praise you if you did that sort of thing for me?!"
    h "No,{w=.3} I didn't mean that!{w=.3} I just….{w=.3} I just didn't want to get caught by you!"
    na "After her answer,{w=.3} tears fill my eyes."
    na "Continuing to blink unconsciously,{w=.3} I keep yelling at her."
    p "What?!{w=.3} You shouldn't talk like that,{w=.3} Hye-na!"
    p "And,{w=.3} what are you going to do with him even if he does like you?!"
    p "So is he going to divorce his wife?"
    p "No,{w=.3} he won't.{w=.3} That bastard!{w=.3} You know those bastards are all alike!{w=.3} He will dump you if he gets tired of you!"
    h "How could you talk like that!{w=.3} You don't know anything about him!"
    h "He loves me!"
    h "Oh- you know better than me,{w=.3} because you used to date a married man!"
    hide blink2
    p "…!"
    p "{size=+10}You're such a bitch!!{/size}{w=.5}{nw}"
    stop music fadeout 3
    hide h_tear
    play sound 'se/att.opus'
    show slap
    with shock2
    pause 3
    scene black
    $ renpy.transition(d)
    $ renpy.pause(1, hard = True)
    show expression Text ('Choi Ga-yeon', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(dl)
    $ renpy.pause(5, hard = True)
    show expression Text ('You\'re so terrible.', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(dl)
    $ renpy.pause(5, hard = True)
    $ renpy.end_replay()
    if persistent.part10 is None:
        $ persistent.unlock_3 = True
        $ persistent.unlock_4 = True
        $ persistent.unlock_23 = True
        $ persistent.gall += 3
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 10)
        $ achievement.progress('KNDW_ART', 12)
        if not persistent.blind is True:
            call unlocked
label mono3:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene room at sepia
        show gb_sepia at right
        show expression 'part_11_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part11]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part11]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    $ save_name = "Monologue"
    $ show_quick_menu = True
    scene room with blind
    play music 'bgm/Unknown mist.opus' fadein 3
    na "Sitting at the table,{w=.3} I look,{w=.3} with vacant eyes at Hye-na's still warm bowl of rice."
    na "What have I done?"
    na "Hye-na did that just for me."
    na "Should I have told her I'm sorry?"
    na "No – the situation just went wrong."
    na "Her decision and attitude is wrong."
    na "But why did I slap her?"
    na "Because of what Hye-na said about him?"
    na "Or because I worry she's dating a married guy?"
    scene black with d3
    $ show_quick_menu = False
    centered "No – both are wrong."
    centered "Ga-yeon,{w=.3} you are just jealous of Hye-na."
    centered "No….{w=.3} Then why?{w=.3} For what reason?{w=.3}"
    centered "I just love her so,{w=.3} so, so much?"
    centered "You failed in love,{w=.3} and you screwed up your own life."
    centered "I just didn't want my sister to go through\nthat terrible hurt and pain which I had."
    centered "But is that all?"
    centered "What if her relationship with that guy works out?"
    centered "You failed in love in spite of your pathetic effort."
    centered "But,{w=.3} what about your sister?"
    centered "She is loved.{w=.3} Even though she is taking money\nfrom him without doing anything."
    centered "However,{w=.3} look at you - you're such a recluse in a tiny room.{w=1}"
    centered "No – this is just a delusion."
    centered "I'm never jealous of my sister."
    centered "She's a really nice sister.{w=.3} She was so worried about me\nthat she did things that she never would have otherwise."
    centered "She has probably suffered a lot,{w=.3} both physically and mentally."
    centered "I'm sorry Hye-na."
    centered "It's all because of me - because I'm useless."
label mono4:
    pause 3
    show imf
    show circle
    with d
    $ show_quick_menu = True
    na "When we were young,{w=.3} the IMF crisis shook the very foundation of the Korean economy."
    na "Our father was fired from his job.{w=.3} He tried to get another job,{w=.3} but he couldn't."
    na "But fortunately,{w=.3} our mother,{w=.3} who was a stay-at-home mom in the marriage up until then,{w=.3} but who was a teacher before she married father,{w=.3} began work as a teacher in a small kindergarten."
    na "Two years later,{w=.3} our home situation got better,{w=.3} and our father tried to set up a new business."
    na "But he failed.{w=.3} Then,{w=.3} even worse,{w=.3} was that after the business failed,{w=.3} father had a car accident,{w=.3} and he became almost unable to move."
    scene delivery with d5
    na "So I wanted to help our parents."
    na "That's why I decided to earn money."
    na "I kept asking Dad to buy a bicycle for me for a couple of days,{w=.3} and finally,{w=.3} I got it."
    na "And every early morning,{w=.3} I left home,{w=.3} riding a bicycle.{w=.3} Of course,{w=.3} I used to tell my parents I was going to work out."
    na "But in reality,{w=.3} I went to a nearby newspaper agency.{w=.3} I got newspapers and delivered them throughout my delivery area."
    scene serving with d5
    na "After I entered high school,{w=.3} I started working part-time in a restaurant on weekends."
    na "During a vacation,{w=.3} I worked almost all day long,{w=.3} from opening to closing time,{w=.3} and had only one day off a week."
    na "It was really,{w=.3} really hard.{w=.3} But I was still happy because I could earn money."
    na "And above all,{w=.3} I had to do that for my family."
    scene black
    show diary05:
        zoom .8 truecenter
    show circle
    with d5
    na "However,{w=.3} in that period,{w=.3} I found my dream and also fell in love,{w=.3} just like many other teenage girls."
    na "Just looking at him would set my heart racing and throbbing."
    na "I became flustered and my face turned red whenever he spoke to me."
    na "Although I couldn't confess my love for him,{w=.3} I was still happy.{w=.3} And like a fool,{w=.3} I felt that was enough."
    scene black with d5
    $ show_quick_menu = False
    centered "Time went by,{w=.3} and my first love went into the military.{w=.3}\nAnd I entered university."
    centered "Actually,{w=.3} I couldn't make up my mind about which major I should choose.{w=.3} But,{w=.3} I took my mother's advice and chose to major in Public Health Administration."
    centered "Though I was unable to graduate because of financial difficulties,{w=.3} fortunately,{w=.3} I got a job at a hospital without finishing school."
    centered "And in the hospital,{w=.3} I met a guy and fell in love with him."
    stop music fadeout 3
    $ renpy.end_replay()
    if persistent.part11 is None:
        $ persistent.con02 = True
        $ persistent.con07 = True
        $ persistent.unlock_5 = True
        $ persistent.unlock_6 = True
        $ persistent.unlock_26 = True
        $ persistent.con += 2
        $ persistent.gall += 3
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 11)
        $ achievement.progress('KNDW_CONCEPT', 5)
        $ achievement.progress('KNDW_ART', 15)
        if not persistent.blind is True:
            call unlocked
label hospital:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene hospital at sepia
        show dr_sepia at right
        show expression 'part_12_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part12]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part12]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    $ save_name = "Broken mind"
    $ show_quick_menu = True
    scene hospital with blind
    $ show_quick_menu = True
    play music 'bgm/Lush garden.opus' fadein 3
    na "The hospital where I worked was quite small,{w=.3} but it was run by a very capable director."
    na "At first,{w=.3} I was only given reception and administrative duties."
    na "Then one day,{w=.3} the Director suggested that I try to get a Hospital Coordinator Certificate."
    na "The Director told me that he thought I had a natural aptitude for that work."
    na "So I thought it over seriously,{w=.3} and,{w=.3} after thinking about it for a long time,{w=.3} I decided to try."
    na "So while working in the hospital,{w=.3} I also took the online course in Hospital Coordination.{w=.3} I studied hard.{w=.3} And finally,{w=.3} I passed the exam."
    na "After that,{w=.3} my contract was renewed,{w=.3} and I started working as a Hospital Coordinator."
    na "I earned more money than before,{w=.3} and the work was much more rewarding."
    na "And one day….{w=.3} A new doctor,{w=.3} the Director's brother-in-law,{w=.3} started working in the hospital."
    show dr
    with d5
    na "When I first saw him,{w=.3} I was very surprised."
    na "Because he looked just like my first love."
    na "Even his personality was similar.{w=.3} So he seemed even more mysterious to me."
    na "It brought back the old feelings I felt during my high-school years,{w=.3} and even before I realized it,{w=.3} I fell in love with him."
    stop music fadeout 3
    na "I was very happy,{w=.3} when I worked with him."
    na "But at the same time,{w=.3} it made me hurt."
    na "He was the Director's brother-in-law – in other words,{w=.3} he was a married man."
    play music 'bgm/Jormungandr.opus' fadein 3
    na "I felt jealous of his wife whenever she came to the hospital and had a conversation with him."
    na "I hoped he recognized my love."
    na "So I made a chocolate to give him on his birthday."
    scene black
    show gift at top
    with d5
    na "On that day,{w=.3} the hospital had a party.{w=.3} And after dinner,{w=.3} he said he was going to take me home."
    na "I thought I was so lucky,{w=.3} because I was just going to give him the chocolate before parting."
    na "Before getting out of his car in front of my house where I still live,{w=.3} I gave it to him."
    na "I don't remember what I said because I was drunk."
    hide gift
    show diary08:
        zoom .8 truecenter
    show circle
    with d5
    na "The only thing I clearly remember is that he told me that he married his wife because of the Director's influential background."
    na "And that he said he was NOT on good terms with her."
    na "And I frankly confessed my feeling towards him."
    na "And I hugged him,{w=.3} and we made love."
    na "And after that,{w=.3} we became secret lovers."
    na "He worked a normal daytime shift except for one night shift per week,{w=.3} and since I worked the night shift at the hospital all week,{w=.3} the only time we could date was that day he worked the night shift."
    na "During those few free hours,{w=.3} we talked about many things."
    na "And sometimes,{w=.3} we made love passionately."
    na "Of course I also felt guilty about what I was doing to his wife."
    na "However,{w=.3} much bigger and stronger feelings of love overwhelmed me at that time,{w=.3} and I couldn't stop."
    na "As time went on,{w=.3} I felt like we were married."
    na "But this happiness didn't last long."
    scene hospital with d3
    stop music fadeout 3
    na "One day,{w=.3} the Director called me into his office."
    na "He turned his laptop to me and,{w=.3} with a serious face,{w=.3} started a video playing."
    na "On the monitor,{w=.3} a video in which he and I were having sex played."
    scene black with d3
    $ show_quick_menu = False
    play music 'bgm/Sigh day.opus' fadein 3
    centered "Yes,{w=.3} our love was an affair."
    centered "I was such a whore who tempted a married man."
    centered "That was a reality."
    centered "Listening to the director of the hospital,{w=.3} I realized."
    centered "He never said I did anything wrong."
    centered "I was fired."
    centered "Since then,{w=.3} I haven't seen him,{w=.3} I haven't even tried."
    centered "Because my heart was broken.{w=.3} I was badly hurt,{w=.3}\nbut I couldn't do anything about it."
    centered "But after a while,{w=.3} I picked myself up and tried to get a job again."
    centered "I had a career in the hospital,{w=.3} but I didn't want to work in a hospital anymore.{w=.3}\nSo I tried to re-enter the restaurant business where I had\nworked before for a little while and where I dreamed of working again."
    centered "However,{w=.3} even though I tried to get a restaurant job for over a year,{w=.3}\nno matter how many doors I knocked on,{w=.3} no one accepted me."
    centered "The reason was that I had no recent experience in that field."
    centered "I also tried to find another job in other fields,{w=.3} but it was fruitless."
    centered "I even tried to find part-time work,{w=.3} but I was continuously rejected."
    centered "So,{w=.3} I just gave up."
    $ renpy.end_replay()
    if persistent.part12 is None:
        $ persistent.doctor = True
        $ persistent.char += 1
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 12)
        $ achievement.progress('KNDW_IDENTIFY', 6)
        if not persistent.blind is True:
            call unlocked
label life:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene room at sepia
        show gb_sepia at right
        show expression 'part_13_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part13]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part13]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    scene room
    show night
    with blind
    $ save_name = "How alive are you?"
    $ show_quick_menu = True
    na "Sitting in front of the bed,{w=.3} I repetitively pick up the phone,{w=.3} and then put it back down."
    na "I want to talk with Hye-na,{w=.3} but have no idea what to say."
    na "I try to text her and write down a message.{w=.3} But soon,{w=.3} I just stop,{w=.3} and delete it,{w=.3} again and again."
    na "I don't know what I'm supposed to do…."
    na "I just put the cell phone down,{w=.3} and burrow down into the bed sheet."
    pause 1
    play sound 'se/bell.opus'
    pause 1
    na "After a moment,{w=.3} the doorbell rings and I raise my head again."
    na "Is that Yunwoo?{w=.3} But he didn't say he was going to come over here."
    na "Is he here because of the pamphlet thing?{w=.3} No….{w=.3} I've still got four days."
    na "I get up and walk towards the door."
    p "Who's that?{w=.5}"
    na "There's no answer."
    na "Oh,{w=.3} you're such an idiot.{w=.3} There's an intercom."
    na "I turn my head to the intercom on the right-hand wall."
    play sound 'se/interphone.opus'
    na "On the monitor,{w=.3} there is Hye-na biting her right thumb."
    na "Well….{w=.3} She shows more maturity than I have."
    na "I smile thinking about that."
    play sound 'se/open.opus'
    na "But I put on a serious face when I open the door."
    na "The door suddenly flies open….{w=.3} Hye-na,{w=.3} surprised at the door so suddenly opening,{w=.3} steps back,{w=.3} startled!"
    show h_poker
    with d5
    h "Uh…,{w=.3} may I come in?"
    na "Hye-na says,{w=.3} wearing an awkward face.{w=.3} She is holding a bag of bread in her left hand."
    na "I chuckle inwardly.{w=.3} You brought bread,{w=.3} again?"
    na "Okay,{w=.3} I take back what I've said about you being more grown up than me."
    hide h_poker
    with d5
    na "After letting Hye-na in,{w=.3} and closing the door,{w=.3} I turn around and face her,{w=.3} making a listless face."
    na "Then I sit by the desk and gaze at her,{w=.3} and speak in calm tones."
    p "Come on in and sit down."
    na "Hye-na warily enters the room and sits opposite me,{w=.3} near the desk."
    na "She casts a furtive glance at me for a moment,{w=.3} then,{w=.3} puts the bag of bread on the desk."
    show h_poker
    with d5
    h "Will you have some bread?{w=1}"
    pause 1
    p "{size=+5}Pffftttt!!{/size}"
    p "{size=+10}Ha-ha ha!!{/size}"
    hide h_poker
    show h_question
    with d5
    h "Ga-yeon…?{w=1}"
    p "{size=+10}Mwahaha!!{/size}"
    na "I try to stifle a laugh,{w=.3} but I can't any more."
    na "I start laughing my head off,{w=.3} like a crazy person."
    na "What's so funny?"
    na "I laugh heartily,{w=.3} then gaze at her."
    p "Hye-na.{w=1}"
    hide h_question
    show h_poker
    with d5
    h "Yes….{w=1}"
    na "I get up,{w=.3} and walk towards her and sit right next to her."
    na "Closing my eyes,{w=.3} I cuddle her close."
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('"I\'m sorry,{w=.3} Hye-na."', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('"Did it hurt a lot?"', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('"I\'m so,{w=.3} so sorry I slapped your face."', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('"And I didn\'t care for you."', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('"And I didn\'t say sorry before you."', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    pause 1
    $ show_quick_menu = False
    centered "She and I cry for a long time,{w=.3} but say nothing."
    centered "We just cry and cry,{w=.3} but with no words between us."
    stop music fadeout 3
    scene rooml
    with d3
    $ show_quick_menu = True
    play music 'bgm/Lush garden.opus' fadein 3
    p "My god!{w=.3} Are you serious?!"
    na "I ask Hye-na,{w=.3} with my mouth full of sesame bread."
    show h_poker
    with d5
    h "Of course!{w=.3} I was completely out of control before!"
    h "Hey old guys with beer bellies are not my type at all."
    h "I told him I can't meet him anymore because my sister found out about us."
    h "And I called the manager of the cafe where I previously worked,{w=.3} and he gave me my old job back as well."
    p "It sounds great."
    na "I'm greatly relieved at her news."
    na "Of course I was worried about her,{w=.3} but I felt much pressure too because she decided to date that guy and take his money just because of me."
    na "But blessedly,{w=.3} now she is back on track."
    na "While I'm thinking about this,{w=.3} Hye-na cheerfully says…."
    hide h_poker
    show h_opinion
    with d5
    h "So,{w=.3} Ga-yeon!{w=.3} Now go find a job and earn lots and lots of money!{w=.3} Okay?"
    h "Don't get me wrong – I don't mean to pressure you.{w=.3} Don't push yourself!"
    h "Take it easy,{w=.3} Ga-yeon.{w=.3} Things will change.{w=.3} Before,{w=.3} you were just too nervous because of a lot of things."
    na "Her words don't really make me feel much better,{w=.3} but with her warm-hearted tone,{w=.3} I can't help but respond to her with a big smile."
    p "Okay,{w=.3} I will try hard."
    hide h_opinion
    show h_smile
    with d5
    na "We start eating bread,{w=.3} smiling and laughing."
    h "Oh,{w=.3} Ga-yeon,{w=.3} I've got something to ask you."
    p "Uh-huh?"
    h "So,{w=.3} you are not going to make out with Yunwoo?"
    p "What…?{w=.3} What do you mean?"
    na "With her sudden question about Yunwoo,{w=.3} I feel my cheeks flush red."
    h "I know your first love was Yunwoo."
    p "Hey,{w=.3} why are you talking about him now?"
    na "I brusquely respond,{w=.3} turning my head to stare at her."
    h "Hmmm~.{w=1}"
    na "Then she starts gazing at me,{w=.3} with a smirk on her face."
    p "What!{w=.3} What's wrong with you!{w=.3} You're going to be in trouble if you keep this up."
    hide h_smile
    show h_laugh
    with d5
    h "I'm going to call Yunwoo~!"
    p "Oh,{w=.3} come on!{w=.3} See what time it is now!"
    na "I scream out."
    h "Come on,{w=.3} what's wrong with that?{w=.3} I will just ask him to grab a beer with us to celebrate your new start!"
    p "What?!{w=.3} Don't!{w=.3} Hye-na!{w=.3} Don't do that!"
    na "I try to stop her,{w=.3} but fail."
    p "Geez!{w=.3} How come you are that strong?!"
    h "Give up!{w=.3} You can't beat me in physical strength!"
    scene rooml
    if persistent.epilepsy is True:
        with d3
    else:
        with f3
    show y_smile at left
    with d5
    y "Enjoy it!{w=.3} But don't drink so much that you get drunk."
    hide y_smile
    show y_smile_gray at left
    show h_laugh at right
    with d5
    h "Ha~!{w=.3} Soooo goooood!!"
    stop music fadeout 3
    p "I'm sorry,{w=.3} Yunwoo.{w=.3} Aren't you tired?{w=.3} The concert just ended."
    hide h_laugh
    hide y_smile_gray
    show y_smile at left
    show h_smile_gray at right
    with d5
    y "Don't worry.{w=.3} This is actually better."
    p "….{w=1}"
    hide y_smile
    hide h_smile_gray
    show y_smile_gray at left
    show h_laugh at right
    with d5
    h "Yunwoo,{w=.3} have a drink~!"
    play music 'bgm/CCCanon.opus' fadein 3
    hide h_laugh
    show h_laugh_gray at right
    with d5
    na "While we are drinking,{w=.3} it's getting dark."
    na "I wish Eunyoung was with us.{w=.3} But it's alright.{w=.3} I'm just happy to spend time with you two."
    na "After several glasses of beer and lots of conversation,{w=.3} Hye-na says."
    hide h_laugh_gray
    show h_opinion at right
    with d5
    h "You know what?{w=.3} I think sometimes things are unfair."
    p "What do you mean?"
    h "Think about this – our futures have been already decided from birth."
    h "Parents' job,{w=.3} the economic situation,{w=.3} and such things have an influence on children."
    p "Yes,{w=.3} it's true.{w=.3} So people say,{w=.3} a rich family leads a rich life for three generations,{w=.3} unless they become bankrupt."
    na "And she's right to some extent,{w=.3} I partially agree with her.{w=.3} But on the other hand,{w=.3} not totally and I say to her."
    p "But we can't blame parents."
    p "Because,{w=.3} in their own way,{w=.3} they have also struggled hard to survive and live well."
    na "Then,{w=.3} Yunwoo begins to tell his opinion."
    hide h_opinion
    hide y_smile_gray
    show h_opinion_gray at right
    show y_think at left
    with d5
    y "I think,{w=.3} this can't be solved because we are living in a capitalistic society."
    y "It is the brutal reality that the poor can't help but keep living in poverty."
    p "But anyway,{w=.3} it can't be helped."
    na "It can't be helped.{w=.3} I think in most cases,{w=.3} that's just the way things are."
    na "Yunwoo nods slightly,{w=.3} and continues to speak."
    y "Nobody wants to be poor in the world.{w=.3} But we live in a world where it's nearly impossible to escape from poverty just by trying."
    y "No matter how hard and desperately people struggle to overcome poverty,{w=.3} there's almost no chance that they could change their lives."
    y "In this society,{w=.3} I think,{w=.3} a reversal of life is almost impossible - because,{w=.3} there's a huge difference not only in the start point,{w=.3} but also in the way of running."
    p "Well,{w=.3} because rich children have a wider opportunity for a better education in better environment….{w=.3} No wonder there is a difference."
    y "Once when I was young,{w=.3} several friends of mine came to my home."
    y "And the next day,{w=.3} when I went to school,{w=.3} I saw them sitting around a desk and they were talking about the size of my house."
    y "Why were such young children giggling and laughing at that sort of stuff like their friend's house size?"
    y "They knew – the competition had already begun."
    y "And they already know full well that I would never be richer than they are,{w=.3} no matter how many years pass and it would be that way forever."
    y "Even back then,{w=.3} children went to a private educational institute in addition to going to public school.{w=.3} Some of them received private tutoring as well."
    y "But me?{w=.3} It was impossible for me to receive private tutoring because my parents couldn't afford it.{w=.3} In fact,{w=.3} my family was so poor that I had to go to work during my early school years to help out."
    y "And,{w=.3} since I was so young and couldn't do any skilled work,{w=.3} I had to do very menial jobs,{w=.3} like handing out flyers to strangers on the street."
    y "The amount of schooling I got was less than those around me.{w=.3} Through the years,{w=.3} my friends begin to drift away because the \"School records\" difference between us gets bigger and bigger."
    if not _preferences.language == 'Korean' and not _preferences.language == 'Chinese':
        y "Soon the number of people I was friends with became limited."
    y "In that way,{w=.3} I and other children like me have grown up,{w=.3} directly feeling the fear of capitalism."
    hide y_think
    hide h_opinion_gray
    show y_think_gray at left
    show h_poker at right
    with d5
    h "Oh,{w=.3} how sad it is…."
    na "Hye-na quietly mumbles to herself."
    hide h_poker
    hide y_think_gray
    show y_think at left
    show h_poker_gray at right
    with d5
    y "I think capitalism has a number of errors.{w=.3} Now,{w=.3} many people are crying out that capitalism has failed."
    y "From now on,{w=.3} whether people figure out how to change this society will determine the future."
    y "If the society doesn't change,{w=.3} then everything will go the way it always has."
    hide y_think
    hide h_poker_gray
    show y_think_gray at left
    show h_poker at right
    with d5
    h "Then,{w=.3} do you mean no matter how hard we try,{w=.3} there are limits?"
    na "Hye-na becomes depressed."
    hide y_think_gray
    hide h_poker
    show y_think at left
    show h_poker_gray at right
    y "Not everything is like that,{w=.3} but obviously,{w=.3} some things are.{w=.3} Even if we don't want to accept it – yes,{w=.3} there are indeed.{w=.3} You already know that,{w=.3} Hye-na."
    hide y_think
    hide h_poker_gray
    with d5
    na "For a long time,{w=.3} we discussed our society."
    na "Heaps and heaps of problems dot our society,{w=.3} like a thin,{w=.3} but invisible spider web."
    na "Blind spots of capitalism and history of our country,{w=.3} South Korea."
    na "From the independence,{w=.3} to division of territory,{w=.3} miracle on the Han River,{w=.3} IMF crisis,{w=.3} and numerous other events,{w=.3} big and small,{w=.3} have happened throughout our history until today."
    na "What we know is only a part of that great history,{w=.3} and even it would not be correct."
    na "But we just interpreted those periods in our own way and talked about it as if we were discussing things of minor importance."
    na "After a while,{w=.3} we lose track of the topic,{w=.3} and we stop talking as we realized we went too far."
    pause .5
    na "Then,{w=.3} Hye-na changes the topic and asks Yunwoo."
    show h_poker at right
    with d5
    h "By the way,{w=.3} why did you choose music?{w=.3} I heard only a few people earn their living by playing music."
    hide h_poker
    show y_think at left
    show h_poker_gray at right
    with d5
    y "Well,{w=.3} I thought the only thing I can do well was just music."
    y "I didn't study hard when I was a student,{w=.3} and I thought there's nothing I could do better than this."
    y "That's why I have done this practically all my life."
    y "Without Eunyoung and Ga-yeon,{w=.3} I would probably have given up long ago.{w=.3} And I might have been a career soldier or just a manual laborer."
    hide y_think
    show y_smile at left
    with d5
    na "Having said that,{w=.3} Yunwoo looks at me."
    p "Me?{w=.3} What did I do for you?"
    na "I become bemused.{w=.3} What does he mean he would have given up without me?"
    y "My parents passed away,{w=.3} and my sister,{w=.3} Eunyoung,{w=.3} and I lived together and I supported both of us as well as I could."
    y "It was so hard for me to pay my parents' debt with the small amount of money I got from the local government as a subsistence allowance."
    y "So I worked part-time every single day,{w=.3} because I didn't want Eunyoung to worry about not having enough money."
    na "I focus on what he's saying,{w=.3} nodding my head."
    y "One day,{w=.3} I thought I just wanted to die."
    hide h_poker_gray
    show h_question_gray at right
    with d5
    p "…!{w=1}"
    na "His words make Hye-na's and my face harden."
    na "This is so shocking.{w=.3} How could he talk like this,{w=.3} as if it's not really him that he's talking about.{w=.3} That makes his confession so much more shocking."
    y "I thought there was no way to escape from poverty."
    hide h_question_gray
    show h_poker_gray at right
    with d5
    y "Can you imagine?{w=.3} A subsistence allowance was paid to my account,{w=.3} and very soon,{w=.3} the creditors withdrew all of it."
    y "I was barely making a living by working part-time,{w=.3} but the situation around me was just so harsh."
    na "I had never thought he was in that much trouble.{w=.3} Why didn't I recognize he was suffering,{w=.3} and even wanted to kill himself."
    y "During class,{w=.3} I couldn't stand that heaviness inside me.{w=.3} So I just grabbed my bass and note,{w=.3} then,{w=.3} went out to the school playground."
    y "Sitting on a bench,{w=.3} I was playing the bass and writing music."
    y "And all of a sudden,{w=.3} Choi Ga-yeon,{w=.3} you were standing in front of me."
    hide h_poker_gray
    show h_smile_gray at right
    with d5
    p "Do you mean the day I followed you for the first time?"
    na "I ask him,{w=.3} recalling the old day."
    y "Yes,{w=.3} right.{w=.3} You sat by me,{w=.3} and looked at my music curiously."
    y "You know,{w=.3} it was great having you -the best student in the whole school- take an interest in my music writing."
    na "Agreeing with what I'm saying,{w=.3} he nods to me and keeps talking,{w=.3} lost in memories."
    y "Oh,{w=.3} do you also remember that?{w=.3} You told me I had a good talent in writing,{w=.3} looking at my lyrics."
    y "So I started playing the bass,{w=.3} and we sang a song together.{w=.3} Do you remember?"
    p "Of course,{w=.3} I do!{w=.3} You made me sing."
    na "I miss talking about the old days from time to time,{w=.3} I reply,{w=.3} slapping my knee."
    y "Then several days later,{w=.3} you took Eunyoung home."
    y "From then on,{w=.3} Eunyoung was your good friend.{w=.3} She got along well with Hye-na,{w=.3} as well."
    na "After saying that,{w=.3} Yunwoo looks at Hye-na.{w=.3} She responds with a smile,{w=.3} and says to Yunwoo."
    hide y_smile
    hide h_smile_gray
    show y_smile_gray at left
    show h_laugh at right
    with d5
    h "Yeah.{w=.3} Eunyoung was really nice to me."
    na "Yunwoo turns his head to me again,{w=.3} and continues."
    hide h_laugh
    hide y_smile_gray
    show y_smile at left
    show h_smile_gray at right
    with d5
    y "Ga-yeon,{w=.3} you,{w=.3} at that time,{w=.3} showed me that Eunyoung and I could survive in this fierce society."
    p "What?{w=.3} No,{w=.3} I did nothing for you."
    na "Though I'm inwardly pleased,{w=.3} I just speak brusquely."
    y "Also when I was worrying about military service,{w=.3} you told me you were going to take good care of Eunyoung.{w=.3} That's why I could enter the army at ease."
    y "Ga-yeon,{w=.3} remember this - my sister and I owe our lives to you."
    p "Bullshit."
    na "I am embarrassed."
    y "I also didn't expect I could earn money in music."
    y "However,{w=.3} these days,{w=.3} I think it would be possible."
    p "You've got confidence?"
    y "Well,{w=.3} I think something becomes clearer."
    y "I'm not 100%% sure for now,{w=.3} but….{w=.3} Yes,{w=.3} I feel something has changed in my mind."
    p "Wow,{w=.3} you are going to be Korea's top band!"
    na "I say to him,{w=.3} with a sincere heart."
    na "Then,{w=.3} Hye-na who has been quietly listening,{w=.3} delivers encouragement."
    hide y_smile
    hide h_smile_gray
    show h_smile at right
    show y_smile_gray at left
    with d5
    h "Wow!{w=.3} Yes,{w=.3} I think it will happen!{w=.3} I also think you could be!"
    hide y_smile_gray
    hide h_smile
    show y_smile at left
    show h_smile_gray at right
    with d5
    y "No,{w=.3} I still have a long way to go.{w=.3} There's a lot of things to get through."
    na "He says embarrassedly,{w=.3} waving his hands."
    p "I can tell you can do it - because you've got something different than with others."
    y "Not different.{w=.3} There're heaps and heaps of people like me around the world."
    y "But I believe I can do it.{w=.3} I will definitely make it."
    y "And I will make sure that no one would dare to walk over my precious people."
    na "Yes,{w=.3} Yunwoo,{w=.3} I believe you can."
    na "Mentally,{w=.3} I shout out a cheer for Yunwoo."
    y "So,{w=.3} you guys,{w=.3} also live your dreams as well!"
    y "I never want to see my precious people go wrong."
    p "Yes,{w=.3} you're right.{w=.3} We will."
    na "Yunwoo,{w=.3} you are always cool."
    na "You really think of me as one of your precious people even though I've always disappointed you?"
    hide y_smile
    hide h_smile_gray
    show y_smile_gray at left
    show h_smile at right
    with d5
    h "However,{w=.3} I think we shouldn't have to struggle so desperately to earn money."
    na "As soon as we stop conversation,{w=.3} Hye-na says contradictory words."
    p "What?{w=.3} You don't remember what you said?{w=.3} You said things seem too unfair?"
    h "Well,{w=.3} I was,{w=.3} but….{w=.3} Now I think,{w=.3} I would be also happy to live just simply with people I love."
    h "Even though we're not that rich,{w=.3} if we could live a happy life with precious family,{w=.3} and not be greedy,{w=.3} then I think that would be good enough."
    hide y_smile_gray
    hide h_smile
    show y_smile at left
    show h_smile_gray at right
    with d5
    y "Yes,{w=.3} you're right,{w=.3} Hye-na.{w=.3} Even if we're not that rich,{w=.3} there are lots of ways to live happily,{w=.3} indeed."
    na "Yunwoo says with a smile to Hye-na."
    hide y_smile
    hide h_smile_gray
    show y_smile_gray at left
    show h_smile at right
    with d5
    h "Yes!{w=.3} The most important thing is that we are alive now!"
    hide y_smile_gray
    hide h_smile
    with d
    na "To be alive.{w=1}"
    na "Yes.{w=.3} I am alive."
    na "Even though I have lived just like a pathetic loser,{w=.3} anyway,{w=.3} I'm still alive."
    na "So,{w=.3} I can get up on my feet."
    na "Yes,{w=.3} I can do it."
    na "If it's difficult,{w=.3} it's alright to get a job in a hospital like before."
    na "If I'm asked what I've done while I was staying away from work,{w=.3} it could be difficult to answer."
    na "But I am qualified and I also have a lot of experience – so it will be fine."
    scene room
    show night
    with f
    na "While laughing and chatting,{w=.3} time has passed quickly."
    na "And Hye-na blacks out again because of drinking too much."
    na "Yunwoo and I clean up the table.{w=.3} Yunwoo gets ready to leave."
    stop music fadeout 3
    na "Yunwoo puts on his shoes,{w=.3} and opens the door quietly."
    p "Hey…,{w=.3} Yunwoo?"
    na "I stop him in a small voice."
    na "He turns back and says with a big smile."
    show y_smile
    with d5
    y "What?{w=.3} If you need something,{w=.3} don't worry and just say it to me.{w=.3} Is there something bothering you?"
    p "No,{w=.3} I just….{w=.3} Because it's so late."
    na "I slur my words."
    na "He takes his cell phone out of his back pocket,{w=.3} sees what time it is now,{w=.3} then puts it back again."
    y "Wow,{w=.3} it's almost three o'clock.{w=.3} I didn't notice it's that late now."
    play music 'bgm/Sigh day.opus' fadein 3
    p "If you want,{w=.3} you can sleep over here tonight…."
    na "I look at his eyes lovingly."
    na "He gazes at my eyes for a moment,{w=.3} too."
    na "For a short moment,{w=.3} I can hardly breathe,{w=.3} then it passes."
    na "He raises his right hand."
    na "And he moves that hand closer and closer to me."
    na "I thought,{w=.3} no,{w=.3} I hoped,{w=.3} his hand was going to touch my cheek,{w=.3} but he moves his hand over my head."
    na "Then,{w=.3} he says,{w=.3} sweetly petting my head."
    y "Alright,{w=.3} you're drunk.{w=.3} Go to bed right away."
    hide y_smile
    with d5
    na "Then he puts his hand down,{w=.3} sticks it into his pocket,{w=.3} and turns back."
    na "No,{w=.3} I can't let him go like this."
    na "When he's about to take his first step out,{w=.3} I stretch out my right hand and grab his arm."
    na "And I pull his arm to me and make him look at me."
    na "Shame on me!{w=.3} What am I doing now?{w=.3} It was like,{w=.3} he has already rejected me."
    na "But once again,{w=.3} I say in a quavering voice,{w=.3} closing my eyes tightly."
    scene black
    $ renpy.transition(d5)
    $ renpy.pause(.5, hard = True)
    show expression Text ('"Kiss me."', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene post
    show night
    with d5
    na "Then,{w=.3} with the feel of his hands on my cheeks,{w=.3} I open my eyes and slightly raise my head."
    na "His hands are sweetly covering my cheeks."
    na "It's warm….{w=.3} I didn't know the feeling of his hands is so heartwarming and sweet like this."
    na "I slowly close my eyes and wait for his kiss."
    hide night
    show kissme
    show night
    with d5
    na "Soon,{w=.3} I feel his lips touching my lips."
    na "His hand gently covers my head."
    na "He overlaps his lips onto my lips,{w=.3} and smoothly draws my lips into his."
    na "The other hand is holding my waist."
    na "I raise my arms and cuddle his neck,{w=.3} to get closer."
    na "Then,{w=.3} I slowly slide my tongue into his mouth and tickle his tongue."
    na "Now,{w=.3} he hugs me more strongly,{w=.3} and sucks my tongue."
    na "And I push him forcefully against the wall and start kissing passionately."
    scene black with d3
    $ renpy.end_replay()
    if persistent.part13 is None:
        $ persistent.unlock_7 = True
        $ persistent.gall += 1
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 13)
        $ achievement.progress('KNDW_ART', 16)
        if not persistent.blind is True:
            call unlocked
label discouraged:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene hospital at sepia
        show gb_sepia at right
        show expression 'part_14_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part14]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part14]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    $ save_name = "Grasping reality"
    $ show_quick_menu = True
    scene room with blind
    na "I wake Hye-na up early in the morning,{w=.3} and prepare breakfast with bean-sprout soup for her.{w=.3} Then,{w=.3} after she goes out to work,{w=.3} a couple of hours have passed."
    na "The warm sunlight is permeating into my small room."
    na "Opening the window,{w=.3} I stick my head outside."
    na "The world out of the window is so bright and shiny."
    na "While looking out of the window,{w=.3} I suddenly blush with my memory of last night."
    na "Then,{w=.3} I smile.{w=.3} Turning back,{w=.3} I walk towards the computer and sit on the chair."
    na "So….{w=.3} Now,{w=.3} I'm going to make Yunwoo's pamphlet thing."
    na "I turn on the computer,{w=.3} and straighten my back.{w=.3} Then,{w=.3} I stretch myself,{w=.3} raising my arms high."
    na "And I take out my cell phone and text Yunwoo."
    na "After writing{w=.3} \"What are you doing? Are you busy?\",{w=.3} I'm about to send it,{w=.3} but soon,{w=.3} I stop."
    na "Should I wait until he texts me?"
    na "Thinking for a while,{w=.3} I nod slightly,{w=.3} and put the cell phone on the desk again."
    na "Well,{w=.3} I will wait until he gets in touch first.{w=.3} He will contact me soon."
    na "I grip the mouse,{w=.3} and use the computer."
    p "Whoops,{w=.3} I didn't install the program."
    na "This computer has only a few programs for document work and video playing."
    na "I try to find a webhard website where I downloaded the coupon before."
    na "I log in the website,{w=.3} and see my coupon box.{w=.3} Fortunately,{w=.3} it's still available."
    play sound 'se/typing.opus'
    na "I enter \"○○\" in the searching box."
    na "While the program is being downloaded,{w=.3} I try to search around for any interesting movie."
    na "Then,{w=.3} I see a spam-like title."
    stop music fadeout 3
    scene black
    $ renpy.transition(d5)
    $ renpy.pause(.5, hard = True)
    show expression Text ('Shocking! A doctor and a nurse in the hospital!', style='centered_text', size=72)
    if persistent.blind is True:
        with dl
        pause 10
    else:
        $ renpy.transition(d3)
        $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    play music 'bgm/Jormungandr.opus' fadein 3
    scene room with d5
    na "I stop searching for a moment,{w=.3} and stare at the title blankly."
    na "Well…,{w=.3} there is another woman like me…."
    na "I click it unconsciously,{w=.3} and open the window."
    na "While scrolling through the contents,{w=.3} I stop at the screen shot."
    play sound 'se/flash.opus'
    scene video at video1
    $ renpy.transition(flash)
    $ renpy.pause(3, hard = True)
    play sound 'se/flash.opus'
    scene video at video2
    $ renpy.transition(flash)
    $ renpy.pause(3, hard = True)
    play sound 'se/flash.opus'
    scene video at video3
    $ renpy.transition(flash)
    $ renpy.pause(3, hard = True)
    scene room
    show bshock
    if persistent.epilepsy is True:
        with d
    else:
        with red
    pause 1
    na "What the…."
    pause 1
    with f
    na "Why….{w=.3} How could this happen…."
    pause 1
    with f
    pause 1
    na "What is this here!!"
    with shock2
    pause 1
    na "Why did I do such a terribly wrong thing?"
    na "I was just about to start again!{w=.3} But why now?"
    pause 1
    na "Does Yunwoo know about this?"
    pause 1
    na "Yes,{w=.3} he probably knew this."
    stop sound
    play sound 'se/flash.opus'
    scene phone at gray
    show e_laugh_gray
    with flash
    $ angelname = 'Clerk'
    ex "Oh, hey, you look familiar, have I seen you on the internet?"
    hide e_laugh_gray
    stop sound
    play sound 'se/flash.opus'
    show y_smile_gray
    with flash
    y "Let's get out of here, Ga-yeon."
    stop sound
    play sound 'se/flash.opus'
    scene room
    show bshock
    with flash
    na "{size=+10}He must have seen this!!{/size}"
    pause 3
    $ renpy.start_predict('video_play')
    na "What I wanted was just Yunwoo."
    na "What he said as soon as he was discharged from the army,"
    na "it was a proposal."
    na "He said he loved me,"
    na "and he had thought of me more than his sister while he was in the army,"
    na "and even though he had nothing for now,{w=.3} he was definitely going to make me happy."
    na "And I was happy with that.{w=.3} However,{w=.3} I couldn't accept him."
    na "It was because he had nothing,{w=.3} just like me."
    na "Yes,{w=.3} I and he had nothing."
    na "If I marry him,{w=.3} could Yunwoo and I be happy?"
    na "I thought,{w=.3} no,{w=.3} we couldn't."
    na "Right,{w=.3} I rejected a guy I had loved so much,{w=.3} just because of his financial situation."
    na "I know,{w=.3} I am such a snob."
    scene expression 'video_play'
    with dl
    na "On my computer,{w=.3} a video is playing showing a man who I once loved and I having sex."
    na "Though I'm looking at it,{w=.3} I don't see it."
    na "What did Yunwoo think about this?"
    na "He didn't avoid me,{w=.3} or look down on me."
    na "Instead,{w=.3} he kissed me."
    na "But why?{w=.3} Does he still love me?"
    na "I look at the guy in the video for awhile."
    na "He looks a lot like Yunwoo."
    na "He used to give me a warm smile."
    na "And his living situation was much better than Yunwoo's."
    na "So,{w=.3} this was the man I chose instead of Yunwoo."
    na "What if this man was Yunwoo?"
    na "What if the man I kissed last night was this man?"
    na "My lips quiver."
    na "Tears are falling down my cheeks."
    na "Now,{w=.3} I can't do anything."
    na "There would be lots and lots of people who already saw this."
    na "I can't even go out into the street."
    na "I will be a huge obstacle in Yunwoo's life."
    na "I'm sorry Yunwoo."
    na "Yunwoo.{w=1}"
    $ renpy.stop_predict('video_play')
    scene room
    show bshock
    with dl
    na "I stand up from the chair,{w=.3} and turn back.{w=.3} Then,{w=.3} I walk on a few steps,{w=.3} then,{w=.3} just collapse on the floor."
    na "Yes,{w=.3} this is a punishment."
    na "I'm being punished by heaven."
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        show blink2 with d5
    na "I breathe hard,{w=.3} sitting on the ground."
    na "I look around,{w=.3} blinking my eyes."
    na "My view becomes narrow,{w=.3} and things in front of my eyes get blurred."
    na "I bow my head,{w=.3} raise my hands from the ground to wipe my tears away with the back of my hands,{w=.3} and shake my head several times."
    na "Then,{w=.3} I lift my head again,{w=.3} and see ahead."
    na "My view is still narrow,{w=.3} and everything I can see is just blurry."
    na "Continuing to blink my eyes,{w=.3} I try to breathe in and out normally,{w=.3} but my breathing instead is shallow."
    na "I'm very anxious,{w=.3} and afraid."
    na "The same fear that I have experienced many times before."
    na "It feels like I've run out of air."
    na "I can't breathe."
    with shock2
    na "At the very moment when I realize it,{w=.3} I burst out crying,{w=.3} making a terrible sound,{w=.3} just like a monster."
    na "Tears roll down my face,{w=.3} and I slobber on the floor."
    na "I have to breathe.{w=.3} I must.{w=.3} Breathe!"
    if not persistent.blind is True:
        if _preferences.transitions == 0:
            system 'Find the Nebulizer'
        else:
            show expression 'anxiety' at times with d3
            hide expression 'anxiety' with d3
        call screen anxiety
    na "I manage to crawl to the computer desk.{w=.3} Then,{w=.3} I take a nebulizer out of the drawer,{w=.3} start it,{w=.3} and cover my face with it."
    na "Please,{w=.3} please help me to breathe."
    na "I try to breathe properly,{w=.3} huffing,{w=.3} puffing and panting very hard."
    na "But I can't breathe."
    pause 3
    na "It's totally meaningless - I stop trying to breathe."
    na "Then,{w=.3} I take the nebulizer away from my face and throw it hysterically."
    na "Yes,{w=.3} a knife….{w=.3} I need a knife."
    if not persistent.blind is True:
        if _preferences.transitions == 0:
            system 'Find a Cutter Knife'
        else:
            show expression 'knife' at times with d3
            hide expression 'knife' with d3
        call screen holder
        scene self_gall
        with flash
        if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
            pass
        else:
            show blink2 with d5
    na "I quickly fumble around my desk,{w=.3} and move the pencil holder aside to get a knife."
    na "Before,{w=.3} I have sometimes relieved my suffering by using a knife."
    na "And this time,{w=.3} it will work again."
    $ renpy.end_replay()
    sv "The next step is an important scene. Do you want to save here?"
    sv "Left arrow key: Yes, Right arrow key: No."
    call screen save_confirm
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        hide blink2 with d5
    if persistent.part14 is None:
        $ persistent.con04 = True
        $ persistent.unlock_8 = True
        $ persistent.con += 1
        $ persistent.gall += 1
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 14)
        $ achievement.progress('KNDW_CONCEPT', 6)
        $ achievement.progress('KNDW_ART', 17)
        $ achievement.progress('KNDW_OBJECT', 6)
        $ achievement.grant('KNDW_VIDEO')
        $ achievement.grant('KNDW_NEBULIZER')
        $ achievement.grant('KNDW_HOLDER')
        if not persistent.blind is True:
            call unlocked
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene room at sepia
        show gb_sepia at right
        show expression 'part_15_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part15]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part15]', style='centered_text')
    $ progress += 1
    pause 3
    scene black with d
    scene room
    show bshock
    with blind
    $ save_name = "Self-inflicted"
label self_inflicted:
    if sigiveup == 1:
        scene room
        show bshock
        with flash
        if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
            pass
        else:
            show blink2 with d5
        na "I've made a gash on my wrist and blood is oozing from the wound.{w=.3} But I still can't breathe."
        na "Before,{w=.3} when I did it this way,{w=.3} the suffering got better soon.{w=.3} But now,{w=.3} why doesn't it work?"
        na "Why am I still having trouble breathing?"
        na "Coughing hard,{w=.3} I put the knife down on the desk,{w=.3} and wrap my wounds,{w=.3} try to find the ointment."
        if not persistent.blind is True:
            if _preferences.transitions == 0:
                system 'Open the Drawer'
            else:
                show expression 'drawer' at times with d3
                hide expression 'drawer' with d3
            if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
                pass
            else:
                show blink2 with d5
            call screen obdrawer
        if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
            pass
        else:
            hide blink2 with d5
        show diary
        with d5
        if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
            pass
        else:
            show blink2 with d5
        na "I stare blankly at them for a while,{w=.3} and then,{w=.3} I take the diary out of a drawer and put it down on the desk.{w=.3} And I also take out the glasses,{w=.3} cradling them with my two hands."
        if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
            pass
        else:
            hide blink2
        hide diary
        show glasses
        with d5
        if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
            pass
        else:
            show blink2 with d5
        na "When I was with him,{w=.3} I hid his glasses while he was taking a shower."
        hide glasses
        with d5
        na "When I'm about to pick up the glasses,{w=.3} I suddenly feel dizzy.{w=.3} I try to turn back,{w=.3} but soon,{w=.3} lose my balance,{w=.3} then fall down."
        na "I think I'm gonna faint."
        na "Please,{w=.3} please help me."
        if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
            pass
        else:
            hide blink2 with d5
        if not achievement.has('KNDW_DIARY'):
            if not achievement.has('KNDW_ACCIDENT') or achievement.has('KNDW_ONLOOKER'):
                $ persistent.unlock_13 = True
                $ persistent.char += 1
                $ persistent.gall += 1
                $ persistent.replay += 1
                $ achievement.progress('KNDW_PROGRESS', 15)
                $ achievement.progress('KNDW_IDENTIFY', 7)
            $ achievement.progress('KNDW_ART', 18)
            $ achievement.progress('KNDW_OBJECT', 8)
            $ achievement.grant('KNDW_DRAWER')
            $ achievement.grant('KNDW_DIARY')
            if persistent.blind is not True and persistent.part15 is None:
                call unlocked
        jump love
    elif sicount == 3:
        scene room with d3
        na "A little while later,{w=.3} I feel strange,{w=.3} as if I'm floating in the air,{w=.3} then,{w=.3} feel drowsy."
        na "I still can't breathe properly,{w=.3} but I think,{w=.3} I'm getting better."
        na "This time, I decide to try once again,{w=.3} and slash the wound on my wrist slowly but more deeply,{w=.3} with the knife in my right hand."
        scene room
        show bshock
        if persistent.epilepsy is True:
            with d
        else:
            with red
        na "Now,{w=.3} I can breathe,{w=.3} and at the same time,{w=.3} the deep red color of the blood squirts out of the wound."
        na "It is such an unexpected new feeling,{w=.3} one I've not experienced before.{w=.3} However,{w=.3} I don't know why,{w=.3} but I think I like it."
        na "I slowly close my eyes,{w=.3} feeling great calm and tranquility."
        scene black with d3
        if not achievement.has('KNDW_ACCIDENT'):
            if not achievement.has('KNDW_ONLOOKER') or achievement.has('KNDW_DIARY'):
                $ persistent.unlock_13 = True
                $ persistent.gall += 1
                $ persistent.replay += 1
                $ achievement.progress('KNDW_PROGRESS', 15)
                $ achievement.progress('KNDW_IDENTIFY', 7)
            $ achievement.progress('KNDW_ART', 18)
            if persistent.blind is not True and persistent.part15 is None:
                call unlocked
        $ gp = 0
        $ gc = 0
        $ gg = 0
        $ gm = 0
        $ gr = 0
        $ gd = 0
        $ progress += 1
        $ save_name = "R.I.P"
        sv "You died. R.I.P."
        scene rip with d3
        pause 3
        scene black with d3
        if persistent.part16 is None:
            $ persistent.unlock_20 = True
            $ persistent.gall += 1
            if achievement.has('KNDW_ACCIDENT') and persistent.unlock_15 is True:
                $ achievement.grant('KNDW_ART')
            elif achievement.has('KNDW_ACCIDENT') or persistent.unlock_15 is True:
                $ achievement.progress('KNDW_ART', 29)
            else:
                $ achievement.progress('KNDW_ART', 19)
            $ achievement.grant('KNDW_KILLER')
            if achievement.has('KNDW_KILLER') and achievement.has('KNDW_ACCIDENT'):
                $ achievement.grant('KNDW_MURDERER')
            if achievement.has('KNDW_KILLER') and achievement.has('KNDW_ACCIDENT') and achievement.has('KNDW_MASTER'):
                $ achievement.grant('KNDW_VOTERS')
            if achievement.has('KNDW_GAMEOVER') and achievement.has('KNDW_IDENTIFY') and achievement.has('KNDW_DEMO') and achievement.has('KNDW_CONCEPT') and achievement.has('KNDW_DIARY') and achievement.has('KNDW_ART') and achievement.has('KNDW_OST') and achievement.has('KNDW_PROGRESS') and achievement.has('KNDW_OBJECT') and achievement.has('KNDW_MURDERER') and achievement.has('KNDW_FRONTIER') and achievement.has('KNDW_START') and achievement.has('KNDW_VOTERS') and achievement.has('KNDW_ADULT') and achievement.has('KNDW_LEFT') and achievement.has('KNDW_RIGHT')  and achievement.has('KNDW_ONLOOKER') and achievement.has('KNDW_VIDEO'):
                $ achievement.grant('KNDW_MASTER_FRONTIER')
                $ achievement.grant('KNDW_SPONSOR')
            if not persistent.blind is True:
                call unlocked
        else:
            if achievement.has('KNDW_ACCIDENT') and persistent.unlock_15 is True:
                $ achievement.grant('KNDW_ART')
            elif achievement.has('KNDW_ACCIDENT') or persistent.unlock_15 is True:
                $ achievement.progress('KNDW_ART', 29)
            if achievement.has('KNDW_KILLER') and achievement.has('KNDW_ACCIDENT'):
                $ achievement.grant('KNDW_MURDERER')
            if achievement.has('KNDW_KILLER') and achievement.has('KNDW_ACCIDENT') and achievement.has('KNDW_MASTER'):
                $ achievement.grant('KNDW_VOTERS')
            if achievement.has('KNDW_GAMEOVER') and achievement.has('KNDW_IDENTIFY') and achievement.has('KNDW_DEMO') and achievement.has('KNDW_CONCEPT') and achievement.has('KNDW_DIARY') and achievement.has('KNDW_ART') and achievement.has('KNDW_OST') and achievement.has('KNDW_PROGRESS') and achievement.has('KNDW_OBJECT') and achievement.has('KNDW_MURDERER') and achievement.has('KNDW_FRONTIER') and achievement.has('KNDW_START') and achievement.has('KNDW_VOTERS') and achievement.has('KNDW_ADULT') and achievement.has('KNDW_LEFT') and achievement.has('KNDW_RIGHT')  and achievement.has('KNDW_ONLOOKER') and achievement.has('KNDW_VIDEO'):
                $ achievement.grant('KNDW_MASTER_FRONTIER')
                $ achievement.grant('KNDW_SPONSOR')
            pause 3
        $ gp = 0
        $ gc = 0
        $ gg = 0
        $ gm = 0
        $ gr = 0
        $ gd = 0
        return
    elif sigiveup <= -1:
        if not achievement.has('KNDW_ONLOOKER'):
            if not achievement.has('KNDW_ACCIDENT') or achievement.has('KNDW_DIARY'):
                $ persistent.unlock_13 = True
                $ persistent.gall += 1
                $ persistent.replay += 1
                $ achievement.progress('KNDW_PROGRESS', 15)
                $ achievement.progress('KNDW_IDENTIFY', 7)
            $ achievement.grant('KNDW_ONLOOKER')
            if persistent.blind is not True and persistent.part15 is None:
                call unlocked
        jump unme
    elif sicount > 0:
        play sound 'se/flash.opus'
        scene self_gall
        with flash
        if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
            pass
        else:
            show blink2 with d5
        na "No,{w=.3} it doesn't help me breathe."
        if sicount == 2:
            na "It hurts….{w=.3} It hurts like hell!"
            play sound 'se/flash.opus'
            scene room
            show bshock
            show self
            show self3
            show self4
            with shock
            if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
                pass
            else:
                show blink2 with d5
        elif sicount == 1:
            na "More….{w=.3} I need more!"
            play sound 'se/flash.opus'
            scene room
            show bshock
            show self
            show self3
            with shock
            if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
                pass
            else:
                show blink2 with d5
        sv "[gui.choice]"
        sv "Left arrow key: [gui.heal] Right arrow key: [gui.judge]"
        call screen self_inflicted
    else:
        play sound 'se/flash.opus'
        hide self
        show self
        with flash
        if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
            pass
        else:
            show blink2 with d5
        sv "[gui.choice]"
        sv "Left arrow key: [gui.heal] Right arrow key: [gui.judge]"
        call screen self_inflicted
label love:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene deep_sepia
        show expression 'part_17_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part17]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part17]', style='centered_text')
    $ progress = 17
    pause 3
    scene black with d
    $ save_name = "Madness"
    $ show_quick_menu = True
    scene room
    show bshock
    if persistent.epilepsy is True:
        with d
    else:
        with red
    if persistent.epilepsy is True or persistent.tic is None or _preferences.transitions == 0:
        pass
    else:
        show blink1 with d5
    na "Yunwoo,{w=.3} I need Yunwoo."
    na "The only one who can save me is Yunwoo."
    na "I bite my lips tightly to swallow the sounds that are trying to escape from my mouth."
    na "I open my eyes firmly,{w=.3} and get up slowly."
    na "Then,{w=.3} I sit down in front of the computer desk."
    na "In the video,{w=.3} I am totally naked."
    na "And the one I'm making love with is."
    scene black with d3
    $ show_quick_menu = False
    centered "{size=+5}Yes,{w=.3} it's Yunwoo.{/size}"
    pause 1
    scene expression 'mas_1'
    with d5
    $ show_quick_menu = True
    na "I see Yunwoo there.{w=.3} How beautiful we are….{w=.3} Yunwoo and I are making love…."
    na "I become calm soon,{w=.3} and my breathing slows and becomes more regular.{w=.3} My tears stop running,{w=.3} too."
    na "I'm watching the video.{w=.3} Yunwoo and I are making love together."
    na "I feel my body is getting hotter,{w=.3} and unconsciously,{w=.3} I'm moving my hand towards my thigh."
    na "I pull up the skirt until my underwear is exposed,{w=.3} and then,{w=.3} I softly touch my private part."
    na "When my hand touches the underwear,{w=.3} I feel something wet."
    scene expression 'mas_2'
    na "Pushing the wet part smoothly,{w=.3} I slowly rub,{w=.3} and rub."
    na "Until he cums inside me.{w=.3} I do it over and over again,{w=.3} and then,{w=.3} I'm reaching orgasm,{w=.3} just like that time."
    na "No,{w=.3} it's much more intense.{w=.3} That strong feeling overwhelms me and makes me feel dizzy."
    scene expression 'mas_3'
    na "Until the lovejuice is coming out of my panties."
    na "I devote my body and my mind to Yunwoo."
    scene black with d3
    scene rooml
    with d5
    na "After I complete his poster and pamphlet,{w=.3} I sit on the bed and call him."
    y "Hello?"
    na "I hear his voice through the line.{w=.3} I can also hear others' faint voices beyond him."
    p "It's me,{w=.3} Ga-yeon."
    y "I know.{w=.3} Have you had a dinner?"
    na "I can hear he's smiling."
    p "Yeah.{w=.3} What about you?"
    y "My band mates and I ate some food that we had delivered.{w=.3} We're just fooling around now."
    p "Well,{w=.3} I've just completed the poster and pamphlet.{w=.3} You want to see them?"
    y "Wow,{w=.3} you've already done that?{w=.3} So quick!"
    p "Of course~!{w=.3} You know,{w=.3} it's not a big deal at all to me!"
    y "Okay,{w=.3} I'll come there.{w=.3} Is it okay now?"
    p "Yes,{w=.3} come right away!"
    y "Okay,{w=.3} I'm leaving right now."
    p "Good,{w=.3} see you!"
    na "After saying those words,{w=.3} I wait for a moment.{w=.3} But I don't hear that he hangs up.{w=.3} So I say to him."
    p "Why don't you hang up?"
    y "You hang up first!"
    stop music fadeout 3
    p "Uh-huh?{w=.3} Okay,{w=.3} then,{w=.3} bye!"
    play sound 'se/dialoff1.opus'
    na "I hang up the phone,{w=.3} then lower my head in shame and cover my face with my hands."
    scene black with d5
    $ show_quick_menu = False
    pause 1
    centered "{size=+5}Choi Ga-yeon{/size}{w=1}"
    centered "{size=+5}You don't deserve to live.{/size}"
    pause 1
    scene rooml
    with d5
    $ show_quick_menu = True
    show y_smile
    with d5
    y "Alright,{w=.3} let me see how well you've done!"
    na "Both of us sit in front of the computer and look at the monitor."
    y "Wow!{w=.3} It's amazing!{w=.3} You've done much better than I expected,{w=.3} Ga-yeon!{w=.3} Why don't you get a job in graphic design?"
    na "Yunwoo admires my work,{w=.3} looking at the poster on the monitor."
    na "I turn my head towards him,{w=.3} and say with a smile."
    p "Do you really think so?{w=.3} Then,{w=.3} praise me."
    hide y_smile
    show y_think
    with d5
    y "What?{w=.3} I've just praised you.{w=.3} You want some more?"
    p "I don't want just lip service.{w=1}"
    hide y_think
    show y_smile
    with d5
    y "Then,{w=.3} what do you want,{w=.3} Ga-yeon?"
    p "Well…."
    y "Come on,{w=.3} just name it.{w=.3} Whatever you want,{w=.3} besides a fee.{w=.3} I would willingly pay it."
    scene black
    $ renpy.transition(d5)
    $ renpy.pause(.5, hard = True)
    show expression Text ('"I want you."', slow_speed=15, style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene room
    show deepkiss
    with d3
    pause 1
    $ save_name = "I want you."
    play music 'bgm/Mare tranquillitatis.opus' fadein 3
    na "After saying that,{w=.3} I'm slowly reaching for his neck to hug,{w=.3} and then,{w=.3} I kiss him."
    na "Then,{w=.3} I take his left hand and put it on my right breast."
    na "He suddenly stops for a moment,{w=.3} but soon,{w=.3} tenderly grabs and teases my boobs."
    na "I feel my heartbeat get faster,{w=.3} and louder.{w=.3} We share a sloppy kiss deeper and deeper."
    na "After a moment,{w=.3} we stand up and move towards the bed,{w=.3} passionately kissing each other."
    scene deepkiss2
    with d
    na "I lay him on the bed,{w=.3} and get on him.{w=.3} Then,{w=.3} I bend down to kiss him again."
    na "Rapture and excitement – I feel I could forget all my sufferings now."
    scene y_dakimakura_0 at y_daki0
    with d5
    na "I stop kissing for a moment,{w=.3} and get up to undress him."
    scene y_dakimakura_0 at y_daki1
    with d5
    na "Then,{w=.3} I take his socks and pants off."
    scene y_dakimakura_0:
        zoom 2 xalign .5 yalign .35
    with d5
    na "Looking at his bulging underwear,{w=.3} I think of his thing beneath the cloth."
    show y_dakimakura_1:
        zoom 2 xalign .5 yalign .35
    with d5
    pause 1
    hide y_dakimakura_1
    with d5
    pause 1
    na "I slowly touch his underwear,{w=.3} and then,{w=.3} grab it tightly."
    scene y_dakimakura_1:
        yalign .1
    with d5
    na "Making a groaning face,{w=.3} he closes his eyes for a moment,{w=.3} and then,{w=.3} opens them again."
    na "I take my hands off him,{w=.3} and undo the buttons on my shirt,{w=.3} from the bottom to top.{w=.3} Then,{w=.3} I show him my bare skin in a pink bra."
    scene caress0
    with d5
    if _preferences.language == 'Chinese':
        na "然后我又重新爬到了他的身上，{w=.3}抬起裙子，{w=.3}让他的阴茎碰到我的小阴唇。"
    else:
        na "And again,{w=.3} I roll up my skirt and sit on him,{w=.3} letting my labia minora meet his penis."
        na "Feeling something hot within my nether part,{w=.3} I gasp for air."
    na "I slide my bra straps off my shoulders,{w=.3} first the right,{w=.3} then the left,{w=.3} and then,{w=.3} unhook my bra,{w=.3} stretching my hand behind my back."
    na "As I haven't taken all my clothes off yet,{w=.3} my bra doesn't fall down."
    na "I slightly bend down towards him,{w=.3} and say,{w=.3} putting my boobs in front of his face."
    p "Take this off."
    scene caress
    with d3
    na "He takes my bra off and completely exposes my bare boobs."
    na "Now,{w=.3} I bend down more and let my left nipple reach his lips."
    na "He starts kissing and sweetly sucking my left nipple,{w=.3} and meanwhile,{w=.3} his left hand grabs my right boob tightly."
    with shock
    na "With a racy feel,{w=.3} I quietly groan with pleasure.{w=.3} And cuddling his head,{w=.3} I let him suck my boobs more strongly,{w=.3} and deeply."
    na "Because of the huge thrill and excitement,{w=.3} my breathing quickens."
    with shock
    na "When he sometimes caresses me strongly,{w=.3} or nips my boobs,{w=.3} I unconsciously make a coquettish sound."
    na "And in that position,{w=.3} I release my arms cuddling his head,{w=.3} and move my left hand to the skirt,{w=.3} supporting myself with my right hand."
    scene caress1
    with d5
    na "While he's teasing my boobs,{w=.3} I take off my skirt and throw it on the floor."
    scene y_dakimakura_1:
        yalign .35
    with d3
    na "I raise myself and take his lips and hands from me.{w=.3} Then,{w=.3} I creep down to his lower part,{w=.3} and take off his underwear."
    scene y_dakimakura_2 at y_daki3
    with d5
    na "I go down more.{w=.3} Then,{w=.3} I grab his penis in my right hand,{w=.3} bend my head,{w=.3} and run my left hand through my hair."
    scene fellatio at fellatio
    with d3
    na "Now,{w=.3} I slowly kiss his urethra opening and lick his glans carefully."
    na "Then,{w=.3} as I start sucking it several times moving my head up and down,{w=.3} he moans and groans."
    na "Satisfied with his reaction,{w=.3} I stop sucking and raise myself again."
    scene riding0 at top
    with d3
    na "Then,{w=.3} I take off the underwear with both hands and throw it."
    scene riding0:
        top
        linear 5 yalign .6
        linear 5 top
        repeat
    na "As I look at Yunwoo,{w=.3} who is now relishing my body with wonder,{w=.3} I'm getting horny."
    na "Again,{w=.3} I grab his penis in my right hand,{w=.3} and get on his body."
    na "I slowly let my pelvis down,{w=.3} and my labia minora meets the tip of his glans."
    na "I feel like my heart is just going to burst."
    na "And now,{w=.3} I lower my pelvis down more,{w=.3} and let his glans reach my vaginal opening."
    na "Then,{w=.3} I slightly squeeze my sphincter,{w=.3} and pull my butt a little bit forward by using my waist to have his glans come inside me,{w=.3} slowly and tightly."
    scene riding0 at center
    with d3
    pause 1
    na "Now,{w=.3} I release my hands from his penis.{w=.3} And completely sitting on his body,{w=.3} I let his penis penetrate deep inside me."
    na "We groan with pain and pleasure almost at the same time."
    pause 1
    na "I slightly release my inner muscle which has tightly held his penis.{w=.3} Then,{w=.3} I pull back my butt slowly,{w=.3} and then,{w=.3} stick it deep inside me."
    scene expression 'riding1' at bottomtotop
    with d5
    pause 5
    $ show_quick_menu = False
    show white
    show gradiant
    centered "{color=#ff0000}{size=72}Yes….{w=.3} Yes…,{w=.3} it's Yunwoo.{/size}{/color}"
    hide gradiant
    hide white
    pause 6
    $ show_quick_menu = True
    na "Until Yunwoo ejaculates into me."
    scene expression 'riding2' at bottomtotop
    with d5
    pause 5
    $ show_quick_menu = False
    show white
    show gradiant
    centered "{color=#ff0000}{size=72}It's…,{w=.3} Yunwoo.{/size}{/color}"
    hide gradiant
    hide white
    pause 6
    $ show_quick_menu = True
    na "He and I have made love."
    scene expression 'riding3' at bottomtotop
    with d5
    pause 12
    $ show_quick_menu = False
    show white
    show gradiant
    centered "{color=#ff0000}{size=72}{cps=15}It's…,{w=.3} Yunwoo.{/cps}{/size}{/color}"
    hide gradiant
    hide white
    pause 20
    show white
    show gradiant
    centered "{color=#ff0000}{size=72}{cps=5}It's Yunwoo?{/cps}{/size}{/color}"
    hide gradiant
    hide white
    pause 5
    stop music fadeout 3
    scene black
    show diary16:
        zoom .8 truecenter
    show circle
    with d3
    pause 3
    scene black
    with d3
    pause .5
    $ show_quick_menu = True
    scene way with d5
    na "Yunwoo and I walk along the street,{w=.3} hand in hand."
    p "I want to go to Hangang for fresh air."
    show y_smile
    with d5
    y "Sorry,{w=.3} Ga-yeon.{w=.3} Today,{w=.3} I gotta go Hongik Uni.{w=.3} We have a concert in the ○○."
    p "Wow,{w=.3} then can I see you playing the bass?{w=.3} I haven't seen you play for a long time!"
    y "Of course.{w=.3} I can tell you it will be better than you expect."
    scene black with d5
    $ show_quick_menu = False
    centered "I'm sorry,{w=.3} Yunwoo."
    centered "I'm a very selfish bitch."
label yunwoo:
    scene black with blind
    pause .5
    show expression Text ('Two hours ago', style='extext') at times with d3
    scene black with d3
    play music 'bgm/Summit showdown.opus' fadein 3
    scene hall
    $ show_quick_menu = True
    $ save_name = "Two hours ago"
    show band
    with d5
    b "Who's this!{w=.3} Ga-yeon,{w=.3} it's been a really long time!{w=.3} I've almost forgotten how you look."
    with d5
    p "My goodness!{w=.3} Long time no see!{w=.3} You still have that long hair!"
    hide band
    show y_smile
    with d5
    y "Eww….{w=.3} I have no idea how many years I've seen that horrible hair."
    hide y_smile
    show band
    with d5
    b "Dude,{w=.3} I'm not going to change my hairstyle until we release our album."
    b "So,{w=.3} have you come to see our concert?"
    p "Yes,{w=.3} I've been looking forward to seeing it for a long time."
    b "Great.{w=.3} Then,{w=.3} please enjoy it!"
    p "Thanks,{w=.3} I'll expect your concert to be fabulous today!"
    b "Okay,{w=.3} then,{w=.3} see you soon.{w=.5}"
    hide band with d5
    pause 1
    p "He hasn't changed at all.{w=.3} That character,{w=.3} that face.{w=.3} All the same."
    show y_smile
    with d5
    y "Yeah,{w=.3} indeed.{w=.3} He's not such a fickle type of person."
    p "Hey,{w=.3} Yunwoo,{w=.3} can I borrow your wallet?"
    y "Why not,{w=.3} here you are.{w=.3} Are you going to drink something?"
    p "Yeah,{w=.3} it's almost time for the concert.{w=.3} I don't want to miss a single moment because I get thirsty."
    y "Okay.{w=.3} Now,{w=.3} I should start getting ready over there.{w=.3} It's almost time for the concert to start."
    p "Good.{w=.3} Go for it,{w=.3} Yunwoo!{w=.3} See you soon!"
    y "All right.{w=.3} You stand in a conspicuous place!{w=.3} Don't hide in a corner!"
    p "No worries.{w=.3} But first I'm going to buy something to drink.{w=.3} See ya!"
    $ renpy.end_replay()
    if persistent.part17 is None:
        $ persistent.dying = True
        $ persistent.taejin = True
        $ persistent.unlock_9 = True
        $ persistent.unlock_10 = True
        $ persistent.unlock_11 = True
        $ persistent.bgm11 = True
        $ persistent.char += 1
        $ persistent.gall += 5
        $ persistent.bgm += 1
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 16)
        if persistent.obdrawer is True:
            $ achievement.progress('KNDW_IDENTIFY', 8)
        else:
            $ achievement.progress('KNDW_IDENTIFY', 7)
        if achievement.has('KNDW_KILLER'):
            $ achievement.progress('KNDW_ART', 25)
        else:
            $ achievement.progress('KNDW_ART', 24)
        $ achievement.progress('KNDW_OST', 11)
        $ achievement.grant('KNDW_DYING_MESSAGE')
        $ achievement.grant('KNDW_ADULT')
        if not persistent.blind is True:
            call unlocked
label yunwoo0:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene sang at sepia
        show y_poker_sepia at right
        show expression 'part_18_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part18]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part18]', style='centered_text')
    $ progress = 18
    pause 3
    scene black with d
    scene hall with blind
    $ save_name = "Yunwoo's view"
    $ show_quick_menu = True
    woo "Yes,{w=.3} it has been a really long time since you came to one of my concerts."
    woo "I'll try my best to live up to your expectations."
    with f
    woo "After a while,{w=.3} our band stands on the stage."
    woo "Ga-yeon looks at me at the edge of the place,{w=.3} away from the crowd."
    woo "I give a sign to the members,{w=.3} and we start playing our first set."
    with f
    show band with d5
    stop music fadeout 3
    b "Well done!{w=.3} Then,{w=.3} you are not going to have a drink with us?"
    pm "Oh,{w=.3} come on.{w=.3} We drink every day.{w=.3} I'm going - see you later,{w=.3} guys."
    b "All right.{w=.3} Then have a great time!"
    hide band with d5
    woo "After leaving my band mates behind,{w=.3} I look for Ga-yeon."
    pm "Uh-oh,{w=.3} where is she?"
    woo "I can't find her."
    woo "Is she in the rest room?"
    woo "I walk towards the entrance of the rest room.{w=.3} At that moment,{w=.3} I feel my cell phone being vibrated in the pocket."
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        play sound 'se/vibrate.opus'
    woo "I stop walking,{w=.3} and take my phone out of the pocket."
    woo "It is a message from Ga-yeon."
    woo "\"You knew it,{w=.3} didn't you.\""
    woo "\"Thank you for everything you've done for me.{w=.3} And….{w=.3} Sorry….\""
    pm "What?{w=.3} What the hell is she talking about now?"
    play music 'bgm/Jormungandr.opus' fadein 3
    woo "Her message struck me speechless for a while."
    woo "What the hell is she doing now…."
    woo "I hurriedly press a call button on the cell phone,{w=.3} and put the phone to my ear."
    woo "\"The person you are calling is not available at the moment.{w=.3} Please leave a message after the beep….\""
    woo "Ignoring the phone message,{w=.3} I hang up and put the phone back in my pocket again,{w=.3} I hesitate for a moment,{w=.3} wondering what to do."
    woo "So….{w=.3} What on earth is going on now…?"
    woo "I turn back,{w=.3} and return to the concert hall."
    woo "With mounting anxiety,{w=.3} I walk faster."
    scene sang with d5
    woo "Though I've looked for Ga-yeon both inside and outside the building,{w=.3} I can't find her."
    woo "Where has she gone?!"
    woo "I think this might not be a sudden problem."
    woo "These days,{w=.3} Ga-yeon has changed a lot."
    woo "She never did rely on others before.{w=.3} But these days,{w=.3} she does."
    woo "And how many times have I seen her crying since we first saw each other again not so long ago now."
    play sound 'se/flash.opus'
    scene black
    $ renpy.transition(flash)
    $ renpy.pause(.5, hard = True)
    show expression Text ('"Just stay like this for a minute, please."', style='extext')
    if persistent.blind is True:
        with dl
        pause 10
    else:
        $ renpy.transition(d)
        $ renpy.pause(1, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('"Kiss me."', style='extext')
    if persistent.blind is True:
        with dl
        pause 10
    else:
        $ renpy.transition(d)
        $ renpy.pause(1, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('"I want you."', style='extext')
    if persistent.blind is True:
        with dl
        pause 10
    else:
        $ renpy.transition(d)
        $ renpy.pause(1, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    play sound 'se/flash.opus'
    scene sang
    with flash
    woo "And now,{w=.3} our relationship has just gone up to the next level.{w=.3} So why does she say this to me now?"
    woo "Thank you for everything?"
    pause 1
    stop sound
    play sound 'se/flash.opus'
    show bshock
    with flash
    woo "I think I've missed the most important word."
    play sound 'se/flash.opus'
    scene black
    $ renpy.transition(flash)
    $ renpy.pause(.5, hard = True)
    show expression Text ('"You knew it,{w=.3} didn\'t you."', style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene sang with d5
    woo "Oh,{w=.3} my god….{w=.3} No….{w=.3} Shit…."
    woo "Probably she saw the video."
    woo "Shit!{w=.3} No,{w=.3} that's not the important thing now."
    woo "Where has she gone?"
    woo "What the hell are you thinking now?"
    pause 1
    play sound 'se/flash.opus'
    scene way at gray
    show g_smile_gray
    with flash
    pp "I want to go to Hangang for fresh air."
    stop sound
    play sound 'se/flash.opus'
    scene sang
    with flash
    pm "Hangang…."
    pm "No way…,{w=.3} you,{w=.3} such a…!!"
    stop music fadeout 3
    $ renpy.end_replay()
    if persistent.part20 is True and persistent.part18 is None:
        $ persistent.part18 = True
        $ persistent.replay += 1
    $ achievement.progress('KNDW_PROGRESS', 17)
label gayeon:
    if not persistent.blind is True:
        scene room at sepia
        show gb_sepia at right
        show expression 'part_19_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part19]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part19]', style='centered_text')
    $ progress = 19
    pause 3
    scene black with d
    scene black with blind
    pause .5
    show expression Text ('An hour and a half ago', style='extext') at times with d3
    scene black with d3
    $ save_name = "An hour and a half ago"
    play music 'bgm/Sigh day.opus' fadein 3
    scene room
    show night
    with d
    play sound 'se/switch.opus'
    scene rooml
    pause .3
    scene room
    show night
    pause .3
    scene rooml
    pause .3
    scene room
    show night
    pause .3
    scene rooml
    with d
    $ show_quick_menu = True
    p "Well….{w=.3} It's been eight years that I've lived here."
    play sound 'se/step.opus'
    na "Taking off my boots,{w=.3} I mumble to myself.{w=.3} I enter and look around in the middle of the room."
    na "I touch the speaker on the shelf for a moment."
    na "Then,{w=.3} I move my eyes upwards,{w=.3} and stretch my arms to see the books."
    p "How has such a long time passed that quickly?"
    p "When I first came here,{w=.3} I thought I was going to leave this room quickly,{w=.3} after earning lots of money…."
    na "Sighing deeply,{w=.3} I drop my head."
    na "I lower my hand from the books,{w=.3} and turn my head to the right."
    na "I walk towards the desk and sit on a chair,{w=.3} then turn on the computer."
    with f
    na "I see what time it is now."
    na "As I have Yunwoo's wallet,{w=.3} he will not be able to come here quickly."
    na "Because he doesn't have any money right now,{w=.3} he'll have to borrow money first,{w=.3} or take a subway to get here."
    na "I got out of the hall before the concert ends.{w=.3} So considering the distance,{w=.3} I would be at least 40 minutes faster than him."
    na "Besides,{w=.3} Yunwoo has to figure out which one to go to: Yeouido Riverside Park,{w=.3} Wonhyo Bridge,{w=.3} Mapo Bridge,{w=.3} or Hangang Bridge."
    na "I'm going to Hangang Bridge.{w=.3} There's very little chance,{w=.3} he'll guess that one and find me."
    na "Nodding my head,{w=.3} I delete the video file from the computer."
    na "Now,{w=.3} I turn off the computer and walk towards the door."
    na "I put on my boots.{w=.3} Then,{w=.3} just before I leave the room,{w=.3} I stop and look back."
    na "Thinking for a while,{w=.3} I just shake my head several times."
    na "I take off the boots again,{w=.3} walk across the room,{w=.3} and put Yunwoo's wallet on the bed."
    na "Then,{w=.3} I walk towards the door again,{w=.3} put on my other shoes,{w=.3} and turn off the light."
    play sound 'se/switch.opus'
    scene room
    show night
    with d5
    p "Good bye.{w=.3} I hope you will meet a good owner soon."
    scene black with d3
    pause .5
    show expression Text ('An hour ago', style='extext') at times with d3
    scene black with d3
    $ save_name = "An hour ago"
    scene mart with f
    show e_laugh
    with d5
    $ angelname = 'Staff'
    if persistent.staff is None:
        $ persistent.staff = True
    ex "Welcome~!"
    p "Oh,{w=.3} we've met in the cell phone shop before,{w=.3} haven't we?"
    ex "Oh my god!{w=.3} Yes,{w=.3} I remember you.{w=.3} Actually I was fired because they said I'm not capable enough to do that job."
    p "Oh…,{w=.3} I'm sorry to hear that…."
    p "Well,{w=.3} that's not a big deal.{w=.3} Can I have a pack of cigarettes and a lighter."
    hide e_laugh
    show e_question
    with d5
    ex "Wow,{w=.3} are you a smoker?"
    p "Nope.{w=.3} I'm just trying now."
    hide e_question
    show e_poker
    with d5
    ex "Then don't….{w=.3} It's not a good thing for your health…."
    p "Now,{w=.3} I'm going to get some fresh air."
    hide e_poker
    show e_think
    with d5
    ex "Uh-huh?{w=.3} To where?"
    p "I'm going to Hangang Bridge.{w=.3} I can't stand this heaviness in my heart.{w=.3} So I want to get some fresh air right now."
    hide e_think
    show e_question
    with d5
    ex "But it seems pretty dangerous at this late hour,{w=.3} especially for a woman."
    p "Well….{w=.3} I don't think anyone would give me a look."
    hide e_question
    show e_poker
    with d5
    ex "….{w=.5}"
    p "Hey,{w=.3} do you have a boyfriend?"
    hide e_poker
    show e_think
    with d5
    ex "No.{w=.3} Do you?"
    p "Well,{w=.3} me neither.{w=.3} However,{w=.3} I have a guy that I like – no,{w=.3} I love.{w=.3} But he's technically not a boyfriend."
    p "Anyway,{w=.3} nice meeting you.{w=.3} I hope you meet a good one soon."
    stop music fadeout 3
    scene way with f
    play music 'se/way.opus' fadein 3
    play sound 'se/dial.opus'
    woo "After getting out of the convenience store,{w=.3} I make a phone call,{w=.3} walking along the street."
    woo "For one last time,{w=.3} I want to hear my parents' voices."
    woo "They always said they were sorry."
    woo "But this time,{w=.3} it's my turn to say sorry."
    woo "As soon as I press the call button,{w=.3} I can hear the very familiar voice - my Mom."
    woo "\"Hello?\""
    woo "When I listen to her slightly excited voice,{w=.3} I feel something very heavy in my mind."
    woo "I stop walking,{w=.3} and say to her in a bright tone."
    stop music fadeout 3
    pm "Mom!{w=.3} It's me,{w=.3} Ga-yeon."
    woo "\"Ga-yeon!{w=.3} Why haven't you called for such a long time?!\""
    woo "She sounds excited,{w=.3} but she's not yelling at me.{w=.3} I can feel she has worried about me."
    pm "I'm sorry,{w=.3} Mom.{w=.3} Have you worried about me a lot?"
    woo "\"You haven't called us,{w=.3} and whenever we called you,{w=.3} we couldn't get in touch with you….{w=.3} What's wrong with you,{w=.3} Ga-yeon?{w=.3} Are you alright?\""
    woo "Mom's voice has slightly changed as time goes by.{w=.3} It sounds a little bit different than the voice that I used to hear when I was young."
    woo "But still,{w=.3} to me her voice is beautiful and heartwarming."
    woo "I speak to her in my most cheerful voice,{w=.3} and to keep my voice cheery,{w=.3} I also smile my brightest smile,{w=.3} even though she can't see it."
    pm "Of course~!{w=.3} Were you sleeping when I called?"
    woo "\"Of course.{w=.3} Don't you know what time it is now!\""
    pm "Then,{w=.3} how did you get to the phone as soon as I called you?{w=.3} I think you are too sensitive,{w=.3} don't you?"
    woo "\"Well,{w=.3} what are you doing up at this late hour?{w=.3} Shouldn't you be sleeping?\""
    pm "Today I went to see Yunwoo's concert.{w=.3} I'm just on my way home from there."
    woo "\"Sounds good.{w=.3} So is he doing well?\""
    pm "Absolutely.{w=.3} He's doing so well."
    woo "\"Ga-yeon.\""
    pm "Yes,{w=.3} what?"
    woo "\"What about you?{w=.3} Are you okay?{w=.3} Isn't it hard to work in Seoul?\""
    woo "With her voice full of anxiety,{w=.3} my face stiffens."
    woo "My eyes become hot,{w=.3} and I hesitate for a while.{w=.3} I look upwards and blink several times to calm myself down."
    woo "Then in a minute,{w=.3} I change my face again,{w=.3} and say to Mom with a big smile."
    pm "Mom,{w=.3} there's nothing hard here.{w=.3} I'm doing just so well.{w=.3} So don't worry about me!"
    woo "\"Ga-yeon,{w=.3} I miss you so much.{w=.3} Come home more often.{w=.3} And you should call more often as well.\""
    pm "All right,{w=.3} all right.{w=.3} How's Dad?{w=.3} Is he sleeping?"
    woo "\"Yes,{w=.3} he's in the room.{w=.3} And I'm out of the room to speak with you.\""
    pm "Okay,{w=.3} sorry to call you this late.{w=.3} Good night,{w=.3} Mom."
    woo "\"Ga-yeon,{w=.3} is there something wrong with you?\""
    pm "No,{w=.3} nothing.{w=.3} I just called to hear your voice."
    pm "Then,{w=.3} bye.{w=.3} Take care,{w=.3} Mom."
    woo "\"Okay.{w=.3} Good night,{w=.3} Ga-yeon.\""
    pm "Yes,{w=.3} Mom.{w=.3} I love you."
    woo "\"I love you too,{w=.3} my baby.\""
    pm "Hang up,{w=.3} Mom."
    woo "\"Okay.{w=.3} You take care!\"{w=1}"
    play sound 'se/dialoff.opus'
    woo "After I see that she hangs up,{w=.3} I stand still for a while,{w=.3} holding the phone in my hand."
    woo "When Mom said \"I love you\",{w=.3} my heart just ached so much."
    woo "I'm sorry,{w=.3} Mommy."
    stop music fadeout 3
    $ renpy.end_replay()
    if persistent.part20 is True and persistent.part19 is None:
        $ persistent.part19 = True
        $ persistent.replay += 1
        $ persistent.char += 1
    $ achievement.progress('KNDW_PROGRESS', 18)
    $ achievement.progress('KNDW_OBJECT', 9)
label yunwoo2:
    if not persistent.blind is True:
        scene way1 at sepia
        show e_think_sepia at right
        show expression 'part_20_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part20]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part20]', style='centered_text')
    $ progress = 20
    pause 3
    scene black with d
    pause .5
    show expression Text ('An hour ago', style='extext') at times with d3
    scene black with d3
    play music 'bgm/Jormungandr.opus' fadein 3
    scene train with f
    $ save_name = "Ga-yeon and Yunwoo"
    $ show_quick_menu = True
    woo "She might be at home.{w=.3} I gotta get off at Yeouinaru Station."
    woo "Please,{w=.3} Ga-yeon,{w=.3} be at home."
    woo "Don't even think about that stupid thing,{w=.3} and please,{w=.3} please be at home.{w=.3} Please."
    scene rooml
    with f
    woo "I just arrived at her house,{w=.3} but I can't find her."
    pm "Then….{w=.3} Hasn't she come home?"
    if not _in_replay:
        sv "The next step is an important scene. Do you want to save here?"
        sv "Left arrow key: Yes, Right arrow key: No."
        call screen save_confirm
    scene rooml
    sv "[gui.choice]"
    sv "Left arrow key: Take a closer look at Ga-yeon's room. Right arrow key: Let's get out of here."
    if not persistent.blind is True and _preferences.transitions == 0:
        system 'Find Your Wallet'
    elif not persistent.blind is True:
        show expression 'walletnot' at times with d3
        hide expression 'walletnot' with d3
    show screen wallet
    $ renpy.pause(3, hard = True)
    hide screen wallet
    if wallet == 1:
        woo "When I'm about to turn around to leave,{w=.3} I find my wallet on her bed."
        woo "She stopped by here."
        woo "She hasn't locked the door….{w=.3} She probably knew I would come here first to find her."
        woo "But, where is she now?"
        woo "She said she wanted to go get some fresh air.{w=.3} But she didn't say where she wanted to go."
        woo "Where can I find her?"
    scene post
    show night
    with f
    woo "As I'm leaving her home,{w=.3} I find something in a mailbox out front."
    play sound 'se/rip.opus'
    show referral with d5
    woo "I take it out to see where it was from."
    pm "Neuropsychiatric Clinic?"
    woo "I open the envelope and read what's inside."
    woo "\"We request you examine the above patient as there was no significant improvement on her at our facility.{w=.3} We have prescribed NP medication on her anxiety and depressive disorders.{w=.3} She has had NP F/U.\""
    woo "It says she had received psychiatric help."
    woo "It seems to be asking another hospital to continue her treatment."
    woo "I'll worry about this later."
    woo "But the truth is….{w=.3} She has received help from the hospital."
    woo "I didn't care enough for her."
    pause .5
    woo "You are a jerk…."
    scene black with f
    pause .5
    show expression Text ('Half an hour ago', style='extext') at times with d3
    scene black with d3
    scene way1 with f
    $ save_name = "Half an hour ago"
    woo "Now,{w=.3} where should I go?"
    woo "I have no idea at all."
    if wallet == 1:
        woo "As I found my wallet,{w=.3} I could go fast by taxi,{w=.3} if I knew her destination."
    show e_laugh
    with d5
    $ angelname = '???'
    if persistent.staffq is None:
        $ persistent.staffq = True
    ex "Oh,{w=.3} my god!{w=.3} Hey,{w=.3} do you remember me?{w=.3} You came to the cell phone shop to pay the bill,{w=.3} didn't you?"
    pm "Uh,{w=.3} you were a…."
    woo "All of a sudden,{w=.3} I recognize the smiling woman in front of me."
    ex "Where are you going this late at night,{w=.3} leaving your girlfriend alone??"
    woo "Leaving my girlfriend alone?{w=.3} What does she mean?"
    woo "Oh,{w=.3} did she see Ga-yeon?"
    pm "Hey,{w=.3} did you see Ga-yeon?"
    ex "I don't know her name.{w=.3} But I saw your girlfriend."
    pm "So you saw Ga-yeon?"
    hide e_laugh
    show e_think
    with d5
    ex "While I was working at the convenience store,{w=.3} she came to buy something."
    ex "She said she was going to Hangang Bridge to get some fresh air."
    pm "Are you sure of that?"
    ex "Yes,{w=.3} she said she was going to Hangang Bridge."
    pm "Okay,{w=.3} you are such an angel to me!{w=.3} Thank you so much!{w=.3} Bye!"
    hide e_think
    with d5
    stop music fadeout 3
    if wallet == 1:
        woo "Passing her by,{w=.3} I run out to the street to hail a taxi."
        woo "As there will be no people walking around Hangang Bridge at this late hour,{w=.3} it will be easy to find her."
        woo "I will save you soon,{w=.3} Ga-yeon.{w=.3} Just get some fresh air as you wanted,{w=.3} please."
    if persistent.part20 is True and persistent.con03 is None:
        $ persistent.con03 = True
        $ persistent.con += 1
label unme:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    scene black with f
    pause .5
    show expression Text ('Half an hour ago', style='extext') at times with d3
    scene black with d3
    scene hang with d3
    play music 'se/wind.opus' fadein 3
    na "Hangang Bridge."
    na "I didn't know there's no people and no cars…,{w=.3} at this hour.{w=.3} Only chilly air and the silence of night welcomes me."
    na "Looking at the right handrail,{w=.3} I put my right hand on it."
    na "It's pretty cold.{w=.3} I feel like I'm going to freeze."
    na "Now,{w=.3} I completely turn my body towards the handrail,{w=.3} and put my left hand on it as well."
    na "I slightly raise my head,{w=.3} and see the entirely clear view ahead of me."
    scene black
    $ renpy.transition(d5)
    $ renpy.pause(.5, hard = True)
    show expression Text ('Cold.', style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene hang with d5
    $ save_name = "Cold."
    na "I take my hands off the handrail.{w=.3} Fixing my gaze,{w=.3} I fumble in my pocket to find a pack of cigarettes and lighter."
    play sound 'se/ciga.opus'
    na "Holding the pack of cigarettes in my left hand which is also holding a lighter,{w=.3} I try to open the new pack."
    na "After tearing away the outer cellophane,{w=.3} I open the pack and my fingers fumble around trying to get a cigarette.{w=.3} Soon,{w=.3} I have it out of the pack."
    na "I lower my eyes,{w=.3} and put the pack back into the pocket of my skirt."
    na "I lift my hand holding the cigarette and lighter,{w=.3} and stick the cigarette in my mouth."
    na "Then,{w=.3} I put my right hand on my left hand which is still holding the lighter."
    na "Both hands start trembling."
    play sound 'se/burn.opus'
    na "I try to strike the lighter by using my left thumb – but fail."
    play sound 'se/burning.opus'
    na "I try several times more,{w=.3} and then,{w=.3} the flame finally arises."
    na "I light the cigarette,{w=.3} and smoke rises."
    with shock2
    na "I try to suck it in,{w=.3} taking a deep breath,{w=.3} but soon,{w=.3} I feel something extremely uncomfortable."
    na "I take the cigarette out of my mouth,{w=.3} and cough violently."
    na "After a fit of coughing,{w=.3} I even have tears in my eyes."
    na "Soon,{w=.3} I get over my coughing fit,{w=.3} and take a deep breath."
    na "Then,{w=.3} I move the cigarette to my mouth and try to suck it in again."
    with shock
    na "And I have another coughing fit."
    na "Oh,{w=.3} my god.{w=.3} How on earth can people smoke?"
    na "Coughing and coughing,{w=.3} and coughing,{w=.3} I think to myself."
    pause 1
    na "After doing the same things several times with the cigarette,{w=.3} I feel dizzy."
    na "I feel like I'm beginning to hallucinate."
    with shock
    na "I take a step backward and stagger,{w=.3} still holding the cigarette in my mouth."
    with shock
    na "And then,{w=.3} a step forward,{w=.3} shaking my head from side to side."
    with shock
    na "And then again,{w=.3} a step backward.{w=.3} Then,{w=.3} I tidy my rumpled hair,{w=.3} blown about by the wind."
    na "Well….{w=.3} I didn't know a cigarette works like this."
    pause 1
    scene smoking with d3
    na "As time goes by,{w=.3} my dizziness goes away."
    na "But still,{w=.3} it is impossible to deeply inhale the cigarette."
    na "I just lightly breathe the cigarette in within my mouth,{w=.3} and then exhale."
    na "I stand still there,{w=.3} until I smoke the whole cigarette."
    scene hang with d3
    na "As I finish the cigarette,{w=.3} I bend down,{w=.3} throw the butt on the ground,{w=.3} and stamp it out."
    na "Then,{w=.3} I straighten myself again,{w=.3} and tidy my disordered hair."
    na "When I try to walk forward,{w=.3} I feel dizzy again."
    na "Only after taking several steps more,{w=.3} am I able to walk properly."
    na "If I had it to do over again,{w=.3} I would never learn to smoke."
    stop music fadeout 3
    pause 1
    if wallet == 1:
        scene black with d5
        show expression Text ('Fifteen minutes ago', style='extext') at times with d3
        scene black with d3
        scene hang with f
        $ save_name = "Fifteen minutes ago"
        woo "I stop a taxi in front of the bridge,{w=.3} and run around to find Ga-yeon."
        woo "No – it was my mistake!{w=.3} It would have been much faster to find her by taxi!"
        woo "I gotta climb up to the bridge."
    scene han with f
    pause 1
    play music 'bgm/Sea of nectar.opus' fadein 3
    na "Some words are written on the handrail."
    na "It seems it's not just graffiti,{w=.3} but a message from someone."
    na "I unconsciously stop for a moment,{w=.3} but soon keep walking around."
    $ renpy.end_replay()
    if persistent.part20 is None:
        $ persistent.unlock_12 = True
        $ persistent.bgm12 = True
        $ persistent.gall += 1
        $ persistent.bgm += 1
        $ persistent.replay += 1
        if not sigiveup <= -1:
            $ persistent.con03 = True
            $ persistent.con += 1
            $ persistent.char += 2
            $ persistent.part18 = True
            $ persistent.part19 = True
            $ persistent.replay += 2
        else:
            $ persistent.char += 1
        $ achievement.progress('KNDW_PROGRESS', 19)
        $ achievement.progress('KNDW_CONCEPT', 7)
        if achievement.has('KNDW_KILLER'):
            $ achievement.progress('KNDW_ART', 26)
        else:
            $ achievement.progress('KNDW_ART', 25)
        $ achievement.progress('KNDW_OST', 12)
        if wallet == 1:
            $ achievement.grant('KNDW_WALLET')
            $ achievement.grant('KNDW_OBJECT')
        if not persistent.blind is True:
            call unlocked
    elif not achievement.has('KNDW_OBJECT'):
        if wallet == 1:
            $ achievement.grant('KNDW_WALLET')
            $ achievement.grant('KNDW_OBJECT')
    if wallet == 1:
        jump bridge
    else:
        jump edge
label bridge:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene bridge at sepia
        show expression 'part_21_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part21]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part21]', style='centered_text')
    $ progress = 21
    pause 3
    scene black with blind
    show expression Text ('Five minutes ago', style='extext') at times with d3
    scene black with d3
    $ save_name = "Bridge of the life"
    $ show_quick_menu = True
    scene bridge
    with blind
    sv "The next step is an important scene. Do you want to save here?"
    sv "Left arrow key: Yes, Right arrow key: No."
    call screen save_confirm
    show screen bridge
label bridge_control:
    if gocount > 0:
        na "While I'm walking along the way,{w=.3} a light shines down onto the handrail.{w=.3} And I can see the words that were probably written by some celebrities.{w=.3} I think about what they say…."
    elif gocount == -7:
        na "Yunwoo…."
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    elif gocount == -6:
        na "Mommy…."
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    elif gocount == -5:
        na "Daddy…."
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    elif gocount == -4:
        na "Hye-na…."
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    elif gocount == -3:
        na "What if I just go back…?"
        $ achievement.grant('KNDW_LEFT')
        hide screen bridge
        scene black
        with d3
        if persistent.part21 is None:
            $ persistent.con06 = True
            $ persistent.unlock_14 = True
            $ persistent.con += 1
            $ persistent.gall += 1
            $ persistent.replay += 1
            $ achievement.progress('KNDW_PROGRESS', 20)
            $ achievement.progress('KNDW_CONCEPT', 8)
            if achievement.has('KNDW_KILLER'):
                $ achievement.progress('KNDW_ART', 27)
            else:
                $ achievement.progress('KNDW_ART', 26)
            if not persistent.blind is True:
                call unlocked
        jump ending
    elif gocount == -2:
        na "What's the use of thinking now?"
        $ achievement.progress('KNDW_LEFT', 2)
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    elif gocount == -1:
        na "No,{w=.3} I can't go back."
        $ achievement.progress('KNDW_LEFT', 1)
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    if gocount == 6:
        na "Well,{w=.3} yes,{w=.3} if I continue to be alive,{w=.3} maybe I could have some days full of hope,{w=.3} someday in the future."
        na "But now,{w=.3} I'm not sure I can live on."
        $ achievement.grant('KNDW_RIGHT')
        hide screen bridge
        scene black
        with d3
        if persistent.part21 is None:
            $ persistent.con06 = True
            $ persistent.unlock_14 = True
            $ persistent.con += 1
            $ persistent.gall += 1
            $ persistent.replay += 1
            $ achievement.progress('KNDW_PROGRESS', 20)
            $ achievement.progress('KNDW_CONCEPT', 8)
            if achievement.has('KNDW_KILLER'):
                $ achievement.progress('KNDW_ART', 27)
            else:
                $ achievement.progress('KNDW_ART', 26)
            if not persistent.blind is True:
                call unlocked
        jump edge
    elif gocount == 5:
        na "What the hell is there beyond this deep and hopeless tunnel?"
        $ achievement.progress('KNDW_RIGHT', 5)
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    elif gocount == 4:
        na "I didn't even dream of such a good life.{w=.3} It's like a happy movie."
        $ achievement.progress('KNDW_RIGHT', 4)
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    elif gocount == 3:
        na "I didn't expect such good luck."
        $ achievement.progress('KNDW_RIGHT', 3)
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    elif gocount == 2:
        na "There's no reversal in my life - it's done."
        $ achievement.progress('KNDW_RIGHT', 2)
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    elif gocount == 1:
        na "If your spring day is like this, can you really bear it?"
        $ achievement.progress('KNDW_RIGHT', 1)
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    else:
        sv "[gui.choice]"
        sv "Left arrow key: [gui.left] Right arrow key: [gui.right]"
        call screen bridge_control
    hide screen bridge
    scene black with d
    if persistent.part21 is None:
        $ persistent.con06 = True
        $ persistent.unlock_14 = True
        $ persistent.con += 1
        $ persistent.gall += 1
        $ persistent.replay += 1
        $ achievement.progress('KNDW_PROGRESS', 20)
        $ achievement.progress('KNDW_CONCEPT', 8)
        if achievement.has('KNDW_KILLER'):
            $ achievement.progress('KNDW_ART', 27)
        else:
            $ achievement.progress('KNDW_ART', 26)
        if not persistent.blind is True:
            call unlocked
label edge:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene bridge at sepia
        show expression 'part_22_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part22]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part22]', style='centered_text')
    $ progress = 22
    pause 3
    scene black with blind
    $ save_name = "Edge of the world"
    $ show_quick_menu = True
    if wallet == 1:
        show expression Text ('Five minutes ago', style='extext') at times with d3
        scene black with d3
        scene han with f
        woo "I climbed up to the bridge,{w=.3} but can't find Ga-yeon."
        woo "Probably she hasn't jumped into the river yet."
        woo "She didn't.{w=.3} I believe in her."
        woo "I will definitely find her."
    scene black with blind
    show expression Text ('Three minutes ago', style='extext') at times with d3
    scene black with d3
    pause 1
    show screen bridge
    na "I pass by a number of messages on the handrail one by one."
    na "I look upwards,{w=.3} continuously blinking."
    na "Soon,{w=.3} I feel my eyes filling with tears."
    na "I feel the trembling on my lips getting stronger."
    hide screen bridge
    scene eotw0 at zoom_blur
    with d3
    na "Trying to bear these annoying things,{w=.3} I keep walking forwards.{w=.3} But soon,{w=.3} I turn my body to the handrail."
    scene eotw0 with d3
    na "Looking up at the dark sky,{w=.3} I grab the handrail with both hands,{w=.3}"
    scene eotw1 at zoom_blur with d3
    scene eotw1 with d3
    na "and let a flood of tears gush out."
    pause 3
    na "I empty my mind with those tears,{w=.3} and cry my eyes out."
    pause 3
    na "Even though my eyes are wide open,{w=.3} I can't see anything because of the tears."
    na "Yes,{w=.3} this is me."
    na "This is a reality.{w=.3} This is where I am now."
    na "I have done my best at all times."
    na "Before,{w=.3} I believed it would be alright if I make more effort and work harder than others."
    na "But now,{w=.3} I'm just a very young and weak child in this world."
    scene eotw1 at zoom_blur with d3
    $ show_quick_menu = False
    scene black
    $ renpy.transition(d)
    $ renpy.pause(1, hard = True)
    show expression Text ("I'm scared of the world.", style='extext')
    $ renpy.transition(d)
    $ renpy.pause(1, hard = True)
    $ renpy.pause(1, hard = True)
    $ renpy.transition(shock)
    $ renpy.pause(1, hard = True)
    scene black
    $ renpy.transition(d)
    $ renpy.pause(1, hard = True)
    show expression Text ("I am scared of people.", style='extext')
    $ renpy.transition(d)
    $ renpy.pause(1, hard = True)
    $ renpy.pause(1, hard = True)
    $ renpy.transition(shock)
    $ renpy.pause(1, hard = True)
    scene black
    $ renpy.transition(d)
    $ renpy.pause(1, hard = True)
    show expression Text ("Why do you keep saying,{w=.3} \"Live\"?", style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    $ renpy.pause(1, hard = True)
    $ renpy.transition(shock)
    $ renpy.pause(1, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ("How could you keep saying…,{w=.3} \"Live\" to me!", style='extext')
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    $ renpy.transition(shock2)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    pause 1
    $ show_quick_menu = True
    scene shoes
    with d
    na "I take off my left shoe by holding the back of that shoe down with my right foot."
    na "Then,{w=.3} I take off the right shoe in the same way."
    na "I wipe my eyes with my left hand.{w=.3} I am still sniffling."
    na "I hold the handrail tightly by gripping it with my left hand."
    na "I take a long breath,{w=.3} and my lips tremble."
    na "I lift up my right leg and put it on the handrail."
    na "Because of the cold,{w=.3} I tightly close my eyes and then,{w=.3} open them again."
    na "When I lower my right leg on the outside of the handrail,{w=.3} my left leg is lifted because of the height of the handrail."
    na "I put my right foot on the ground,{w=.3} and then,{w=.3} move my left leg up and over the handrail."
    na "My hands,{w=.3} while tightly grasping the rail,{w=.3} start quivering."
    na "And my heart beats violently."
    na "Now finally,{w=.3} I put my left foot down on the ground."
    na "Breathing hard,{w=.3} I lightly close my eyes."
    scene black with d3
    $ show_quick_menu = False
    centered "{cps=15}If I release my hands grabbing the rail,{w=.3}\nI will lose my balance and fall into the river.{/cps}"
    centered "{cps=15}Release the hands,{w=.3} then it's done.{/cps}"
    centered "{cps=15}Just release.{/cps}"
    centered "{cps=15}Then I can be free from this terrible hell.{/cps}"
    centered "{cps=15}I don't need to struggle to survive any more.{/cps}"
    centered "{cps=15}I'm going to a world where no one points a finger at me.{/cps}"
    centered "{cps=15}I'm dying and disappearing from this disgusting place.{/cps}"
    centered "{cps=15}And will be free soon.{/cps}{w=1}"
    stop music fadeout 3
    $ renpy.end_replay()
    if wallet == 1:
        scene black
        $ renpy.transition(d3)
        $ renpy.pause(3, hard = True)
        show expression Text ('"Choi Ga-yeon!"', style='extext')
        $ renpy.transition(d3)
        $ renpy.pause(3, hard = True)
        scene black
        $ renpy.transition(d3)
        $ renpy.pause(3, hard = True)
        if persistent.part22 is None:
            $ persistent.unlock_27 = True
            $ persistent.gall += 1
            $ persistent.replay += 1
            $ achievement.progress('KNDW_PROGRESS', 21)
            if achievement.has('KNDW_KILLER'):
                $ achievement.progress('KNDW_ART', 28)
            else:
                $ achievement.progress('KNDW_ART', 27)
            if not persistent.blind is True:
                call unlocked
        jump epilogue
    else:
        if persistent.part22 is None:
            $ persistent.unlock_27 = True
            $ persistent.gall += 1
            $ persistent.replay += 1
            $ achievement.progress('KNDW_PROGRESS', 21)
            if achievement.has('KNDW_KILLER'):
                $ achievement.progress('KNDW_ART', 28)
            else:
                $ achievement.progress('KNDW_ART', 27)
            if not persistent.blind is True:
                call unlocked
        $ gp = 0
        $ gc = 0
        $ gg = 0
        $ gm = 0
        $ gr = 0
        $ gd = 0
        if not persistent.blind is True:
            scene corruption at sepia
            show expression 'part_23_sepia' at part_polaroid
            show born_balls at main_balls
            show gradiant
            with centerblind
            show expression Text ('[gui.part23]', style='part_title')
            with d
        else:
            scene black
            show expression Text ('[gui.part23]', style='centered_text')
        $ progress = 23
        pause 3
        scene black with d
        $ save_name = "Accident"
        sv "You fell from the bridge and died."
        scene corruption with d3
        pause 3
        if persistent.part23 is None:
            $ persistent.con08 = True
            $ persistent.unlock_19 = True
            $ persistent.con += 1
            $ persistent.gall += 1
            $ persistent.replay += 1
            $ achievement.progress('KNDW_CONCEPT', 9)
            if achievement.has('KNDW_KILLER') and persistent.unlock_15 is True:
                $ achievement.grant('KNDW_ART')
            elif achievement.has('KNDW_KILLER') or persistent.unlock_15 is True:
                $ achievement.progress('KNDW_ART', 29)
            else:
                $ achievement.progress('KNDW_ART', 28)
            $ achievement.grant('KNDW_ACCIDENT')
            if achievement.has('KNDW_KILLER') and achievement.has('KNDW_ACCIDENT'):
                $ achievement.grant('KNDW_MURDERER')
            if achievement.has('KNDW_KILLER') and achievement.has('KNDW_ACCIDENT') and achievement.has('KNDW_MASTER'):
                $ achievement.grant('KNDW_VOTERS')
            if achievement.has('KNDW_GAMEOVER') and achievement.has('KNDW_IDENTIFY') and achievement.has('KNDW_DEMO') and achievement.has('KNDW_CONCEPT') and achievement.has('KNDW_DIARY') and achievement.has('KNDW_ART') and achievement.has('KNDW_OST') and achievement.has('KNDW_PROGRESS') and achievement.has('KNDW_OBJECT') and achievement.has('KNDW_MURDERER') and achievement.has('KNDW_FRONTIER') and achievement.has('KNDW_START') and achievement.has('KNDW_VOTERS') and achievement.has('KNDW_ADULT') and achievement.has('KNDW_LEFT') and achievement.has('KNDW_RIGHT')  and achievement.has('KNDW_ONLOOKER') and achievement.has('KNDW_VIDEO'):
                $ achievement.grant('KNDW_MASTER_FRONTIER')
                $ achievement.grant('KNDW_SPONSOR')
            if not persistent.blind is True:
                call unlocked
        return
label epilogue:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    if not persistent.blind is True:
        scene bridge at sepia
        show part24_sepia
        show expression 'part_24_sepia' at part_polaroid
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.part24]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.part24]', style='centered_text')
    pause 3
    scene black with d
    $ progress = 24
    play music 'bgm/Sea of nectar.opus' fadein 3
    scene doa_1 with blind
    pause 1
    $ show_quick_menu = True
    na "When I'm about to release my hands,{w=.3} I hear Yunwoo's voice like an echo a long way away.{w=.3} I open my eyes and turn my head towards the sound.{w=.3} And I see Yunwoo is running toward me."
    na "As soon as I see him,{w=.3} I suddenly burst into tears again,{w=.3} and to force back the tears,{w=.3} I desperately grit my teeth.{w=.3} Really,{w=.3} I knew he will come to me.{w=.3} And now,{w=.3} Yunwoo is running toward me to save me."
    y "No!{w=.3} Stop!{w=.3} Hold it tight!!"
    na "I see Yunwoo is getting closer and closer to me."
    scene doa_2 with d
    p "Go away!{w=.3} If you come closer,{w=.3} I will jump!"
    na "With a tear-stained face,{w=.3} I cry out to him to stop.{w=.3} He saw the video,{w=.3} and I can't be in his arms any more.{w=.3} I mustn't.{w=.3} I must not make him hurt for the rest of his life,{w=.3} and it's too selfish.{w=.3} I must end here.{w=.3} I don't have any more hope and courage."
    y "Ga-yeon,{w=.3} Hold on!{w=.3} You can't do that!"
    na "Catching his breath,{w=.3} he walks towards me,{w=.3} and at about two meters away, he holds out his right hand to me, urging me to stop."
    p "Shut up!{w=.3} It's over!{w=.3} Over!{w=.3} Go away!{w=.3} Don't come any closer!"
    na "I scream out.{w=.3} He slowly lowers his hand,{w=.3} and now tries to persuade me."
    scene doa_5 with d
    y "Please,{w=.3} Ga-yeon!{w=.3} Just calm down and let's have a talk.{w=.3} Just give me a second.{w=.3} If you leave me alone,{w=.3} then how can I live on without you?!{w=.3} Are you just playing with my emotions?{w=.3} Seriously?!"
    y "Alright,{w=.3} even if you are,{w=.3} I'm still fine.{w=.3} And what about your family?{w=.3} How could your parents and Hye-na live without you?"
    p "Play with you?{w=.3} How could you say that?!{w=.3} That's absolutely not true!{w=.3} It is real! My heart is true!"
    na "What he said makes me crazy for an instant,{w=.3} and I shout without thinking.{w=.3} My shout echoes through the bridge.{w=.3} Yunwoo slowly comes closer and closer to me,{w=.3} staring at me."
    y "Okay,{w=.3} then,{w=.3} listen to me.{w=.3} What you've felt is true,{w=.3} and also my heart is true.{w=.3} So,{w=.3} let's go back home together.{w=.3} Ga-yeon,{w=.3} the river is bloody cold."
    na "No,{w=.3} don't let him persuade you,{w=.3} Ga-yeon.{w=.3} It's over.{w=.3} I'm just a loser."
    scene doa_3 with d
    na "Thinking this way,{w=.3} I turn my head back again,{w=.3} and look down at the river.{w=.3} It looks blurry through my tears,{w=.3} but I can see the sloshing black water of the river,{w=.3} and I feel giddy.{w=.3} I turn my head to Yunwoo.{w=.3} I stare at him.{w=.3} The moment of decision is close at hand."
    y "Live,{w=.3} Ga-yeon,{w=.3} please.{w=.3} I'll be with you.{w=.3} Please come back with me.{w=.3} All your pains…,{w=.3} they will become nothing.{w=.3} Time will heal all your sorrow."
    if not _preferences.language == 'Korean' and not _preferences.language == 'Chinese':
        y "I'm sure there will come a day we can look back on this day with a smile.{w=.3} But,{w=.3} for now,{w=.3} please hang in there.{w=.3} I'll help you.{w=.3} I'll be with you,{w=.3} Ga-yeon,{w=.3} please."
    na "He says,{w=.3} gently reaching out his hand again to me.{w=.3} I see his hands,{w=.3} and then,{w=.3} his face.{w=.3} He slowly nods his head,{w=.3} and comes closer to me little by little."
    na "Weeping and sniffling,{w=.3} I grit my teeth.{w=.3} If I hold his hand,{w=.3} I go back home with him,{w=.3} and if not,{w=.3} I fall down into the river.{w=.3} That scary-looking black river."
    na "Now he is standing very close.{w=.3} He could take hold of me.{w=.3} I have to choose whether to die,{w=.3} or go back home.{w=.3} But…,{w=.3} what should I do?{w=.3} I'm afraid of myself.{w=.3} I have no idea how to overcome all these things around me,{w=.3} and what I can do even if I choose to live on."
    na "I become confused for a while,{w=.3} and then,{w=.3} I see him again.{w=.3} In spite of his smile on his lips,{w=.3} his eyes are full of tears.{w=.3} And it makes me release my right hand from the guardrail,{w=.3} and reach out towards him."
    scene doa_4 with d
    y "I promise,{w=.3} Ga-yeon.{w=.3} I'll never leave you alone any more.{w=.3} I'll always be with you."
    na "I nod my head,{w=.3} and I realize I'm smiling at him,{w=.3} even before I knew it.{w=.3} I slowly put out my hand to reach him."
    stop music
    scene black with d5
    $ show_quick_menu = False
    if persistent.teddy is not True and persistent.blind is not True:
        centered "However,{w=.3} at the moment when we are just about to grab each other,{w=.3} I suddenly feel dizzy.{w=.3} Then,{w=.3} an extreme fear which I've never experienced before,{w=.3} penetrates into my heart.{w=3}"
    $ renpy.end_replay()
    if persistent.part24 is None:
        $ persistent.gall += 2
        $ persistent.replay += 1
        $ persistent.unlock_28 = True
        $ achievement.progress('KNDW_PROGRESS', 24)
        if not persistent.blind is True:
            call unlocked
    pause 1
    if persistent.teddy is True or persistent.blind is True:
        scene dw2017_3 with f3
        $ persistent.unlock_30 = True
        if persistent.blind is True:
            $ persistent.unlock_29 = True
        pause 5
        jump ending
    else:
        scene black
        show dw2017_0 at fell
        with d3
        pause 1
        scene dw2017_1 with f3
        pause 1
        scene dw2017_2 with f3
        scene black with f3
        $ persistent.unlock_29 = True
        $ persistent.dw2017 = True
        jump gameover
label ending:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    play music 'bgm/Love song.opus' fadein 3
    if not gocount == -3:
        if not persistent.blind is True:
            scene wall at sepia
            show wall_sepia
            show expression 'part_25_sepia' at part_polaroid
            show born_balls at main_balls
            show gradiant
            with centerblind
            show expression Text ('[gui.part25]', style='part_title')
            with d
        else:
            scene black
            show expression Text ('[gui.part25]', style='centered_text')
        $ progress = 25
        $ save_name = "Flowery mornings and moonlit nights"
        pause 3
        scene black with d
    scene caffe with blind
    $ show_quick_menu = True
    woo "An hour left before the interview."
    woo "Though Hye-na asked me to interview her older sister,{w=.3} it's still ridiculous…."
    with f
    show g_question
    with d5
    ga "Hello,{w=.3} may I come in?{w=.3} I made an appointment for an interview today."
    woo "While wiping a wine bottle,{w=.3} I hear a woman's voice,{w=.3} and lift my head up.{w=.3} Oh,{w=.3} there she is."
    pm "Oh,{w=.3} you must be Choi Ga-yeon.{w=.3} Glad to see you.{w=.3} Please have a seat."
    woo "Nodding my head,{w=.3} I put the bottle down on the table and say to her."
    hide g_question
    show gb
    ga "Yes…."
    woo "She answers in a very small voice.{w=.3} After slowly pulling back the chair,{w=.3} she sits on it."
    woo "After I glance down at her picture in the resume on the table,{w=.3} I say to her."
    pm "Then,{w=.3} shall we begin the interview?"
    woo "She answers in a small voice,{w=.3} with her head bowed.{w=.3} She looks somewhat uneasy."
    ga "Okay…."
    woo "Well…,{w=.3} not good."
    woo "Adjusting my glasses with my right hand,{w=.3} I look her in the eyes,{w=.3} and say to her."
    pm "Could you raise your head,{w=.3} please?"
    woo "Then,{w=.3} she looks at me – although it was for just a moment – and replies."
    ga "Yeah…."
    woo "Then,{w=.3} she rolls her eyes down to the ground again."
    pm "Is there something interesting on the ground?{w=.3} You don't want to have an interview today?"
    woo "I say to her,{w=.3} with a smile.{w=.3} Finally,{w=.3} she lifts her head up,{w=.3} and answers in a very small voice,{w=.3} as if she's mumbling to herself."
    ga "I'm sorry…."
    pm "You weren't forced to have an interview today,{w=.3} were you?{w=.3} Do you really want to work here?"
    hide gb
    show g_shock
    ga "No,{w=.3} I wasn't.{w=.3} I came here today to get a job here.{w=.3} I was not forced."
    woo "She hurriedly answers my question,{w=.3} shaking her head."
    pm "Let's see….{w=.3} Oh,{w=.3} you look younger than you are….{w=.3} Hm….{w=.3} You worked as a coordinator at a hospital….{w=.3} Then,{w=.3} you're probably good at serving customers….{w=.3} Oh,{w=.3} have you worked part time before?"
    hide g_shock
    show g_question
    ga "Uh…,{w=.3} yes,{w=.3} I've done a paper route,{w=.3} milk route,{w=.3} and….{w=.3} Also worked in a family restaurant."
    woo "Her voice becomes clear,{w=.3} and it sounds pretty charming."
    pm "You have a beautiful voice.{w=.3} Why were you lacking in confidence before?"
    ga "Uh…,{w=.3} that was…,{w=.3} uhm…."
    woo "She lowers her head with hesitation,{w=.3} and I find she's unnaturally blinking her eyes."
    woo "Hm…,{w=.3} weird.{w=.3} She's quite weird."
    woo "I thought she just lacks confidence,{w=.3} but….{w=.3} Is there something wrong with her?"
    hide g_question
    show g_tear
    with d5
    woo "While I'm thinking this way,{w=.3} it looks as if she's about to cry,{w=.3} and seconds later,{w=.3} she starts crying."
    if persistent.vibrate is True:
        $ renpy.vibrate(1)
    else:
        pass
    with shock
    pm "My goodness!{w=.3} Hey,{w=.3} oh dear,{w=.3} what's wrong with you?{w=.3} Huh?{w=.3} Why are you crying?"
    hide g_tear with d5
    woo "I'm so flummoxed,{w=.3} and quickly stand up to approach her.{w=.3} But she suddenly jumps up out of the chair,{w=.3} then runs away from the store."
    pause 1
    pm "What….{w=.3} What the hell is going on with her?"
    if gocount == -3:
        scene black with d3
        stop music
        jump gameover
    show h_smile
    with f3
    h "Hey boss,{w=.3} are you mad at me?"
    woo "When I'm checking the order list,{w=.3} Hye-na comes up to me and says."
    woo "I pretend I didn't hear her,{w=.3} and just keep checking."
    hide h_smile
    show h_poker
    with d5
    h "I'm sorry.{w=.3} I wanted to tell you about her,{w=.3} but….{w=.3} If I told you,{w=.3} you wouldn't have interviewed her."
    h "But she has to work.{w=.3} She needs a job.{w=.3} You saw her.{w=.3} If she fails to get a job,{w=.3} I have no idea what will happen to her."
    woo "Saying this,{w=.3} she gently lays her hand on my elbow.{w=.3} But I pretend I don't care about her at all,{w=.3} and just continue to check the list."
    h "Please help her.{w=.3} You can save her.{w=.3} Once you offer a job to her,{w=.3} I'm sure,{w=.3} she'll never disappoint you."
    pm "You're so annoying!{w=.3} I'm busy now.{w=.3} Stop bothering me."
    hide h_poker
    show h_question
    with d5
    pause 1
    hide h_question
    show h_poker
    with d5
    woo "Saying this,{w=.3} I move my arm and her hand drops away from my elbow.{w=.3} Then,{w=.3} she stands without saying anything for a while,{w=.3} then,{w=.3} turns around.{w=.3} Before she walks away,{w=.3} I say to her in a low voice."
    pm "The interview hasn't finished yet.{w=.3} If she wants to get a job,{w=.3} tell her to come here again,{w=.3} tomorrow."
    hide h_poker
    show h_question
    with d5
    scene black with d3
    scene caffe with d5
    woo "After finishing a band rehearsal,{w=.3} Yunwoo drops by Ga-yeon's cafe to see her."
    show h_smile at right
    with d5
    h "Yunwoo!{w=.3} Did you come to see Ga-yeon?"
    hide h_smile
    show h_smile_gray at right
    show y_smile at left
    with d5
    y "Yeah.{w=.3} Because Taejin was going to meet someone in Marronnier Park,{w=.3} I just left him at the station and thought I'd drop by here on my way home."
    hide y_smile
    show y_smile_gray at left
    with d5
    woo "While Yunwoo and Hye-na are exchanging words,{w=.3} there's a strange noise in the cafe."
    play sound 'se/plate.opus'
    with shock
    hide h_smile_gray
    hide y_smile_gray
    show h_question_gray at right
    show y_think_gray at left
    with d5
    woo "\"Aargh!{w=.3} Damn!{w=.3} What the hell are you doing!\""
    woo "\"Sorry!{w=.3} I'm sorry!{w=.3} Are you alright?\""
    woo "\"Are you blind or something?!\""
    hide h_question_gray
    show h_smile at right
    with d5
    h "Oh- no….{w=.3} What has she done now?{w=.3} Hey,{w=.3} wait a few minutes outside,{w=.3} will you?{w=.3} I'll tell Ga-yeon you're waiting for her after we clean up that mess,{w=.3} ok?"
    hide h_smile
    show h_smile_gray at right
    hide y_think_gray
    show y_smile at left
    with d5
    y "Alright,{w=.3} thanks."
    scene black with d3
    scene wall
    show wall_gayeon_sigh
    show wall_yunwoo
    with d3
    ga "Phew…."
    woo "Ga-yeon gives Yunwoo a cup of coffee,{w=.3} and lets out a deep sigh.{w=.3} Yunwoo has a sip of it,{w=.3} then asks Ga-yeon."
    y "So,{w=.3} what happened to you this time?"
    hide wall_gayeon_sigh
    show wall_gayeon_glaring
    with d5
    ga "It's all because of you.{w=.3} It happened because I saw you coming into the cafe."
    woo "Tapping her foot on the ground and glaring at Yunwoo,{w=.3} she puts her two hands into the pockets of her apron,{w=.3} and grumbles at him.{w=.3} Yunwoo chuckles,{w=.3} and says to her,{w=.3} looking ahead."
    y "How could you say that.{w=.3} You are the one who made a mistake."
    hide wall_gayeon_glaring
    show wall_gayeon_normal
    with d5
    woo "She stretches her back once,{w=.3} and then,{w=.3} says,{w=.3} looking ahead."
    ga "Okay,{w=.3} then,{w=.3} let's say it was my fault."
    y "Uh-oh,{w=.3} no,{w=.3} I mean,{w=.3} it is obviously your fault."
    ga "Alright,{w=.3} alright.{w=.3} Let's say it is."
    y "Okay,{w=.3} you win!{w=.3} It was my fault."
    hide wall_gayeon_normal
    show wall_gayeon_side
    with d5
    ga "You're right.{w=.3} It IS your fault."
    woo "Ga-yeon,{w=.3} who wins in this small argument,{w=.3} giggles for some time while looking down.{w=.3} Then,{w=.3} she raises her gaze again to look at Yunwoo,{w=.3} and asks him."
    ga "So,{w=.3} you finished the morning rehearsal?"
    y "Yes.{w=.3} After that,{w=.3} since Taejin had an appointment near here,{w=.3} we came to the station together,{w=.3} then I dropped by here."
    ga "Did you?{w=.3} So,{w=.3} how's my coffee?"
    hide wall_yunwoo
    show wall_yunwoo_side
    with d5
    y "Hm,{w=.3} it's great.{w=.3} Actually I don't like this straw,{w=.3} but anyway,{w=.3} it tastes good."
    ga "I made it."
    y "Uh-huh?{w=.3} I feel your coffee has become a little bit strong.{w=.3} But I love it."
    woo "It makes Ga-yeon smile,{w=.3} and she asks him."
    ga "Do you want me to pack a lunch for you later?"
    y "No,{w=.3} thank you.{w=.3} Don't do that.{w=.3} Just come yourself."
    ga "But Taejin and Wooseok said they liked my cooking."
    y "No- if you go over there,{w=.3} it's enough.{w=.3} Just take care of your health."
    ga "Hey,{w=.3} you heard the doctor said I'm getting better."
    hide wall_yunwoo_side
    show wall_yunwoo
    with d5
    y "Yes,{w=.3} but you haven't fully recovered yet."
    hide wall_gayeon_side
    show wall_gayeon_sigh
    with d5
    ga "Yes,{w=.3} but…."
    y "So,{w=.3} take good care of yourself."
    hide wall_gayeon_sigh
    show wall_gayeon_normal
    with d5
    ga "Okay,{w=.3} I will."
    scene black with d3
    scene daehangno with d3
    show i_think at right
    with d5
    pa "I didn't even think I would be obsessed with a guy,{w=.3} younger than me."
    hide i_think
    show i_think_gray at right
    show y_smile at left
    with d5
    y "Oh,{w=.3} hi,{w=.3} how are you?"
    hide y_smile
    show y_smile_gray at left
    hide i_think_gray
    show i_smile at right
    with d5
    pa "Oh,{w=.3} my!{w=.3} Hi,{w=.3} Yunwoo!{w=.3} You didn't hear what I was saying did you?"
    hide i_smile
    show i_smile_gray at right
    hide y_smile_gray
    show y_think at left
    with d5
    y "What?{w=.3} I don't….{w=.3} Oh,{w=.3} by the way,{w=.3} I thought you were going to meet Taejin."
    hide y_think
    show y_think_gray at left
    hide i_smile_gray
    show i_smile at right
    with d5
    pa "Yes,{w=.3} yes,{w=.3} I did.{w=.3} I met him,{w=.3} but….{w=.3} Uh…,{w=.3} so….{w=.3} Oh,{w=.3} there's a good franchise cafe near here,{w=.3} and I was going there."
    hide i_smile
    show i_smile_gray at right
    hide y_think_gray
    show y_smile at left
    with d5
    y "Okay."
    hide y_smile
    show y_smile_gray at left
    hide i_smile_gray
    show i_smile at right
    with d5
    pa "However,{w=.3} what're you doing here?"
    hide i_smile
    show i_smile_gray at right
    hide y_smile_gray
    show y_smile at left
    with d5
    y "Oh,{w=.3} I'm on my way home after meeting someone."
    hide y_smile
    show y_smile_gray at left
    hide i_smile_gray
    show i_smile at right
    with d5
    pa "Uh-huh?{w=.3} Your girlfriend?{w=.3} You met your girlfriend?{w=.3} Taejin said that.{w=.3} I want to see her,{w=.3} too.{w=.3} Let's get together sometime!"
    hide i_smile
    show i_smile_gray at right
    hide y_smile_gray
    show y_smile at left
    with d5
    y "She always goes to our concerts.{w=.3} Feel free to go anytime too.{w=.3} You'll likely see her there."
    hide y_smile
    show y_smile_gray at left
    hide i_smile_gray
    show i_smile at right
    with d5
    pa "Sounds great!{w=.3} Alright,{w=.3} then,{w=.3} see you soon!"
    hide i_smile
    show i_smile_gray at right
    hide y_smile_gray
    show y_smile at left
    with d5
    y "Okay,{w=.3} then,{w=.3} bye."
    scene black with d3
    scene wall with d5
    woo "Late spring of 2013,"
    woo "I haven't died.{w=.3} I'm still alive."
    woo "I have no idea how my life may change."
    woo "It may be tougher than my yesterdays,{w=.3} or happier."
    woo "Yes,{w=.3} right now I think I'm having a happier life."
    woo "With those who take care of me,"
    woo "with those who worry about me,"
    woo "with those who give me unconditional love,"
    woo "and with you who always support me,"
    woo "I breathe in the world where you are,"
    woo "and I live on,{w=.3} in the world where you are."
    scene black with d3
    scene rooml
    show g_tear
    with d3
    ga "Hey,{w=.3} by the way…,{w=.3} can you feed me?{w=.3} I think…,{w=.3} I'm having your baby.{w=1}"
    scene black
    $ renpy.transition(Dissolve(3))
    $ renpy.pause(3, hard = True)
    scene mart
    show e_question
    with d3
    $ angelname = 'Seol-ah'
    ex "Wow,{w=.3} she was pregnant.{w=1}"
    scene black with d3
    $ renpy.end_replay()
    if persistent.ending is None:
        $ persistent.unlock_15 = True
        $ persistent.bgm13 = True
        $ persistent.einterviewer = True
        $ persistent.eangel = True
        $ persistent.char += 2
        $ persistent.con += 4
        $ persistent.gall += 2
        $ persistent.bgm += 1
        $ persistent.replay += 1
        if achievement.has('KNDW_KILLER') and achievement.has('KNDW_ACCIDENT'):
            $ achievement.grant('KNDW_ART')
        elif achievement.has('KNDW_KILLER') or achievement.has('KNDW_ACCIDENT'):
            $ achievement.progress('KNDW_ART', 31)
        else:
            $ achievement.progress('KNDW_ART', 30)
        $ achievement.grant('KNDW_IDENTIFY')
        $ achievement.grant('KNDW_CONCEPT')
        $ achievement.grant('KNDW_PROGRESS')
        $ achievement.grant('KNDW_OST')
        $ achievement.grant('KNDW_MASTER')
        if achievement.has('KNDW_KILLER') and achievement.has('KNDW_ACCIDENT') and achievement.has('KNDW_MASTER'):
            $ achievement.grant('KNDW_VOTERS')
        if achievement.has('KNDW_GAMEOVER') and achievement.has('KNDW_IDENTIFY') and achievement.has('KNDW_DEMO') and achievement.has('KNDW_CONCEPT') and achievement.has('KNDW_DIARY') and achievement.has('KNDW_ART') and achievement.has('KNDW_OST') and achievement.has('KNDW_PROGRESS') and achievement.has('KNDW_OBJECT') and achievement.has('KNDW_MURDERER') and achievement.has('KNDW_FRONTIER') and achievement.has('KNDW_START') and achievement.has('KNDW_VOTERS') and achievement.has('KNDW_ADULT') and achievement.has('KNDW_LEFT') and achievement.has('KNDW_RIGHT')  and achievement.has('KNDW_ONLOOKER') and achievement.has('KNDW_VIDEO'):
            $ achievement.grant('KNDW_MASTER_FRONTIER')
            $ achievement.grant('KNDW_SPONSOR')
        if not persistent.blind is True:
            call unlocked
    jump credits
label credits:
    $ gp = 0
    $ gc = 0
    $ gg = 0
    $ gm = 0
    $ gr = 0
    $ gd = 0
    stop music
    play music 'bgm/Sea of nectar.opus' fadein 3
    scene black with d
    sv "You married Yunwoo, lived happily together, and gave birth to a daughter."
    sv "Thank you for playing Discouraged Workers. We are YGGDRASIL STUDIO."
    if persistent.blind is not True and not renpy.variant("small"):
        scene expression 'ending' with d
        show expression Text ('[gui.credits]', style='credits_title')
        show expression Text ('{b}Lee Yunseok{/b}\n\nDirecting, Design, Programming,\nMusic, Sound, Writing,\nUI Design, Background CG, Object Sprites,\nPackaging, Video, Website\n-From April 21, 2013', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('{b}Lee Yunseok{/b}\n\nDirecting, Design, Programming,\nMusic, Sound, Writing,\nUI Design, Background CG, Object Sprites,\nPackaging, Video, Website\n-From April 21, 2013', style='credits_text')
        show expression Text ('{b}chibilis studio{/b}\n\nAnimation, Character Sprites, CG Sprites\n-From March 10, 2015', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('{b}chibilis studio{/b}\n\nAnimation, Character Sprites, CG Sprites\n-From March 10, 2015', style='credits_text')
        show expression Text ('{b}Adam Patric Kratz{/b}\n\nEpilepsy Adviser\n-November 15, 2015~November 20, 2015', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('{b}Adam Patric Kratz{/b}\n\nEpilepsy Adviser\n-November 15, 2015~November 20, 2015', style='credits_text')
        show expression Text ('{b}Brian Connors{/b}\n\nEnglish Translation Adviser\n-June 3, 2015~July 1, 2017\n\n{b}Ga Younghee{/b}\n\nEnglish Translator\n-April 11, 2015~June 10, 2016', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('{b}Brian Connors{/b}\n\nEnglish Translation Adviser\n-June 3, 2015~July 1, 2017\n\n{b}Ga Younghee{/b}\n\nEnglish Translator\n-April 11, 2015~June 10, 2016', style='credits_text')
        show expression Text ('{b}IVY{/b}\n\nChinese Translator\n-July 25, 2016~February 10, 2018\n\n{b}Roman Koledin{/b}\n\nRussian Translator\n-August 28, 2016~December 7, 2017', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('[gui.credits]', style='credits_title')
        hide expression Text ('{b}IVY{/b}\n\nChinese Translator\n-July 25, 2016~February 10, 2018\n\n{b}Roman Koledin{/b}\n\nRussian Translator\n-August 28, 2016~December 7, 2017', style='credits_text')
        show expression Text ('{font=gui/fonts/Edo.ttf}{size=64}Project Gamer Japonés{/size}{/font}', style='credits_title')
        show expression Text ('{b}Oscar Ballona Centeno{/b}\n\nProject Leader in Spanish, Spanish Translator\n-From May 29, 2017\n\n{b}AxelBodga{/b}\n\nSpanish Editor\n-From May 29, 2017\n\n{b}Yisus{/b}\n\nSpanish Translator\n-From May 29, 2017', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('{font=gui/fonts/Edo.ttf}{size=64}Project Gamer Japonés{/size}{/font}', style='credits_title')
        hide expression Text ('{b}Oscar Ballona Centeno{/b}\n\nProject Leader in Spanish, Spanish Translator\n-From May 29, 2017\n\n{b}AxelBodga{/b}\n\nSpanish Editor\n-From May 29, 2017\n\n{b}Yisus{/b}\n\nSpanish Translator\n-From May 29, 2017', style='credits_text')
        show expression Text ('Old Version', style='credits_title')
        show expression Text ('{b}YANG{/b}\n\nMale sprites, CG sprites\n-April 8, 2015~September 13, 2015\n\n{b}Jeon Junsik{/b}\n\nUnofficial Demo Sprites\n-January 5, 2015~February 25, 2015\n\n{b}Kyle Fawcett{/b}\n\nEnglish Demo Translation Adviser\n-June 3, 2015~June 14, 2015', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('Old Version', style='credits_title')
        hide expression Text ('{b}YANG{/b}\n\nMale sprites, CG sprites\n-April 8, 2015~September 13, 2015\n\n{b}Jeon Junsik{/b}\n\nUnofficial Demo Sprites\n-January 5, 2015~February 25, 2015\n\n{b}Kyle Fawcett{/b}\n\nEnglish Demo Translation Adviser\n-June 3, 2015~June 14, 2015', style='credits_text')
        show expression Text ('Contributors', style='credits_title')
        show expression Text ('{b}ACOC, Aiman Sharul, Axel Mertes,\nBgame, Brandon Tanimoto, Brian Connors,\nBRISAK Kim Doohyeon, cheif.choi, Choi Irang,\nChoi Jihye, cloture, Danielle Bell,\nEdward N Puckering, Gary King, Gwak Jaeryeol,\nHan Ihyeong, Hoe Namyoon, Hong Eunki,\nHwang Daehoon, Hyojoon, James Emmerson,\nJeong Dongwon, Jeong Wookjin, Jeong Yoonsoo,{/b}', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('{b}ACOC, Aiman Sharul, Axel Mertes,\nBgame, Brandon Tanimoto, Brian Connors,\nBRISAK Kim Doohyeon, cheif.choi, Choi Irang,\nChoi Jihye, cloture, Danielle Bell,\nEdward N Puckering, Gary King, Gwak Jaeryeol,\nHan Ihyeong, Hoe Namyoon, Hong Eunki,\nHwang Daehoon, Hyojoon, James Emmerson,\nJeong Dongwon, Jeong Wookjin, Jeong Yoonsoo,{/b}', style='credits_text')
        show expression Text ('{b}Jianmin Zhang, Karina Schulze, Keira Val\'Azr,\nKim Hanseol, Kim Hyeoncheol, Kim Jaeseong,\nKim Jeongwoong, Kim Myeongwook,\nLee Changki, Lee Eunji, Lee Gunhae,\nLee Hyejin, Lee Jaewi, Light Twins, Lim Jisoo,\nMaddy Wootton, Marshall Proudfoot, Mirumu,\nMojaeng, Oh Hyeonjun, Park Hyeonjun,\nPark JoonKoo, Rewind, Sander Tieleman,\nsrwss, Sung Chanaul, YottaCho, Zerial.net{/b}', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('Contributors', style='credits_title')
        hide expression Text ('{b}Jianmin Zhang, Karina Schulze, Keira Val\'Azr,\nKim Hanseol, Kim Hyeoncheol, Kim Jaeseong,\nKim Jeongwoong, Kim Myeongwook,\nLee Changki, Lee Eunji, Lee Gunhae,\nLee Hyejin, Lee Jaewi, Light Twins, Lim Jisoo,\nMaddy Wootton, Marshall Proudfoot, Mirumu,\nMojaeng, Oh Hyeonjun, Park Hyeonjun,\nPark JoonKoo, Rewind, Sander Tieleman,\nsrwss, Sung Chanaul, YottaCho, Zerial.net{/b}', style='credits_text')
        show expression Text ('Rooters', style='credits_title')
        show expression Text ('{b}Caz Woolley, Game Dev Robot, Gamsadev,\nIndie GameDev Bot, Indie Game Lover,\nIndie Games Devel, IndieVideoGames,\nJoachim Dimitri Jensen, Kim Kyeongtae,\nKim Younghwan, Kurt Simon, Linda Lee King,\nPeter Christiansen, Sakimichi, Sebastian Haba,\nSpero Mcgee, The Indie Sloth, Vrachos,\nXin Liu, Yu Shinhyeon{/b}', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        hide expression Text ('Rooters', style='credits_title')
        hide expression Text ('{b}Caz Woolley, Game Dev Robot, Gamsadev,\nIndie GameDev Bot, Indie Game Lover,\nIndie Games Devel, IndieVideoGames,\nJoachim Dimitri Jensen, Kim Kyeongtae,\nKim Younghwan, Kurt Simon, Linda Lee King,\nPeter Christiansen, Sakimichi, Sebastian Haba,\nSpero Mcgee, The Indie Sloth, Vrachos,\nXin Liu, Yu Shinhyeon{/b}', style='credits_text')
        with blind
        $ renpy.pause(5, hard = True)
        scene black
        with d3
        $ renpy.pause(3, hard = True)
        show start:
            xalign .5 yalign .2
        show expression Text ('Special Thanks To', style='thanks_title')
        show expression Text ('{b}Christopher Rice, George Winston, Kim Sooyoung, Lee Illseong,\nPixabay, Shin Haechul, So Reyeon, Tom Rothamel, Valve Corporation{/b}', style='thanks_text')
        with d3
        $ renpy.pause(5, hard = True)
        scene black with d3
        $ renpy.pause(3, hard = True)
        $ persistent.ending = True
        $ persistent.unlock_31 = True
    stop music fadeout 3
    return
label gameover:
    if not persistent.blind is True:
        scene room at sepia
        show born_balls at main_balls
        show gradiant
        with centerblind
        show expression Text ('[gui.game_over]', style='part_title')
        with d
    else:
        scene black
        show expression Text ('[gui.game_over]', style='centered_text')
    pause 3
    scene black with d
    $ achievement.grant('KNDW_GAMEOVER')
    if achievement.has('KNDW_KILLER') and achievement.has('KNDW_ACCIDENT') and achievement.has('KNDW_MASTER'):
        $ achievement.grant('KNDW_VOTERS')
    if achievement.has('KNDW_GAMEOVER') and achievement.has('KNDW_IDENTIFY') and achievement.has('KNDW_DEMO') and achievement.has('KNDW_CONCEPT') and achievement.has('KNDW_DIARY') and achievement.has('KNDW_ART') and achievement.has('KNDW_OST') and achievement.has('KNDW_PROGRESS') and achievement.has('KNDW_OBJECT') and achievement.has('KNDW_MURDERER') and achievement.has('KNDW_FRONTIER') and achievement.has('KNDW_START') and achievement.has('KNDW_VOTERS') and achievement.has('KNDW_ADULT') and achievement.has('KNDW_LEFT') and achievement.has('KNDW_RIGHT')  and achievement.has('KNDW_ONLOOKER') and achievement.has('KNDW_VIDEO'):
        $ achievement.grant('KNDW_MASTER_FRONTIER')
        $ achievement.grant('KNDW_SPONSOR')
    if persistent.dw2017 is True and persistent.teddy is None:
        scene main_menu
        show gradiant
        with blind
        show expression Text('[gui.teddy]', style='unlocked_title') as text at spread
        show teddy at unlocked_center:
            zoom 2
        $ renpy.pause(3, hard = True)
    else:
        pause 3
    return
label unlocked:
    scene main_menu
    show gradiant
    with blind
    show expression Text('[gui.unlocked]', style='unlocked_title') as text at spread
    pause 1
    if persistent.part01 is None:
        $ gp = 1
        $ gm = 1
        $ gr = 1
        show expression 'arc_char_01' at unlocked_two_left
        show expression 'arc_char_03' at unlocked_two_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Characters +2", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_char_01'
        hide expression 'arc_char_03'
        show expression Text ("[gui.bgm02]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +1", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_01' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part01 = True
    elif persistent.part02 is None:
        $ gp = 1
        $ gc = 1
        $ gg = 1
        $ gm = 1
        $ gr = 1
        show expression 'arc_char_06' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Characters +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_char_06'
        show expression 'arc_con_01' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Concept +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_con_01'
        show expression 'arc_gall_01' at unlocked_three_left
        show expression 'arc_gall_02' at unlocked_center
        show expression 'arc_gall_03' at unlocked_three_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +3", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_01'
        hide expression 'arc_gall_02'
        hide expression 'arc_gall_03'
        show expression Text ("[gui.bgm03]\n[gui.bgm07]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +2", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_02' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part02 = True
    elif persistent.part03 is None:
        $ gp = 1
        $ gm = 1
        $ gr = 1
        show expression 'arc_char_02' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Characters +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_char_02'
        show expression Text ("[gui.bgm04]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +1", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_03' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part03 = True
    elif persistent.part04 is None:
        $ gp = 1
        $ gg = 1
        $ gm = 1
        $ gr = 1
        show expression 'arc_char_04' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Characters +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_char_04'
        show expression 'arc_gall_04' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_04'
        show expression Text ("[gui.bgm05]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +1", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_04' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part04 = True
    elif persistent.part05 is None:
        $ gg = 1
        $ gm = 1
        $ gr = 1
        show expression 'arc_gall_05' at unlocked_three_left
        show expression 'arc_gall_06' at unlocked_center
        show expression 'arc_gall_07' at unlocked_three_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +3", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_05'
        hide expression 'arc_gall_06'
        hide expression 'arc_gall_07'
        show expression Text ("[gui.bgm06]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +1", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_05' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part05 = True
    elif persistent.part07 is None:
        $ gc = 1
        $ gr = 1
        show expression 'arc_con_05' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Concept +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_con_05'
        show expression 'part_07' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part07 = True
    elif persistent.part08 is None:
        $ gm = 1
        $ gr = 1
        show expression Text ("[gui.bgm08]\n[gui.bgm09]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +2", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_08' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part08 = True
    elif persistent.part09 is None:
        $ gg = 1
        $ gm = 1
        $ gr = 1
        show expression 'arc_gall_08' at unlocked_two_left
        show expression 'arc_gall_09' at unlocked_two_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +2", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_08'
        hide expression 'arc_gall_09'
        show expression Text ("[gui.bgm10]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +1", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_09' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part09 = True
    elif persistent.part10 is None:
        $ gg = 1
        $ gr = 1
        show expression 'arc_gall_10' at unlocked_three_left
        show expression 'arc_gall_11' at unlocked_center
        show expression 'arc_gall_12' at unlocked_three_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +3", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_10'
        hide expression 'arc_gall_11'
        hide expression 'arc_gall_12'
        show expression 'part_10' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part10 = True
    elif persistent.part11 is None:
        $ gc = 1
        $ gg = 1
        $ gr = 1
        show expression 'arc_con_02' at unlocked_two_left
        show expression 'arc_con_07' at unlocked_two_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Concept +2", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_con_02'
        hide expression 'arc_con_07'
        show expression 'arc_gall_13' at unlocked_three_left
        show expression 'arc_gall_14' at unlocked_center
        show expression 'arc_gall_15' at unlocked_three_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +3", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_13'
        hide expression 'arc_gall_14'
        hide expression 'arc_gall_15'
        show expression 'part_11' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part11 = True
    elif persistent.part12 is None:
        $ gp = 1
        $ gr = 1
        show expression 'arc_char_07' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Characters +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_char_07'
        show expression 'part_12' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part12 = True
    elif persistent.part13 is None:
        $ gg = 1
        $ gr = 1
        show expression 'arc_gall_16' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_16'
        show expression 'part_13' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part13 = True
    elif persistent.part14 is None:
        $ gc = 1
        $ gg = 1
        $ gr = 1
        show expression 'arc_con_04' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Concept +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_con_04'
        show expression 'arc_gall_17' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_17'
        show expression 'part_14' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part14 = True
    elif persistent.part15 is None:
        $ gg = 1
        if persistent.obdrawer is True:
            $ gp = 1
            $ gd = 1
            show expression 'arc_char_07_e' at unlocked_center
            show expression Text ("{font=[gui.fontawesome]}{/font} Characters +1", color='#000') at unlocked_text
            pause 1.5
            hide expression 'arc_char_07_e'
            show expression 'arc_diary_01' at unlocked_five_left
            show expression 'arc_diary_02' at unlocked_three_left
            show expression 'arc_diary_03' at unlocked_center
            show expression 'arc_diary_04' at unlocked_three_right
            show expression 'arc_diary_05' at unlocked_five_right
            pause 1.5
            hide expression 'arc_diary_01'
            hide expression 'arc_diary_02'
            hide expression 'arc_diary_03'
            hide expression 'arc_diary_04'
            hide expression 'arc_diary_05'
            show expression 'arc_diary_06' at unlocked_five_left
            show expression 'arc_diary_07' at unlocked_three_left
            show expression 'arc_diary_08' at unlocked_center
            show expression 'arc_diary_09' at unlocked_three_right
            show expression 'arc_diary_10' at unlocked_five_right
            pause 1.5
            hide expression 'arc_diary_06'
            hide expression 'arc_diary_07'
            hide expression 'arc_diary_08'
            hide expression 'arc_diary_09'
            hide expression 'arc_diary_10'
            show expression 'arc_diary_11' at unlocked_five_left
            show expression 'arc_diary_12' at unlocked_three_left
            show expression 'arc_diary_13' at unlocked_center
            show expression 'arc_diary_14' at unlocked_three_right
            show expression 'arc_diary_15' at unlocked_five_right
            show expression Text ("{font=[gui.fontawesome]}{/font} Diary +15", color='#000') at unlocked_text
            pause 1.5
            hide expression 'arc_diary_11'
            hide expression 'arc_diary_12'
            hide expression 'arc_diary_13'
            hide expression 'arc_diary_14'
            hide expression 'arc_diary_15'
        if sigiveup <= -1:
            $ smoke = 1
            show expression 'arc_gall_25' at unlocked_two_left
            show expression 'arc_gall_18' at unlocked_two_right
            show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +2", color='#000') at unlocked_text
        else:
            show expression 'arc_gall_18' at unlocked_center
            show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part15 = True
    elif persistent.part16 is None and progress == 16:
        $ gg = 1
        show expression 'arc_gall_19' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part16 = True
    elif persistent.part17 is None and progress == 17:
        if persistent.obdrawer is True:
            $ gd = 1
        $ gp = 1
        $ gg = 1
        $ gm = 1
        $ gr = 1
        show expression 'arc_char_05' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Characters +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_char_05'
        if persistent.obdrawer is True:
            show expression 'arc_diary_16' at unlocked_center
            show expression Text ("{font=[gui.fontawesome]}{/font} Diary +1", color='#000') at unlocked_text
            pause 1.5
            hide expression 'arc_diary_16'
        show expression 'arc_gall_20' at unlocked_five_left
        show expression 'arc_gall_21' at unlocked_three_left
        show expression 'arc_gall_22' at unlocked_center
        show expression 'arc_gall_23' at unlocked_three_right
        show expression 'arc_gall_24' at unlocked_five_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +5", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_20'
        hide expression 'arc_gall_21'
        hide expression 'arc_gall_22'
        hide expression 'arc_gall_23'
        hide expression 'arc_gall_24'
        show expression Text ("[gui.bgm11]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +1", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_17' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part17 = True
    elif persistent.part20 is None and progress == 20:
        if not sigiveup <= -1:
            $ gp = 1
            $ gc = 1
        if not smoke == 1:
            $ gg = 1
        $ gm = 1
        $ gr = 1
        if not sigiveup <= -1:
            show expression 'arc_char_04_q' at unlocked_center
            show expression Text ("{font=[gui.fontawesome]}{/font} Characters +1", color='#000') at unlocked_text
            pause 1.5
            hide expression 'arc_char_04_q'
            show expression 'arc_con_03' at unlocked_center
            show expression Text ("{font=[gui.fontawesome]}{/font} Concept +1", color='#000') at unlocked_text
            pause 1.5
            hide expression 'arc_con_03'
        if not smoke == 1:
            show expression 'arc_gall_25' at unlocked_center
            show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +1", color='#000') at unlocked_text
            pause 1.5
            hide expression 'arc_gall_25'
        show expression Text ("[gui.bgm13]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +1", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        if not sigiveup <= -1:
            show expression 'part_18' at unlocked_three_left
            show expression 'part_19' at unlocked_center
            show expression 'part_20' at unlocked_three_right
            show expression Text ("{font=[gui.fontawesome]}{/font} Replay +3", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part20 = True
    elif persistent.part21 is None and not sigiveup <= -1 and progress == 21:
        $ gc = 1
        $ gg = 1
        $ gr = 1
        show expression 'arc_con_06' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Concept +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_con_06'
        show expression 'arc_gall_26' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part21 = True
    elif persistent.part22 is None and progress == 22:
        $ gg = 1
        $ gr = 1
        show expression 'arc_gall_27' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_27'
        show expression 'part_22' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part22 = True
    elif persistent.part23 is None and wallet == 0 and progress == 23:
        $ gc = 1
        $ gg = 1
        show expression 'arc_con_08' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Concept +1", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_con_08'
        show expression 'arc_gall_28' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part23 = True
    elif persistent.part24 is None and progress == 24:
        $ gg = 1
        $ gr = 1
        show expression 'arc_gall_29' at unlocked_two_left
        show expression 'arc_gall_30' at unlocked_two_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +2", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_24' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part24 = True
    elif persistent.ending is None:
        $ gp = 1
        $ gg = 1
        $ gm = 1
        $ gr = 1
        show expression 'arc_char_06_e' at unlocked_two_left
        show expression 'arc_char_04_e' at unlocked_two_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Characters +2", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_char_06_e'
        hide expression 'arc_char_04_e'
        show expression 'arc_gall_31' at unlocked_two_left
        show expression 'arc_gall_32' at unlocked_two_right
        show expression Text ("{font=[gui.fontawesome]}{/font} Gallery +2", color='#000') at unlocked_text
        pause 1.5
        hide expression 'arc_gall_31'
        hide expression 'arc_gall_32'
        show expression Text ("[gui.bgm12]", color='#000', style="centered_text")
        show expression Text ("{font=[gui.fontawesome]}{/font} Music +1", color='#000') at unlocked_text
        pause 1.5
        scene main_menu
        show gradiant
        show expression Text('[gui.unlocked]', style='unlocked_title') as text
        show expression 'part_25' at unlocked_center
        show expression Text ("{font=[gui.fontawesome]}{/font} Replay +1", color='#000') at unlocked_text
        pause 1.5
        $ persistent.part25 = True
    scene main_menu with blind
    $ persistent.part_clear = True
    call screen part_clear
    return
label teddy:
    scene main_menu
    show gradiant
    with blind
    show expression Text("Back to the bridge!", style='unlocked_title') as text at spread
    pause 1
    show expression '5m_bronze' at unlocked_center
    $ persistent.teddy = True
    pause 1.5
    scene main_menu with blind
    return
label esteregg_01:
    scene ester_1
    $ grid_width = 5
    $ grid_height = 5
    $ puzzle_field_size = 1280
    $ puzzle_field_offset = 30
    $ puzzle_piece_size = 450
    $ grip_size = 75
    $ active_area_size = puzzle_piece_size - (grip_size * 2)
    $ chosen_img = 'images/photo.webp'
    python:
        img_width, img_height = renpy.image_size(chosen_img)
        if img_width >= img_height and img_width > puzzle_field_size:
            img_scale_down_index = round( (1.00 * puzzle_field_size / img_width), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)
        elif img_height >= img_width and img_height > puzzle_field_size:
            img_scale_down_index = round( (1.00 * puzzle_field_size / img_height), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)
        else:
            img_to_play = chosen_img
        x_scale_index = round( (1.00 * (img_width/grid_width)/active_area_size), 6)
        y_scale_index = round( (1.00 * (img_height/grid_height)/active_area_size), 6)
        mainimage = im.Composite((int(img_width+(grip_size*2)*x_scale_index), int(img_height+(grip_size*2)*y_scale_index)),(int(grip_size*x_scale_index), int(grip_size*y_scale_index)), img_to_play)
        top_row = []
        for i in range (0, grid_width):
            top_row.append(i)
        bottom_row = []
        for i in range (0, grid_width):
            bottom_row.append(grid_width*(grid_height-1)+i)
        left_column = []
        for i in range (0, grid_height):
            left_column.append(grid_width*i)
        right_column = []
        for i in range (0, grid_height):
            right_column.append(grid_width*i + (grid_width-1) )
        jigsaw_grid = []
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                jigsaw_grid.append([9,9,9,9])
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                if grid_width*i+j not in top_row:
                    if jigsaw_grid[grid_width*(i-1)+j][2] == 1:
                        jigsaw_grid[grid_width*i+j][0] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][0] = 1
                else:
                    jigsaw_grid[grid_width*i+j][0] = 0
                if grid_width*i+j not in right_column:
                    jigsaw_grid[grid_width*i+j][1] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][1] = 0
                if grid_width*i+j not in bottom_row:
                    jigsaw_grid[grid_width*i+j][2] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][2] = 0
                if grid_width*i+j not in left_column:
                    if jigsaw_grid[grid_width*i+j-1][1] == 1:
                        jigsaw_grid[grid_width*i+j][3] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][3] = 1
                else:
                    jigsaw_grid[grid_width*i+j][3] = 0
        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        testlist = dict()
        for i in range(0,grid_width):
            for j in range (0,grid_height):
                piecelist[i,j] = [int(renpy.random.randint(0, (config.screen_width * 0.9 - puzzle_field_size))+puzzle_field_size), int(renpy.random.randint(0, (config.screen_height * 0.8)))]
                temp_img = im.Crop(mainimage, int(i*active_area_size*x_scale_index), int(j*active_area_size*y_scale_index), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))
                imagelist[i,j] = im.Composite((int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index)), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/puzzle/_00%s.webp"%(jigsaw_grid[grid_width*j+i][0]), 0, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/puzzle/_00%s.webp"%(jigsaw_grid[grid_width*j+i][1]), 270, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/puzzle/_00%s.webp"%(jigsaw_grid[grid_width*j+i][2]), 180, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/puzzle/_00%s.webp"%(jigsaw_grid[grid_width*j+i][3]), 90, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))))
                placedlist[i,j] = False
    jump esteregg_01_puzzle
label esteregg_01_puzzle:
    call screen esteregg_01
    jump esteregg_01_win
label esteregg_01_win:
    scene ester_1
    show photop:
        xpos 30 ypos 30
    with blind
    scene ester_1
    with centerblind
    pause 1
    if not persistent.introduction is True:
        scene main_menu
        show gradiant
        with blind
        show expression Text("[gui.unlocked]", style='unlocked_title') as text at spread
        pause 1
        show expression '1m_gold' at unlocked_center
        $ persistent.introduction = True
        $ achievement.grant('KNDW_INTRODUCTION')
        pause 1.5
        scene main_menu with blind
    return
label esteregg_02:
    $ persistent.ester_order = 0
    scene ester_2
    show arc_gall_10:
        xpos 290 ypos 172
    show arc_gall_11:
        xpos 620 ypos 172
    show arc_gall_12:
        xpos 950 ypos 172
    show arc_gall_13:
        xpos 1280 ypos 172
    show arc_gall_14:
        xpos 290 ypos 540
    show arc_gall_15:
        xpos 620 ypos 540
    show arc_gall_16:
        xpos 950 ypos 540
    show arc_gall_17:
        xpos 1280 ypos 540
    call screen esteregg_02
    scene ester_2
    with centerblind
    pause 1
    if not persistent.development is True:
        scene main_menu
        show gradiant
        with blind
        show expression Text("[gui.unlocked]", style='unlocked_title') as text at spread
        pause 1
        show expression '2m_gold' at unlocked_center
        $ persistent.development = True
        $ achievement.grant('KNDW_DEVELOPMENT')
        pause 1.5
        scene main_menu with blind
    return
label esteregg_03:
    scene ester_3
    $ grid_width = 7
    $ grid_height = 7
    $ puzzle_field_size = 960
    $ puzzle_field_offset = 30
    $ puzzle_piece_size = 450
    $ grip_size = 75
    $ active_area_size = puzzle_piece_size - (grip_size * 2)
    $ chosen_img = 'images/diary_puzzle.webp'
    python:
        img_width, img_height = renpy.image_size(chosen_img)
        if img_width >= img_height and img_width > puzzle_field_size:
            img_scale_down_index = round( (1.00 * puzzle_field_size / img_width), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)
        elif img_height >= img_width and img_height > puzzle_field_size:
            img_scale_down_index = round( (1.00 * puzzle_field_size / img_height), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)
        else:
            img_to_play = chosen_img
        x_scale_index = round( (1.00 * (img_width/grid_width)/active_area_size), 6)
        y_scale_index = round( (1.00 * (img_height/grid_height)/active_area_size), 6)
        mainimage = im.Composite((int(img_width+(grip_size*2)*x_scale_index), int(img_height+(grip_size*2)*y_scale_index)),(int(grip_size*x_scale_index), int(grip_size*y_scale_index)), img_to_play)
        top_row = []
        for i in range (0, grid_width):
            top_row.append(i)
        bottom_row = []
        for i in range (0, grid_width):
            bottom_row.append(grid_width*(grid_height-1)+i)
        left_column = []
        for i in range (0, grid_height):
            left_column.append(grid_width*i)
        right_column = []
        for i in range (0, grid_height):
            right_column.append(grid_width*i + (grid_width-1) )
        jigsaw_grid = []
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                jigsaw_grid.append([9,9,9,9])
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                if grid_width*i+j not in top_row:
                    if jigsaw_grid[grid_width*(i-1)+j][2] == 1:
                        jigsaw_grid[grid_width*i+j][0] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][0] = 1
                else:
                    jigsaw_grid[grid_width*i+j][0] = 0
                if grid_width*i+j not in right_column:
                    jigsaw_grid[grid_width*i+j][1] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][1] = 0
                if grid_width*i+j not in bottom_row:
                    jigsaw_grid[grid_width*i+j][2] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][2] = 0
                if grid_width*i+j not in left_column:
                    if jigsaw_grid[grid_width*i+j-1][1] == 1:
                        jigsaw_grid[grid_width*i+j][3] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][3] = 1
                else:
                    jigsaw_grid[grid_width*i+j][3] = 0
        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        testlist = dict()
        for i in range(0,grid_width):
            for j in range (0,grid_height):
                piecelist[i,j] = [int(renpy.random.randint(0, (config.screen_width * 0.9 - puzzle_field_size))+puzzle_field_size), int(renpy.random.randint(0, (config.screen_height * 0.8)))]
                temp_img = im.Crop(mainimage, int(i*active_area_size*x_scale_index), int(j*active_area_size*y_scale_index), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))
                imagelist[i,j] = im.Composite((int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index)), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/puzzle/_00%s.webp"%(jigsaw_grid[grid_width*j+i][0]), 0, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/puzzle/_00%s.webp"%(jigsaw_grid[grid_width*j+i][1]), 270, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/puzzle/_00%s.webp"%(jigsaw_grid[grid_width*j+i][2]), 180, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/puzzle/_00%s.webp"%(jigsaw_grid[grid_width*j+i][3]), 90, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))))
                placedlist[i,j] = False
    jump esteregg_03_puzzle
label esteregg_03_puzzle:
    call screen esteregg_03
    jump esteregg_03_win
label esteregg_03_win:
    scene ester_3
    show diary_puzzle:
        xpos 30 ypos 30
    with blind
    scene ester_3
    with centerblind
    pause 1
    if not persistent.turn is True:
        scene main_menu
        show gradiant
        with blind
        show expression Text("[gui.unlocked]", style='unlocked_title') as text at spread
        pause 1
        show expression '3m_gold' at unlocked_center
        $ persistent.turn = True
        $ achievement.grant('KNDW_TURN')
        pause 1.5
        scene main_menu with blind
    return
label esteregg_04:
    $ persistent.ester_last_order = 0
    scene ester_4
    show arc_gall_25:
        xpos 290 ypos 172
    show arc_gall_26:
        xpos 620 ypos 172
    show arc_gall_27:
        xpos 950 ypos 172
    show arc_gall_28:
        xpos 1280 ypos 172
    show arc_gall_29:
        xpos 290 ypos 540
    show arc_gall_30:
        xpos 620 ypos 540
    show arc_gall_31:
        xpos 950 ypos 540
    show arc_gall_32:
        xpos 1280 ypos 540
    call screen esteregg_04
    scene ester_4
    with centerblind
    pause 1
    if not persistent.conclusion is True:
        scene main_menu
        show gradiant
        with blind
        show expression Text("[gui.unlocked]", style='unlocked_title') as text at spread
        pause 1
        show expression '4m_gold' at unlocked_center
        $ persistent.conclusion = True
        $ achievement.grant('KNDW_CONCLUSION')
        pause 1.5
        scene main_menu with blind
    return
label wimcj_001:
    stop music
    play music 'bgm/wimcj_intro.opus' fadein 3
    scene wimcj_title
    $ renpy.transition(Dissolve(1))
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(Dissolve(3))
    $ renpy.pause(3, hard = True)
    call screen wimcj_detail_001
    scene black
    show expression Text ('One day morning in 2012', style='extext') at times with d3
    scene black with d3
    pause 1
    play sound 'se/bell.opus'
    pause 3
    play sound 'se/bell.opus'
    pause 3
    play music 'bgm/Sigh day.opus' fadein 3
    scene wimcj_voxel_0001 with d
    play sound 'se/wimcj_hover.opus'
    $ show_quick_menu = False
    show wimcj_system_comment_flip at wimcj_emoticons:
        xpos .01 ypos -.083
    ga 'Hmm….'
    hide wimcj_system_comment_flip
    play sound 'se/wimcj_hover.opus'
    show wimcj_system_hungry at wimcj_emoticons:
        xpos .005 ypos -.06
    ga 'Hungry….'
    scene wimcj_voxel_0002 with d5
    play sound 'se/wimcj_hover.opus'
    show wimcj_system_comment_black_flip at wimcj_emoticons:
        xpos .51 ypos .02
    ga 'I want bread….'
    hide wimcj_system_comment_black_flip
    pause 1
    play sound 'se/wimcj_click.opus'
    show wimcj_system_bulb_black at wimcj_emoticons:
        xpos .505 ypos .035
    pause 2
    scene wimcj_cafe_sepia
    show h_smile_sepia
    with blind
    h "Hey,{w=.3} Ga-yeon,{w=.3} do you know a new fruit jam brand launched by one of our company affiliates?{w=.3} It tastes amazing.{w=.3} Take it and try when you're having bread."
    ga "Jam?{w=.3} Does your company have an affiliate even for jam?{w=.3} Unbelievable!{w=.3} Restaurants,{w=.3} cafes,{w=.3} and even food ingredients….{w=.3} It has such a great financial strength,{w=.3} doesn't it?"
    h "According to the manager,{w=.3} it started as a private restaurant,{w=.3} which was run by the manager's father and the chairman when the chairman was young,{w=.3} and has steadily developed this much today."
    ga "What?{w=.3} Do you mean that manager?{w=.3} The one who likes you?{w=.3} My gosh!{w=.3} I didn't even imagine his father has such a close relationship with the chairman!{w=.3} Then why you don't want to go out with him?"
    h "I told you before.{w=.3} We don't get along well."
    ga "Come on,{w=.3} don't say like that.{w=.3} You really want to end up a lonely spinster?"
    h "Alright,{w=.3} alright.{w=.3} Ga-yeon,{w=.3} I don't want to hear such silly things.{w=.3} Hey,{w=.3} just take the jam,{w=.3} go home,{w=.3} and try it!{w=.3} It's your favorite cranberry jam!"
    ga 'Wow,{w=.3} cranberry!{w=.3} Love it!'
    h 'Yeah….{w=.3} It is so you.'
    scene wimcj_voxel_0002 with blind
    play sound 'se/wimcj_click.opus'
    show wimcj_system_bulb_black at wimcj_emoticons:
        xpos .505 ypos .035
    ga 'Oh,{w=.3} my cranberry jam!'
    scene wimcj_voxel_0004 with blind
    play sound 'se/wimcj_hover.opus'
    show wimcj_system_question at wimcj_emoticons:
        xpos .74 ypos -.01
    ga "Hm,{w=.3} where's it?"
    scene wimcj_voxel_0005 with blind
    play sound 'se/wimcj_hover.opus'
    show wimcj_system_question_black at wimcj_emoticons:
        xpos .4 ypos .05
    ga 'Where are you,{w=.3} my cranberry jam?'
    stop music fadeout 3
    play sound 'se/wimcj_hover.opus'
    scene wimcj_voxel_0005_sepia with blind
    system "Jam has disappeared.{w=.3} Try to find it."
    $ wimcj_level = 1
    $ wimcj_time = 60
    $ wimcj_timer_range = 60
    $ wimcj_timer_jump = 'wimcj_gameover'
    scene wimcj_level_001_01 with blind
    show wimcj_system_black
    show wimcj_sys_radar at wimcj_sys_center
    play sound 'se/wimcj_hover.opus'
    $ renpy.pause(3, hard = True)
    hide wimcj_sys_radar
    show wimcj_sys_start at wimcj_sys_center
    play sound 'se/wimcj_click.opus'
    $ renpy.pause(3, hard = True)
    play music 'bgm/Summit showdown.opus' fadein 3
    scene wimcj_level_001_01
label wimcj_001_play:
    if wimcj_time == 0:
        jump wimcj_gameover
    elif wimcj_time == 30:
        scene wimcj_voxel_0002
        show wimcj_system_black
        show wimcj_sys_warning at wimcj_sys_center
        play sound 'se/wimcj_gameover.opus'
        $ renpy.pause(3, hard = True)
        hide wimcj_sys_warning
        hide wimcj_system_black
        ga 'No….{w=.3} No jam….{w=.3} Where is it….'
        play sound 'se/wimcj_hover.opus'
        scene wimcj_voxel_0002_sepia with blind
        system 'She is reaching hyperventilation due to her anxiety disorder.{w=.3} She needs a plastic bag to get her breath.'
        $ wimcj_time = 29
        $ wimcj_level_001_trick_1 = 1
        $ wimcj_level_001_move = 0
        hide wimcj_voxel_0002_sepia
        call screen wimcj_level_001
    elif wimcj_time == 10:
        $ wimcj_time = 9
        call screen wimcj_level_001
    else:
        if wimcj_level_001_move == 7:
            if wimcj_time <= 29:
                pass
            else:
                play sound 'se/washing.opus'
        call screen wimcj_level_001
label wimcj_001_bag:
    stop music fadeout 3
    scene black
    scene wimcj_voxel_0003 with d3
    pause 3
    play sound 'se/wimcj_hover.opus'
    scene wimcj_voxel_0003_sepia with blind
    system "She's finally getting her breath back."
    play music 'bgm/Sigh day.opus' fadein 3
    scene wimcj_voxel_0001 with d
    pause 1
    ga "I'm exhausted…."
    pause 1
    play sound 'se/wimcj_hover.opus'
    scene wimcj_voxel_0001_sepia with blind
    system 'She looks so worn out.{w=.3} Let her sleep.'
    scene black with d
    pause .5
    scene wimcj_voxel_0001 with d
    ga 'Yeah,{w=.3} actually there was no jam,{w=.3} in reality.{w=.3} I knew that.'
    ga 'Idiot….{w=.3} What have I been looking for?'
    pause 1
    stop music fadeout 3
    scene wimcj_voxel_0001_sepia with d3
    woo 'What had she been looking for?'
    woo 'Perhaps,{w=.3} herself.'
    woo 'Her former self used to try her best to live on with the utmost effort,{w=.3} though she looked nervous and unpredictable as,{w=.3} at that time,{w=.3} she was just raw.'
    woo "She's been looking for her former self - who used to regard herself as a {b}\"gem\"{/b}."
    play music 'bgm/wimcj_intro.opus' fadein 3
    scene black with d3
    pause 1
    scene wimcj_level_001_07 with d3
    ga '….'
    pause 1
    play sound 'se/wimcj_click.opus'
    ga '…!'
    pause 1
    play sound 'se/wimcj_kitchen.opus'
    scene wimcj_voxel_0006 with d5
    pause 3
    scene wimcj_level_001_12
    show level_001_obj_002:
        xpos 0.3588 ypos 0.4731
    with d5
    pause 3
    scene wimcj_voxel_0006 with d5
    ga 'Jam…?'
    pause 1
    scene wimcj_voxel_0006_sepia with d3
    pause 1
    scene black with d3
    if not persistent.esteregg is True:
        scene main_menu
        show gradiant
        with blind
        show expression Text("[gui.unlocked]", style='unlocked_title') as text at spread
        pause 1
        show expression '5m_gold' at unlocked_center
        $ persistent.esteregg = True
        pause 1.5
        scene main_menu with blind
    return
label wimcj_gameover:
    stop music
    play sound 'se/wimcj_gameover.opus'
    scene black
    show wimcj_gameover
    show expression Text('!GAME OVER!', style='wimcj_message', xalign=.5, yalign=.99)
    with d3
    pause 3
    return
label leannoth:
    stop music
    play music 'bgm/Pandemic.opus' fadein 3
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('Hey, you know what?', style='centered_text') as text
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_0
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('The sun, full of energy, makes people smile with its warm sunshine.', style='centered_text') as text
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_1
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('The moon, brings people rest and peaceful sleep, with its generous moonlight.', style='centered_text') as text
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_2
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('However, do you also know that…?', style='centered_text') as text
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_3
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('The sun makes people wear a smile full of anger, with its sunlight in flaming red.', style='centered_text') as text
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_4
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('The moon makes people fall into sleep, possessed by madness, with its dazzling-white moonlight.', style='centered_text') as text
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_5
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('Did you know that?', style='centered_text') as text
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_6
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('Yeah, Hye-na.', style='centered_text') as text
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_7
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('Yeah, Hyena.', style='centered_text') as text
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_8 at zoom_blur
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show leannoth_8
    $ renpy.transition(Dissolve(3))
    $ renpy.pause(3, hard = True)
    scene black
    $ renpy.transition(d3)
    $ renpy.pause(3, hard = True)
    show expression Text ('You shall be as god.', style='centered_text') as text
    $ renpy.pause(3, hard = True)
    scene black
    show expression Text('{font=gui/fonts/YiSunShinBold.ttf}Mahalath\nLeannoth{/font}', size=256, color='#fff', style="centered_text")
    $ renpy.pause(5, hard = True)
    if persistent.mahalath is None:
        scene main_menu
        show gradiant
        with blind
        show expression Text("[gui.unlocked]", style='unlocked_title') as text at spread
        pause 1
        show expression '6m_gold' at unlocked_center
        $ persistent.mahalath = True
        $ achievement.grant('KNDW_DETECTIVE')
        pause 1.5
        scene main_menu with blind
    return
label dlc:
    scene main_menu
    show gradiant
    if persistent.dlc == 'buy':
        if dlc_key == 404910:
            $ steam.activate_overlay_to_store(404910, flag=steam.STORE_NONE)
        if dlc_key == 375160:
            $ steam.activate_overlay_to_store(375160, flag=steam.STORE_ADD_TO_CART_AND_SHOW)
            call screen music_room
        if dlc_key == 382390:
            $ steam.activate_overlay_to_store(382390, flag=steam.STORE_ADD_TO_CART_AND_SHOW)
        if dlc_key == 384650:
            $ steam.activate_overlay_to_store(384650, flag=steam.STORE_ADD_TO_CART_AND_SHOW)
        if dlc_key == 407760:
            $ steam.activate_overlay_to_store(407760, flag=steam.STORE_NONE)
        if dlc_key == 375161:
            $ steam.activate_overlay_to_store(375161, flag=steam.STORE_ADD_TO_CART_AND_SHOW)
        if dlc_key == 558690:
            $ steam.activate_overlay_to_store(558690, flag=steam.STORE_ADD_TO_CART_AND_SHOW)
    elif persistent.dlc == 'install':
        if dlc_key == 404910:
            $ steam.install_dlc(404910)
        if dlc_key == 375160:
            $ steam.install_dlc(375160)
        if dlc_key == 382390:
            $ steam.install_dlc(382390)
        if dlc_key == 384650:
            $ steam.install_dlc(384650)
        if dlc_key == 407760:
            $ steam.install_dlc(407760)
        if dlc_key == 375161:
            $ steam.install_dlc(375161)
        if dlc_key == 558690:
            $ steam.install_dlc(558690)
    elif persistent.dlc == 'delete':
        if dlc_key == 404910:
            $ steam.uninstall_dlc(404910)
        if dlc_key == 375160:
            $ steam.uninstall_dlc(375160)
        if dlc_key == 382390:
            $ steam.uninstall_dlc(382390)
        if dlc_key == 384650:
            $ steam.uninstall_dlc(384650)
        if dlc_key == 407760:
            $ steam.uninstall_dlc(407760)
        if dlc_key == 375161:
            $ steam.uninstall_dlc(375161)
        if dlc_key == 558690:
            $ steam.uninstall_dlc(558690)
    call screen downloadable
label refresh:
    $ renpy.restart_interaction()
    call screen downloadable
label sync:
    $ achievement.sync()
    pause 1
    call screen default_language
label rmsteam:
    $ achievement.clear_all()
    pause 1
    call screen default_language
label reset:
    $ renpy.loadsave.location.unlink_persistent()
    $ renpy.persistent.should_save_persistent = False
    pause 1
    call screen default_language
label resetall:
    $ achievement.clear_all()
    $ renpy.loadsave.location.unlink_persistent()
    $ renpy.persistent.should_save_persistent = False
    if renpy.windows:
        $ shutil.rmtree(os.path.join(os.environ.get("APPDATA", ""), "RenPy", "Discouraged-Workers-saves"))
    elif renpy.macintosh:
        $ shutil.rmtree(os.path.join(os.environ.get("HOME", ""), "Library", "RenPy", "Discouraged-Workers-saves"))
    else:
        $ shutil.rmtree(os.path.join(os.environ.get("HOME", ""), ".renpy", "Discouraged-Workers-saves"))
    $ shutil.rmtree('game/saves/')
    pause 1
    if renpy.windows:
        $ os.mkdir(os.path.join(os.environ.get("APPDATA", ""), "RenPy", "Discouraged-Workers-saves"))
    elif renpy.macintosh:
        $ os.mkdir(os.path.join(os.environ.get("HOME", ""), "Library", "RenPy", "Discouraged-Workers-saves"))
    else:
        $ os.mkdir(os.path.join(os.environ.get("HOME", ""), ".renpy", "Discouraged-Workers-saves"))
    $ os.mkdir('game/saves/')
    pause 1
    call screen default_language
