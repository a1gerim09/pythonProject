# # from random import randint
# #
# # class Player:
# #     hp = 100
# #     damage = 10
# #
# # # Записываем в переменную, чтобы было удобно.
# # p = Player()
# #
# # class Enemy:
# #     # Рандомно получает хп врага от 70 до 130, рандомно получает дамаг врага от 6 до 13.
# #     hp = randint(70,130)
# #     damage = randint(6,13)
# #
# # # Записываем в переменную, чтобы было удобно.
# # e = Enemy()
# #
# # def menu(p):
# #     while True:
# #         print("1) Сражаться")
# #         print("2) Посмотреть статистику")
# #         # try и except просто фиксят ошибки. Не обращайте внимания.
# #         try:
# #             n = input("Введите число: ")
# #
# #             if n == 1:
# #                 menu_fight(p)
# #             if n == 2:
# #                 menu_stats(p)
# #             else:
# #                 print("Чего ждем?")
# #
# #         except NameError:
# #             print("Введите число")
# #         except SyntaxError:
# #             print("Введите число")
# #
# # def menu_stats(p):
# #     print("Статистика игрока")
# #     print("*****************")
# #     # Попробую обьяснить, что значит %s. Она по последовательности списка вписывает в %s переменную.
# #     print("hp %s."%(p.hp))
# #     print(f"Вы hp: {p.hp} damage: {p.damage}")
# #     print("damage %s."%(p.damage))
# #     input("Нажмите Enter для продолжения.")
# #
# # def menu_fight(p):
# #     while e.hp > 0:
# #         # Также, как я и сказал по последовательности списка расставляет переменные.
# #         print("Вы hp: %s damage: %s")%(p.hp, p.damage)
# #         print("Враг hp: %s damage: %s")%(e.hp, e.damage)
# #         print("**********************")
# #         print("1)Ударить")
# #         print("2)Хил 0-5")
# #         n = input("Введите число: ")
# #         if n == 1:
# #             # Здоровье врага отнимает от вашего дамага.
# #             e.hp -= p.damage
# #             print("Вы ударили противника, у него осталось %s hp")%(e.hp)
# #             # Здоровье игрока отнимает от дамага врага.
# #             p.hp -= e.damage
# #             print("Противник ударил вас, у вас осталось %s hp")%(p.hp)
# #
# #             print("*********************")
# #
# #         if n == 2:
# #             # Рандомно от 0 до 5 добавляет хп.
# #             p.hp += randint(0,5)
# #             # Если здоровье игрока больше, то хп игрока будет равна 100.
# #             if p.hp > 100:
# #                 p.hp = 100
# #
# #             print("Ваши хп %s")%(p.hp)
# #
# #         else:
# #              print("Чего ждем?")
# #         if p.hp < 0:
# #             print("Вы проиграли")
# #         if e.hp < 0:
# #             print("Вы победили")
# #
# #         print("******************")
# #
# # # Вызов меню.
# # menu(p)
#
#
# import random
#
# class Hero:
#     def __init__(self, name, health, attack):
#         self.name = name
#         self.health = health
#         self.attack = attack
#
#     def attack_boss(self, boss):
#         damage = self.attack
#         boss.take_damage(damage)
#
# class Warrior(Hero):
#     def attack_boss(self, boss):
#         damage = self.attack * random.uniform(1, 2)
#         boss.take_damage(damage)
#
# class Berserk(Hero):
#     def attack_boss(self, boss):
#         blocked_damage = boss.attack * random.uniform(0, 1)
#         self.health -= blocked_damage
#         damage = self.attack + blocked_damage
#         boss.take_damage(damage)
#
# class Magic(Hero):
#     def __init__(self, name, health, attack, boost_factor):
#         super().__init__(name, health, attack)
#         self.boost_factor = boost_factor
#
#     def boost_attack(self, heroes):
#         for hero in heroes:
#             hero.attack += self.boost_factor
#
# class Thor(Hero):
#     def attack_boss(self, boss):
#         stun_chance = random.uniform(0, 1)
#         if stun_chance > 0.5:
#             boss.stunned = True
#         else:
#             damage = self.attack
#             boss.take_damage(damage)
#
# class Golem(Hero):
#     def defend(self, boss, heroes):
#         for hero in heroes:
#             if self.health > 0:
#                 damage = boss.attack / 5
#                 self.health -= damage
#                 hero.health += damage
#
# class Witcher(Hero):
#     def revive(self, heroes):
#         revive_chance = random.uniform(0, 1)
#         if revive_chance > 0.5:
#             for hero in heroes:
#                 if hero.health <= 0:
#                     hero.health = self.health
#                     self.health = 0
#                     break
#
#
# class Golem(Hero):
#     def __init__(self, name, health, damage):
#         # Golem имеет увеличенную жизнь
#         super().__init__(name, health * 2, damage // 2)
#         self.__heal_points = 5
#
#     def apply_super_power(self, boss, heroes):
#         # Golem может исцелить своих товарищей на небольшое количество здоровья
#         for hero in heroes:
#             if hero.health > 0 and hero != self:
#                 hero.health += self.__heal_points
#         print(f'{self.name} heals all teammates for {self.__heal_points} health points')
#
# def start_game():
#     boss = Boss('Pudge', 800, 50)
#     warrior = Warrior('Ahiles', 280, 10)
#     doc = Medic('Invoker', 250, 5, 15)
#     magic = Magic('Lolita', 290, 15)
#     berserk = Berserk('Thor', 270, 10)
#     assistant = Medic('Rafael', 300, 5, 5)
#     golem = Golem('Hulk', 500, 5)
#     heroes_list = [warrior, doc, magic, berserk, assistant, golem]
#
#     print_statistics(boss, heroes_list)
#     while not is_game_finished(boss, heroes_list):
#         play_round(boss, heroes_list)
