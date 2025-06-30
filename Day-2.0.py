# if user wants to give list in n numbers and print
new_list =[]

# def show_list(list_item):
#     for i in range(0,len(list_item)):
#         print (f'listed iterms {i}::',list_item[i])

def total_items(new_list):
    print("Enter * to end the list")
    while True:
        user = input("Enter the items::")
        if (user == '*'):
            break
        else:
            new_list.append(user)
    return print('New list::',new_list)

       
total_items(new_list)