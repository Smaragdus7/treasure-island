print('''
     ?
             ____"_                   |   |
            /"  _)))                  |\_/|______,
           /===( _\                  /::| Q  ____)
          ("___|   >   ,_           /:::|   /    ,_
             o  _=    / _///       /::::|_ /    / _///
       _______| |____/ |         _|:::::| |:___/ |
      |  __)  \_/ /____|        | '----'\_/  /___|
     _| / \    ) )             _| /  \   :  /
 _\\\__/   \    /          _\\\__/    \    /
           /   (                      /===(
          / \   \                    /     \
         /   \   \                  /       \
         |    \   \                 |        \
         |     \   \                |         \
         |      \   \               |,_________\
         |       \   \               /  )  / )
         |,_______\___\             /  /  (  |
           | /   \ |                | /    \ |
           |/     \|                |/      \|
           S__     S__              S__      S__
          /___\   /___\   b'ger    /___\    /___\
''')
print("Welcome to Ancient Egypt.")
print("Your mission is to find the treasure of the Pharao.")

#Write your code below this line 👇
doors = input("You have two doors in front of you, which one do you choose? Type left or right\n")
doors = doors.lower()
if doors == "left":
    direction = input("Do you want to go downstairs or keep walking? Type stairs or walk\n")
    direction = direction.lower()
    if direction == "stairs":
        sarcophagus = input("You found a sarcophagus and a box, which one do you open? Type s or b\n")
        sarcophagus = sarcophagus.lower()
        if sarcophagus == "s":
            print("You found the treasure. YOU WON!")
        else:
            print("You found sand. GAME OVER!")
    elif direction == "walk":
        print("Run away, there's a mummy chasing you. GAME OVER!")
    else:
        print("GAME OVER")
elif doors == "right":
    print("You chose wrong, here comes the Pharao's army. GAME OVER!")
else:
    print("You coward. GAME OVER!")
