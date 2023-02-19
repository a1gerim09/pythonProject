class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f'Computer with CPU: {self.__cpu} and Memory: {self.__memory}'

    def __eq__(self, other):
        if isinstance(other, Computer):
            return self.memory == other.memory
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Computer):
            return self.memory > other.memory
        return False

    def __lt__(self, other):
        if isinstance(other, Computer):
            return self.memory < other.memory
        return False

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {sim_card_number} с сим-карты- {call_to_number} - Beeline')

    def __str__(self):
        return f'Phone with sim cards list: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        return f'Routing to location {location}'

    def __str__(self):
        return f'SmartPhone with CPU: {self.cpu}, Memory: {self.memory} and Sim Cards List: {self.sim_cards_list}'


computer = Computer(2, 4)
phone = Phone([1, 2, 3])
smartphone1 = SmartPhone(4, 8, [1, 2, 3])
smartphone2 = SmartPhone(6, 16, [4, 5, 6])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print(f"Is computer's memory the same is smartphone's memory: {computer.memory == smartphone1.memory}")
print(f"Is computer's cpu not equal with smartphone's cpu: {computer.cpu != smartphone2.cpu}")
print(f"Is smartphone's memory bigger than computer's cpu: {smartphone2.memory > computer.cpu}")
print(f"Is computer's memory less than smartphone's memory: {computer.memory < smartphone1.memory}")
print(f"Is smartphone's cpu equal or more than smartphone's cpu: {smartphone1.cpu >= smartphone2.cpu}")
print(f"Is computer's memory equal or less than smartphone's memory: {computer.memory <= smartphone1.memory}")

computer.make_computations()
print(computer)

phone.call(2, 2512)
print(phone)

smartphone1.use_gps('Bishkek')
print(smartphone1)
