# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.
my_list = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9, 11, 11]
result_list = []
for i in my_list:
    if my_list.count(i) > 1:
        result_list.append(i)
print(list(set(result_list)))