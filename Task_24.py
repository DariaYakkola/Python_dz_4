# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на
# круглой грядке, причём кусты высажены только по окружности. Таким
# образом, у каждого куста есть ровно два соседних. Всего на грядке
# растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко
# времени сбора на них выросло различное число ягод — на i-ом кусте выросло
# ai ягод. В этом фермерском хозяйстве внедрена система автоматического
# сбора черники. Эта система состоит из управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с
# двух соседних с ним. Напишите программу для нахождения максимального числа
# ягод, которое может собрать за один заход собирающий модуль, находясь перед
# некоторым кустом заданной во входном файле грядки.
from random import randint
number_bushes = int(input('Введите количество кусов: '))
bush = [randint(10, 100) for _ in range(number_bushes)]
print(f'Количство ягод на кустах - {bush}')
max_sum = 0
sdvig = 2
for i in range(number_bushes - 2):
    sum = bush[i] + bush[i + 1] + bush[i + 2]
    if sum > max_sum:
        max_sum = sum
for _ in range(sdvig):
    bush.insert(0, bush.pop())
    for j in range(3):
        sum = bush[j] + bush[j + 1] + bush[j + 2]
        if sum > max_sum:
            max_sum = sum
print(f'Максимальная сумма ягод, которую можно собрать - {max_sum}')
