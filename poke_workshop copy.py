import random

def menu():
    print("1. fight")
    print("2. bag")
    print("3. pokemon")
    print("4. run")

def enemy_attack(starter, p_hp):
    print("-------------")
    print("pikachu used thunderbolt!")

    e_attack = random.randint(1, 10)

    p_hp = max(0, p_hp - e_attack)

    print(f"{starter}'s hp is now {p_hp}!")

    return p_hp

def choice1(enemy_hp):
    p_attack = random.randint(1, 10)

    enemy_hp = max(0, enemy_hp - p_attack)

    print(f"pikachu's hp is now {enemy_hp}")

    return enemy_hp

def choice2(starter, p_hp, max_hp, potion):
        print(f"youhave {potion} hp potion(s).")

        if potion > 0:
            use = input("do you want to use it? type 'yes' or 'no'\n")
            if use == 'yes':
                if p_hp < max_hp:
                    heal = random.randint(1,15)
                    p_hp += heal
                    potion -= 1
                    if p_hp > max_hp:
                        p_hp = max_hp
                    print(f"{starter}'s hp is now {p-hp}")
                else:
                    print("you cannot use this item.")
        else:
            print("you have no more potions...")
        return p_hp, potion
def main():
    print("hello! welcome to the world of pokemon, today, you will do your first ever pokemon battle!")
    name = input("before we begin, what's your name/\n")
    print(f"hey {name}!")

    print("it's time to choose your starter, please select from the following choices:")
    print("charmander | squirlte | bulbasaur")

    valid_starters = [ ' charmander', 'squirtle', 'bulbasaur']
    starter = input("who do you choose?\n").lower()
    while starter not in valid_starters:
        print("that is not one of the options. please try again")
        starter = input("who do you choose?\n").lower()
    print("n\great choice!n\nnow let's begin the battle.n\")")

    print("--- A WILD PIKACHU APPEARED ---")

    max_hp = 25
    enemy_hp = 30
    potion = 1

    print(f"your max hp is {max_hp}!\n")
    p_hp = max_hp

    while True:
            print("-------------------------")

            menu()
            choice = int(input(f"what will {starter} do?\n"))

            if starter == 'charmander':
                if choice == 1:
                    print("charmander used scratch!")
                    enemy_hp = choice1(enemy_hp)

                    if enemy_hp == 0:
                        print("you win!!:D")
                        break
                    else:
                        pass
                    p_hp = enemy_attack(starter, p_hp)
                    if p_hp == 0:
                        print("you lose :(")
                elif choice == 2:
                    p_hp, potion = choice2(starter, p_hp, max_hp, potion)
                elif choice == 3:
                    print("you have no other pokemon available.")
                elif choice == 4:
                    print("you ran away!")
                    break
                else:
                    print("choose a valid option...")
            if starter == 'squirtle':
                if choice == 1:
                    print("squirtle used water gun!")
                    enemy_hp = choice1(enemy_hp)

                    if enemy_hp == 0:
                        print("you win!!:D")
                        break
                    else:
                        pass
                    p_hp = enemy_attack(starter, p_hp)
                    if p_hp == 0:
                        print("you lose :(")
                elif choice == 2:
                    p_hp, potion = choice2(starter, p_hp, max_hp, potion)
                elif choice == 3:
                    print("you have no other pokemon available.")
                elif choice == 4:
                    print("you ran away!")
                    break
                else:
                    print("choose a valid option...")
            if starter == 'bulbasaur':
                if choice == 1:
                    print("bulbasaur used vinewhip!")
                    enemy_hp = choice1(enemy_hp)

                    if enemy_hp == 0:
                        print("you win!!:D")
                        break
                    else:
                        pass
                    p_hp = enemy_attack(starter, p_hp)
                    if p_hp == 0:
                        print("you lose :(")
                elif choice == 2:
                    p_hp, potion = choice2(starter, p_hp, max_hp, potion)
                elif choice == 3:
                    print("you have no other pokemon available.")
                elif choice == 4:
                    print("you ran away!")
                    break
                else:
                    print("choose a valid option...")
main()