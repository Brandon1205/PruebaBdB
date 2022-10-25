#hash 572cdea48471e195e35f43bfcda58cba

s = 5
ss = (s*10)+s

input_array = {"array":[-6, -5, 0, 5, 6]}

def square_array_sorted(array):
    output_list = []
    for item in array:
        item_square = item*item
        if item_square >= ss:
            item_square = ''

        if item_square != '':
            output_list.append(item_square)

    quick_sort(output_list)
    return output_list

def partition_items(items, low, high):
    pivot  = items[(low + high)//2]
    i = low - 1
    j = high + 1

    while True:
        i =  i + 1
        while items[i] < pivot:
            i = i + 1

        j = j - 1

        while items[j] > pivot:
            j = j - 1

        if i >= j:
            return j

        items[i], items[j] = items[j], items[i]

def quick_sort(list):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition_items(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(list, 0, len(list) - 1)

output_array = square_array_sorted(input_array["array"])

print(input_array, "->", output_array)