import json
import chardet


def open_and_read_file(article):
    '''Функция открывает переданный файл для чтения в байтах,

    декодирует его с помощью импортируемой фунции chardet.
    '''
    str_list = []
    with open(article, 'rb') as f:
        data_byte = f.read()
        result = chardet.detect(data_byte)
        s = data_byte.decode(result['encoding'])
        data = json.loads(s)
        str_list.append(data['rss']['channel']['description'].strip().split(' '))
        for i in data['rss']['channel']['items']:
            str_list.append(i['description'].strip().split(' '))
            str_list.append(i['title'].strip().split(' '))
    return str_list


def sorted_list(article):
    '''Функция сортирует список и создает новый список из строк,

    отвечающих условию: длина строки больше 6 символов.
    '''
    result_list = []
    str_list = open_and_read_file(article)
    for words_string in str_list:
        for word in words_string:
            if len(word) > 6:
                result_list.append(word)
    return result_list



def count_words_in_list(article):
    '''Функция получает на вход атрибут с названием файла,

    для передачи этого значения функции open_and_read_file(article).
    Получая от нее список используемых в файле слов, формирует множество,
    с помощью которого получает значения кол-ва вхождения каждого элемента
    множества в полученном списке.
    '''
    count_words_list = []
    words_lst = sorted_list(article)
    set_of_words = set(words_lst)
    for word_of_set in set_of_words:
        quantity = 0
        for i in words_lst:
            if i == word_of_set:
                quantity += 1
        count_words_list = count_words_list + [[word_of_set, quantity]]
    return count_words_list


def get_top_words_list(article):
    ''' Функция сортирует элементы списка по второму значению.

    Элементы списка являются спискамии. Функция возвращает
    список  из 10 отсортированных слов с максимальной частотностью в
    порядке убывания.
    '''
    lst = count_words_in_list(article)
    while True:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i][1] < lst[i+1][1]:
                lst[i][1], lst[i+1][1] = lst[i+1][1], lst[i][1]
                sorted = False
        if sorted:
            break
    return lst[:10]


def print_result(article, top_words_list):
    '''Функция print_result выводит на экран название

    файла и полученный список максимальных значений.
    '''
    print('В файле {0} самые высокочастотные слова: {1}\n'.format(article, top_words_list))



def ten_most_used_words():
    '''Функция определяет 10 самых высокочастотных слов с заданных файлах'''
    article_list = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    for article in article_list:
        top_words_list = get_top_words_list(article)
        print_result(article, top_words_list)


ten_most_used_words()

