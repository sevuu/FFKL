# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# TODO obmyslec jakies minigierki




label start:

    $ player_name = ""

    define w = Character(_("Wojtek"), color="#6097ff")
    define p = Character('[player_name]', color ="#ebff00")
    define j = Character(_("Jan"), color="#955be5")
    define idk = Character ("???")
    define ncz = Character ("Nauczyciel")
    define f = Character ("Filip")



    $ chapter = 0
    call ch0_main from _call_ch0_main
    call ch1_main from _call_ch1_main

    return
