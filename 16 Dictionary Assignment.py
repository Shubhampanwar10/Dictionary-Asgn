# Dictionary Assignment

# Q1. Write a program that takes two lists of equal length as input and creates a dictionary that maps elements from one list to corresponding elements in the other list.
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3, 4]
# Output:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

"""
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
d={}

for i in range(len(keys)):
    d.update({keys[i]:values[i]})
print(d)
"""

# Q2. Write a program that takes a list of names as input and creates a dictionary that counts the number of times each name appears in the list.
# names = ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob', 'Alice']
# Output:
# {'Alice': 3, 'Bob': 2, 'Charlie': 1, 'David': 1}


names = ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob', 'Alice']
count={}

for i in names:
    if i in count:
        count[i] +=1
    else:
        count[i] =1
print(count)

s={}
for i in names:
    s[i]=names.count(i)
    print(i)
print(s)


# Q3. Write a program that takes a list of words as input and creates a dictionary that groups the words by their length.
# words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'frog', 'giraffe', 'horse']
# Output:
# {5: ['apple', 'horse'], 6: ['banana'], 3: ['cat', 'dog'], 8: ['elephant'], 4: ['frog'], 7: ['giraffe']}

words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'frog', 'giraffe', 'horse']
new={}
for i in words:
    if len(i) in new:
        new[len(i)].append(i)
    else:
        new[len(i)]=[i]
print(new)

# Q4. Write a program that takes a list of numbers as input and creates a dictionary that counts the number of times each number appears, but only for numbers that appear more than once.
# numbers = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 7, 7]
# Output:
# {1: 2, 2: 2, 4: 2, 7: 3}


numbers = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 7, 7]
count={}
for i in numbers:
    if i in count:
        count[i] +=1
    else:
        count[i] =1
print(count)

result={}
for x,y in count.items():
    if y>1:
        # result[x]=y
        result.update({x:y})
print(result)

l={}
for i in numbers:
    if numbers.count(i)>1:
        l[i]=numbers.count(i)
print(l)


# Q5. Write a program that takes a list of dictionaries as input, where each dictionary represents a person with keys for "name", "age", and "city". The program should create a new dictionary that maps each city to a list of people who live there.
people = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'Chicago'},
    {'name': 'Charlie', 'age': 35, 'city': 'New York'},
    {'name': 'Dave', 'age': 40, 'city': 'Chicago'},
    {'name': 'Eve', 'age': 45, 'city': 'San Francisco'}
]
output={}
for i in people:
    if i["city"] in output:
        output[i["city"]].append(i)
    else:
        output[i["city"]]=[i]
print(output)

for i in people:
    if i.get("city") in output:
        output[i.get("city")]=[i]
print(output)

# Output:
# {
#     'New York': [
#         {'name': 'Alice', 'age': 25, 'city': 'New York'},
#         {'name': 'Charlie', 'age': 35, 'city': 'New York'}
#     ],
#     'Chicago': [
#         {'name': 'Bob', 'age': 30, 'city': 'Chicago'},
#         {'name': 'Dave', 'age': 40, 'city': 'Chicago'}
#     ],
#     'San Francisco': [
#         {'name': 'Eve', 'age': 45, 'city': 'San Francisco'}
#     ]
# }

# Q6. Write a program that takes a string as input and creates a dictionary that maps each character to the number of times it appears in the string.
# string = 'hello world'
# Output
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

string = 'hello world'
m={}
for i in string:
    if i in m:
        m[i]=string.count(i)
    else:
        m[i]=1
print(m)

for i in string:
    m[i]=string.count(i) 
print(m)

# Q7. Write a program that takes a list of tuples as input and creates a dictionary that maps each key to a list of its values.
# my_list = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
# Output:
# {'a': [1, 3], 'b': [2], 'c': [4]}

my_list = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]



# Q8. Write a program that takes a list of tuples as input and returns a dictionary where each key is a unique value that appears in the tuples and each value is a list of keys that correspond to that value.
# my_list = [('a', 1), ('b', 2), ('a', 3), ('c', 1)]
# Output:
# {1: ['a', 'c'], 2: ['b'], 3: ['a']}


# Q9. Write a program that takes a list of strings as input and returns a dictionary where each key is a unique character that appears in the list of strings and each value is a list of strings that contain that character.
# my_list = ['apple', 'banana', 'cherry', 'date']
# Output:
# {'a': ['apple', 'banana', 'date'], 'p': ['apple'], 'l': ['apple'], 'e': ['apple', 'date'], 'b': ['banana'], 'n': ['banana'], 'c': ['cherry'], 'h': ['cherry'], 'r': ['cherry'], 'y': ['cherry']}

# Q10. Write a program that takes a string as input and returns a dictionary where each key is a unique word in the string and each value is a list of the indices where that word appears in the string.
# my_string = 'the quick brown fox jumps over the lazy dog '
# Output:
# {'the': [0, 6], 'quick': [1], 'brown': [2], 'fox': [3], 'jumps': [4], 'over': [5], 'lazy': [7], 'dog': [8]}

# Q11. Write a program that takes a list of dictionaries as input and returns a dictionary that contains the union of all the keys in the dictionaries and the corresponding list of values for each key.
# dicts = [ {'a': 1, 'b': 2, 'c': 3},    {'b': 4, 'c': 5, 'd': 6},    {'a': 7, 'd': 8, 'e': 9}]
# Output
# {'a': [1, 7], 'b': [2, 4], 'c': [3, 5], 'd': [6, 8], 'e': [9]}

