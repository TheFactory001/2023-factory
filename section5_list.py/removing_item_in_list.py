letters = ["a", "b", "c", "d"]
letters.pop(0)
print(letters)
fruits = ["apple", "Mango", "banana"]
fruits.pop(-1)
print(fruits)
# using remove method
fruits = ["apple", "mango", "banana"]
fruits.remove("mango")
print(fruits)
# using delete method
fruits = ["apple", "mango", "banana"]
del fruits[0:2]
print(fruits)
# clearing all object in the list
fruits = ["apple", "mango", "banana"]
fruits.clear()
print(fruits)


def remove_item_in_list(letters):
    remove_item = letters.pop(1)
    return remove_item


letters = ["a", "b", "c", "d"]
print(remove_item_in_list(letters))