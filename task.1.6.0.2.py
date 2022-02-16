
class Character:  # Персонаж
    '''     Некий игровой персонаж
    '''
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name  # Имя
        self.power = power     # Сила
        self.energy = energy  # Энергия
        self.hands = hands     # Число конечностей
        self.backpack = []    # Рюкзак
    
    def eat(self, food):      # Покушать.
        print('  Отработал метод: eat')
        if self.energy < 100:
            self.energy += food
        else:
            print(' Not hanqry')
    
    def do_exercise(self, hours):  # Потренероваться.
        print('  Отработал метод: do_exercise')
        if self.energy > 0:
            self.energy -= hours * 3
            self.power += hours * 2
        else:
            print(' Too tired')
    
    def chenge_alias(self, meaning_alias):  # Поменять псевдоним.
        print('  Отработал метод: chenge_alias')
        print(self)
        self.alias = meaning_alias
    
    def beat_up(self,foe):   # Сражение (бой)
    	if not isinstance(foe, Character):
    		return
    	if 'status' not in self.__dict__:
    		self.status = ''
    	if 'status' not in foe.__dict__:
    		foe.status = ''
    	if foe.power < self.power:
    		foe.status = 'defeated'
    		self.status = 'winner'
    		print(f' {self.name}: "Victory!"')
    	else:
    		print(f' {self.name}: "Retreat!"')
    	print(f" {self.name}.status = '{self.status}'\
    		\n {foe.name}.status = '{foe.status}'")


peter = Character('Peter Parker', 80)
bruce = Character('Bruce Wayne', 85)
print(peter.__dict__)
print(bruce.__dict__)
peter.backpack.append('web-shooters')
print()
print(peter.__dict__)
print(bruce.__dict__)
print('\n1.')
peter.beat_up(bruce)
print()
peter.do_exercise(3)
print(peter.__dict__)
print(bruce.__dict__)
print('\n2.')
peter.beat_up(bruce)
