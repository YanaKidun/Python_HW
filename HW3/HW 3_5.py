""""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу."""

def my_str_sum():
    summary = 0
    a = False
    while a == False:
        str1 = input('Iprut str or 999-exit').split()
        res = 0
        for el in range(len(str1)):
            if str1[el] == '999':
                a = True
                break
            else:
                res = res + int(str1[el])
        summary = summary + res
        print(f'Sum is {summary}')
    print(f'Your result is {summary}')


my_str_sum()



"""test"""

# str1 = input("STR")
# summary = 0
# while str1!='999':
#     if '999' in str1:
#         str2 = str1.split(" ")
#         b = str2.index("999")
#         str3 = str2[0:b]
#         for i, elem in enumerate(str3):
#             str3[i] = int(elem)
#         summary = summary+sum(str3)
#         print(summary)
#         break
#     else:
#         str2 = str1.split(" ")
#         for i, elem in enumerate(str2):
#             str2[i] = int(elem)
#         summary = summary+sum(str2)
#     print(summary)
#     str1 = input("input str")
#



