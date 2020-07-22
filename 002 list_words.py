import sys

def print_top(sort_words):        # вывод топа на консоль
    for i in sort_words:
        print(i[0], i[1])

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print('Введите имя файла ')
        filename = input()

    try:
        with open(filename) as file:
            words = []
            for line in file:
                data = line.lower().strip('\n\r\t')  # все слова делаем одного регистра и убираем символы переноса

                delimiters = ' .,:;?!\"'
                word = ''
                i = 0
                while i < len(data):      # проверяем все символы
                    if data[i] == '\'':    # проверяем, чтоб это не был апостроф
                        words.append(word)
                        word = ''
                        i += 1
                        while data[i] not in delimiters:             # если это был апостроф, то записываем слово в список и ищем первый пробел после апострофа
                            i += 1
                    elif data[i] not in delimiters:      # проверяем, чтоб этого символа не было в нашем списке разделителей
                        word += data[i]
                        i += 1
                    else:
                        if len(word) != 0:            # если символ в списке разделителей, и строка со словом что-то в себе содержит, то добавляем это слово в список
                            words.append(word)
                            word = ''
                        i += 1

        dict_of_words = {}
        sort_words = []


        for i in words:
            dict_of_words[i] = words.count(i)  # записываем слово и количество повторений в словарь

        for i in sorted(dict_of_words.items(), key=lambda x: (-x[1], x[0])):  # сортировка по количеству, а потом в лексикографическом порядке
            sort_words.append(tuple((i[0], i[1])))  # получившиеся данные записываем в виде кортежей в список


        if '--count' in sys.argv:
            count = int(sys.argv[sys.argv.index('--count')+1])
            if len(sort_words) < count:       # если список меньше указанного количества, то выводим весь список
                count = len(sort_words)
        else:
             if len(sort_words) < 3:
                 count = len(sort_words)       # если список меньше 3х элементов, то выводим весь список
             else:
                 count = 3                  # по умолчанию будем выводить топ-3, если не указано иное

        if '--only-frequent' in sys.argv and '--only-rare' in sys.argv:        # если указано вывести 2 топа
            print_top(sort_words[:count])
            print('###')
            print_top(sort_words[len(sort_words)-count:])
        elif '--only-frequent' in sys.argv:           # если только топ частотных
            print_top(sort_words[:count])
        elif '--only-rare' in sys.argv:               # если только топ редких слов
            print_top(sort_words[len(sort_words)-count:])
        else:
            print_top(sort_words[:count])     # если не указано ничего, то будет топ-3
            print('###')
            print_top(sort_words[len(sort_words)-count:])


    except FileNotFoundError:
        print('Файл ' + str(filename) + ' не найден.')

if __name__ == '__main__':
    main()