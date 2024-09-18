calls = 0
list_to_search = []

def count_calls():
    global calls
    calls += 1
    return calls



def string_info(string):
    len(string)
    string.lower()
    string.upper()
    count_calls()
    print(f"{len(string)},'{string.upper()}','{string.lower()}'")


# def is_comtains(string, list_to_search):
#     for str in list_to_search:
#         print(str == list_to_search):
#     pass

list_to_search.append(input('Введите список в котором будет искаться соответствие '))

print(list_to_search)
string = input('Введите строку')
string_info(string)
# is_comtains()
print(calls)
