'''
Created on Sep 12, 2012

@author: lfeier
'''


def insert_all(arr, at_index, to_add):
    for idx, el in enumerate(to_add):
        arr.insert(at_index + idx, el)
    return arr


def flatten_with_insert(arr):
    i = 0
    while(i < len(arr)):
        if isinstance(arr[i], list):
            idx_to_remove = i + len(arr[i])
            arr = insert_all(arr, i, arr[i])
            arr.pop(idx_to_remove)
        print(i, arr[i])
        i += 1
    return arr


def flatten_by_level(arr, level):
    to_ret = []
    for el in arr:
        if isinstance(el, list) and level > 0:
            to_ret += flatten_by_level(el, level - 1)
        else:
            to_ret.append(el)
    return to_ret


def flatten(list_a, list_b, max_depth):
    return flatten_by_level(list_a, max_depth) + flatten_by_level(list_b, max_depth)

print(flatten([1, 2, [3, 4, 5], [6, 7, 8], [9, [10, 11, [12, 13, 14, [15, 16, 17]]]]], [1, 2, [3, 4, 5], [6, 7, 8], [9, [10, 11, [12, 13, 14, [15, 16, 17]]]]], 2))
#**********************************************
#pb2
#**********************************************
a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}

b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}


def merge_dict(hash1, hash2):
    for key in hash1:
        if key in hash2:
            if type(hash1[key]) == type(hash2[key]):
                if type(hash1[key]) in [list, int, str]:
                    hash1[key] += hash2[key]
                elif type(hash1[key]) is set:
                    hash1[key] = set(hash1[key].union(hash2[key]))
                elif type(hash1[key]) is dict:
                    hash1[key] = merge_dict(hash1[key], hash2[key])
            else:
                hash1[key] = (hash1[key], hash2[key])
#check 4 elem that are not in hash1 but exist in hash2
    for key in hash2:
        if key not in hash1:
            hash1[key] = hash2[key]
    return hash1

print(merge_dict(a, b))

#**********************************************
#pb3
#**********************************************
lines = open('./../tmp/input', 'r').readlines()
all_dicts = []
aux_dict = {}
for i, line in enumerate(lines):
    if len(line.strip()) != 0:
        items = line.strip().split()
        aux_dict[items[0]] = int(items[1])
    if len(line.strip()) == 0 or i == len(lines) - 1:
        all_dicts.append(aux_dict)
        aux_dict = {}

sorted_dicts = []
for a_dict in all_dicts:
    sorted_dicts.append(sorted(a_dict.items(), key=lambda x: x[0]))

arr_not_sorted = sorted_dicts[:]


def my_cmp(val1, val2):
    if val1[0][1] < val2[0][1]:
        return -1
    elif val1[0][1] > val2[0][1]:
        return 1
    else:
        #maybe todo check the max to loop through
        for i in range(len(val1)):
            if(val1[i][1] < val2[i][1]):
                return -1
        return 1


def sort_arr(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if my_cmp(arr[j], arr[i]) < 0:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
    return arr

print("not sorted dicts")
print(arr_not_sorted)
print("sorted dicts")
print(sort_arr(sorted_dicts))

f = open("./../tmp/output", "w")
for elem in sorted_dicts:
    f.write(str(arr_not_sorted.index(elem)) + " ")
f.close()
