import random
string_one = 'pynative'
print("Original String:", string_one)

char_list = list(string_one)

random.shuffle(char_list)

string_one = ''.join(char_list)
print('Shuffled string is:', string_one)
