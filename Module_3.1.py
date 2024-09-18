calls = 0

def count_calls():
    global calls
    calls += 1
    return calls



def string_info(string):
    count_calls()
    len(string)
    string.lower()
    string.upper()
    return (f"{len(string)},'{string.upper()}','{string.lower()}'")


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for str in list_to_search:
        if str.lower() == string:
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
