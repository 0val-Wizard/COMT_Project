# Creating (e.g Earth, Fighter, Assassin )
class ElementalControl:
    # magic skills: Fire, Water, Air
    def __init__(self):
        self.magic_skills = {
            'fire': 20,
            'water': 25,
            'air': 30,
        }

    def fire(self):
        ap = self.magic_skills["fire"]
        return ap

    def water(self):
        ap = self.magic_skills["water"]
        return ap

    def air(self):
        ap = self.magic_skills["air"]
        return ap


class SumoWrestler:
    # magic skills: Powerbomb, Spear, Sumo punch
    def __init__(self):
        self.magic_skills = {
            'power bomb': 30,
            'spear': 25,
            'the stunner': 20,
        }

    def power_bomb(self):
        ap = self.magic_skills["power bomb"]
        return ap

    def spear(self):
        ap = self.magic_skills["spear"]
        return ap

    def the_stunner(self):
        ap = self.magic_skills["the stunner"]
        return ap


class Assassin:
    # magic skills:
    pass


class Character:
    def __init__(self, name, hp, ap, dp, mp, sp, char_type):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.dp = dp
        self.mp = mp
        self.sp = sp
        self.char_type = char_type
        # self.image = image

    def attack(self, target):
        print(type(self.ap))
        print(type(target.hp))
        if self.ap > target.hp:
            target.hp = 0
        else:
            result_damage = self.ap - target.dp
            target.hp -= result_damage
            print(target.hp)
        self.mp += 5

    def is_able_to_use_magic(self):
        print("You are only allowed to use magic when you have 20 magic points.")
        if self.mp >= 20:
            print("You are allowed to use magic skills.")
            return True
        elif self.mp < 20:
            print(f"You are not allowed to use magic skills, {self.mp} points. You need to have at least 20 magic "
                  f"points.")
            return False
        # Implement attack logic here
        # Calculate damage based on self.ap and target.dp
        # Update target's HP accordingly

    def use_skill(self, target, skill):
        if skill == '1':
            chosen_move = input(
                "Which element would you like to control?\n1) Fire 🔥 (20 AP)\n2) Water 💧(25 AP)\n3) Air 💨"
                "(30 AP)\n").lower()
            chosen_skill = ElementalControl()
            if chosen_move == '1':
                ap = chosen_skill.fire()
                target.hp -= ap
                self.mp -= 20
            elif chosen_move == '2':
                ap = chosen_skill.water()
                target.hp -= ap
                self.mp -= 20

            elif chosen_move == '3':
                ap = chosen_skill.air()
                target.hp -= ap
                self.mp -= 20

        elif skill == '2':
            chosen_move = input("Which element would you like to control?\nChoose a number\n"
                                "1) Power Bomb 💣 (30 AP) \n2) Spear 𐃆 (25 AP)\n3) The stunner (20 AP)"
                                "\n").lower()
            chosen_skill = SumoWrestler()
            if chosen_move == '1':
                ap = chosen_skill.power_bomb()
                target.hp -= ap
                self.mp -= 20

            elif chosen_move == '2':
                ap = chosen_skill.spear()
                target.hp -= ap
                self.mp -= 20

            elif chosen_move == '3':
                ap = chosen_skill.the_stunner()
                target.hp -= ap
                self.mp -= 20

    def defend(self):
        pass
        # Implement defend logic here
        # Increase self.dp for defense effect

    #         job = Earth()
    #         job.water()

    def is_alive(self):
        pass
        # Check if the character's HP is greater than zero

    #         return self.hp > 0

    def print(self):
        if self.char_type == "player":
            print(f"name: {self.name}, HP: {self.hp}, AP:{self.ap}, DP:{self.dp}, MP:{self.mp}, SP: {self.sp}")
        elif self.char_type == "enemy":
            print(f"name: {self.name}, HP: {self.hp}, AP:{self.ap}, DP:{self.dp}, SP: {self.sp}")


class Player(Character):
    def __init__(self, name, hp, ap, dp, mp, sp, char_type):
        super().__init__(self, name, hp, ap, dp, mp, sp)
        self.char_type = char_type
    # def __init__(self, name, hp, ap, dp, mp, sp, image, job_class, skill_type):
    # super().__init__(name, self, name, hp, ap, dp, mp, sp, image) --> add "char_type" attribute


class Enemy(Character):
    def __init__(self, name, hp, ap, dp, sp, char_type):
        super().__init__(self, name, hp, ap, dp, sp, char_type)
    # def __init__(self, name, hp, ap, dp, sp, image, job_class, skill_type):
    #     super().__init__(name, self, name, hp, ap, dp, sp, image)


player1 = Player("Player1", 100, 20, 10, 0, 10, char_type='player')
enemy1 = Enemy("Enemy1", 100, 20, 10, 20, 'enemy')
go_again = True
fight = True

while go_again:

    if player1.sp >= enemy1.sp:
        # Player is going first
        decision = input("The fight would be difficult. Would you like to\n1)Continue\n2)Quit\nPick a number\n")

        while fight:
            if decision == "1":
                # Gamer decides to fight
                print("Good luck! 🫡")

                if player1.hp != 0 and enemy1 != 0:
                    # Both characters are alive
                    print("\nIt is your turn:\n\n")
                    move_chosen = True
                    while move_chosen:
                        move = input("What move would you like to play (Attack/Defend/Skill):").lower()
                        if move == "attack":
                            player1.attack(enemy1)
                            if enemy1.hp < player1.ap - enemy1.dp:
                                enemy1.hp = 0
                            player1.print()
                            enemy1.print()
                            move_chosen = False

                        elif move == "defend":
                            if player1.hp <= 60:
                                player1.hp += 20
                                print(f"Your hp has risen to {player1.hp}")
                            elif player1.hp > 80:
                                player1.hp = 100
                                print(f"Your hp has risen to {player1.hp}")
                            move_chosen = False

                        elif move == "skill":
                            is_allowed = player1.is_able_to_use_magic()
                            if is_allowed:
                                move_chosen = False
                                player1.use_skill(enemy1, skill=input("Which skill would you pick?\n1)Elemental Control"
                                                                      "\n2)Sumo Punch"))
                                player1.print()
                                enemy1.print()

                                if enemy1.hp < player1.ap - enemy1.dp:
                                    enemy1.hp = 0
                                    player1.print()
                                    enemy1.print()
                            else:
                                move_chosen = False

                    else:
                        print("Invalid Input")
                    # give a solution for this

                    # Checking whether enemy is dead
                    if enemy1.hp == 0:
                        fight = False
                        print("Your enemy 1 has died.")

                    else:
                        # enemy's turn
                        print("\nIt is the enemy's turn:\n\n")
                        enemy1.attack(player1)
                        if player1.hp < enemy1.ap - player1.dp:
                            player1.hp = 0
                        enemy1.print()
                        player1.print()

                        # Checking of player is dead
                        if player1.hp == 0:
                            fight = False
                            print("Your player 1 has died.")
                else:
                    pass
                # this should be a pass
            #                 if player1.hp == 0:
            #                     print("Your player 1 died.")
            #                     fight = False
            #                 elif enemy1.hp == 0:
            #                     print("Enemy 1 died.")
            #                     fight = False

            elif decision == "2":

                print("🫵 dont give up next time.")
                fight = False
                print("Player runs away")

        print("Player runs")
        go_again = False
    else:
        # Enemy is going first

        while fight:
            decision = input("Do you want to;\n1)Continue\n2)Quit\n3)Restart")
            if decision == '1':
                print("Good luck! 🫡")
                if player1.hp != 0 and enemy1.hp != 0:
                    print("\nIt is the enemy's turn:\n\n")
                    enemy1.attack(player1)
                    if player1.hp < enemy1.ap - player1.dp:
                        player1.hp = 0
                    enemy1.print()
                    player1.print()
                    print("hello")

                    if player1.hp == 0:
                        print("Your player 1 has died")
                        fight = False
                    else:
                        # player's turn
                        print("\nIt is your turn:\n\n")
                        move_chosen = True
                        while move_chosen:
                            move = input("What move would you like to play (Attack/Defend/Skill):").lower()
                            if move == "attack":
                                player1.attack(enemy1)
                                if enemy1.hp < player1.ap - enemy1.dp:
                                    enemy1.hp = 0
                                player1.print()
                                enemy1.print()
                                move_chosen = False
                                if enemy1.hp == 0:
                                    fight = False
                                    print("The enemy1 died")

                            elif move == "defend":
                                if player1.hp <= 60:
                                    player1.hp += 20
                                    print(f"Your hp has risen to {player1.hp}")
                                elif player1.hp > 80:
                                    player1.hp = 100
                                    print(f"Your hp has risen to {player1.hp}")
                                move_chosen = False

                            elif move == "skill":
                                is_allowed = player1.is_able_to_use_magic()
                                print(player1.mp)
                                if is_allowed:
                                    move_chosen = False
                                    player1.use_skill(enemy1, skill=input("Which skill would you pick?\n1)Elemental "
                                                                          "Control\n2)Sumo Punch"))
                                    player1.print()
                                    enemy1.print()
                                    if enemy1.hp < player1.ap - enemy1.dp:
                                        enemy1.hp = 0
                                        player1.print()
                                        enemy1.print()
                                        if enemy1.hp == 0:
                                            fight = False
                                            print("The enemy1 died")
                                else:
                                    move_chosen = True

                            else:
                                print("Your input given is incorrect. Type again.")
                                move_chosen = True
                else:
                    pass
                    # THIS SHOULD BE A PASS
            #                 if player1.hp == 0:
            #                     print("Your player 1 died.")
            #                     fight = False
            #                 elif enemy1.hp == 0:
            #                     print("Your enemy 1 has died.")
            #                     fight = False
            elif decision == '2':
                print("🫵 dont give up next time.")
                fight = False
                print("Player runs away")
                go_again = False
            elif decision == '3':
                player1 = Player("Player1", 100, 20, 10, 0, 10, "player")
                enemy1 = Enemy("Enemy1", 100, 20, 10, 20, "enemy")
                print("The game is restarting now")
                print("\n\nRestarting...\n\n\n")
                go_again = True
                fight = True
