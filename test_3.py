input_array = {"coins": [1,5,1,1,1,10,15,20,55,111,1]}

def minimum_change(list):
    list.sort()
    current_minimum_change = 0

    for item in list:
        if item > current_minimum_change + 1:
            return current_minimum_change + 1
        
        current_minimum_change = current_minimum_change + item

    return current_minimum_change + 1


output_change = minimum_change(input_array["coins"])

print(input_array, "->", output_change)