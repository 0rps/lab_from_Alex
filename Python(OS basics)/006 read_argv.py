# Написать функцию в программе, которая имеет следующий формат вызова
# python read_argv.py filename1 filename2 --key1 some_value1 --key2 some_value2
# Все аргументы опциональные, кроме filename1, т.е. я могу вызвать скрипт как
# python read_argv filename1

import sys

def read_argv(number_of_required_positional_args):
    args = []
    kwargs = {}
    i = 1
    while i < len(sys.argv):
        if '--' not in sys.argv[i]:
            args.append(sys.argv[i])
        else:
            if i != len(sys.argv)-1 and '--' not in sys.argv[sys.argv.index(sys.argv[i]) + 1]:
                key = sys.argv[i][2:]
                kwargs[key] = sys.argv[sys.argv.index(sys.argv[i]) + 1]
                i += 1
            else:
                key = sys.argv[i][2:]
                kwargs[key] = None
        i += 1

    if len(args) < number_of_required_positional_args:
        raise Exception

    return args, kwargs


def main(filename1, *args, **kwargs):
    print('filename1: ', filename1)
    if len(args) > 0:
        for i in args:
            print(i)

    if 'key1' in kwargs:
        print('key1 in kwargs')

    if 'key2' in kwargs:
        print('key2 in kwargs')


if __name__ == '__main__':
    data = read_argv(1)
    main(*data[0], **data[1])
