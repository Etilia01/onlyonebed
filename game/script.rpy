#oh no so much defining. why do i feel like there was a better way to do this (o﹏o)

define e = Character("Narrator")
define y= Character ("'You'")
define who= Character ("?")
define c= Character ("Cat")
define a= Character ("Scientist? Probably.")

default doorcode = 6423315

image slowburn bnottalking:
    "slowburn bnottalking.png"
    zoom 1.5
image slowburn btalking:
    "slowburn btalking.png"
    zoom 1.5
image slowburn blooking:
    "slowburn blooking.png"
    zoom 1.5
image slowburn nbtalking:
    "slowburn nbtalking.png"
    zoom 1.5
image slowburn shocked:
    "slowburn shocked.png"
    zoom 1.5
image slowburn nb:
    "slowburn nb.png"
    zoom 1.5
image scie neutra:
    "scie neutral.png"
    zoom 1.5
image scie angr:
    "scie angry.png"
    zoom 1.5
image scie shocke:
    "scie shocked.png"
    zoom 1.5
image scie happ:
    "scie happy"
    zoom 1.5
image mc neutral:
    "mc neutral.png"
    zoom 1.7
image mc annoyed:
    "mc annoyed.png"
    zoom 1.7
image mc happy:
    "mc happy.png"
    zoom 1.7
image mc shocked:
    "mc shocked.png"
    zoom 1.7
image mc thinking:
    "mc thinking.png"
    zoom 1.7
image mc talking:
    "mc talking.png"
    zoom 1.7
image cat talking:
    "cattalk.png"
    zoom 2.0
image cat:
    "cat.png"
    zoom 2.0


label start:


    scene bg voidbe2

    e "You wake up."
    show mc shocked at right with moveinright
    y "What the hell!?"
    y "Where am I???"

    e "Looking around you see... Nothing."
    scene bg voidbed1
    show mc neutral at right
    e "You stand up, and step away a bit, looking back at your bed."
    e "Its still there, but otherwise, theres nothing around it."
    show mc talking at right
    y "How..?"
    y "Im still dreaming, right?"
    e "You pinch yourself. It hurts. A lot actually."
    show mc thinking
    y "ow"
    e "sorry"
    y "its ok."

    label choices:
        menu:
            "Stay here and investigate":
                jump choicesa1
            "Leave. Theres nothing to find here anyways":
                jump choicesa2
    
    
    label choicesa1:
        scene bg voidbe2
        e "You decide to investigate the area around the bed, and the bed itself."
        e "You find that it is just a regular bed."
        e "You look under it too. There is nothing but void."
        e "What did you expect???"
        menu:
            "Stay.":
                jump ending_void
            "Leave":
                jump choicesa2
    
    label ending_void: #my dnd players be like. completely ignoring plothooks for funsies
        e "You decide to stay here. Who know what dangers could be lurking further away?"
        e "As you make your way to the bed to sit down and rest, you start sinking into the darkness below."
        scene bg void5 with fade
        e "You struggle to try and get out, but eventually you give up and let yourself fall into the nothingness."
        jump choices_common

    
    label choicesa2:
        scene bg void
        e "You walk."
        e "And walk."
        e "Until, after what felt like hours, you finally see a pillar of smoke rising in the distance."
        e "You run towards it, thinking there might be a clue on getting out there."
        e "As you come close enough to see it clearly, you make out… a person?"
        show mc neutral at right
        show slowburn bnottalking at left with moveinleft 
        
        jump choices_dia1


        
    label choices_dia1:    
        menu:
        
            "Who are you?":
                show mc talking at right
                pause 0.3
                show mc neutral at right
                show slowburn btalking at left
                who "Im me."
                show slowburn blooking at left
                jump choices_dia1
              
            "Why are you burning?":
                show mc talking at right
                pause 0.3
                show mc neutral at right
                show slowburn btalking at left
                who "Thats just how things are."
                show slowburn blooking at left
                jump choices_dia1
            "How long have you been like that?":
                show mc talking at right
                pause 0.3
                show mc neutral at right
                show slowburn btalking at left
                who "For a very long time. At this rate, it'll take another five thousand years until Im completely burned away."
                show slowburn blooking at left
                jump choices_dia2
            
    label choices_dia2:
        menu:
            "Extinguish them with the bucket of water you conveniently see standing right next to them.": #Why would you do that without asking? Thats so mean (•́ ᴖ •̀)
                show slowburn shocked at left
                who "Whaaa-!?" #why
                show slowburn nbtalking at left
                who "Its over...thank you? I guess?"
                who "I suppose I should help you too now."
                who "You need to get to another dimension, dont you? Over there are portals to elsewhere. Take the left one."
                show slowburn nb at left
                y "Youre welcome, and thank you!"
                scene bg voidportal
                e "Just a few metres away you see two portals, both leading to different dimensions."
                e "You decide to follow the kind strangers advice and take the left one."
                y "Do I really tho? It looks kinda scary..."
                e "You walk through the portal at the left without hesitation and die, please and thank you."
                scene bg endingred with fade
                e "Goodbye."
                jump choices_common
            "Ask if they need help.":
                show slowburn btalking at left
                who "No Im fine."
                show slowburn blooking
                y "Are you sure about that? That seems painful."
                e "They stay quiet."
                menu:
                    "Hello? You hear me?":
                        e "They stay quiet."
                        menu: 
                            "Continue to try and talk to them.": #I, and the narrator, are heavily judging you if you choose this.
                                e "Will you give up already?"
                                e "You wave goodbye, earning an annoyed look, which you pretend to be oblivious to, and continue your journey."
                                jump choices_portal
                            "Leave, like a normal person with respect for boundaries.":
                                e "You wave goodbye, and continue your journey."
                                jump choices_portal
                    "Leave.":
                        e "You wave goodbye, and continue your journey."
                        jump choices_portal



    label choices_portal:
        scene bg voidportal
        e "Just a few metres away you see two portals, both leading to different dimensions."
        show mc thinking at right
        y "Which should I take...?"
        e "How about you try the one without blood on its frame, that doesnt look deadly either? You know, the one with the bright arrows pointing to it?"
        menu:
            "Choose the left portal":
                e "You step through the portal."
                scene bg red
                e "It feels as if youre stepping into some kind of liquid"
                e "You cant breathe."
                e "So you decide to go back. But, you cannot find where you came from, no matter how hard you try."
                e "Want to try the other portal instead?"
                menu:
                    "Nah, Im good":
                        scene bg endingred with fade
                        pause 1.0
                        jump choices_common
                    "Absolutely.":
                        jump choices_portal2
                
            "Choose the right portal":
                jump choices_cafe
label choices_portal2:
    scene bg voidportal
    menu:
        "Choose the left portal":
            scene bg red
            e "Really?"
            e "You die. Again."
            e "Happy now?"
            e "No, but genuinely, why would you do this."
            e "I mean, the first time this happened was weird enough, I did my best to make the left portal creepy to make sure you chose the right one."
            e "But having this happen a second time?"
            e "At this point, I think youre doing it on purpose."
            jump choices_portal3
            
        "Choose the right portal":
            jump choices_cafe
label choices_portal3:
    scene bg voidportal
    menu:
        "Choose the left portal":
            scene bg red
            e "I GIVE UP"
            e "youre dead now"
            scene bg endingred with fade
            e "go play another game, if you dont like this ones story"
            e "but dont sabotage it on purpose"
            
            jump choices_common
            
        "Choose the right portal":
            jump choices_cafe

    
    label choices_cafe:
        scene bg cafe
        e "You step through the portal and find yourself in a cozy little cafe."
        show mc happy at right
        y "Finally! Im back!"
        e "It sure does SEEM that way."
        show mc annoyed at right
        y "Youre kidding, right?"
        e "No idea what youre talking about."
        jump choices_cafe2
    
    label choices_cafe2:
        scene bg cafe
        menu:
            "Look around":
                e "The cafe is very nicely decorated."
                jump choices_cafe2
                
            "Look at the calendar": #to-do, draw different calendars.
                scene bg calendar
                show mc thinking at right
                y "Hm..."
                jump choices_cafe2
                
            "Buy a hot beverage": #done
                scene bg barista
                e "You look at the menu for a while and decide to get a hot chocolate." #for lack of a better option
                scene bg hc
                show mc happy at right
                y "Looks delicious!"
                scene bg cafe
                menu:
                    "Sit down on the couch.":
                        e "You sit down on the couch and pick up a random magazine to read while drinking."
                        scene bg book
                        e "It appears to be a booklet for children to learn german."
                        #scene lizard-book 
                        
                        jump choices_cafe2
                        
                    "Drink it while standing":
                        e "You gulp down the hot chocolate as quickly as possible, burning your throat."
                        jump choices_cafe2
                
            "Look at the door in the back of the room.":
                scene bg lock
                e "It seems there is a lock in place."
                e "Do you know the code?"
                    
                $tempdoorcode = renpy.input("What is the code?").strip()
                if int(tempdoorcode) == doorcode:
                    "Correct!"
                    e "You step into the small backroom."
                    jump choices_thebackrooms
                else:
                    "Error!"
                    show mc thinking
                    y "Maybe I should try finding a clue for the right solution somewhere in the cafe..."
                    jump choices_cafe2
            "Leave the cafe":
                scene bg wall
                e "Outside, there is a wall."
                menu:
                    "Too bad. (Go back)":
                        e "You decide it isnt worth it to run headfirst into a wall, and turn back."
                        jump choices_cafe2
                    "No.":
                        show mc annoyed at right
                        e "What?"
                        y "No."
                        y "There ISNT a wall."
                        e "You know what? Fine, I'll go along with this."
                        show mc neutral at right
                        e "Outside is a wall,"
                        scene bg wallrun
                        show mc neutral at right
                        e "with a hole in it, that looks like someone ran through the wall."
                        jump choices_cat



    label choices_cat:
        scene bg catcafe
        show cat at left with moveinleft
        show mc neutral at right
        e "You walk forward, into what seems to be a cat cafe."
        show mc thinking at right
        y "huh."
        
        c "Good Morning. Wanna Go Through My Portal?"
        show cat talking at left
        c "I Have A Portal."
        c "It Leads Somewhere Very Great."
        c "Wanna Know Where It Leads To?"
        menu:
            "No":
                show cat at left
                e "You turn back and go back to the normal cafe."
                jump choices_cafe2
            "Sure":
                show cat talking at left
                c "Solve My Riddle!"
              
    label thesnailitsthesnail:
        c "Platymma Tweediei"
        menu:
            "Cat":
                
                c "That Is..."
                c "Wrong! Try Again!"
                jump thesnailitsthesnail
            "Snail":
                c "Huh. Did You Look That Up?"
                c "Either Way, Its Right!"
                jump right

            "You know, this is stupid.":
                e "What really? I was trying so-"
                e "The cat was trying so hard. Why are you mean like that."
                c "The Narrator Needs A Break To Go Cry." #The Narrators situation here is a metaphor for my worst fears when dm'ing dnd campains, and writing visual novels, if it wasnt obvious already.
                jump thesnailitsthesnail
            "42":
                c "The Best Option, Always, And Right Too!"
                jump right
            "WTF":
                c "Hm?"
                jump thesnailitsthesnail
            "Echsen":
                c "Wrong, Whered You Get That Idea From?"
                jump thesnailitsthesnail
            "Im secretly a werewolf!":
                c "No Youre Not."
                jump thesnailitsthesnail
    label right:
        c "Here You Go!"
        e "The cat steps back and reveals a shimmering portal behind it."
        c "See You Soon! :)"
        show cat at left
        jump choices_cat




    label choices_thebackrooms:
        scene bg backroom
        show mc neutral at right
        menu:

            "Look into one of the boxes":
                scene bg flowers
                e "Inside you see some suspiciously explosion shaped flowers."
                show mc thinking at right
                y "Explosion shaped?"
                menu:
                    "Throw them up at the ceiling":
                        scene bg backroomhole
                        e "There a hole in the ceiling now, leading to some ind of hallway. Its too high up for you to reach."
                        jump choices_thebackrooms2
                    "Throw them in a corner":
                        show mc happy
                        e "There now is a dent in the wall. Nothing else happened"
                        jump choices_thebackrooms

                    "Eat them :3":
                        
                        
                        e "The flowers taste very sour."
                        e "Surprisingly, you dont die."
                        jump choices_thebackrooms

            "Take a look at the corner hidden by the boxes":
                scene bg exlovers
                e "You discover two lizards having a very fancy dinner"
                show mc shocked at right
                y "sorry for disrupting your evening!"
                e "You quickly back out and let them be"
                jump choices_thebackrooms

            "Open one of the potato sacks":
                scene bg wool
                show mc shocked at right
                e "As you open them you are pressed against the ceiling by the wool inside it expanding rapidly."
                e "quite an inconvenient situation you found yourself in here, isnt it? Want to try again?"
                y "Obviously I want to try again, what kinda question is that?"
                jump choices_thebackrooms



label choices_thebackrooms2:
    scene bg backroomhole    
    menu:

        "Look into one of the boxes":
            scene bg flowers
            e "Inside you see some suspiciously explosion shaped flowers."
            show mc thinking at right
            y "Explosion shaped?"
            menu:
                "Throw them up at the ceiling":
                        
                    e "You already did that."
                    show mc annoyed at right
                "Throw them in a corner":
                    e "There now is another dent in the wall. Nothing else happened"
                    jump choices_thebackrooms2

                "Eat them :3":
                    show mc thinking at right
                    e "The flowers taste very sour."
                    e "Surprisingly, you dont die."
                    jump choices_thebackrooms2

        "Take a look at the corner hidden by the boxes":
            scene bg exlovers
            e "You discover two lizards having a very fancy dinner"
            show mc shocked at right
            y "sorry for disrupting your evening!"
            e "You quickly back out and let them be"
            jump choices_thebackrooms2

        "Open one of the potato sacks":
            scene bg wool
            show mc shocked at right
            e "You get launched up, superhero-landing on the floor above"
            scene bg tridoor
            e "Its a hallway? But theres just one door, that right in front of you." #The illusion of choice
            menu:
                "Open the door":
                    jump tfwasthiserrorplsbefixed
                    
label tfwasthiserrorplsbefixed: #it was some kinda max recursion depth hing. it wasnt the menu or anything, but this was too much work to make a new section and im lazy so
    scene bg lab
    e "So, you open the door. Behind it seems to be some kind of laboratory?"
            
    
    show scie happ at left
    show mc neutral at right
    a "Hello, you found me!"
    a "I assume youre here for an autograph?"
    menu:
        "Yes":
            show mc happy at right
            a "Wonderful, here you go."
            a "You know what, since youre such a big fan of my work, why dont you help me out here a bit?"#This man desperately needs friends
            menu:
                "Why not.":
                    scene bg e4 with fade
                    e "And so, you become a mad scientists lab assitant."
                    e "cool. No really."
                    e "Youll never go home now, but triangles I guess?"
                    jump choices_common
                "Nope. I didnt even want an autograph actually.":
                    show mc annoyed at right
                    a "Oh...Ok?"
                    show scie shocke at left
                    e "He looks at you quite sad."
                    jump triangledude
        "Nope":
            jump triangledude

label triangledude:
    show scie neutra at left
    e "You explain that youre here because you were trying to get home."
    show mc talking at right
    a "Huh? But why? Ive created the perfect triangular world...?"#dude triangles suck, get over it.
    show scie shocke at left
    show mc neutral at right
    menu:
        "What triangles?":
            show mc thinking at right
            a "Wait...No!Nonononononononononono....."
            e "He opens his window."
            a "Where are the triangles????"
            a "Ok, I get why you want to leave, Im sorry for bringing you here in the first place."
            
            a "Heres the portal to your home dimension."
            show scie neutra at left
            scene bg labportal
            menu:
                "Ok, thanks":
                    scene bg e5 with fade
                    e "You leave and go home."

                    jump choices_common
                "You brought me here!?":
                    show mc shocked at right
                    show scie happ at left
                    a "Yes, but only because I wanted someone to appreciate my triangles. Everyone else here always seems bored when I show them, because theyve seen them so often already."
                    y "You can forget your stupid excuses, Im outta here!"
                    show scie shocke at left
                    a "I-"
                    scene bg e5 with fade
                    e "You run through the portal, the scientists sad gaze following you."
                    jump choices_common
        "I dont like triangles":
            show mc annoyed at right
            show scie angr at left
            pause 0.5
            scene bg e3 with fade
            e "He zaps you out of existence. Good job buddy."
            
                      
        
        
    
    label choices_common:
        return
