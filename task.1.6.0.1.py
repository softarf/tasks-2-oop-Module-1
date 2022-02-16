
class Character:  # Персонаж
    ''' Некий игровой персонаж
    '''
    name = ''     # Имя
    power = 0     # Сила
    energy = 100  # Энергия
    hands =2     # Число конечностей
    backpack = []

    def eat(self, food):      # Покушать
        print('  Отработал метод: eat')
        if self.energy < 100:
            self.energy += food
        else:
            print(' Not hanqry')

    def do_exercise(self, hours):  # Потренероваться
        print('  Отработал метод: do_exercise')
        if self.energy > 0:
            self.energy -= hours * 3
            self.power += hours * 2
        else:
            print(' Too tired')

    def chenge_alias(self, new_alias):  # Смена псевдонима
        print('  Отработал метод: chenge_alias')
        print(self)
        self.alias = new_alias


print(Character.__dict__)
print(dir(Character))

peter = Character()
print('\n    peter: ', type(peter))
print(peter.name)
print(peter.power)
print(peter.energy)
print(peter.hands)
print(peter.__dict__)
print()
peter.name = 'Peter Parker'
peter.power = 70
peter.alias = 'Spyder-Man'
print(peter.name)
print(peter.power)
print(peter.energy)
print(peter.hands)
print(peter.alias)  # Псевдоним (Кличка, Nick)
print(peter.__dict__)

bruce = Character()
print('\n    bruce: ', type(bruce))
print(bruce.name)
print(bruce.power)
print(bruce.energy)
print(bruce.hands)
print(bruce.__dict__)
print()
bruce.name = 'Bruce Wayne'
bruce.power = 85
bruce.chenge_alias('Batman')
print(bruce.name)
print(bruce.power)
print(bruce.energy)
print(bruce.hands)
print(bruce.alias)  # Псевдоним (Кличка, Nick)
print(bruce.__dict__)
peter.backpack.append('web-shooters')
print(peter.backpack)
print(bruce.backpack)

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
