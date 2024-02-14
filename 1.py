# открытие файла
fin = [x.split('*') for x in list(open('space.txt', encoding='utf-8'))]
# проверяем каждый элемент
for i in range(1, len(fin)):
    # есть потерянные данные
    if fin[i][2] == '0 0':
        # восстанавливаем по формуле
        n = int(fin[i][0].split('-')[1][0])
        m = int(fin[i][0].split('-')[1][1])
        t = len(fin[i][1])
        x = 0
        y = 0
        xd = int(fin[i][3].split(' ')[0])
        yd = int(fin[i][3].split(' ')[1])
        if n > 5:
            x = n + xd
        else:
            x = -(n+xd)*4+t
        if m > 3:
            y = m+t+yd
        else:
            y = -(n+yd)*m
        fin[i][2] = f'{x} {y}'
# записываем в новый файл
fout = open('space_new.txt', 'w', encoding='utf-8')
for k in fin:
    fout.write('*'.join(k))
fout.close()

# выводим корабли
for j in range(1, len(fin)):
    if fin[j][0][3] == 'V':
        print(f'{fin[j][0]} - {fin[j][2]}')