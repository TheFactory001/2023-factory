def save_user(**user):
    print(user)


# save_user(id=1, name="Joe", age=30)
def safe_user(**user):
    print(user)


# afe_user(first_name="Joel",  last_name="John", age=30, occ="business")


def save_user(**user):
    print(user["id", "name", "age"])
    print(user["university"])


safe_user(id=1, name="Joe", age=30)
safe_user(university="Bowen")
