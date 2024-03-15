'''
# ? ----> common function for list
# l1 = [6,7,8,9,0]
# print(len(l1))
# print(max(l1)) # ----> eroe cause its a combination of list and string
# print(min(l1)) # ----> error cause its a combination of list and string

# l1 = [6,7,8,9,0]
# print(len(l1))

# l1 = [6,7,8,9,0,8.89, -5, 0.16]
# # index()----> to get the index value of specific element
# print(l1.index(9))

# l1 = [6,7,8,9, 8,0,8.89, -5, 0.16]
# count()---> how many no of times an element is printed
# print(l1.count(8))

# some function which is specifically used for list
# to add element inside list
# insert ()-----> to add element at specific index position
l1 = [6,7,8,9,0,8.89, -5, 0.16]
# l1.insert (7, "cars")
# print(l1)
# pop (index_value) ----> used to delete element at specific index
# l1.pop(4) # 4 is index value
# print(l1)

# remove(element) ----> used to delete element directly
# l1.remove(8.89)
# print(l1)

# l1.clear(7)
# print(l1)

# del.l1
# print(l1)

l1 = [1,2,3,4]
l2 = [1,2,3,4]
# print(l1+l2)

# or
# extend( ---> to combine 2 lists)
# l1.extend(l2)
# print(l1)

# ? -------> copy ()
l1 =[6,7,8,9]
l2 = l1.copy()
print(l2)

print(id(l1))
print(id(l2))


# ! diff between shallow copy and deep copy
# shallow copy
import copy
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
l1.append(209)
print(l1)
print(l2)

# deep copy

import copy
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[-1][1]) ---> to index nested list

l2=copy.copy(l1)
l1.append(209)
print(l1)
print(l2)

# ? sort -> arrange elemebnts in list in ascending or decending order
# M:-2 --> descending order

l1 = [9,7,2,3,5,23,63,32]
l1.sort(reverse=True)
print(l1)

# ! ---->nested list
 
l1 = [8,9,[0,8,7],["p","o","y"],[8,'t']]
print(l1[-2][1])
print(l1[1:4])
print(l1[1:-1])

# ? to delete "t" from l1
l1[-1].remove('t)
print(l1)

# ? combine these ["p","o",'y']
# eg:
# t1 = (8, 8, 9, 6, 5.78, [9,0],(6, 8), "hey", 9+6j)
# print(t1)
# print(type(t1))

# ? indexing, slicing are all same as list
l1 = (8)
print(type(l1))



# M:-3

t1=8,9
print(type(t1))

# M:-4

t2=8,
print(type(t2))


# len(), min(), max(), index(), count() --> all same as kist


# To add all element inside list and tuple
#sum()
#l1 = (8, 9, 7, 6)
#print(sum(l1))



# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)

 # * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "welcome to all"
print(s1.endswitch('1'))
print(s1.startswitch('w'))

s1 = "67"
print(type(s1))
print(s1.isdigit())


# * print the string in reverse manner
s1 = "Welcome to all"
print(s1.endswith('L'))             

'''
characters =len(s1)
#print(characters)
'''
words = s1.split(" ")
print(words)


words = s1.split(" ")
print(len(words))

'''
#sentences = s1.split('.')
#print(len(sentences))


sentences = s1.split('.')
for val in sentences:
    if val =='':
        index = sentences.index('')
        sentences.pop(index)
print(len(sentences))











