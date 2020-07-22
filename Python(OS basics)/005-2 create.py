# Написать программу, которая создает файл по определенному пути и записывает в нее
# некоторое содержимое (в кавычках передаем), путь может быть как относительным, так и абсолютным:
# python create_file.py data.txt "Содержимое файла"

import sys
import os

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input('Задайте имя файла ')

    if not os.path.isabs(filename):
        filename = os.path.join('.', filename)

    if len(sys.argv) == 3:
        text = sys.argv[2]
    else:
        text = input('Что записать в файл? ')

    file = open(filename, 'w')
    file.write(text)
    file.close()

    print('Новй файл создан.')

if __name__ == '__main__':
    main()

