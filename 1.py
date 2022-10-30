# Формат: Объясняет преподаватель

# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут 
# точно решать не имеет смысла) - исходите из уровня группы и студента.

#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

input_lst = [1, 2, 3, 4, 5]

negative_index = [i for i in range(1, len(input_lst)) if not i % 2 == 0]
lst = list(enumerate(input_lst)) 
print('\n', input_lst, '-> элементы ', negative_index, ', сумма =', sum(negative_index))

# дополнительный код
negative_elements = list(filter(lambda x: x % 2, input_lst)) # находит нечетные элементы списка
positive_elements = [v for k,v in enumerate(input_lst) if not k % 2 == 0] # находит четные элементы списка
# print(negative_elements)