def add_target(mylist, target):
    if target in mylist:
        print("Target already in list")
    else:
        mylist.append(target)
        print(mylist)        

mylist = ["a", "g", "h"]
add_target(mylist, "h")      