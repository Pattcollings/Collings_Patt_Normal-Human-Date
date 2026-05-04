# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("juno", color= '#03fcd3')
define w = Character("waiter", color= '#fc030b')


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

label location_found:
    show table
    show juno happy

label parking_trouble:
    show table
    show juno shock
    j "NO"













    return
