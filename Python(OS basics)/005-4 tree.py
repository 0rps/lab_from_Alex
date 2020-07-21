# Написать программу, которая будет выводить файлы и папки в виде древовидной структуры.
# Должна поддерживать параметр depth, который задает максимальную глубину, в которую можно зайти программа.
# ФУНКЦИЯ ПЕЧАТИ ДОЛЖНА БЫТЬ РЕАЛИЗОВАНА РЕКУРСИВНО
#
# Пример использования программы. C:\files\ - стартовая папка, --depth 1, глубина вывода = 1
# >> python tree.py C:\files\ --depth 1
#
# |-file1.txt
# |-file2.txt
# |-folder1
# |-folder2
#
#
# >> python tree.py C:\files --depth 2
#
# |-file1.txt
# |-file2.txt
# |-folder1
#   |-file12.txt
#   |-file13.txt
# |-folder2
#   |-file21.txt
#   |-file22.txt


import sys
import os
from pprint import pprint


def print_result(tree, depth_now, depth_data):
    if depth_now == 0:
        return
    else:
        delta_depth = depth_data - depth_now   # дельта, чтоб вывести отступы
        for key, value in tree.items():
            print(' '*delta_depth, '|-', key)
            if value != None:
                print_result(value, depth_now-1, depth_data)


def create_new_tree(file_in_dir):
    new_tree = {}
    if isinstance(file_in_dir, list):      # если папка содержит внутрии один файл, то его передает как тип str
        for i in file_in_dir:
            new_tree[i] = None
    else:
        new_tree = dict([[file_in_dir, None]])
    return new_tree


def create_tree(files, way, data_tree):
    for i in files:
        filepath = os.path.join(way, i)
        if data_tree == None:
            data_tree = create_new_tree(i)
        if os.path.isdir(filepath):             # если это директория
            data_tree[i] = create_new_tree(os.listdir(filepath))            # создаем словарь с именем директории и ее содержимым
            create_tree(os.listdir(filepath), filepath, data_tree[i])       # проверяем чемя является содержимое директории
    return data_tree


def main():
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[-1]):
            way_data = sys.argv[-1]
        else:
            print('Нет такой папки.')
            while True:
                way_data = input('С какой папки начать поиск? ')
                if os.path.isdir(way_data) is False:
                    print('Указанный путь не является директорией.')
                    continue
                break
    else:
        while True:
            way_data = input('С какой папки начать поиск? ')
            if os.path.isdir(way_data) is False:
                print('Указанный путь не является директорией.')
                continue
            break

    tree_file = None
    res = create_tree(os.listdir(way_data), way_data, tree_file)  # в функцию отправляем содержимое папки, путь к папке, пустой словарь для записи

    if '--depth' in sys.argv:
        depth = int(sys.argv[sys.argv.index('--depth') + 1])
    else:
        while True:
            try:
                depth = int(input('Введите глубину '))
                if depth < 0:
                    print('Введите число больше 0.')
                    continue
            except:
                print('Не верный тип данных.')
                continue
            break

    print('Дерево ->')
    pprint(res)
    print_result(res, depth, depth)

if __name__ == '__main__':
    main()