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
    show table
    






    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
