
immutable_var=tuple_="abc",123,[456]

print(immutable_var)
#tuple_[1]=5
# TypeError: 'tuple' object does not support item assignment
#print(tuple_)

mutable_list=['zyw',678,True]
print(mutable_list)
#index = mutable_list.index(True)
#print(index)
mutable_list[2]=False
mutable_list[1]='6,7,8'
mutable_list[0]='ZYW'
print(mutable_list)
