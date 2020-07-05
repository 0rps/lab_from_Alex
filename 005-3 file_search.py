# Написать программу, которая будет рекурсивно искать все файлы (не директории),
# в имени которых встречается поисковое слово, начиная в определенной директории.

# python file_search-1.py txt C:\users\  # поиск всех файлов, в имени которых есть "txt"
# # и поиск начинается с директории c:\files
#
# # пример вывода
# >> C:\files\subfolder\1.txt
# >> C:\files\subfolder\2.txt
# >> C:\files\atxtament.html

import sys
import os



def search(files, way, word, data):      #
    for i in files:
        filepath = os.path.join(way, i)         # путь до файла
        if os.path.isdir(filepath):             # выясняем папка это или файл
            search(os.listdir(filepath), filepath, word, data)    # если папка, то всё её содержимое отправляем в функцию
        elif os.path.isfile(filepath):                 # если файл, то проверяем наличие по поисковому слову
            if i.find(word) != -1:
                data.append(os.path.join(way, i))                      # мы нашли подходящие файлы



def main():
    if len(sys.argv) == 3:
        if os.path.isdir(sys.argv[-1]):
            way_data = sys.argv[-1]
            word_search = sys.argv[1]
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
            word_search = input('Введите слово для поиска')
            if os.path.isdir(way_data) is False:
                print('Указанный путь не является директорией.')
                continue
            break

    res = []
    search(os.listdir(way_data), way_data, word_search, res)  # в функцию отправляем содержимое папки, путь к папке, поисковое слово

    if len(res) == 0:      # если список res пуст, значит ничего не найдено
        print('Файлов не найдено.')
    else:
        for i in res:
            print(i)


if __name__ == '__main__':
    main()