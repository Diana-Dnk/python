class Character:
    def __init__(self,name,hp,damage):
        self.name=name
        self.__hp=hp
        self.damage=damage

    def info(self):
        print(f"Имя:{self.name}|HP:{self.__hp}|Урон:{self.damage}")

    def take_damage(self,dmg):
        if dmg<0:
            return
        self.__hp-=dmg
        if self.__hp<0:
            self.__hp=0

    def heal(self,amount):
        if amount<0:
            return
        self.__hp+=amount
        if self.__hp>100:
            self.__hp=100

    def attack(self,target):
        print(self.name,"бьет",target.name,"на", self.damage)
        target.take_damage(self.damage)

    def is_alive(self):
        return self.__hp>0

class Warrior(Character):
    pass

w=Warrior("Тралл",100,15)
w.info()


class Warrior(Character):
    def __init__(self,name):
        super().__init__(name,150,20)

    def attack(self, target):
        print(self.name,"рубит мечом")
        target.take_damage(self.damage)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80, 30)
        self.mana=100

    def cast_spell(self,target):
        if self.mana<20:
            print(self.name,"не хватает маны")
            return
        self.mana-=20
        print(self.name,"кастует фаербол")
        target.take_damage(self.damage+10)

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 120, 18)

    def heal_ally(self,target):
        if target==self:
            print("Себя лечить нельзя")
            return
        if not target.is_alive():
            print("Нельзя лечить мёртвого")
            return
        print(self.name, "лечит", target.name)
        target.heal(20)

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, 90, 25)
        self.energy = 100

    def attack(self, target):
        print(self.name, "атакует")
        target.take_damage(self.damage)

    def backstab(self, target):
        if self.energy < 30:
            print(self.name, "не хватает энергии для удара")
            return

        self.energy -= 30
        print(self.name, "атака")
        target.take_damage(self.damage * 2)

    

war=Warrior("Тралл")
mage=Mage("Джайна")
paladin=Paladin("Паладин")
rogue=Rogue("Валира")


# бой 
while war.is_alive() and  mage.is_alive() and paladin.is_alive() and rogue.is_alive():
    
    war.attack(mage)
    mage.attack(war)
    mage.attack(paladin)
    rogue.backstab(mage)
    rogue.attack(paladin)
    paladin.heal_ally(paladin)
    mage.info() 