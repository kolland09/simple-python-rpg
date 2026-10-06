import random
import time

class Player:
    def __init__(self, name):
        self.lvl = 1
        self.name = name
        self.perm_hp = 100
        self.hp = 100
        self.perm_mana = 50
        self.mana = 50
        self.defense = 5
        self.p_xp = 0
        self.xp_needed = 100
        self.p_coins = 0
        self.p_dmg = 10

    def gain_xp(self, amount):
        self.p_xp += amount
        print(f"Gained {amount} XP!")

        if self.p_xp >= self.xp_needed:
            self.lvl += 1
            self.p_xp -= self.xp_needed
            self.perm_hp = int(self.perm_hp * 1.1)
            self.perm_mana = int(self.perm_mana * 1.1)
            self.defense += 1
            self.xp_needed = int(self.xp_needed * 1.2)
            self.p_dmg += 1
            print(f"You leveled UP! Stats increased!")

    def use_potion(self):
        if self.hp == self.perm_hp:
            print("Your Health is already Full! You wasted your turn!")
            print("")
            time.sleep(1.5)

        else:
            print("Glug glug glug... You healed...")
            print("")
            time.sleep(1.5)

            self.hp += 50
            if self.hp >= self.perm_hp:
                self.hp = self.perm_hp

class Monster:
    def __init__(self, name, level, base_hp):
        self.name = name
        self.lvl = level
        self.base_hp = base_hp

        if self.lvl == 1:
            pass
        elif self.lvl == 2:
            self.base_hp += 15
        elif self.lvl == 3:
            self.base_hp += 25
        elif self.lvl == 4:
            self.base_hp += 35
        elif self.lvl == 5:
            self.base_hp += 45

        self.hp = self.base_hp

    def slash_attack(self):
        damage = random.randint(12, 15)
        print("Enemy goblin used Slash Attack...")
        time.sleep(1.5)
        if self.lvl == 2:
            damage += 4
        elif self.lvl == 3:
            damage += 7
        elif self.lvl == 4:
            damage += 10
        elif self.lvl == 5:
            damage += 13

        crit = random.randint(1, 10)
        if crit <= 2:
            damage = int(damage * 1.5)
            print(f"Enemy goblin landed a Critical Hit of {damage}!")
            print("")
            time.sleep(1.5)
            return damage
        else:
            print(f"Enemy hit you with {damage} damage.")
            print("")
            time.sleep(1.5)
            return damage


    def pumpkin_bomb(self):
        damage = random.randint(18, 20)
        print("Enemy goblin used Pumpkin Bomb...")
        time.sleep(1.5)
        if self.lvl == 2:
            damage += 4
        elif self.lvl == 3:
            damage += 7
        elif self.lvl == 4:
            damage += 10
        elif self.lvl == 5:
            damage += 13

        crit = random.randint(1, 10)
        if crit <= 2:
            damage = int(damage * 1.5)
            print(f"Enemy goblin landed a Critical Hit of {damage}!")
            print("")
            time.sleep(1.5)
            return damage
        else:
            print(f"Enemy hit you with {damage} damage.")
            print("")
            time.sleep(1.5)
            return damage

    def gas(self):
        damage = 10
        print("Enemy goblin used Gas...")
        time.sleep(1.5)

        print("You got Confused and was not able to Attack.")
        time.sleep(1.5)
        print("You inhaled too much of gas and lose some HP.")
        print("")
        return damage

    def missed(self):
        print("Enemy goblin missed Attack...")
        print("")
        time.sleep(1.5)
        return 0

    def run(self):
        print("The Goblin accepted your offering and run away")
        time.sleep(1.5)

        print("Something was dropped")
        time.sleep(1.5)

        print("You pick it up and Receive a small bottle with unidentified water.")
        print("")
        time.sleep(1.5)

player_bag = []
player_b_weight_limit = 30
small_bottle = 0
item_weights = {"Long Sword": 15, "Dagger": 5, "Potion": 0.1}

potion = 1
player_bag_weight = 0
player_bag_weight += potion * 0.1
player_bag_weight = round(player_bag_weight, 1)

hero = Player("Hades")

while True:
    has_clothing = False
    player_confused = False
    flee = False

    print("----------------------------------------------")
    print(f"Lvl: {hero.lvl}")
    print(f"Player HP: {hero.hp}| Mana: {hero.mana}")
    print(f"EXP: {hero.p_xp}/{hero.xp_needed}")
    print(f"Coins: {hero.p_coins}")
    print("----------------------------------------------")
    print("")
    time.sleep(1.5)

    print("1. Enter the Cathedral")
    print("2. Go to the Forest")
    print("3. Check Bag")
    print("4. Quit Game")
    choice = input("What do you want to do...")
    print("")

    if choice == "1":
        print("Welcome to the Cathedral!")
        print("")
        time.sleep(1.5)
        while True:
            print("1. Talk to the Priest")
            print("2. Talk to Blacksmith Elrond")
            print("3. Go outside of Cathedral")
            choice = input("What do you want to do...")
            print("")
            if choice == "1":
                while True:
                    time.sleep(1.5)
                    print("1. Ask the Priest to Heal you...")
                    print("2. Nothing...")
                    choice = input("What do you want to do...")
                    print("")
                    if choice == "1":
                        print("The Priest is Healing you...")
                        print("")
                        time.sleep(3.0)
                        print("You are Healed...")
                        print("")
                        hero.mana += 999
                        if hero.mana > hero.perm_mana:
                            hero.mana = hero.perm_mana
                        hero.hp += 999
                        if hero.hp > hero.perm_hp:
                            hero.hp = hero.perm_hp
                            time.sleep(1.5)
                        break
                    elif choice == "2":
                        print("Priest: Stop wasting my time and go forth young adventurer.")
                        print("")
                        time.sleep(1.5)
                        break
            elif choice == "2":
                while True:
                    print("Elrond: Welcome newcomers! What can I help you?")
                    print("")
                    time.sleep(1.5)
                    print("1. Buy")
                    print("2. Sell")
                    print("3. Nothing...")
                    choice = input("What do you want to do...")
                    if choice == "1":
                        while True:
                            time.sleep(1.5)
                            print("")
                            print(f"Browsing Shop:      Player Coins({hero.p_coins})")
                            print("1. Long Sword + 10 dmg | Weight: 15kg | Cost: 550 Coins")
                            print("2. Dagger + 5 dmg | Weight: 5kg | Cost: 350 Coins")
                            print("3. Potion + 40hp | Weight: 0.5 | Cost: 100")
                            print("4. Exit Shop")
                            choice = input("What do you want to do...")
                            if choice == "1":
                                if hero.p_coins < 550:
                                    print("You don't have enough coins...")
                                    print("")
                                    time.sleep(1.5)
                                else:
                                    item_wt = item_weights["Long Sword"]
                                    if item_wt <= player_b_weight_limit - player_bag_weight:
                                        player_bag_weight += item_weights["Long Sword"]
                                        print("You bought Long Sword for 550 Coins")
                                        print("")
                                        time.sleep(1.5)
                                        player_bag.append("Long Sword")
                                        hero.p_coins -= 550
                                    else:
                                        print("Weight limit or bag limit for bag has been maxed...")
                                        print("")
                            elif choice == "2":
                                if hero.p_coins < 350:
                                    print("You don't have enough coins...")
                                    print("")
                                    time.sleep(1.5)
                                else:
                                    item_wt = item_weights["Dagger"]
                                    if item_wt <= player_b_weight_limit - player_bag_weight:
                                        player_bag_weight += item_weights["Dagger"]
                                        print("You bought Dagger for 350 Coins")
                                        print("")
                                        time.sleep(1.5)
                                        player_bag.append("Dagger")
                                        hero.p_coins -= 350
                                    else:
                                        print("Weight limit or bag limit for bag has been maxed...")
                                        print("")
                            elif choice == "3":
                                if hero.p_coins < 100:
                                    print("You don't have enough coins...")
                                    print("")
                                    time.sleep(1.5)
                                else:
                                    potion += 1
                                    item_wt = item_weights["Potion"]
                                    if item_wt <= player_b_weight_limit - player_bag_weight:
                                        player_bag_weight += item_weights["Potion"]
                                        print("You bought Potion for 100 Coins")
                                        print("")
                                        time.sleep(1.5)
                                        hero.p_coins -= 100  
                                    else:
                                        print("Not enough storage.. Weight limit or bag limit has been maxed...")
                                        print("")
                            elif choice == "4":
                                print("")
                                break
                    elif choice == "2":
                        time.sleep(1.5)
                        print("Selling Items:")
                        print("")
                        while True:
                            print("1.")
                            print("Exit")
                            choice = input("What do you want to do...")

                            if choice == "1":
                                print("Nothing happens...")
                                print("")
                                time.sleep(1.5)
                            elif choice == "2":
                                print("")
                                break
                    elif choice == "3":
                        time.sleep(1.5)
                        print("")
                        break
            elif choice == "3":
                print("You go outside of the Cathedral...")
                print("")
                time.sleep(1.5)
                break
    elif choice == "2":
        g_lvl = random.randint(1, 5)
        enemy = Monster("Goblin", g_lvl, 60)
        print("You venture the forest...")
        print("")
        time.sleep(1.5)
        print("You walk around the forest and encounter a goblin...")
        print("")
        time.sleep(1.5)
        print("Preparing to battle...")
        print("")
        time.sleep(1.5)

        print("=====================================")
        print(f"You encountered Lvl {enemy.lvl} Goblin!")
        print("=====================================")
        print("")
        time.sleep(1.5)

        g_xp = random.randint(50, 100)
        if g_lvl == 2:
            g_xp = int(g_xp * 1.2)
        elif g_lvl == 3:
            g_xp = int(g_xp * 1.3)
        elif g_lvl == 4:
            g_xp = int(g_xp * 1.4)
        elif g_lvl == 5:
            g_xp = int(g_xp *1.5)

        drop_coins = random.randint(10, 15)
        if g_lvl == 2:
            drop_coins = int(drop_coins * 1.2)
        if g_lvl == 3:
            drop_coins = int(drop_coins * 1.2)
        if g_lvl == 4:
            drop_coins = int(drop_coins * 1.2)
        if g_lvl == 5:
            drop_coins = int(drop_coins * 1.2)

        while hero.hp > 0 and enemy.hp > 0:
            guarding = False


            print("=======================================================================")
            print(f"Lvl: {hero.lvl}")
            print(f"Player HP {hero.hp} | Mana {hero.mana} | Potion {potion} | Current XP ({hero.p_xp}/{hero.xp_needed})")
            print(f"Level {enemy.lvl} Goblin HP {enemy.hp}")
            print("=======================================================================")
            print("")
            time.sleep(1.5)

            if player_confused:
                print("You are too confused to act! You stumble around blindly...")
                time.sleep(2.0)
                player_confused = False
            else:
                while True:
                    print("1. Use Sword Attack")
                    print("2. Use Fire Ball (15 Mana)")
                    print("3. Use Shield")
                    print("4. Use Potion")
                    print("5. Run")
                    choice = input("Player making a move (1-4): ")

                    if choice == "1":
                        chance = random.randint(1, 10)
                        if chance <= 1:
                            print("You missed to Attack the enemy!")
                            print("")
                            time.sleep(1.5)
                            chance = random.randint(1, 15)
                            if chance <= 1:
                                print("You accidentally swung too far and hurt yourself instead...")
                                print("")
                                hero.hp -= 10
                            break

                        else:
                            damage = random.randint(7, 10)
                            print("You used Sword Attack...")
                            time.sleep(1.5)

                            crit = random.randint(1, 10)

                            if crit <= 2:
                                damage = int(damage * 1.5)
                                damage += hero.p_dmg
                                print(f"You landed a Critical Hit of {damage} using Sword Attack!")
                                
                                enemy.hp -= damage
                                print("")
                                time.sleep(1.5)
                                if enemy.hp < 0:
                                    enemy.hp = 0

                                print("=======================================================================")
                                print(f"Lvl: {hero.lvl}")
                                print(f"Player HP {hero.hp} | Mana {hero.mana} | Potion {potion} | Current XP ({hero.p_xp}/{hero.xp_needed})")
                                print(f"Level {enemy.lvl} Goblin HP {enemy.hp}")
                                print("=======================================================================")
                                print("")
                                time.sleep(1.5)
                                break

                            else:
                                print(f"You hit the enemy with {damage} Normal Damage.")
                                time.sleep(1.5)
                                damage += hero.p_dmg
                                enemy.hp -= damage
                                print("")
                                if enemy.hp < 0:
                                    enemy.hp = 0

                                print("=======================================================================")
                                print(f"Lvl: {hero.lvl}")
                                print(f"Player HP {hero.hp} | Mana {hero.mana} | Potion {potion} | Current XP ({hero.p_xp}/{hero.xp_needed})")
                                print(f"Level {enemy.lvl} Goblin HP {enemy.hp}")
                                print("=======================================================================")
                                print("")
                                time.sleep(1.5)
                                break

                    elif choice == "2":
                        if hero.mana < 15:
                            print("You don't have enough mana to use Fire Ball...")
                            print("")
                            time.sleep(1.5)
                            continue
                            
                        else:
                            chance = random.randint(1, 10)
                            if chance <= 1:
                                print("You tried to use Fire Ball but missed your Attack!")
                                print("")
                                time.sleep(1.5)
                                hero.mana -= 15
                                break
                            else:
                                damage = random.randint(20, 25)
                                print("You used Fire Ball...")
                                time.sleep(1.5)

                                crit = random.randint(1, 10)

                                if crit <= 2:
                                    damage = int(damage * 1.5)
                                    print(f"You landed a Critical Hit of {damage} using Fire Ball!")
                                    enemy.hp -= damage
                                    print("")
                                    time.sleep(1.5)
                                    print("- 15 mana")
                                    hero.mana -= 15
                                    if enemy.hp < 0:
                                        enemy.hp = 0

                                    print("=======================================================================")
                                    print(f"Lvl: {hero.lvl}")
                                    print(f"Player HP {hero.hp} | Mana {hero.mana} | Potion {potion} | Current XP ({hero.p_xp}/{hero.xp_needed})")
                                    print(f"Level {enemy.lvl} Goblin HP {enemy.hp}")
                                    print("=======================================================================")
                                    print("")
                                    time.sleep(1.5)
                                    break
                                else:
                                    print(f"You hit the enemy with Fire Ball damage of {damage}.")
                                    enemy.hp -= damage
                                    print("")
                                    time.sleep(1.5)
                                    print("- 15 mana")
                                    hero.mana -= 15
                                    if enemy.hp < 0:
                                        enemy.hp = 0

                                    print("=======================================================================")
                                    print(f"Lvl: {hero.lvl}")
                                    print(f"Player HP {hero.hp} | Mana {hero.mana} | Potion {potion} | Current XP ({hero.p_xp}/{hero.xp_needed})")
                                    print(f"Level {enemy.lvl} Goblin HP {enemy.hp}")
                                    print("=======================================================================")
                                    print("")
                                    time.sleep(1.5)
                                    break

                    elif choice == "3":
                        guarding = True
                        print("You used Shield. Block 20 enemy incoming damage...")
                        print("")
                        time.sleep(1.5)
                        break

                    elif choice == "4":
                        if potion > 0:
                            potion -= 1
                            print("You used Potion...")
                            print("")
                            time.sleep(1.5)

                            hero.use_potion()
                            print("=======================================================================")
                            print(f"Lvl: {hero.lvl}")
                            print(f"Player HP {hero.hp} | Mana {hero.mana} | Potion {potion} | Current XP ({hero.p_xp}/{hero.xp_needed})")
                            print(f"Level {enemy.lvl} Goblin HP {enemy.hp}")
                            print("=======================================================================")
                            print("")
                            time.sleep(1.5)
                            break

                        else:
                            print("You search for potion in your bag but found nothing...")
                            print("")
                            time.sleep(1.5)

                            if not has_clothing:
                                has_clothing = True
                                print("✨ SECRET: Deep inside your empty bag, you found an old set of fine clothing!")
                                print("You tuck it under your arm. Maybe it's useful for something...?")
                                print("")
                                time.sleep(2.0)
                            break

                    elif choice == "5":
                        flee_failed = random.randint(1,15)
                        if flee_failed <= 1:
                            print("You tried to run away but freeze... Battle will continue...")
                            print("")
                            time.sleep(1.5)
                        else:
                            flee = True
                            print("You run away from the battle...")
                            print("")
                            time.sleep(1.5)
                            print("Battle ended...")
                        break

                    else:
                        print("You missed your turn to attack...")
                        print("")
                        time.sleep(1.5)
                        break

                if flee:
                    break

                if hero.hp <= 0:
                    print("You have been slain by the enemy goblin... You died.")
                    time.sleep(1.5)
                    print("Game Over!")
                    break

                if enemy.hp <= 0:
                    hero.gain_xp(g_xp)
                    hero.p_coins += drop_coins
                    print("You have slained the enemy goblin...")
                    time.sleep(1.5)
                    print("You Win!")
                    print(f"✨ XP gained {g_xp}...")
                    print(f"💰 Coins gained {drop_coins}...")
                    print("")
                    time.sleep(3.0)
                    break

            print("Goblin is attacking...")
            time.sleep(1.5)

            attack = random.randint(1, 10)

            if attack == 10 and not has_clothing:
                attack = random.randint(1, 9)

            if attack in [1, 3, 5]:
                enemy_dmg = enemy.slash_attack()

            elif attack in [2, 4, 6]:
                enemy_dmg = enemy.pumpkin_bomb()

            elif attack in [7, 8]:
                enemy_dmg = enemy.gas()
                player_confused = True

            elif attack == 9:
                enemy.missed()
                enemy_dmg = 0
                
            elif attack == 10:
                if has_clothing:
                    print("The goblin spots the fine clothing in your hands and stops attacking!")
                    time.sleep(1.5)

                    print("You decide to offer the clothing to the goblin...")
                    print("")
                    time.sleep(1.5)
                    
                    enemy.run()
                    small_bottle += 1
                    print("Battle ended...")
                    break

            if attack in [1, 2, 3, 4, 5, 6, 7, 8]:
                if guarding:
                    enemy_dmg = max(0, enemy_dmg - 20)
                    print(f"Your shield blocked damage! You take {enemy_dmg} instead.")
                    hero.hp -= enemy_dmg
                    if hero.hp < 0:
                        hero.hp = 0
                    print("")
                    time.sleep(1.5)
                else:
                    hero.hp -= enemy_dmg
                    if hero.hp < 0:
                        hero.hp = 0

        if hero.hp <= 0:
            print(f"|Player HP drop to {hero.hp}|")
            print("")
            time.sleep(1.5)
            print("Your have been slained by the enemy goblin.")
            time.sleep(1.5)
            print("YOU DIED!")
            print("")
            time.sleep(1.5)
            choice = input("Press ENTER to Respawn")
            if choice == "":
                print("Respawning...")
                print("")
                time.sleep(3)
            continue

    elif choice == "3":
        print("Opening Bag...")
        print("")
        time.sleep(1.5)
        if potion > 0:
            player_bag.append(f"Potion: {potion}")
        if len(player_bag) > 0:
            print(f"Bag Weight: {player_bag_weight}/{player_b_weight_limit}")
            for item in player_bag:
                print(item)
            if potion > 0:
                player_bag.remove(f"Potion: {potion}")
            choice = input("Press Enter to exit Bag...")
        if len(player_bag) == 0:
            print("Your bag is completely empty!")
            print("")
            time.sleep(1.5)

    elif choice == "4":
        time.sleep(1.5)
        print("Good bye Adventurer! Until next time.")
        break