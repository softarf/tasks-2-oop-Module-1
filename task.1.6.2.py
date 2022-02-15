
class Character:  # Персонаж
    ''' Некий игровой персонаж
    '''
    
    def __init__(self, name, power, energy=100, hands=2):  # Имя
        self.name = name
        self.power = power     # Сила
        self.energy = energy  # Энергия
        self.hands = hands     # Число конечностей
        self.backpack = []    # Рюкзак
    
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


peter = Character('Peter Parker', 80)
bruce = Character('Bruce Wayne', 85)
print(peter.__dict__)
print(bruce.__dict__)
peter.backpack.append('web-shooters')
print()
print(peter.__dict__)
print(bruce.__dict__)
