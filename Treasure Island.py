print("""
      _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|
""")


print("Welcome to Treasure Island!" )
print("Your mission is to find the treasure.")
print("But first you must answer riddles correctly ")

print(r"""       ___
                  /`\      .' -,'-.__,@
                 /        |     `).-'
               _/       _\V^V^V^V/_
              | /\     .=// ^.^ \\=.
              /\ /     .'/| ._. |\'.
             / /-`.       _\___/_
              |/\/\   _@->`   _  `<-@._
                \  \.'  @-'`\( `'-,@   '-.
                 \      ,    @    , _.-   `\
                  \   .'|    :    |` /'. _.'
                   `"`   \   :    / /`\_|  @
                   @_  _.'`""""""`'-\_\.--;`
                   `-.`      /,     `, .-'
                   _.@--; .-'| '. ;-._;@
             jgs .'     @' _.'.  `@  \
                |     _.-'`    '-.    \
                 '-._  `-._n_     )   |
                     `'-._ ) `-,.'   /
                          u-'--;`@ .'
                               |  /
                              ,\ /,
                              )\.'/
                             /   (
                             \_.. '._.@
                                 `-.-'""")

print("Here is your first Riddle! If answered correctly you can make your first RIGHT on the upcoming path. If you answer incorrectly then you will make a LEFT")

print(r""" ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/""")

Answer1= (input ("what do you have to break before you can use it?: ")).upper()
if Answer1 == 'Egg'.upper():
    print("You can make a left in the first fork of the road")
     
    
    Answer2= (input("You have moved on to the next level!. You have to SLAY Gargon and his Fire Breathing Dragon. If you answer the next riddle correctly, you will SLAY Gargon and his Fire Breathing Dragon. If not, then Gargon and his Dragon will SLAY you and the game will end!!!! Here is the next Riddle: I'm tall when I'm young, and I'm short when I'm old. What am I?: ")).upper()
    if Answer2 == 'Candle'.upper():
        print("Congratulations! you have slayed the Gargon and his Fire Breathing Dragon and have moved on to the last level!")
    
   
    
        Answer3 = (input("Here is the last Riddle: What month of the year has 28 days? ")).upper() 
        if Answer3 == 'All'.upper():
            print("Congrats you have won the GAME and have won the treasure!!!!!")       #To fix this, you need to tell Python not to treat backslashes in the string as escape characters. You can do this by using a raw string literal, which is done by prefixing the string with r. Here's the corrected code:
            print(r"""                         _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'`""")
    
        else:
             #Answer3 != 'All'.upper():
            print("You have lost the GAME!")
             
    else:
        #Answer2 != 'Candle'.upper():
        print("The Gargon and the Fire Breathing Dragon has slayed you and the GAME IS Over!")    
        print(r"""                _
                              ==(W{==========-      /===-
                                ||  (.--.)         /===-_---~~~~~~~----__
                                | \_,|**|,__      |===-~___            _,-'`
                   -==\\        `\ ' `--'   ),    `//~\\   ~~~~`--._.-~
               ______-==|        /`\_. .__/\ \    | |  \\          _-~`
         __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\       ,'
      _-~       /'    |  \\     )__/==0==-\<>/   / /      \     /
    .'        /       |   \\      /~\___/~~\/  /' /        \   /
   /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
  /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                    \_|      /        _) | ;  ),   __--~~
                      '~~--_/      _-~/- |/ \   '-~ \
                     {\__--_/}    / \\_>-|)<__\      \
                     /'   (_/  _-~  | |__>--<__|      |
                    |   _/) )-~     | |__>--<__|      |
                    / /~ ,_/       / /__>---<__/      |
                   o-o _//        /-~_>---<__-~      /
                   (^(~          /~_>---<__-      _-~
                  ,/|           /__>--<__/     _-~
               ,//('(          |__>--<__|     /                  .--_
              ( ( '))          |__>--<__|    |                 /' _-_~\
           `-)) )) (           |__>--<__|    | -Tua Xiong    /'  /   ~\`\
          ,/,'//( (             \__>--<__\    \            /'  //      ||
        ,( ( ((, ))              ~-__>--<_~-_  ~--__---~'/'/  /'       VV
      `~/  )` ) ,/|                 ~-_~>--<_/-__      __-~ _/
    ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~__--~
     ;'( ')/ ,)(                              ~~~~~~~~
    ' ') '( (/""")
   
        
else:
    if Answer1 != 'Egg'.upper(): 
        print("You can make a Right and SUPRISE, SUPRISE, You have been bit by the Giant Rattlesnake AND HAVE DIED! Please try your luck again! GAME OVER")                                                
        print(r"""          _.--....
                 _....---;:'::' ^__/
               .' `'`___....---=-'`
              /::' (`
              \'   `:.
               `\::.  ';-"":::-._  {}
            _.--'`\:' .'`-.`'`.' `{I}
         .-' `' .;;`\::.   '. _: {-I}`\
       .'  .:.  `:: _):::  _;' `{=I}.:|
      /.  ::::`":::` ':'.-'`':. {_I}::/
      |:. ':'  :::::  .':'`:. `'|':|:'
       \:   .:. ''' .:| .:, _:./':.|
    jgs '--.:::...---'\:'.:`':`':./
                       '-::..:::-'""")
      
        
    
         