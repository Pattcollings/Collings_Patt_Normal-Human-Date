# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("juno", color= '#03fcd3')
define w = Character("waiter", color= '#fc030b')
define y = Character("you", color= '#ffe647')


# The game starts here.

label start:
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
        jump 

        "Yes, I shall have your finest chicken tendies and fries.":


label fancy:
    show table
    show waiter open
    show juno angry w

    w "Ooo, a fancy choice!"
    





















    return
