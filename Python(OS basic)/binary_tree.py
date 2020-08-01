def create(value):
    tr = {'value': value, 'left': None, 'right': None}     # создание нового элемента дерева
    return tr


def is_number(str):    # проверяем, что введено число 
    try:
        int(str)
        return True
    except ValueError:
        return False


def add(tree, ch):
    ch = int(ch)
    if tree == None:
        tree = create(ch)
    else:
        if ch > tree['value']:           # если число больше
            if tree['right'] == None:     # если справа нет числа
                tree['right'] = create(ch)
            else:
                add(tree['right'], ch)
        if ch < tree['value']:           # если число меньше
            if tree['left'] == None:      # если слева нет числа
                tree['left'] = create(ch)
            else:
                add(tree['left'], ch)        
    return tree


def is_false():
    return False


def is_true():
    return True


def find(tree, ch):
    ch = int(ch)
    if tree == None:           # вся ветка пройдена и число не обнаружено
        return is_false()
    elif tree['value'] == ch:
        return is_true()
    elif ch > tree['value']:  # если число больше, то выбираем правого предка
        return find(tree['right'], ch)
    elif ch < tree['value']:   # если число меньше, то выбираем левого предка
        return find(tree['left'], ch)


def min_find(tree):
    if tree['left'] != None:
        return min_find(tree['left'])
    else:
        return tree


def remove(tree, ch):
    ch = int(ch)
    if tree is None:  # это лист без предков
        return None
    if ch > tree['value']:  # если число больше, то выбираем правого предка
        tree['right'] = remove(tree['right'], ch)
        return tree
    elif ch < tree['value']:   # если число меньше, то выбираем левого предка
        tree['left'] = remove(tree['left'], ch)
        return tree    
    if ch == tree['value']:  # если число найдено
        if tree['left'] is None:   # предок только справа
            return tree['right']
        elif tree['right'] is None:   # предок только слева
            return tree['left']
        else:    # есть оба предка
            minimum = min_find(tree['right'])
            tree['value'] = minimum['value']
            tree['right'] = remove(tree['right'], minimum['value'])
            return tree
        
        
if __name__ == "__main__":
    tree = None
    while True:
        data = input("Введите команду(add, del, find) и число через пробел ").split()
        if len(data) == 1:
            if data[0] == 'end':
                break
            else:
                print('Не корректный ввод. Попробуйте ещё раз')
                continue
        else:
            if (data[0] == 'add' or data[0]=='find' or data[0]=='del') and is_number(data[1])== True and len(data)==2: # проверяем, что ввёл пользователь
                if data[0] == 'add':
                    if find(tree, data[1]) == False:  # проверяем, что такого числа еще нет в дереве
                        tree = add(tree, data[1])
                        print('Число ' + data[1] + ' добавлено.')
                    else:
                        print('Число ' + data[1] + ' уже есть в дереве. Попробуйте ввести другое.')
                if data[0] == 'find':
                    if find(tree, data[1]) == True:
                        print('Есть число ' + data[1])
                    else:
                        print('Нет числа ' + data[1])
                if data[0] == 'del':
                    if find(tree, data[1]) == True:
                        print('Было \n', tree)
                        tree = remove(tree, data[1])
                        print('Стало \n', tree)
                        print('Число ' + data[1] + ' удалено.')                    
                    else:
                        print('Невозможно удалить число ' + data[1] + ', т.к. его нет в дереве.')
            else:
                print('Не корректный ввод. Попробуйте ещё раз')
                continue

    print('Полученное бинарное дерево \n', tree)
