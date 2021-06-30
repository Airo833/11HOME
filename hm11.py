from random import randint

class Cards:
    def __init__(self, name, count_name):
        self.name = name
        self.count_name = count_name
        self.result = []
        self.finish = 0
        self.count = 0
    def creat_card(self):
        for x in range(3):
            n = 0
            a1 = randint(0, 2)
            a2 = randint(3, 4)
            a3 = randint(5, 6)
            a4 = randint(7, 8)
            for i in range(10):
                if i < 9 and i != a1 and i != a2 and i != a3 and i != a4:
                    self.result.append("%2.f" % randint(n, n + 18))
                    n += 18
                elif i == a1 or i == a2 or i == a3 or i == a4:
                    self.result.append('__')
        return self.result
    def save_card(self):
        return self.result
    def change_card(self, number2):
        n=0
        for k, el in enumerate(self.result):
            if el == number2:
                self.result[k] = '><'
                print('\n', 'Такое число есть')
                n += 1
                self.count += 1
        if n == 0:
            print('\n', 'Ответ неверный')
            self.finish += 1
        return self.result
    def change_card2(self, number2):
        n1 = 0
        for k, el in enumerate(self.result):
            if el == number2:
                n1 += 1
                print('\n', 'Ответ неверный')
                self.finish += 1
        if n1 == 0:
            print('\n', 'Действительно, такого числа в карточке нет')
    def check_comp_card(self, number2):
        for k, el in enumerate(self.result):
            if el == number2:
                self.result[k] = '><'
                print('\n', 'Такое число есть карточке компьютера')
                self.count += 1
        return self.result
    def print_card(self):
        result2 = [self.result[0:9], self.result[9:18], self.result[18:27]]
        print(f'---{self.name}----')
        print('\n'.join(' '.join(str(j) for j in line) for line in result2))
        print('--------------------------', '\n')
    def save_finish(self):
        return self.finish
    def save_count(self):
        print(f'{self.count_name} {self.count}')
        return self.count

class Number:
    def __init__(self, max):
        self.max = max
        self.memory_nym = []
    def my_num(self):
        nn = 0
        while nn == 0:
            self.number1 = "%2.f" % randint(0, self.max)
            if self.number1 in self.memory_nym:
                x = 1
            else:
                nn = 1
                print('Выпал бочонок с числом: ', self.number1)
                print('Числа, которые уже выпадали:', self.memory_nym)
                print(f'Ранее выпадало {len(self.memory_nym)} знач. Ещё осталось {self.max - len(self.memory_nym)}')
                self.memory_nym.append(self.number1)
        return self.number1

    def save_num(self):
        return str(self.number1)
class Game(Cards, Number):
    def __init__(self):
        return
    def question(self):
        self.answer = input('Зачеркиваем выпавшее число в карточке? д/н ')
        return self.answer
    def save_answer(self):
        return self.answer



my_card = Cards('---Ваша карточка---', 'Ваш счёт:')
comp_card = Cards('-Карточка компьютера-', 'Счёт компьютера:')

num1 = Number(90)

game1 = Game()


my_card.creat_card()
comp_card.creat_card()

my_card.print_card()
comp_card.print_card()

def find():
    num1.my_num()
    game1.question()
    if game1.save_answer() == 'д':
        my_card.change_card(num1.save_num())
    else:
        my_card.change_card2(num1.save_num())
    my_card.print_card()
    comp_card.check_comp_card(num1.save_num())
    comp_card.print_card()

while 1:
    find()
    if my_card.save_count() == 15:
        print('Вы победили')
        break
    elif my_card.save_finish() != 0:
        break
    elif comp_card.save_count() == 15:
        print('Победил компьютер')
        break
print('GAME OVER')


while len(barrels) > 0:
    print('\n' * 100)
    if check_nums_end(player) == 0:
        print('Поздравляем. Вы выиграли.')
    current_bar = barrels.pop(random.randint(0, (len(barrels)) - 1))
    comp = strike(current_bar, comp)
    if check_nums_end(comp) == 1:
        print('Новый бочонок: {} (осталось {})\n'.format(current_bar, len(barrels)))
    else:
        print('Последний бочонок: {}. Компьютер выиграл'.format(current_bar))
        break

    print('------ Ваша карточка -----')
    for i in player:
        for some in i:
            print('{:<3}'.format(some), end='')
        print()
    print('-' * 26, '\n')

    print('-- Карточка компьютера ---')
    for i in comp:
        for some in i:
            print('{:<3}'.format(some), end='')
        print()
    print('-' * 26)
    if check_nums_end(player) == 0:
        break
    choice = input('Зачеркнуть цифру? (y/n)')
    last_player = copy.deepcopy(player)
    if choice == 'y':
        player = strike(current_bar, player)
        if last_player == player:
            print('Вы проиграли. В вашей карточке нет номера {}'.format(current_bar))
            break
        else:
            print('\n' * 100)
    elif choice == 'n':
        player = strike(current_bar, player)
        if last_player != player:
            print('Вы проиграли. В вашей карточке есть номер {}'.format(current_bar))
            break
        else:
            print('\n' * 100)
    else:
        print('Вы проиграли. Вы ввели {}, вместо y/n'.format(choice))
        break