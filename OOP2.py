# class Product ():
#     def __init__(self,title,price):
#         self.title=title 
#         self.price=price

#     def info(self):
#         print("Название:",self.title, "Цена",self.price)

# laptop = Product("Asus",600)
# iphone=Product("Iphone 17",700)
# laptop.info()
# iphone.info()


# class Character:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage

#     def info(self):
#         print(f"Name:{self.name}|HP:{self.hp}|Damage:{self.damage}")

#     def attack(self,target):
#         print(self.name,"бьет",target.name,"на", self.damage)
#         target.hp-=self.damage

# orc=Character("Орк",100,15)
# human=Character("Человек",80,10)

# orc.info()
# human.info()
# orc.attack(human)
# human.info()



# class Character:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.__hp=hp
#         self.damage=damage

#     def info(self):
#         print(f"Имя:{self.name}|HP:{self.__hp}|Урон:{self.damage}")

#     def take_damage(self,dmg):
#         if dmg<0:
#             return
#         self.__hp-=dmg
#         if self.__hp<0:
#             self.__hp=0

#     def heal(self,amount):
#         if amount<0:
#             return
#         self.__hp+=amount
#         if self.__hp>100:
#             self.__hp=100

#     def attack(self,target):
#         print(self.name,"бьет",target.name,"на", self.damage)
#         target.take_damage(self.damage)

# orc=Character("Орк",100,15)
# human=Character("Человек",80,10)

# orc.info()
# human.info()
# orc.attack(human)
# human.info()
# human.heal(5)
# human.info()


# class Character:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.__hp=hp
#         self.damage=damage

#     def info(self):
#         print(f"Имя:{self.name}|HP:{self.__hp}|Урон:{self.damage}")

#     def take_damage(self,dmg):
#         if dmg<0:
#             return
#         self.__hp-=dmg
#         if self.__hp<0:
#             self.__hp=0

#     def heal(self,amount):
#         if amount<0:
#             return
#         self.__hp+=amount
#         if self.__hp>100:
#             self.__hp=100

#     def attack(self,target):
#         print(self.name,"бьет",target.name,"на", self.damage)
#         target.take_damage(self.damage)

#     def is_alive(self):
#         return self.__hp>0

# class Warrior(Character):
#     pass

# w=Warrior("Тралл",100,15)
# w.info()


# class Warrior(Character):
#     def __init__(self,name):
#         super().__init__(name,150,20)

#     def attack(self, target):
#         print(self.name,"рубит мечом")
#         target.take_damage(self.damage)


# class Mage(Character):
#     def __init__(self, name):
#         super().__init__(name, 80, 30)
#         self.mana=100

#     def cast_spell(self,target):
#         if self.mana<20:
#             print(self.name,"не хватает маны")
#             return
#         self.mana-=20
#         print(self.name,"кастует фаербол")
#         target.take_damage(self.damage+10)


# war=Warrior("Тралл")
# mage=Mage("Джайна")
# # war.attack(mage)
# # mage.info()
# # mage.cast_spell(war)
# # war.info()

# # бой 
# while war.is_alive() and  mage.is_alive():
#     war.attack(mage)
#     mage.info()


# Создать класс Paladin:
# Требования:
# наследуется от Character
# HP = 120
# Damage = 18
# метод heal_ally(target):
# лечит другого персонажа
# нельзя лечить врага
# нельзя лечить мёртвого
# Подсказка:
# class Paladin(Character):
#     pass
# Ты ходишь и смотришь:
# используют ли super()
# используют ли heal()
# не лезут ли в __hp

# class Character:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.__hp=hp
#         self.damage=damage

#     def info(self):
#         print(f"Имя:{self.name}|HP:{self.__hp}|Урон:{self.damage}")

#     def take_damage(self,dmg):
#         if dmg<0:
#             return
#         self.__hp-=dmg
#         if self.__hp<0:
#             self.__hp=0

#     def heal(self,amount):
#         if amount<0:
#             return
#         self.__hp+=amount
#         if self.__hp>100:
#             self.__hp=100

#     def attack(self,target):
#         print(self.name,"бьет",target.name,"на", self.damage)
#         target.take_damage(self.damage)

#     def is_alive(self):
#         return self.__hp>0

# class Warrior(Character):
#     pass

# w=Warrior("Тралл",100,15)
# w.info()


# class Warrior(Character):
#     def __init__(self,name):
#         super().__init__(name,150,20)

#     def attack(self, target):
#         print(self.name,"рубит мечом")
#         target.take_damage(self.damage)


# class Mage(Character):
#     def __init__(self, name):
#         super().__init__(name, 80, 30)
#         self.mana=100

#     def cast_spell(self,target):
#         if self.mana<20:
#             print(self.name,"не хватает маны")
#             return
#         self.mana-=20
#         print(self.name,"кастует фаербол")
#         target.take_damage(self.damage+10)

# class Paladin(Character):
#     def __init__(self, name):
#         super().__init__(name, 120, 18)

#     def heal_ally(self,target):
#         if target==self:
#             print("Себя лечить нельзя")
#             return
#         if not target.is_alive():
#             print("Нельзя лечить мёртвого")
#             return
#         print(self.name, "лечит", target.name)
#         target.heal(20)




# war=Warrior("Тралл")
# mage=Mage("Джайна")
# paladin=Paladin("Паладин")

# # бой 
# while war.is_alive() and  mage.is_alive() and paladin.is_alive():
    
#     war.attack(mage)
#     mage.attack(war)
#     mage.attack(paladin)
#     paladin.heal_ally(paladin)
#     war.info() 
# 
# 
#     