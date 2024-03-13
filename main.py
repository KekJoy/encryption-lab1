import math
from heapq import heappop, heapify, heappush
from typing import List

from haffman import huffman_coding
from shannon_fano import shannon_fano_coding

# odds = [0.285, 0.183, 0.164, 0.122, 0.093, 0.086, 0.056, 0.011]
# alphabet = {'a': 0.285, 'b': 0.183, 'c': 0.164, 'd': 0.122, 'e': 0.093, 'f': 0.086, 'g': 0.056, 'h': 0.011}
odds = [0.214, 0.197, 0.154, 0.153, 0.107, 0.101, 0.051, 0.023]
alphabet = {'a': 0.214, 'b': 0.197, 'c': 0.154, 'd': 0.153, 'e': 0.107, 'f': 0.101, 'g': 0.051, 'h': 0.023}

res = {odd: "" for odd in odds}


# TODO: 1. Преобразовать функции в классы, 2. Функция кодирования исходного сообщения, 3. Функция декодировани сообщения, 4. Расчеты коэффициентов 5. Рефакторинг


def encoding_message(word: str) -> str:
    encoded_message = ""
    for letter in word:
        if letter not in alphabet.keys():
            return "Error. Letter not in alphabet"
        encoded_message += res[alphabet[letter]]
    return encoded_message


def decode_message(encoded_message: str) -> str:
    decoded_message = ""
    c = {res[y]: x for x, y in alphabet.items()}
    tmp = ""
    for digit in encoded_message:
        tmp += digit
        if tmp in c.keys():
            decoded_message += c[tmp]
            tmp = ""
    return decoded_message


def relative_efficiency_ratio(func):
    H = 0
    for odd in odds:
        H += odd * math.log2(odd)
    avg_lenght = 0
    for key, value in func.items():
        avg_lenght += len(value) * key

    return -H / avg_lenght


def statistical_compression(func):
    H_max = math.log2(len(odds))
    avg_lenght = 0
    for key, value in func.items():
        avg_lenght += len(value) * key
    return H_max / avg_lenght


# shannon = shannon_fano_coding(odds, res=res)
# print(shannon)
# var = encoding_message('adce')
# print(var)
# print(decode_message(var))

res = huffman_coding(res)
print(res)
var = encoding_message('adce')
print(var)
print(decode_message(var))

print(f"Относительная эффективность:{relative_efficiency_ratio(res)}")
print(f"Статистическое сжатие:{statistical_compression(res)}")
