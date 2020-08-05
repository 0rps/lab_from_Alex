import sys
import datetime

def is_number(str):    # проверяем, что это число
    try:
        int(str)
        return True
    except ValueError:
        return False

def minute(minute):
    if minute % 10 == 0 or 5 <= minute % 10 <= 9 or 11 <= minute % 100 <= 19:
        return ' минут'
    elif 2 <= minute % 10 <= 4:
        return ' минуты'
    elif minute % 10 == 1:
        return ' минута'


def dijkstra(number, start, matrix, finish):
    valid = [False]*number   # это значит, что вершина ещё не рассмотрена
    weight = [float('inf')]*number     # всем вершинам даем значение бесконечность
    weight[start] = 0  # кроме той, с которой начинаем отсчёт
    min_vertex = start
    min_weight = 0
    parent = [None]*number  #родители каждого элемента
    way = []   #путь, который вернём в качестве ответа
    st_time = []  # время до каждой станции
    while min_weight < float('inf'):
        index_min = min_vertex
        valid[index_min] = True
        for j in range(number):
            if weight[index_min]+matrix[index_min][j]<weight[j] and matrix[index_min][j] != -1:
                weight[j] = weight[index_min]+matrix[index_min][j]
                parent[j] = index_min   #записываем родителя под индексом предка
        min_weight = float('inf')
        for i in range(number):
            if not valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                min_vertex = i

    catalog = finish
    while catalog is not None:              #ищем до тех пор, пока не дойдем до корня с родителем None
        if weight[catalog] == float('inf'):
            way = False
            break
        else:
            way.append(catalog)
            if parent[catalog] != None:       #если родитель не None, то находим время в матрице и записываем
                st_time.append(matrix[catalog][parent[catalog]])  # записываем время до станции
            catalog = parent[catalog]

    return weight, way[::-1], st_time[::-1]     # way и st_time разворачиваем в обратном порядке, т.к. записывали с конца


def main():
    adjacency_matrix = []
    station = []
    number_of_stations = None

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print('Введите имя файла ')
        filename = input()


    try:
        with open(filename) as file:
            time_start = datetime.datetime.now()
            data = file.read().splitlines()

            print(data)

            if is_number(data[0]) == True and len(data) == int(data[0])*2+1 and int(data[0]) > 0:  #если на нулевой строке число, и оно не равно 0, и это число равно количеству последующих строк
                number_of_stations = int(data[0])
                for i in range(1, number_of_stations+1):
                    station.append(data[i].lower())

                for i in range(number_of_stations+1, len(data)):  #проверяем содержимое матрицы
                    flag = True
                    string = data[i].split()
                    if len(string) == number_of_stations:
                        for j in range(len(string)):  #проверям, что записано в каждой строке файла
                            if is_number(string[j]) == False:
                                flag = False
                                print('Ошибка. Проверьте данные файла (в строке '  + str(i+1) + ' не все данные числа)')
                                return
                            else:
                                string[j] = int(string[j])
                        if flag == True:
                            adjacency_matrix.append(string)
                    else:
                        print('Ошибка. Проверьте данные файла (не верная длина строки ' + str(i+1) + ')')
                        return
            else:
                print('Ошибка. Проверьте данные файла (количество станций)')
                return

        if len(adjacency_matrix) == number_of_stations:    #если все строчки матрицы успешно были перенесены в массив
            while True:   # чтоб не было несуществующей станции
                start = input('Едем от ').lower()
                if start not in station:
                    print('Ошибка. Нет такой станции')
                    continue
                break

            while True:   # чтоб не было несуществующей станции
                finish = input('До ').lower()
                if finish not in station or finish == start:
                    print('Ошибка. Введите любую станцию исключая ' + str(start))
                    continue
                break


            distance = dijkstra(number_of_stations, station.index(start), adjacency_matrix, station.index(finish))[0]
            way = dijkstra(number_of_stations, station.index(start), adjacency_matrix, station.index(finish))[1]
            station_time = dijkstra(number_of_stations, station.index(start), adjacency_matrix, station.index(finish))[2]
            travel_time = distance[station.index(finish)]//60
            print('Время в пути от станции ' + str(start).title() + ' до станции ' + str(finish).title() + ' равно ' +
                  str(travel_time) + minute(travel_time))

            if way == False:
                print('Станция ' + str(finish).title() + ' недостижима со станции ' + str(start).title())
            else:
                print('Путь от станции ' + str(start).title() + ' до станции ' + str(finish).title() + ': ')

                for i in range(len(way)):
                    if i == len(way)-1:
                        print(station[way[i]].title())
                    else:
                        print(station[way[i]].title(), end='->')

                print('Сейчас ' + time_start.strftime('%H:%M'))

                time_res1 = time_start

                for i in range(1, len(way)):
                    timedelta = datetime.timedelta(seconds=station_time[i-1])
                    time_res1 += timedelta
                    print('На станции ' + station[way[i]].title() + ' будете в ' + time_res1.strftime('%H:%M'))
                    timedelta = time_res1

        else:
            print('Проверьте матрицу.')
            return


        time_finish = datetime.datetime.now()
        time_res2 = time_finish - time_start
        print('Время работы программы: {}с {}мкс'.format(time_res2.seconds, time_res2.microseconds))


    except:
        print('Файл не найден.')


if __name__ == '__main__':
    main()