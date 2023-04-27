# sorting list in ascending order
numbers = [4, 3, 7, 9, 8, 6, 2]
numbers.sort()
# print(numbers)
# sorting in decending order using reverse function
numbers = [4, 3, 7, 9, 8, 6, 2]
numbers.sort(reverse=True)
print(numbers)
# sorting list using in built function sorted that will brings out the original list and the remodified list
numbers = [4, 3, 7, 9, 8, 6, 2]
print(sorted(numbers))
print(numbers)
# dealing with a list of tuples which have two items
items = [
    ("product1", 30),
    ("product2", 20),
    ("product3", 30)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
