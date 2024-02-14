# открытие файла
fin = [x.split('*') for x in list(open('space.txt', encoding='utf-8'))]

# получаем название
id = input()
while id != 'stop':
    fl = False
    # проходим по каждому кораблю
    for i in range(1, len(fin)):
        if fin[i][0] == id:
            print(
                f'Корабль {fin[i][0]} был отправлен с планеты: {fin[i][1]} и его направление движения было: {fin[i][3]}')
            fl = True
            break
    if not fl:
        print('error.. er.. ror..')
    id = input()
