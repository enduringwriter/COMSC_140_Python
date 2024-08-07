"""
'ID' - Mutable
This program demonstrates that the list object remains the same 
for the list variable even if the list variable is modified.
This property of ID being the same for a variable if modified applies
to all mutable objects .e.g lists, dictionaries.

'Mutable'
It also shows how changes to the list within a function affect the 
original list due to Python's handling of mutable objects such as lists.

Advantage of mutable IDs
When a function is called with arguments in Python,
it receives references to the actual objects, not copies of them.
This distinction between passing references and copying objects
is important for both performance and memory usage. 

Passing References: When passing an object (e.g. list, dictionary, or custom object) to a function,
the function gets a reference to the original object.
This means that the function can modify the object without creating a new one.

'ID' - Immutable
The ID of an object changes when an immutable variable is modifed e.g.
a = 10
print(id(a))  # e.g. 71164989011
a = 20
print(id(a))  # e.g. 71164989027
"""

def myfunc(lst):
    print(id(lst), 'ID of lst in myfunc() as soon as the function starts')
    lst[0] = 999
    print(id(lst), 'ID of lst in myfunc() after changing value of the 1st element')
    return lst


def main():
    n = [1, 2, 3]
    print(id(n))
    ret = myfunc(n)
    print(id(ret))


if __name__ == '__main__':
    main()
