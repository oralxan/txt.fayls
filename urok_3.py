


'''a='gdhfg'
with open('names.txt',mode='a') as file:
    file.write(a)
    file.close()'''
#1
'''def sum_list_elements(lst):
    return sum(lst)
numbers = [1, 2, 3, 4, 5]
result = sum_list_elements(numbers)
with open("urok_3.txt", "w") as file:
    file.write(str(result))'''
#2
'''def elements(tpl):
    return tuple(set(tpl))
my_tuple = (1, 2, 3, 2, 4, 4, 5)
unique_elements = elements(my_tuple)
with open("result2.txt", "w") as file:
    file.write(str(unique_elements))'''
#3
'''def create_dictionary(keys, values):
    return dict(zip(keys, values))
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = create_dictionary(keys, values)
with open("result3.txt", "w") as file:
    for key, value in dictionary.items():
        file.write(f"{key}: {value}\n")'''
#5
'''def merge_lists_to_dictionary(keys, values):
    dictionary = dict(zip(keys, values))
    return dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3] 
result_dict = merge_lists_to_dictionary(keys, values)
with open("result5.txt", "w") as file:
    for key, value in result_dict.items():
        file.write(f"{key}: {value}\n")'''
#6
'''def count_frequency(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency
my_list = [1, 2, 3, 1, 2, 1, 3, 4, 5, 4, 3, 2, 1]
frequency = count_frequency(my_list)
with open("result6.txt", "w") as file:
    for element, count in frequency.items():
        file.write(f"{element}: {count}\n")'''
#7
'''def reverse_strings_in_list(lst):
    reversed_list = [string[::-1] for string in lst]
    return reversed_list
my_list = ['hello', 'world', 'python', 'programming']
reversed_list = reverse_strings_in_list(my_list)
with open("result7.txt", "w") as file:
    for string in reversed_list:
        file.write(string + "\n")'''
#8
'''def ch_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

def anagrams(lst):
    anagram_p = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if ch_anagrams(lst[i], lst[j]):
                anagram_p.append((lst[i], lst[j]))
    return anagram_p
word_list = ['listen', 'silent', 'bad', 'dad', 'cat', 'act']
anagram_pairs =anagrams(word_list)
with open("result8.txt", "w") as file:
    for pair in anagram_pairs:
        file.write(f"{pair[0]} - {pair[1]}\n")'''
#9
'''my_tuple = (1, 2, 3, 2, 4, 3, 5)
unique_tuple = tuple(set(my_tuple))
with open("result9.txt", "w") as file:
    for element in unique_tuple:
        file.write(str(element) + "\n")'''
#10
'''def dictionaries(dict1, dict2):
    dict1.update(dict2)
    return dict1
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dictionaries(dict1, dict2)
with open("result10.txt", "w") as file:
    for key, value in merged_dict.items():
        file.write(f"{key}: {value}\n")'''
#11
'''def max_key_1(dictionary):
    max_key = max(dictionary, key=dictionary.get)
    return max_key
my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
max_key = max_key_1(my_dict)
with open("result11.txt", "w") as file:
    file.write(max_key)'''
#12
'''def square_numbers_1(numbers):
    squared_numbers = [num**2 if num % 2 == 0 else num for num in numbers]
    return squared_numbers
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = square_numbers_1(my_numbers)
with open("result12.txt", "w") as file:
    for num in squared_numbers:
        file.write(str(num) + "\n")'''
#13
'''def elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = elements(list1, list2)
with open("result13.txt", "w") as file:
    for element in common_elements:
        file.write(str(element) )'''
#14?
#15
'''def a (dictionary):
    total_sum = sum(dictionary.values())
    return total_sum
my_dictionary = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
sum_values = a (my_dictionary)
with open("result15.txt", "w") as file:
    file.write(str(sum_values))'''
#16
'''def a(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    return common_keys
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
common_keys =a(dict1, dict2)
with open("result16.txt", "w") as file:
    for key in common_keys:
        file.write(str(key))'''
#17
'''def a(tuple1, tuple2):
    if tuple1 == tuple2:
        return "birdey"
    else:
        return "birdey emes"
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
result = a(tuple1, tuple2)
with open("result17.txt", "w") as file:
    file.write(result)'''
#18
'''def a(list1, list2):
    merged_list = list1 + list2
    return merged_list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
b_list = a(list1, list2)
with open("result18.txt", "w") as file:
    for element in b_list:
        file.write(str(element))'''
#19
def a(numbers):
    b = sum(numbers[::2])
    return b
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = a(numbers)
with open("result19.txt", "w") as file:
    file.write(str(c))