# Написать программу, которая принимает на вход имя файла, который нужно прочитать и распечатывает содержимое этого файла.
# python print_file %filename% [--count %number_of_lines%] [--help]
# Данная программа должна уметь принимать на вход опциональный параметр с количеством строчек,
# которые нужно распечатать. Параметр должен называться --count. Также данная программа должна поддерживать параметр --help,
# считав которой программа должна выдать справочную информацию о том, как работает данный файл и список возможных параметров,
# которые она принимает. За основу для  --help можно взять раздел Usage по данный ссылке
# https://github.com/suncat2000/console-commands/blob/master/README.md

import sys

def main():
    if '--help' in sys.argv:
        print('''This program prints lines from a file.
You need to set data:
file      file to print
--count   prints lines from a file
number    number of lines''')
    else:
        if len(sys.argv) > 1:
            filename = sys.argv[1]
        else:
            filename = input('Задайте имя файла ')

        try:
            with open(filename) as file:
                data = file.read().splitlines()

            if '--count' in sys.argv:
                number = int(sys.argv[sys.argv.index('--count')+1])
            if '--count' not in sys.argv or number < 0:
                while True:
                    try:
                        number = int(input('Введите положительное количество строк '))
                        if number < 0:
                            print('Введите число больше 0.')
                            continue
                    except:
                        print('Не верный тип данных.')
                        continue
                    break

            if len(data) < number:
                number = len(data)
            for i in range(number):
                print(data[i])

        except:
            print('Файл не найден.')


if __name__ == '__main__':
    main()