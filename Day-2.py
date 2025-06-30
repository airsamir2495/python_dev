#Day-2
# Create a list called shopping_list and populate it with the initial items: "Milk", "Eggs", "Bread", and "Bananas".
# Add the item "Apples" to the end of the list.
# Remove "Bread" from the list.
# Create a function named show_list that takes a list as an argument and prints each item on a new line.
# Create a function named total_items that takes a list as an argument and returns the number of items in the list.
# Call show_list and total_items with your shopping_list and display the results.


shopping_list = ["Milk","Bread","Egg","Rice","Banana"]
shopping_list.append("Apples")
print("New item added in the list::",shopping_list)
shopping_list.remove('Bread')
print("Removed item:",shopping_list)
new_list =["Sam","Dam","Ram",1,2,3]

def show_list(list_item):
    for i in range(0,len(list_item)):
        print (f'listed iterms {i}::',list_item[i])

def total_items(new_list):
    return print ('Number of items::',len(new_list))


show_list(shopping_list)
total_items(new_list)
