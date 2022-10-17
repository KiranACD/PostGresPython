# Python Basics

## Variables in Python

A variable is a name for a value. In python, we define a variable x as
```
x = 15
```
Behind the scenes, python stores the value on the right side of the assignment operator ('=') first. Then that value will be referred as the variable name that you provided, which in this case is x.

An important point to note here is that python has already created and stored certain values before you have even run the code. The numbers range from -5 to 255. Any number outside this range will have to be created by Python and then stored.

Apart from integers, we can create values with floating points.
```
price = 9.99
discount = 0.2
```
Suppose, we want to find the price after applying the discount, then we peform the following operaions.
```
discounted_price = price * (1-discount)
print(discounted_price)
```
Following the rules of mathematics, the expression in the parantheses is evaluated first and then the rest of the expression is evaluated as per the hierarchy of the mathematical operators. Then we call a built-in python function called print to see the discount price. 

When you run the above piece of code, the discounted_price will be printed out in the console.

Another variable type in python is String. Strings are used to store characters like a person's name, email or phone number. Some of them may contain numbers, but they are not used for mathematics, so we store them as strings.
```
name = 'Rolf'
```
As usual, behind the scenes, python creates the string first and then refers to it by the variable name that we have provided. Note that one variable name can only refer to one value of any datatype (int or float or string). If we do,
```
name = 'Bob'
```
then the variable *name* will now refer to 'Bob'. The quotes are used to signal to python that the value should be treated as a string. It is not stored in the value. We can use double quotes ("Bob") or single quotes('Bob'), but do not mix and match.

What do you think will happen when we run
```
print(name*2)
```
The console will print 'BobBob'.

## String Formatting in Python

Here, we will explore somthing called f-string in python.
```
name = 'Bob'
greeting = f'Hello, {name}'
```

By putting f in front of string, we can put variables inside string in the format {variable_name} as seen above. This lets us create strings where we can insert variable values.

However, if we subsequently change the variable *name* to 'Bob', the greeting string does not change.
```
name = 'Bob'
greeting = f'Hello, {name}'
name = 'Rolf'
print(greeting)
``` 
This will still print 'Hello, Bob' in the console. 

We can create a template greeting string where we can pass the name we want when required. We can, hence, reuse the template whenever required. This is how to do it.
````
name = 'Bob'
greeting = 'Hello, {}'
greeting_1 = greeting.format(name)
name = 'Rolf'
greeting_2 = greeting.format(name)
print(greeting_1)
print(greeting_2)
````
Run this code at your end and check what is printed out in the console.

## Getting User Input in Python

Ask the user for their name.
```
name = input('Enter your name: ')
print(name)
```

Here we see another built-in function input(). This function will print the prompt out and then will wait for user to enter a value and press enter. On doing this, the name gets printed onto the console.

The input function always gives the value as string. So if you ask the user to input a value on which you want to perform mathematical operation, you will have the change the datatype of the return value to the required one.

Suppose we want to convert the value to integer datatype, then we run
```
size_input = input('Enter the size of your house (square feet): ')
square_feet = int(size_input)
```
if you want to convert to float datatype, then we run
```
square_feet = float(size_input)
```

## More Formatting

Say we want to convert square feet into square meters and then print it out.
```
size_input = input('Enter the size of your house (square feet): ')
square_feet = int(size_input)
square_meters = square_feet/10.8
print(f'{square_feet} square feet is {square_meters} square meters.')
```
To format floating point number and specify the number of decimal places you want, then
```
print(f'{square_feet} square feet is {square_meters:.2f} square meters.')
```
This will format the floating point number as a value with 2 decimal places only.

## List, Tuples and Sets

List is defined as
```
l = ['Bob', 'Rolf', 'Anne']
```
We can access the first element and the second element of the list by
```
print(l[0], l[1])
```
We can access the last element of the list by
```
print(l[-1])
```
We can change an item in a list by using the position of the item in the list.
Suppose we want to change the first name to 'Mo', then
```
l[0] = 'Mo'
print(l)
```
The above code will print Mo, Rolf, Anne.

We can add elements to the list by using the append function.
```
l.append('Pappu')
```
To remove 'Mo' from the list, we can run
```
l.remove('Mo')
```
If you want to initialize an empty list,
```
new_l = []
new_l_1 = list()
```
We can run either of the above 2 lines to initialize an empty list

Tuple is defined as
```
t = ('Bob', 'Rolf', 'Anne')
```
Tuples are immutable whereas lists are mutable. This means we cannot add or remove values from a tuple, whereas in lists, we can perform these operations.

We can access the first element and the second element of the tuple by
```
print(t[0], t[1])
```
We can access the last element of the tuple by
```
print(t[-1])
```
Attempting to change an item in a tuple will result in an error. We cannot append any value to an existing tuple either. 
```
t.append('Shiva')
```
Run the above code and check the error message. It will throw and 'AttributeError'. We will explore what this means seperately.

We cannot remove items from a tuple either.

Set is defined as
```
s = {'Bob', 'Rolf', 'Anne'}
```
In sets, we can add and remove values as we do in lists. However, we cannot have duplicate values in a set. The order of elements in a set in not maintained.

We can add new elements to a set by
```
s.add('Mogambo')
```

To initialize an empty set
```
new_set = set()
```

There are some unique operations associated with set that are not available for lists or tuples.
```
friends = {'Bob', 'Rolf', 'Anne'}
friends_abroad = {'Bob', 'Anne'}
local_friends = friends.difference(friends_abroad)
```
The difference method applied in this way removes the elements in friends that are also in friends_abroad.

What do you think will happen when we do
```
local_friends = friends_abroad.difference(friends)
```
Lets look at the union operation.
```
local = {'Rolf'}
abroad = {'Bob', 'Anne'}
friends = local.union(abroad)
```
friends set will have {'Rolf', 'Bob', 'Anne'}

Lets look at the intersection operation.
```
art = {'Bob', 'Jen', 'Rolf', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

both = art.intersection(science)
```
both set will have {'Bob', 'Jen'}

## Mutability in Python



## Functions in Python

Functions are things that perform action or calculate outputs based on inputs (or both).

