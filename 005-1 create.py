#Написать программу для создания папки с определенным именем в текущей рабочей директории

import sys
import os

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input('Задайте имя папки ')

    try:
        abs_dir = os.path.abspath('.')
        os.mkdir(os.path.join(abs_dir, filename))
        new_dir = os.path.join(abs_dir, filename)
        print('Новая папка создана. Путь ', new_dir)
    except OSError:
        print("Такая папка в этой директории уже есть.")

if __name__ == '__main__':
    main()