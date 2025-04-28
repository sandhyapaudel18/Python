#unordered="jun sequence ma ni aaucna sakcha" must be unique and immutable like strings
#cannot have lists and dic as they are mutable in nature

collection={1,"hey",2,4,3,"hello"}
# print(collection)
# print(len(collection))

# null_set=set() declaring the null set here
# print(type(null_set))

#set method
# set.add() adding an element
#set.remove(element name) removes particular element
#set.clear() empties the set
#set.pop() removes a random value

# print(collection.clear()) gives none
collection.add(10)


# collection.add([3,4,7])
collection.clear()
# print(collection)

#union = having all without duplication
#intersection=only similar values

set1={4,5,6,2}
set2={5,8,9,2,1}
print(set1.union(set2))
set3=set1.intersection(set2)
print(set3)
