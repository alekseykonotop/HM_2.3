from lxml import etree
import chardet
from pprint import pprint


def open_and_read_file(name_file):
    '''Функция ...............'''
    result_list = []
    str_list = []

    with open(name_file, "rb") as f:
        s = f.read()
        encode = chardet.detect(s)
        print(encode) # Отладочный принт

    parser = etree.XMLParser(encoding=encode['encoding'])
    tree = etree.parse(name_file, parser)
    nodes = tree.xpath(u'/Файл/Справочники/ПроизводителиИмпортеры')
    # with open(name_file, encoding=encode['encoding']) as f:
    # tree = ElementTree.parse(name_file, encoding=encode['encoding'])
    # pprint(tree.text) # Отладочный принт

    #     channel_tag = tree.find('channel')
    #     title_tag = channel_tag.find('title')
    #     str_list.append(title_tag.text.strip().split(' '))
    #     description_tag = channel_tag.find('description')
    #     str_list.append(description_tag.text.strip().split(' '))
    #     tag_list = channel_tag.findall('item')
    #
    #     for tg in tag_list:
    #         str_list.append(tg.find('title').text.strip().split(' '))
    #         str_list.append(tg.find('description').text.strip().split(' '))
    #
    #     for string in str_list:
    #         for word in string:
    #             # print(word) # Отладочный принт
    #             if len(word) > 6:
    #                 result_list.append(word)
    # print('result_list', result_list) # Отладочный принт
    # return result_list



open_and_read_file("newscy.xml")

# def open_and_read_file(article):
#     '''Функция ...............'''
    # result_list = []
    # str_list = []
    # tree = ElementTree.parse(article)
    # print(tree)
    # channel_el = tree.find('channel')
    #
    # print(channel_el.text)

    # with open(article, 'rb') as f:
    #     data_byte = f.read()
    #     result = chardet.detect(data_byte)
    #     s = data_byte.decode(result['encoding'])
    #     data = json.loads(s)
    #     str_list.append(data['rss']['channel']['description'].strip().split(' '))
    #     for i in data['rss']['channel']['items']:
    #         str_list.append(i['description'].strip().split(' '))
    #         str_list.append(i['title'].strip().split(' '))
    # for words_string in str_list:
    #     for word in words_string:
    #         if len(word) > 6:
    #             result_list.append(word)
    # return result_list

# open_and_read_file("newsafr.xml")


def count_words_in_list(article):
    '''Функция получает на вход атрибут с названием файла,

    для передачи этого значения функции open_and_read_file(article).
    Получая от нее список используемых в файле слов, формирует множество,
    с помощью которого получает значения кол-ва вхождения каждого элемента
    множества в полученном списке.
    '''
    count_words_list = []
    words_lst = open_and_read_file(article)
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


# ten_most_used_words()

