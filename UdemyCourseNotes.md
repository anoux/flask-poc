# Python and flask framework 

---

## Section 1

Starts with a Python owerview, just like how to define variables and lists, how calculations can be done. Also, it shows some functions, "print" for example.

#### What's Python?

- Python is a **OOP language** (object oriented programming). Object is simply a collection of data (variables) and methods (functions). Class is a blueprint for the object.
  And object is an **instance of a class**, that means this object **inherits** attributes and methods of that class.
  The process of creating an object is called **instantiation**

####  Python arrays implementation

- append() --> to add element to the end of the list
- extend() --> to extend all elements of a list to another list
- insert() --> to insert an element at the another index
- remove() --> to remove an element from the list
- pop() --> to remove elements return element at the given index
- clear() --> to remove all elements from the list
- index() --> to return the index of the first matched element
- count() --> to count of numbers of elements passed as an argument
- sort() --> to sot the elements in ascending order by default
- reverse() --> to reverse order element in a list
- copy() --> to return a copy of elements in a list

#### File methods in Python

- close() --> to close an open file
- detach() --> to separate the underlying binary buffer from the TextIOBase and reutrn it
- fileno() --> return an integer number (file descriptor) of the file
- flusch() --> to flush the write buffer of the file stream
- isatty() --> return True if the file stream is interactive
- read(n) --> read atmost n characters from the file. Reads till end of file if it is negative or None
- readable() --> return True if the file stream can be read from
- readline(n=-1) --> read and return one line from the file. Reads in at mst bytes if specified
- readlines(n=-1) --> read and return a list of lines from the file. reads in at most nbyres/characters if specified
- seek(offset,from=SEEK_SET) --> change the file position to oofset bytes, in reference to from (start, current, end)
- seekable() --> return True if the file stream supports random acces
- tell() --> return the current file location
- truncate(size=None) --> resize the file stream to size bytes. If size is not specified, resize to current location
- writable( ) --> return True if the file stream can be written to
- write(s) --> write string to the file and return the number of characters written
- writelines(lines) --> write a list of lines to the file

#### Python keywords and identifiers

**Keywords** are reserved words in Python 

|        |          |         |          |        |
| :----: | :------: | ------- | -------- | ------ |
| False  |  class   | finally | is       | return |
|  None  | continue | for     | lambda   | try    |
|  True  |   def    | from    | nonlocal | while  |
|  and   |   del    | globaal | not      | with   |
|   as   |   elif   | if      | or       | yield  |
| assert |   else   | import  | pass     |        |
| break  |  except  | in      | raise    |        |

**Identifiers** are the names given to entities, like classes, functions and variables. 

- Identifiers can be a combination of letters in lowercase or uppercase, digits and underscores.
- Identifiers can not start with digits
- You can not use special symbols for identifiers

#### Python tuples

A tuple's elements can't be changed once they have been asgined. This means that **tuples are immutable** Although, a list's elements can be changed.

<u>	Tuples vs Lists</u>

- Tuples are used for heterogeneous datatypes whiles lists are used for homogeneous datatypes
- It is faster to iterate a tuple than a list due to its immutability.
- Tuples can be used as key for a dictionary. Lists can't
- Tuple's data remain write-protected

<u>	Built-in functions with tuples</u>

- all() --> returns True if **all elements** of the tuple are true or if the tuple is empty
- any() --> returns True if **any element** of the tuple is true. If the tuple is empty, returns False
- enumerate() --> return an enumerate object. It contains the index and value for all the items of a tuple as pairs
- len() --> returns the tuple's length
- max() --> returns the largest item in the tuple
- min() --> returns the smallest item in the tuple
- sorted() --> takes elements in the tuple and return a new sorted list
- sum() --> return the sum of all elements in the tuple
- tuple() -->  covert an iterable (list,string,set,dictionary) to a tuple

#### Python sets

A set is an **unordered collection of unique items**. There can't be duplicated items. Different to tuples, set are **mutable**. This means you can add and delete items in a set. Set are usually **used to perform mathematical operations**, like union, intersection, symmetric difference, etc.

​	<u>Python set methods</u>

- add() --> adds an element to a set
- clear() --> removes all elements from a set
- copy() --> returns a shallow copy of a set
- difference() -->  returns the difference of two or more sets as new set
- difference_update() --> remove all elements of another set from this set
- discard() --> remove an element from a set if it is a member. (does nothing if the element is not in set)
- intersection() -->  return the intersection of two sets as a new set
- intersection_update() --> updates the set with the intersection of itself and antooher
- isdisjoint() -->  returns True if two sets have a null intersection
- issubset() -->  returns True if antoher set contains this set
- issuperset() -->  returns True if this set contains another set
- pop() -->  remove and return an arbitrary set element. Raise a KeyError if the set is empty
- remove() -->  removes an element form a set. If the element is not a member, raise a KeyError
- symmetric_difference_update() --> updates a set with symmetric difference of itself and another
- union() --> returns the union of two sets in a new one
- update() -->  updates a set with the union of itsel and others
- all() -->  returns True if all elements of a set are true or if the set is empty
- any() --> returns True if any element of a set is true. If the set is empty, returns False
- enumerate() --> return and enumerate object. It contains the indez and value of all the items of set as a pair
- len() --> returns set's length
- max() --> returns the largest item in a set
- min() --> returns the smallest item in a set
- sorted() -->  returns a new sorted list from elements in the set (doesn't sort the set itself)
- sum() --> returns the sum of all elements in the set
- frozenset --> it makes a set immutable

#### Python different modules

Python modules are Python source files which can expose classes, functions and global variables. When imported from another Python source fies, the file name is treated as a namespace. A Python package is a simply a directory of Python module(s)