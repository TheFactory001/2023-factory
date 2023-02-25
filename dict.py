point = {"x": 1, "y":2}
point = dict(x=1, y=2)
point["x"] = 20
point["z"] = 40
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["y"]
print(point)
for key, value in point.items():
    print(key, value)