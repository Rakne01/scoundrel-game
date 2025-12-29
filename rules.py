TITLE = """
                                                                                                     ,--,    
                           ,----..                          ,--.                                  ,---.'|    
  .--.--.     ,----..     /   /   \                       ,--.'|    ,---,    ,-.----.       ,---,.|   | :    
 /  /    '.  /   /   \   /   .     :          ,--,    ,--,:  : |  .'  .' `\  \    /  \    ,'  .' |:   : |    
|  :  /`. / |   :     : .   /   ;.  \       ,'_ /| ,`--.'`|  ' :,---.'     \ ;   :    \ ,---.'   ||   ' :    
;  |  |--`  .   |  ;. /.   ;   /  ` ;  .--. |  | : |   :  :  | ||   |  .`\  ||   | .\ : |   |   .';   ; '    
|  :  ;_    .   ; /--` ;   |  ; \ ; |,'_ /| :  . | :   |   \ | ::   : |  '  |.   : |: | :   :  |-,'   | |__  
 \  \    `. ;   | ;    |   :  | ; | '|  ' | |  . . |   : '  '; ||   ' '  ;  :|   |  \ : :   |  ;/||   | :.'| 
  `----.   \|   : |    .   |  ' ' ' :|  | ' |  | | '   ' ;.    ;'   | ;  .  ||   : .  / |   :   .''   :    ; 
  __ \  \  |.   | '___ '   ;  \; /  |:  | | :  ' ; |   | | \   ||   | :  |  ';   | |  \ |   |  |-,|   |  ./  
 /  /`--'  /'   ; : .'| \   \  ',  / |  ; ' |  | ' '   : |  ; .''   : | /  ; |   | ;\  \'   :  ;/|;   : ;    
'--'.     / '   | '/  :  ;   :    /  :  | : ;  ; | |   | '`--'  |   | '` ,/  :   ' | \.'|   |    \|   ,/     
  `--'---'  |   :    /    \   \ .'   '  :  `--'   \'   : |      ;   :  .'    :   : :-'  |   :   .''---'      
             \   \ .'      `---`     :  ,      .-./;   |.'      |   ,.'      |   |.'    |   | ,'             
              `---`                   `--`----'    '---'        '---'        `---'      `----'               
                                                                                                             
"""

RULES = """FROM © 2011, Zach Gage and Kurt Bieg. stfj.net

Rules:
The 26 Clubs and Spades in the deck are Monsters. Their damage is equal to their ordered value. (e.g.
10 is 10, Jack is 11, Queen is 12, King is 13, and Ace is 14)
The 9 Diamonds in the deck are Weapons. Each weapon does as much damage as its value. 
The 9 Hearts in the deck are Health Potions. You may only use one health potion each turn, even if you
pull two. The second potion you pull is simply discarded. You may not restore your life beyond your
starting 20 health.
The Game ends when either your life reaches 0 or you make your way through the entire Dungeon

COMBAT:
If you chose a Monster...
You may either fight it barehanded or with an equipped Weapon.
- If you choose to fight the Monster barehanded, subtract its full value from your Health
- If you choose to fight the Monster with your equipped Weapon, subtract the
Weapon's value from the Monster's value and subtract any remaining value from your health.
! For example, if your Weapon is a 5, and you place a 3 Monster on it, you take no damage. ( 3-5 < 0)
! If your Weapon is a 5 and you place a Jack Monster on it, you take 6 damage. ( 11 - 5 = 6 dmg)

***It is important to note that although you retain your weapons until they are replaced, once a
Weapon is used on a monster, the Weapon can then only be used to slay Monsters of a lower
value (less than equal) than the previous Monster it had slain.
! For example, if your 5 Weapon has killed a Queen Monster and you then choose a 6 Monster, you
! may use !your Weapon on the 6 Monster, as 6 is less than 12.
! But, if you have used your 5 Weapon on a 6 Monster, and you then choose a Queen Monster,
! you must fight the Queen barehanded as Queen,12, is greater than 6. Despite this, the Weapon is not
! discarded, as it could still be used against Monsters weaker than a 6.

"""