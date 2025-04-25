import random

## Player Stats
health = 0
dmg = 0
response = input("Choose your Character \n Josuke, Dio, Jotoro \n Name:")
##response = "Jotoro"

## TO CHOOSE YOUR CHARACTER STATS
def characterChooser(char):
    global health 
    global dmg
    match char:
        case "Jotoro":
            health = 25
            dmg = 5
        case "Josuke":
            health = 10
            dmg = 15
        case "Dio":
            health = 5
            dmg = 25
    
characterChooser(response)
#print(dmg)
#print(health)

## [NAME, HEALTH, DMG]
enemyJohn = ["John Madden", 20, 4]
enemyGlorp = ["GLROP", 2, 10]
enemyDogg = ["Snoop", 15, 8]
 
enemyList = [enemyGlorp, enemyDogg, enemyJohn]

def playerHeal():
    global health
    health += 5

def enemyEncounter(List):
    global health 
    global dmg
    enemy = random.choice(List) ## chose nemy here
    print("YOU encountered a wild", enemy[0], "\n")
    while enemy[1] >= 1 and health >= 1:
        print("You have", health, "HP \nYou can do", dmg, "damage\n")
    
        action = input("What do you want to do??? \n \n [ATTACK] [HEAL] [MASTERBATE]\n :")
        match action:
            case "attack":
                enemy[1] -= dmg
                print("You Attack! \n", enemy[0], "Now has", enemy[1], "HP!")
            case "heal":
                playerHeal()
                print("You heal, gaining 5 HP and a total of", health, "HP!")
            case "masterbate":
                enemy[2] += 10
                print( enemy[0], "has been inspired \n\n he now does,", enemy[2], "damage!!!" )
            case _:
                print("You do nothing!!!")
        health -= enemy[2]
        print(enemy[0], "attacks you with a damage of", enemy[2])


enemyEncounter(enemyList)
