import random

def get_name():
    name = input("Enter your character's name: ")
    return name
get_name()

def sum_of_four_six_sided_dice_with_lowest_dropped():
    sumOfRoll = 0
    diceRoll = []  #makes an empty array
    for _ in range(4):
        num = random.randint(1, 6)
        diceRoll.append(num)  #creating an array and storing the found values- append like stapling papers to add all values into one array

    diceRoll.sort()  #sort from least to greatest
    #print(diceRoll)  #printing sorted array

    sumOfRoll = sum(diceRoll[-3:])

    return sumOfRoll

strength = sum_of_four_six_sided_dice_with_lowest_dropped()
dexterity = sum_of_four_six_sided_dice_with_lowest_dropped()
constitution = sum_of_four_six_sided_dice_with_lowest_dropped()
intelligence = sum_of_four_six_sided_dice_with_lowest_dropped()
wisdom = sum_of_four_six_sided_dice_with_lowest_dropped()
charisma = sum_of_four_six_sided_dice_with_lowest_dropped()

print(f"\nWelcome. The abilities chosen for you are:\n\n"
      f"Strength: {strength}"
      f"\nDexterity: {dexterity}"
      f"\nConstitution: {constitution}"
      f"\nIntelligence: {intelligence}"
      f"\nWisdom: {wisdom}"
      f"\nCharisma: {charisma}")

def get_ability_modifier(score):
    if score == 3:
        modifier = -4
    elif score == 4 or 5:
        modifier = -3
    elif score == 6 or 7:
        modifier = -2
    elif score == 8 or 9:
        modifier = -1
    elif score == 10 or 11:
        modifier = 0
    elif score == 12 or 13:
        modifier = 1
    elif score == 14 or 15:
        modifier = 2
    elif score == 16 or 17:
        modifier = 3
    elif score == 18:
        modifier = 4

    return modifier

def menu():
    action = input("\nEnter an action(Attack/Negotiate/Search/Eat): ")

    match action:
        case "attack":
            twentySideDieRoll = random.randint(1, 20)
            abilityModifierScore = twentySideDieRoll + get_ability_modifier(strength or dexterity)
            print(f"You rolled {twentySideDieRoll}/20")
            if abilityModifierScore >= 12:
                print("Hit")
                sixSideDieRoll = random.randint(1, 6)
                totalDamageDealt = sixSideDieRoll + get_ability_modifier(strength)
                totalDamageDealt >= 0  #has to be greater or equal to 0
                print(f"You've dealt {totalDamageDealt} damage!")
            else:
                print("Miss")
        case "negotiate":
            twentySideDieRoll = random.randint(1, 20)
            abilityModifierScore = twentySideDieRoll + get_ability_modifier(charisma)
            print(f"You rolled {twentySideDieRoll}/20")
            if abilityModifierScore >= 15:
                print("You have successfully negotiated a truce. Nice!")
            else:
                print("Nothing happened.")
        case "search":
            twentySideDieRoll = random.randint(1, 20)
            abilityModifierScore = twentySideDieRoll + get_ability_modifier(intelligence or wisdom)
            print(f"You rolled {twentySideDieRoll}/20")
            if abilityModifierScore >= 12:
                print("You found gems!")
            else:
                print("You didn't find anything.")
        case "eat":
            print("Oh no! You ate rotten food!")
            twentySideDieRoll = random.randint(1, 20)
            abilityModifierScore = int(twentySideDieRoll + get_ability_modifier(constitution))
            print(f"You rolled {twentySideDieRoll}/20")
            if abilityModifierScore >= 10:
                print("Luckily, you could handle it.")
            else:
                print("You were not able to handle the food. You are now sick and must stay in bed.")
    return action


for _ in range(4):
    menu()