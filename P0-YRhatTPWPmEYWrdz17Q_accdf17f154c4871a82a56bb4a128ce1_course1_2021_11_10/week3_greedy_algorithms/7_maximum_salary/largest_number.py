# Uses python3

import sys


def preprocess(arr):
    arr_set = set(arr)

    item_dictionary = {unique_item: 0 for unique_item in arr_set}
    for item in arr:
        item_dictionary[item] += 1

    processed_arr = [''.join([item]*count) for item, count in item_dictionary.items()]

    return processed_arr


def f2(arr):
    item_freq = {}
    for item in arr:
        if len(item) not in item_freq:
            item_freq[len(item)] = [item]
        else:
            item_freq[len(item)].append(item)

    item_freq = {k: sorted(items) for k, items in item_freq.items()}

    sorted_keys = sorted(item_freq)
    for key in sorted_keys:
        for item in item_freq[key]:
            print(item)

    return ''


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]

    output = f2(preprocess(a))
    print(output)
