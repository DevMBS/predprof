# открытие файла
fin = [x.split('*') for x in list(open('space.txt', encoding='utf-8'))]


def gen_pass(name, code):
    """

    :param name: Название планеты (str)
    :param code: Код корабля(str)
    :return: Пароль (str)
    """

    password = f'{name[-3]}{name[-2]}{name[-1]}{code[2]}{code[1]}{name[2]}{name[1]}{name[0]}'.upper()
    return password


# составляем пароли и записываем
for i in range(1, len(fin)):
    passw = gen_pass(fin[i][1], fin[i][0].split('-')[0])
    if '\n' in fin[i][3]: fin[i][3] = fin[i][3][:-1]
    fin[i].append(f'{passw}\n')

fin[0][3] = fin[0][3][:-1]
fin[0].append('password\n')

# записываем в новый файл
fout = open('space_uniq_password.txt', 'w', encoding='utf-8')
for k in fin:
    fout.write('*'.join(k))
fout.close()
