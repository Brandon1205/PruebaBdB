#hash 572cdea48471e195e35f43bfcda58cba

s = 5

input_list = [10, 20, 30, 70]
output_list = []

for item in input_list:

    item_dec = item // 10
    item_unt = item % 10

    if item_dec >= s or item_dec == 0:
        item_dec = ''
    if item_unt >= s:
        item_unt = ''
    
    item = str(item_dec) + str(item_unt)

    if item != '':
        output_list.insert(0,int(item))

print(input_list,"->",output_list)

