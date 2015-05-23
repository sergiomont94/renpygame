# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg bckrnd = "bckrnd.jpg"
image margo = "images/margo.png"
image noir = "images/noir.png"
# Declare characters used by this game.
define e = Character('Narrator', color="#c8ffc8")
define l = Character(_("Margo   "), color="#ffcccc")
define n = Character(_("Noir   "), color="#ccccff")

# The game starts here.
label start:
    
    $player_choice = "ninguno"
    
    scene bckrnd

menu:
    
    e "Please pick a character:"
    
    "Margo":
            $player_choice = "margo"
            jump choice1_margo
            #jump margo4ever

    "Noir.":
            $player_choice = "noir"
            jump choice1_noir
            #jump noir4ever
          
label choice1_margo:
    
    

    e "Margo is a Blood Bathing warrior that uses the art of brutality and archery. He has no fears nor enemy he cant defeat. He is taller than an averge door and stronger than a mammoth. He hates snakes but has a love affection for sweets."
    
    jump choice1_done
    
label choice1_noir:
    
    
    e "He holds the title of Whisper of the Moon, his name is Noir"
    
    jump choice1_done
    
    
    
label choice1_done:
    e "Its done, good luck hero..."
    e "You're gonna need it. *grin*"
    
    if player_choice == "margo":
        show margo
        l "Great choice summoner, now you'll see true power"
        l "Lets kick some ass!"
        jump margo4ever
    else:
        show noir
        n "I wont dissapoint you, lets do our best!"
        jump noir4ever
    return
    
    
    
label margo4ever:
    l "Test margo!"
    jump margo4evercap1
    return
    
label noir4ever:
    n "Test noir!"
    jump noir4evercap1
    return


label margo4evercap1:
    l "Test margo cap 1!"
    return
    
label noir4evercap1:
    n "Test noir cap 2!"
    return
    
