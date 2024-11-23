immutable_var = (['i', 'am', 'a', 'list'], 1, 2.22, "String", True)
print(immutable_var)
immutable_var[0][0:2] = 'it', 'is'
print(immutable_var)
# Внетри картежа я могу изменять только списк
mutable_list = ['a', 1, 2.22, True]
print(mutable_list)
mutable_list[:] = 'b', 2, 3.33, False
print(mutable_list)