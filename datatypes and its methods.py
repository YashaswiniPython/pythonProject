# Dictionary and its methods
# keys(),values(),pop(),popitem(), values(), update().
# h = {"m":"n","o":"p","q":"r"}
# y = 10
# print(h.keys())
# print(h.values())
# r = h.copy()
# print(r)
# n =dict.fromkeys(h,y)   #replaces values of h with y assigned values.
# n =dict.fromkeys(h,y)
# print(n)
# print(h.get("m"))       #get the value of m

# The items() method returns a view object.
# The view object contains the key-value pairs of the dictionary, as tuples in a list.
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.items()
#
# print(x)


# The pop() method removes the specified item from the dictionary.
# The value of the removed item is the return value of the pop()
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.pop("model")
# print(car)

# The popitem() method removes the item that was last inserted into the dictionary.
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.popitem()
# print(car)

# The setdefault() method returns the value of the item with the specified key.
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.setdefault("model", "Bronco")
#
# print(x)
# print(car)


# The update() method inserts the specified items to the dictionary.
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.update({"color": "White"})
# print(car)

# The values() method returns a view object. The view object contains the values of the dictionary, as a list.
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.values()
# print(x)

