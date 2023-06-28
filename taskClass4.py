# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.


text = input('Введите строку: ')
temp = {}
result = ''
for i in range(len(text)):
    if text[i] not in temp.keys():
        temp[text[i]] = 1
        result += f'{text[i]} '
    else:
        result += f'{text[i]}_{temp[text[i]]} '
        temp[text[i]] += 1
print(result)



