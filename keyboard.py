import time

number_of_keys = int(input())  # number_of_keys = 3
sym_id = [int(i) for i in input('Введите значения через пробел ').split()]  # sym_id = [42, 3, 14]
rows = [int(i) for i in input('Введите значения через пробел ').split()]  # rows = [1, 3, 3]
count_of_sym_in_referat = int(input())  # count_of_sym_in_referat = 4
sym_id_in_referat = [int(i) for i in input('Введите значения через пробел ').split()]  # sym_id_in_referat = [3, 14, 14, 3]

# number_of_keys = 3
# sym_id = [42, 3, 14]
# rows = [1, 3, 3]
# count_of_sym_in_referat = 4
# sym_id_in_referat = [3, 14, 14, 3]


# number_of_keys = 4
# sym_id = [1, 2, 3, 4]
# rows = [1, 2, 1, 2]
# count_of_sym_in_referat = 5
# sym_id_in_referat = [1, 2, 3, 1, 4]


start1 = time.time()
matching_dictionary = dict(zip(sym_id, rows))  # словарь, где {инд.клавиши:ряд}
end1 = time.time()
print(end1 - start1, 'время matching_dictionary = dict(zip(sym_id, rows)) с вводом данных')


start2 = time.time()
count = 0
for i in range(1, count_of_sym_in_referat):
    if matching_dictionary.get(sym_id_in_referat[i]) != matching_dictionary.get(sym_id_in_referat[i-1]):
        count += 1
end2 = time.time()
print(end2 - start2, 'время цикла for с вводом данных')

print(count)




