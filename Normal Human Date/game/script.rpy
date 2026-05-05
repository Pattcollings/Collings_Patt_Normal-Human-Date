# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("juno", color= '#03fcd3')
define w = Character("waiter", color= '#fc030b')
define y = Character("you", color= '#ffe647')


# The game starts here.

label start:
    play music "NHD soundtrack.mp3" volume 0.75
    scene bg restaurant
    show table

label narration_begining:
    show table
    "You sit alone at a table for two, minutes upon minutes pass by. Your date should have been here by now…"
    "When all of a sudden-"

label crash:
    scene bg restaurant with vpunch:
        zoom 1.0


label juno_intro:
    scene bg restaurant
    show table
    "You hear a loud noise from outside. Did someone ram their car into the building??"
    "Then you see her. She looks… different."

label juno_apperance:
    
    show juno neutral
    show table
    j "..."

    menu:
        "Hey! Juno, right?":
            jump fake_name
        "Hi! Did you find this place alright?":
            jump location_found
        "Did you hear that crash outside?":
            jump parking_trouble


label fake_name:
    show juno panic
    show table
    j "\"Ju-\"?"
    show juno happy
    j "Oh yes! My human person name is Juno! Nice to meet you."
    jump flirt

label location_found:
    show table
    show juno happy
    j "Yes, I managed to pinpoint your exact location through the satellite system that keeps your planet under surveillance."

    show juno panic
    j "I mean..."

    show juno neutral talk
    j "Google"
    jump flirt

label parking_trouble:
    show table
    show juno shock
    j "NO"

    show juno panic
    j "uh- I mean-"

    show juno angry talk
    j "Yeah! What was that?? Indeed a strange noise."

    show juno ramble
    j "Someone probably crashed their non-spaceship vehicle as these human parking spaces are TINY."

    show juno neutral talk
    j "We should stop talking about it right now."
    jump flirt


label flirt:
    menu:
        "You uh…look-um… you don’t look like your picture.":
            jump read
        "I got you something.":
            jump rose_scene

label read:
    show table
    show juno happy
    j "..."
    j "Indeed I don’t."

    show juno angry talk
    j "Well you said you were 6’4 on your profile so let’s call it a draw."

    y "Damn...got my ass..."
    jump waiter_appear

label rose_scene:
    show table
    show juno shock
    show you rose

    "You hand her a beautiful rose that you picked up on your way here."

    hide you
    show juno rose
    j "OOOHH! Rosa Rubignosa!!!!"

    show juno rose point
    j "I LOVE these."
    y "Great! I hoped you w-"

    show juno rose munch
    "You watch as she shoves the entire thing in her mouth"
    y "..."

    show juno rose talk
    j "A lot of people don’t like the thorns but I think it adds to the flavor."
    
    jump waiter_appear

label waiter_appear:
    show table
    show juno neutral w
    show waiter closed
    
    "A waiter comes by your table"
    show waiter open
    w "Are you two ready to order?"

    menu:
        "I’ll have a ribeye steak with a glass of Cabernet Sauvignon.":
            jump fancy

        "Yes, I shall have your finest chicken tendies and fries.":
            jump cringe


label fancy:
    show table
    show waiter open
    show juno angry w

    w "Ooo, a fancy choice!"
    show juno angry you
    show waiter shock
    j "Too fancy, I am intimidated"

    show juno blast you
    "She pulls out a laser gun and vaporizes you."

    show blast
    "ZAP"
    return

label cringe:
    show table
    show waiter cringe
    show juno angry w
    w "Bruh, that’s CRAZY work on a first date."

    show juno blast open
    show waiter shock
    j "DO NOT INSULT THEM."

    show juno blast close
    show waiter blast
    "You watch as she pulls out a laser gun and vaporizes the waiter"

    show juno angry w
    show waiter dust
    "..."
    jump wtf

label wtf:
    hide waiter dust
    menu:
        "WHAT THE HELL??":
            jump gun_saftey

        "Cool! Thanks!":
            jump soulmate


    
label gun_saftey:
    show table
    show juno angry you
    j "I am showing my protectiveness and fierce loyalty."

    menu:
        "YOU JUST KILLED SOMEONE, I DO NOT FEEL PROTECTED.":
            jump how_many
        "Oh I see, I completely understand now.":
            jump soulmate
        

label how_many:
    show table
    show juno neutral talk
    j "How many people should I kill for you to feel protected?"

    menu:
        "NONE!":
            jump bad_ending

        "5":
            jump good_ending

label bad_ending:
    show table
    show juno blast you
    j "See and that attitude is why you’re not ruling the world."
    show blast
    "She vaporizes you next"
    return

label good_ending:
    show table
    show juno happy
    j "Good thing I killed 5 people on the way here, then!"

    y "That was genuinely my one and only hangup. I love you now."
    jump soulmate

label soulmate:
    show juno neutral talk
    j "Perfect. Would you like to copulate with me now?"

    show juno neutral
    y "Sure! But before we do I have a question"

    menu:
        "Why do you have a gun?":
            jump lore_drop
        "Are you an alien?":
            jump unsuspicious

label lore_drop:
    show table
    show juno ramble
    j "DEFINITELY not because of some intergalactic federation that I work for!"

    show juno happy
    j "No-sir-ee. It is because..."

    show juno panic
    j "..."

    show juno happy
    j "because it is a free country. Yee and haw!"
    jump final_end

label unsuspicious:
    show table
    show juno happy
    j "HHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHA"
    j "THAT'S A FUNNY JOKE, YOU"
    j "YOU ARE SO FUNNY. NOw why on EARTH would an alien be here???"
    show juno ramble
    j "Would they be trying to infiltrate human society through romance in order to slowly but surely replace the planet’s population with a superior race of Junorians?"
    show juno neutral
    j "..."
    y "..."
    show juno neutral talk
    j "Because that would be crazy, why would you suggest that???"
    jump final_end


label final_end:

    y "fair enough, let's go!"
    scene black


















    return
