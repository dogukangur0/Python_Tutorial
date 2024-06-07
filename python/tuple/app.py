# tuples are stored multiple items in a single variable
# a tuple is a collection which is ordered and unchangeable  -> allow duplicate values. -> contain different data types
# there are only 2 methods in tuple -> count() and index()


tupletype = ("a","b","c",1,2,True)   # tuple -> ()

print(type(tupletype))

print(tupletype[0]) # access the tuple value

print(tupletype[1:3])  # 1 -> include, 3 -> not include

print(tupletype[:2])   # by leaving out the start value, the range will start at the first value.

convertListToTuple = tuple([1,2,3,4,5]) # list -> []
print(type(convertListToTuple)) 

convertTupleToList = list((1,2,3))
print(type(convertTupleToList)) 
