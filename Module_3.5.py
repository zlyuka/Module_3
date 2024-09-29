#
# def get_multiplied_digits(number):
#     str_number = str(number)
#     first = int(str_number[0])
#     if first == 0:
#         first = 1
#     elif len(str_number) > 1:
#         first = first * get_multiplied_digits(int(str_number[1:]))
#     return first
#
# result = get_multiplied_digits(40203)
# print(result)
# result = get_multiplied_digits(420)
# print(result)


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return  first * get_multiplied_digits(int(str_number[1:]))
    if first != 0:
        return first
    return 1



result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(420)
print(result)

# def get_multiplied_digits(number):
#     str_number = str(number)
#     first = int(str_number[0])
#     for int in number:
#     if first == 0:
#         first = 1
#     if len(str_number) > 1:
#         first = first * get_multiplied_digits(int(str_number[1:]))
#     return first
#
# result = get_multiplied_digits(420)
# print(result)