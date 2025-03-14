# def pass_by_reference(thisdict3):
#     d_thisdict = thisdict.copy()
#     print(id(d_thisdict))
#     pass
#
#
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(id(thisdict))
# pass_by_reference(thisdict)
def pass_by_reference(tuple3):
    tuple3 += [3]
    new_tuple = tuple(tuple3)
    print(id(tuple3))
    print(tuple3)
    pass


o_tuple = [0, 1, 34, 60]

print(id(o_tuple))
pass_by_reference(o_tuple)
