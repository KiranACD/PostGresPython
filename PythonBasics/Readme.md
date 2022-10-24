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

## Booleans in Python

A boolean is a value that can be either True or False. Using boolean logic, we can tell whether a user's age in above 18, or whether the user has pressed the up arrow in a game.

Some of the applications of boolean

1. Check whether two items are the same or different.
```
print(5 == 5)
```
Two '=' sign used to compare items. The above piece of code prints True in the console.

```
print(5 > 5)
```
The above piece of code prints False in the console.

```
print(10 != 10)
```
The '!=' operator returns True when the two items being compared do not have the same value.

Other comparison operators are
```
>, <, >=, <=
```

It is important to talk about the difference between '==' operator and the 'is' operator.
```
friends = ['Bob', 'Rolf']
abroad = ['Bob', 'Rolf']
print(friends == abroad)
print(friends is abroad)
```
The first print statement return True and the second print statement returns False. This is because the first == operators check whether the variables have the same values, and the 'is' operator checks whether the two variables are pointing to the same location in the memory.

## Conditionals

Suppose we want to take a user input of the current day of the week and check if it is Monday
```
day_of_week = input('What day of the wek is it today?')
if day_of_week == 'Monday':
    print('Have a great start to your week')
else:
    print('Full speed ahead')
print('This always runs')
```
The above piece of code shows how to run an if/else conditional statement.

What if we want output a message if the day of the week is also Tuesday?
```
if day_of_week == 'Monday':
    print('Have a great start to your week!)
elif day_of_week == 'Tueday':
    print('Today is Tuesday!)
else:
    print('Full speed ahead')
```
As you can see, elif and else statements are optional and can be used whenever you want additional branches to your if statement. The above piece of code is dependent on the format of the user input. If the user enters 'monday', then the desired block of code will not run.

Can we standardize the format of the days of the week? Yes, we convert the string input to lower case and the checks into lower case too.
```
day_of_week = input('What day of the wek is it today?')
day_of_week = day_of_week.lower()
if day_of_week == 'monday':
    print('Have a great start to your week!)
elif day_of_week == 'tueday':
    print('Today is Tuesday!)
else:
    print('Full speed ahead')
```
This ensures the program will work for any format of user input.

## Membership

The 'in' keyword is used to check for membership. This means we check if a thing is inside a list, tuple or set. 
```
friends = ['Rolf', 'Bob', 'Jen']
print('Jen' in friends)
```
When we run this, True is printed on to the console. This means we can use the the 'in' keyword with if/elif statements as well as they evaluate the boolean result of the statement.
```
oscar_nominees = {'THE MATRIX', 'GREEN BOOK', 'HER'}
user_movie = input('Enter a movie you watched recently: ').upper()
if user_movie in oscar_nominees:
    print(f'{user_movie} was nominated for Oscars.')
else:
    print(f'{user_movie} was not nominated for Oscars.')
```

The 'in' key word works for all sequence data types. This means we can check if a substring is part of a string using the 'in' key word.
```
main_string = 'xyz@gmail.com'
sub_string = 'gmail'
print(sub_string in main_string')
```
This will print True in the console.

## Loops in Python

### While Loops

Lets play a magic number game. We will assign a number as the magic number and then we will ask the user to guess the magic number.
```
magic_number = 7
user_input = input('Would you like to play? (Y/n) ')

while user_input != 'n':
    choice = int(input('Enter your guess: '))
    if choice == magic_number:
        print(f'You guessed the magic number {magic_number}.')
    elif abs(choice - magic_number) == 1:
        print('You were off by 1. Guess again!')
    else:
        print(f'{choice} is not the magic number. Try again!')

    user_input = input('Would you like to play? (Y/n) ')

print('Bye!')
```
We assign 7 as the magic number. Then we ask the user if they want to play. If the user enters 'n' as the input, then the while loop will not run. 

The while statement will evaluate to False and we will exit the program. If the user enters any other character, then the while statement will evaluate to True and the code inside the while block will run. We ask the user to enter their guess. 

We check if the choice is the magic number in the first if statement. If true, we print the magic number. In the next elif statement, we check if the absolute value of the difference between the choice and the magic number is equal to 1. If it is, we print 'you were off by one'. If none of the if statements evaluate to True, the code inside the else block will run, which just prints that the guess is not the magic number. 

Then, we ask the user if they want to play again? The while loop block will run again if the user enters any value other than 'n'.

The user can play as many times as they want.

There is a better way to approach the code while maintaining the same functionality.
```
magic_number = 7

while True:
    user_input = input('Would you like to play? (Y/n) ')
    if user_input == 'n':
        break

    choice = int(input('Enter your guess (1-10): '))
    if choice == magic_number:
        print(f'You guessed the magic number {magic_number}.')
    elif abs(choice - magic_number) == 1:
        print('You were off by 1. Guess again!')
    else:
        print(f'{choice} is not the magic number. Try again!')

print('Bye!')
```
We change the while statement to just True. This will result in an infinite loop as the while statement will always evaluate to True, because the statement is True.

Then we ask the user if they want to play. If they enter 'n', then the *break* key word is used to break the infinite loop.

Another change we can make is change the magic number when the user makes a correct guess. This is incase the user wants to play again.
```
magic_number = 7

while True:
    user_input = input('Would you like to play? (Y/n) ')
    if user_input == 'n':
        break

    choice = int(input('Enter your guess (1-10): '))
    if choice == magic_number:
        print(f'You guessed the magic number {magic_number}.')
        magic_number = random.randint(1, 10)
    elif abs(choice - magic_number) == 1:
        print('You were off by 1. Guess again!')
    else:
        print(f'{choice} is not the magic number. Try again!')

print('Bye!')
```
All we need to do is change the magic number in the first if block where we check if the guess is the magic number. We use a built-in library called random to generate a random number between 1 and 10. We will learn more about the random library seperately.

This way if the user wants to play again after making a correct guess, they can do so without having to guess the same number again.

### For loops in Python

Suppose you want to print out the names of all your friends in a list. How would you do this without using a for loop?
```
friends = ['Rolf', 'Jen', 'Bob', 'Anne']
print(f'{friends[0]} is my friend.')
print(f'{friends[1]} is my friend.')
print(f'{friends[2]} is my friend.')
print(f'{friends[3]} is my friend.')
```
As you can see, doing this is okay when you have only 4 friends, but it would be ugly if you have 50 friends. This is where for loops come in handy.

```
friends = ['Rolf', 'Jen', 'Bob', 'Anne']

for friend in friends: 
    print(f'{friend} is my friend.')
```
This produces the exact result as the previous block of code.

Another way to do this is to use the built-in function range() along with the for loop. If you run,
```
range(4)
```
it will generate 4 numbers from 0 to 3. You can put these numbers in a list by running
```
numbers = list(range(4))
```
So, how do you use this with for loop?
```
friends = ['Rolf', 'Jen', 'Bob', 'Anne']

for number in range(4): 
    print(f'friends[number] is my friend.')
```
The variable number takes values 0 to 3 in each iteration. When you run friends[0], then we get the first element of the list as we have seen earlier. As we iterate over the range, we access each item in friends list by passing the number variable as the subscript of the friends variable.

Lets look at another use case of for loops.
```
grades = [35, 67, 98, 100, 100]
total = 0
number_of_grades = len(grades)
```
*len()* is a built-in python function that we can use to find the length of a list.
```
grades = [35, 67, 98, 100, 100]
total = 0
number_of_grades = len(grades)

for grade in grades:
    total += grade

print('average = ', total/number_of_grades)
```
The expression *total += grade* is the same as running *total = total + grade*. 

We added up the grade one by one and at each iteration, we stored the total in the variable called *total*. To calculate the average, we divided total by the number of grades and hence we get our answer.

Python provides us a built-in function *sum()* to calculate the sum of all items in a list.
```
grades = [35, 67, 98, 100, 100]
number_of_grades = len(grades)
total = sum(grades)
print('average = ', total/number_of_grades)
```

## List Comprehensions in Python

List comprehensions allow us to create new lists on the fly from existing lists.
```
numbers = [1, 3, 5]
doubled = []

for num in numbers:
    doubled.append(num*2)
```
In order to get a new list doubled, in which each item is double the corresponding item in the list numbers, the above code is one way to approach it.

Using list comprehension,
```
numbers = [1, 3, 5]
doubled = [num*2 for num in numbers]
```
This does the same thing as the previous code block, but in a succint way.

We can use if/else statement in list comprehension.
Suppose we have a friends list and we want to add names that start with 'S' to a new list.
```
friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
friends_name_starts_s = []

for name in friend:
    if name.startswith('S'):
        friends_name_starts_s.append(name)

print(friends_name_starts_s)
```
We can do this with list comprehension too.
```
friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
friends_name_starts_s = [name for name in friends if name.startswith('S')]
print(friends_name_starts_s)
```
See how neat the code becomes.

## Hash Maps in Python

Hash maps in Python are called dictionary.
Dictionaries are used to create key-value pairs. So, if you know keys, then you can get their values quickly. 
```
friends_ages = {'Rolf':24}
```
The item to the left of the colon is the key and to the right of the colon is the value. Keys can be strings or integers or any other hashable type. We will get to hashable type seperately.

If you want multiple key, value pairs
```
friends_ages = {'Rolf':24, 'Adam':30, 'Anne':27}
print(friends_ages['Anne'])
```
To add a new key value pair
```
friends_ages['Saurabh'] = 25
```

We can iterate over all items in a dictionary
```
student_attendance = {'Rolf':96, 'Bob':80, 'Anne':100}
for student in student_attendance:
    print(f'{student}: {student_attendance[student]}')
```
This will print out each item in the dictionary.
```
student_attendance = {'Rolf':96, 'Bob':80, 'Anne':100}
for student, attendance in student_attendance.items():
    print(f'{student}: {attendance}')
```
This will produce the same result as the previous code block.

We can also check membership of a key in a dictionary
```
student_attendance = {'Rolf':96, 'Bob':80, 'Anne':100}
if 'Bob' in student_attendance:
    print(f'Bob: {student_attendance['Bob']}')
else:
    print('Bob is not a student in this class')
```

To get the keys and values in seperate lists
```
student_attendance = {'Rolf':96, 'Bob':80, 'Anne':100}

student_attendance_keys = student_attendance.keys()
student_attendance_values = student_attendance.values()
```

## Unpacking Variables in Python

Earlier, we had seen the way to initialize a tuple
```
t = (1, 2)
```
However, to declare a tuple, we do not need to use the brackets
```
t = 1, 2
```
We need to use brackets only where we want python to explicity treat the values as part of a tuple
```
l = [(1, 2)]
```
In this case, if you do not add the brackets, python will just give us a list of two seperate values 1 and 2 instead of a list with a singe tuple (1, 2) like we wanted.

We can run
```
t = 1, 2
x, y = t
```
Here the values in the tuple gets unpacked into the two variables x and y.

So when we do
```
student_attendance = {'Rolf':96, 'Bob':80, 'Anne':100}
for student, attendance in student_attendance.items():
    print(f'{student}: {attendance}')
```
*student_attendance.items()* returns a list of tuples containing (key, value) and then we are iterating over each tuple and unpacking the items in the tuple to student and attendance.

If we want to ignore an item in a tuple while unpacking, we can assign it to a variable _. This is the standard followed in the python communnity.
```
persons = ('Bob', 24, 'Mechanic')
name, _, profession = persons
print('Name: ', name, ' profession: ', profession)
```
In the code block above, we did not want to use age, so we assign it to the variable _ and will not use it again.

Suppose we have a list and we want to unpack it in such a way that we assign the first item of the list in one variable and the rest of the items in a seperate list
```
l = [1, 2, 3, 4, 5]
first, *last = l
```
Say we want to do the opposite and get the last item of a list in a variable
```
l = [1, 2, 3, 4, 5]
*first, last = l
```

## Functions in Python

We have seen some built-in functions like print(), len() etc. Now, let us define our own function. The pros of creating our own functions and giving them a name is that we can resuse the block of code within that function as many times as we want.
```
def hello():
    print('Hello')
```
Python treats the hello() function as a callable variable. When we define a function, the code block inside the function does not run. The code block runs only when we call the function 
```
hello()
```
Running the above line prints 'Hello' in the console.

As we have seen with the if statements, while and for loops, python knows which code block to run because of the indentation. 

Lets look at a more elaborate function.
```
def user_age_in_seconds():
    age = int(input('Enter your age: '))
    age_in_seconds = age * 365 * 24 * 60 * 60
    print(f'Your age in second: {age_in_seconds}.')
```
Inorder to run the above code, we have to call the function
```
user_age_in_seconds()
```

An important point to remember while naming functions is to not use the name of a python built-in function. Doing this will override the built-in function and its behaviour will change. If we call the built-in function at a later point, the code block defined by us will execute rather than the built-in code block.
```
def print(s):
    x = 2
    y = 2
    return x+y
```
When we call the print() function elsewhere within the same program, it will always return 4.

We can send data to functions by defining functions with parameters.
```
def add(x, y):
    return x+y
```
We have placed the parameters inside the brackets in the above format. When you call the function, the two variables are created in local function namespace. These variables can then be used inside the function body.
```
add(5, 3)
```
When we call the function, we pass the arguments to the function and these arguments are assigned to the respective variables.

If we define a function without parameters and try to pass it arguments when calling it, python will throw an error
```
def say_hello():
    print('hello')
say_hello('Bob')
```
Similarly, if we define a function with parameters, then when calling the function, we have to pass the required number of arguments, else, python will throw an error.
```
def say_hello(name):
    print('hello, {name}')
say_hello()
```

All the paramters that we have been using till now are all positional parameters. This means the position in which they are defined will determine the argument that is assigned to it.
```
def say_hello(name, surname):
    print(f'hello, {name} {surname}')
```
When we call the function
```
say_hello('Bob', 'Smith')
```
'Bob' is assigned to name and 'Smith' is assigned to surname as that is the order in which these arguments are passed. This is because Python has no other way to determine how arguments are assigned to parameters.

If we assign the arguments to the parameters at the time of function call, then the order in which we pass them will not matter.
```
say_hello(surname='Smith', name='Bob')
```

A positional argument cannot follow a keyword argument. So we cannot call
```
say_hello(name='Bob', 'Smith')
```
Positional arguments have to go first and keyword arguments later.

We can assign default parameter values while defining functions
```
def add(x, y=8):
    print(x + y)
```
Now we can call
```
add(5)
```
Here, x will take the argument 5 and y will take the default parameter value and this will print 13 in the console. Note that if you do not want to use the default value, we can call
```
add(5, 3)
```
This will print 8 in the console. x takes the value 5 and y takes the value 3.

When we define a function, a positional parameter cannot follow a parameter with default value.
```
def add(x = 5, y):
    print(x+y)
```
Python will throw an error here.

When using default parameter values, the parameter is assigned the defalt value at the time of creation.
```
default_y = 3
def add(x, y=default_y):
    print(x+y)
```
At this point y has already been assigned the value 3. 
If we then do
```
default_y = 5
add(5)
```
This will print 8 in the console and not 10, because changing the value of default_y will not change the default value assigned to the paramter y.

We can have functions return values
```
def add(x, y):
    print(x+y)
```
If we call the function
```
result = add(5,5)
print(result)
```
This will first print 10 in the console followed by None. None is a special value in a python that means no value or undeclared value. As we have not specified a return statement in the add function definition, it return None by default.

```
def add(x,y):
    return (x+y)
```
Calling the function now
```
result = add(5, 5)
print(result)
```
Now the function itself will not print 10. It will calculate the result of addition and return it and this return value is assigned to the result variable. Then python prints 10 in the console when it runs the last line of the code block.

## Lambda functions in Python

Lambda functions are used to operate on inputs and return outputs. They are not used to perform actions.
```
add = lambda x, y: x+y
add(5, 5)
```
Here, x and y are parameters. You dont need to specify the return keyword as lambdas by default return the result of the operations. The function reference is stored in the add variable.

There are 4 parts to a lambda function. There is lambda keyword, parameter list, colon and the return value.

Lets look at an example we saw earlier.
```
def double(x):
    return x*2
sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
```
We get a new list called doubled that has double each value in the sequence list. We can perform the same operation this way
```
def double(x):
    return x*2
doubled = map(double, sequence)
```
This produces the same result as the previous block of code. The map is a built-in function in python and it returns a map object. We will talk about this seperately. The important point is doubled is not quite a list yet. To make it a list we have to run
```
doubled = list(doubled)
```

Lets do the same thing using a lambda function.
```
sequence = [1, 3, 5, 9]
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x*2, sequence))
```

## Unpacking arguments

Lets create a multiply function that takes in any number of arguments
```
def multiply(*args):
    print(args)
```
When we call
```
multiply(1, 3, 5)
```
It will print (1, 3, 5) in the console. As we have seen in unpacking variables earlier, when we put *args as the parameter and we pass multiple arguments, they get collected into a tuple.

So now we can formally define a multiply function.
```
def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product
```
When we call
```
print(multiply(1, 3, 5))
```
15 is printed to the console.

We can do this vice-versa as well
```
def add(x, y):
    return x + y
nums = [1, 4]
print(add(*nums))
```
We are destructuring the list into its individual items and then assigning these items to the function parameters respectively. Note that the number of parameters should be equal to the number of items in the list.

Lets create a mini calculator that supports addition and multiplication
```
def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        print('Invalid operator')
        return None
```
There are a few things going on here. 

First, the parameters will take any number of positional arguments followed by a named argument. This means when calling apply function, the operator keyword has to be specified, otherwise python will throw and error.
```
apply(1, 3, 5, operator='+')
```
This is because all the parameters after a *args parameter should be either named parameters or keyword parameters.

Second, we have to unpack the args tuple when passing it as argument when calling the multiply function. If we dont unpack the tuple to its individual items, the args parameter in the multiply function gets assigned a tuple of tuples with one tuple in it. It then iterates over the tuple of tuples and multiplies the one tuple with the product, which is 1, and returns the tuple.

## Unpacking keyword arguments

A function that takes in any number of keyword arguments
```
def named(**kwargs):
    print(kwargs)

print(named(name='Bob', age=25)
```
This will print
```
{'name':'Bob', 'age':25}
```

We can unpack a dictionary and pass it as keyword arguments.
```
def add(x, y):
    return x+y
nums = {'x':15, 'y':25}
print(add(**nums))
```
This works because the parameter variable names are the same as the key names in the dictionary.

We can do it this way as well
```
def add(**kwargs):
    return kwargs['x']+kwargs['y']
nums = {'x':15, 'y':25}
print(add(**nums))
```
This will also print 40 to the console.

```
def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')
```
We call print_nicely function by passing 2 keyword arguments.
```
print_nicely(name='Bob', 'age':25)
```
These keyword arguments are collected in the kwargs parameter in the print_nicely function as a dictionary. 

This dictionary is then unpacked and the sent as arguments to the named function where these named arguments are again collected as a dictionary by the kwargs parameter of the named function and printed out as a dictionary.

Then we iterate over the kwargs dictionary of the print_nicely function and then print the key and its corresponding value. 

We can combine *args and **kwargs in a function as its parameters. All the positional arguments will be collected by the *args parameter in the form of a tuple and the keyword arguments will be collected by the **kwargs parameter in the form of a dictionary.

```
def both(*args, **kwargs):
    print(args)
    print(kwargs)
```
Then when we call
```
both(1, 3, 5, name='Bob', age=25)
```
This will print out 
```
(1, 3, 5)
{'name':'Bob', 'age'=25}
```
in the console.

## Dictionary Comprehensions in Python

A dictionary comprehension is like a list comprehension, where we get a dictionary at the end of it. So we have to provide key-value mappings.
```
users = [
    (0, 'Bob', 'password'),
    (1, 'Rolf', 'bob123'),
    (2, 'Jose', 'long4password'),
    (3, 'username', '1234')
]
username_mapping = {user[1]: user for user in users}
```
This creates a dictionary in this format
```
{
    'Bob': (0, 'Bob', 'password'),
    'Rolf': (0, 'Rolf', 'bob123'),
    'Jose': (0, 'Jose', 'long4password'),
    'username': (0, 'username', '1234')
}
```
Now accessing a user's details will be easy if you know their username. Say we ask a user to input their username and password, then we can perform the following operation easily, now that we have this mapping.
```
username_input = input('Enter your username: ')
password_input = input('Enter your password: ')

_, username, password = username_mapping[username_input]
if password_input == password:
    print('Logged in')
else:
    print('Password does not match!')
```

## Local and Global Scope in Python

Consider this block of code
```
friends = ['Rolf', 'Bob']
def add_friend():
    friend_name = input('Enter friend's name: ')
    friends = friends + [friend_name]
```
When we call the function add_friend(), python creates a variable in local function namespace called friends which is entirely different from the friends list defined outside the function or in the global namespace. Hence calling the function will throw an error.
```
UnboundLocalError: local variable 'friends' referenced before assignment
```
This means that python first adds the variable friends into the local namespace, then tries to access the value that it references. However, we have not assigned it any value and hence python is unable to find any value to perform the add operation.

## Nested Data Structures

We can have a list of dictionaries
```
friends = [
    {'name':'Rolf', 'age':24},
    {'name':'Adam', 'age':30},
    {'name':'Anne', 'age':27}
]
print(friends[0]['name'])
```
The above code block will print 'Rolf' in the console.

## Mutability in Python

Given 2 lists
```
a = [1, 2, 3]
b = a
```
a and b are references to the same list.

If you create 2 lists
```
a = [1, 2, 3]
b = [3, 4, 5]
```
a and b point to different lists store in seperate memory location.

We can change/mutate a list after creating it. This means lists are mutable.

Some values cannot be changed. They are called immutable. For example, tuples are immutable. Tuples cannot be modified.

Now consider 2 integers.
```
a = 8585
b = 8585
```
In this case, a and b point to the same memory location. Integers are also immutable. You cannot change them. So when you do
```
a = 8586
```
a starts pointing to a new object that contain 8586.

Like integers, strings, floats and boolean are also immutable.

To create an immutable class/object, do not add any methods in the class that can change the object's attributes.

```
a = 'hello'
b = a
```
if we do
```
a += ' world.'
```
b will still be pointing to 'hello' while a will be pointing to 'hello world'.

It is a bad idea to create mutable default parameters. Let us look at an example.
```
class Student:
    def __init__(self, name: str, grades: List(int) = []):
        self.name = name
        self.grades = grades
    def take_exam(self, result: int):
        self.grades.append(result)
```
In this case, suppose we create 2 objects.
```
bob = Student('Bob')
rolf = Student('Rolf')
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
```
Both bob and rolf's grades list will be [90]. How did this happend? Because Python assigns default values to parameter at time of definition.
So in both objects the grades list is pointing to the same default value. Hence any change in the grades list in bob object or rolf object will result in change in the other objects grades list.

The solution is to not have mutable values as the default.
```
from typing import List, Optional
class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []
    def take_exam(self, result: int):
        self.grades.append(result)
```

Now this works,
```
bob = Student('Bob')
rolf = Student('Rolf')
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
```

## Object-Oriented Programming in Python

The purpose of object-oriented programming is to make a developer's life simpler. It allows us to develop entities that look like what we would work with in the real world.

Consider a dictionary
```
student = {'name':'Rolf', 'grades':(89, 90, 93, 78, 90)}
```
This is not a student itself, but contains data about students. Suppose we want to get Rolf's average grade.
```
def average(sequence):
    return sum(sequence)/len(sequence)

print(average(student['grades']))
```

Imagine if you could have a kind of variable called Rolf, that contained all the relevant information about Rolf and we could just call 
```
Rolf.average()
```
to get his average grade. Its like asking his average grade to Rolf directly. This looks so much better than
```
average(student['grades'])
```

Let us look at the way we initialize class in python.
```
class Student:
    def __init__(self):
        self.name = 'Rolf'
        self.grades = (90, 90, 93, 78, 90)
```
We define a class using the *class* keyword and we give the class a name. Developers in Python follow the camel case convention when naming their classes. This means the first letter of each word in the name in capitalized and consecutive words are not seperated by underscore.

Then, there is a function __init__() in which we have to provide a parameter called self. This parameter can be given any name, but by convention, we name it self. The parameter self is assigned the current instance of the class. It is through this variable that we access the attributes and methods of the current instance inside the class. The __init__() function is used by python to initialize attributes or run methods upon the creation of an object of the class.

In order to make an object of the class
```
student = Student()
```
When we run this line, and object of the class is created by Python and the __init__() function is called to initialize the attributes we want to create and initialize. Then the reference to the object is stored in the variable student.

To access attributes of the object
```
print(student.name)
print(student.grades)
```

We can define functions within a class. These are called methods.

```
class Student:
    def __init__(self):
        self.name = 'Rolf'
        self.grades = (90, 90, 93, 78, 90)
    
    def average_grade(self):
        return sum(self.grades)/len(self.grades)
```
As you can see we need to specify a parameter, called self, in the function average_grade(), that will take the current instance of the class. It is through this instance that we access the attributes and methods of the object. 

How do we access this new method?
```
student = Student()
student.average_grade()
```
This is the same syntax as when we need to access the attributes. When we run it like this, it is the same as running
```
Student.average_grade(student)
```
In fact, Python does this in the background when we run student.average_grade().

The __init__() method can take other parameters that will take arguments that we pass when we create an object of the class. Let us make the Student class generic, so that we can use it for any number of students and their grades
```
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average_grade(self):
        return sum(self.grades)/len(self.grades)
```
Now we can create and instance of Rolf using the Student class that we defined above.
```
student_rolf = Student('Rolf', (90, 90, 93, 78, 90))
```
And we can calculate Rolf's grade average by running
```
student_rolf.average_grade()
```

## Magic methods in Python

The __init__() is an example of a magic method in Python. Python calls these methods in the background when you do certain things. In the case of the init method, python call this method when you create an object of the class even if you did not specifically call the __init__() method.

There are other magic methods in Python. Suppose we want to print the representation of an object of a class. Consider this class
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
Lets create an object of the class Person and print it out.
```
person = Person('Bob', 21)
print(person)
```
At this point, Python will print in the console, something that looks like '<__main__.Person object at 0106h9be88>'. This is the default representation of the person object currently.

Python allows us to redefine the represenation of an object to a format we specify. This will be useful when we want to print out an object for users to view it in a readable format.

The way to do this is to override a magic method in our class itself.
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'Name: ' + self.name + ', age: ' + str(self.age)
```
When we run
```
person = Person('Bob', 21)
print(person)
```
Then Python will call the magic method that we have specified and print the following in the console.
```
Name: Bob, age: 21
```

Another way to do this is to use the __repr__() method
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'<Person({self.name}, {self.age})>'
```
If the __str__() method is also specified, then when printing the object, Python will use the __str__() method as it is higher in the hierarchy.


## Static Method and Class Method

Lets define a class
```
class ClassTest:
    def instance_method(self):
        print(f'Called instance_method of {self}')
    
    @classmethod
    def class_method(cls):
        print(f'Called class_method of {cls}')
```

All functions in a class that use the instance parameter are call instance methods. These methods are usually accessed through the instance variable as we saw earlier.

Class methods are defined like a regular method, except we specify a parameter cls in the function definition. Class methods are accessed using the class name itself.
```
ClassTest.class_method()
```
When we run the above line, in the background, Python calls the method this way. 
```
ClassTest.class_method(ClassTest)
```

To classify a method as a class method, we have include @classmethod above the def func_name() line. We study this seperately.

Static methods are defined like a regular method, we do not need to specify any parameter in the function definition unlike the class method and instance methods.
```
class ClassTest:
    def instance_method(self):
        print(f'Called instance_method of {self}')
    
    @classmethod
    def class_method(cls):
        print(f'Called class_method of {cls}')
    
    @staticmethod
    def static_method():
        print('Called static_method')

```
We can call a static method by running
```
ClassTest.static_method()
```

If we want a method in the class that does not need to use the instance or class, we can decorate it with @staticmethod.
If we want a method in the class that uses the class itself for something, we can decorate it with @classmethod and specify a parameter that will take the class.
If we want a method in the class that uses the instance, we do not need to decorate it with anything, but we need specify a parameter that will take the instance that we are dealing with currently.

Instance methods are used when we need to produce an action that uses data within the instance. If we want to change the data within any instance, then too, we need to use the instance method.

Class methods are often used a factories.

Static methods are used to just place a method inside a class because as a developer you feel the method belongs inside the class.

Lets look at how class methods are used as factories.
```
class Book:
    TYPES = ('hardcover', 'paperback')
```
To access the class attribute TYPES we run
```
Book.TYPES
```
Then we include the __init__() and other attrributes
```
class Book:
    TYPES = ('hardcover', 'paperback')
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    def __repr__(self):
        return f'<Book({self.name}, {self.book_type}, {self.weight})>'
```
If you want to avoid passing a book_type and if you want to restrict the book type to one of two book types specified in the TYPES tuple, then we can structure the code like this

```
class Book:
    TYPES = ('hardcover', 'paperback')
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    def __repr__(self):
        return f'<Book({self.name}, {self.book_type}, {self.weight})>'
    
    @classmethod
    def hardcover(cls, name, weight):
        return Book(name, Book.TYPES[0], weight)
    
    @classmethod
    def paperback(cls, name, weight):
        return Book(name, Book.TYPES[1], weight)
```
Now, when we want to create an object, we can directly call the classmethod
```
book = Book.hardcover('Harry Potter', 1500)
```
Notice we are not using cls anywhere in the two class methods. In this case, Book is the cls. So, instead of cls, we should use cls.

```
class Book:
    TYPES = ('hardcover', 'paperback')
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    def __repr__(self):
        return f'<Book({self.name}, {self.book_type}, {self.weight})>'
    
    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight)
    
    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)
```

## Inheritance in Python

Inheritance allows one class to take methods and attributes of another class.
```
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f'Device {self.name!r} ({self.connected_by})'
    
    def disconnect(self):
        self.connected = False
        print('Disconnected')
```
The !r at the end of self.name is to call the repr method of the attribute self.name. The quotes appear around the name without us having to put the quotes there.

Consider we make a printer object
```
printer = Device('printer', 'USB')
print(printer)
printer.disconnect()
```
That looks good.

Lets say we want to add a functionality to this class that prints out a document. However, we cannot add it to the Device class as it can be used to create an object of any device that can connect to a computer like webcam, usb drive etc. Inheritance helps with this.
```
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
        self.capacity = capacity
```
We have created a new class Printer which inherits from the Device class. This way we can use the attributes and methods of the Device class in the Printer class. The Device class is the parent class and the Printer class is the child class.

We do not need to initialize the name, connected_by, connected attributes in the Printer __init__() method when this is already being done in the Device class. 
```
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages} pages remaining)'
    def print(self, pages):
        if not self.connected:
            print('Printer is not connected')
            return
        print(f'Printing {pages} pages.')
        self.remaining_pages -= pages
```
Now we can instantiate a printer object
```
printer = Printer('Printer', 'USB', 500)
printer.print(50)
print(printer)
```
The first line instantiates a new printer object. It initializes the attributes in the parent class as well. The second line prints 50 pages and reduced the remaining_pages attribute accordingly. The third line prints out our representation of the printer object
```
Device 'Printer' (USB) (450 pages remaining)
```
What happens when we want to run
```
printer.disconnect()
```
Python will look for the disconnect method in the Printer class. Upon not finding there, it will look for the method in the Device class. There it will find the method and then it will run the code inside the disconnect() method.

## Class Composition in Python

There are cases where composition makes more sense than inheritance. Consider a bookshelf which is composed of many books. We could create a bookshelf class as a parent class and then create book class as child class where the book class inherits from bookshelf class. However, this does not make much sense as inheritance is usually used when the child shares certain attributes of the parent and has a few other attributes of their own. Hence inheritance does not apply in this case as a book does not share any attribute with bookshelf.

However, a bookshelf is composed of many books. So we could write our class such that this property is reflected.
```
class Bookshelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f'Bookshelf with {len(self.books)} books'

class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'Book({self.name})'
```
Then we can create a few book objects and then instantiate a bookshelf class with many books in it.
```
book1 = Book('Harry Potter')
book2 = Book('Fluent Python')
shelf = Bookshelf(book1, book2)
print(shelf)
```
This will print out 
```
Bookshelf with 2 books
```
in the console.

## Type Hinting in Python

```
def list_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)
```
Here we are telling python that the sequence expected here is a list and the return type will be a float.
```
from typing import List
class Book:
    pass
class BookShelf:
    def __init__(self, books: List(Book)):
        self.books = books
```
Lets look at a more elaborate example.
```
class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self) -> str:
        return f'<Book({self.name}, {self.book_type}, {self.weight})>'
    
    @classmethod
    def hardcover(cls, name: str, weight: int) -> 'Book':
        return cls(name, cls.TYPES[0], weight)
    
    @classmethod
    def softcopy(cls, name: str, weight: int) -> 'Book':
        return cls(name, cls.TYPES[1], weight)
```
The return type of the class methods is the class itself. When the return type is the class itself, we have to write the return type in quotes. If the return type is any other class, we do not have to put the class name in quotes.

## Importing in Python

Importing is used when you want to get code fro other python files into your current file.
Consider a folder called Import_in_python with 2 files in it called code.py and mymodule.py.
```
Import_in_python
    |
    |----code.py
    |----mymodule.py
```
In mymodule.py, we will write the following code.
```
def divide(divdend, divisor):
    return dividend / divisor

print('mymodule.py: ', __name__)
```
__name__ is a global variable in python and it stores the name of the file. If we run mymodule.py, then the following is printed in the console.
```
mymodule.py: __main__
```
This means the __name__ variable takes the value '__main__' when it is in the file that is run.

Now, in code.py, we will write the following code
```
from mymodule import divide
```
This is how to import a specific thing from mymodule.py. In this case we are importing the function divide.

Alternately, if we want to import the entire file, then we write the following code
```
import mymodule
```
To access the divide function we run
```
import mymodule
mymodule.divide(10, 5)
```
Let us continue with the former style
```
from mymodule import divide
print(divide(10, 5))
```
When we run this file, the following gets printed in the console.
```
mymodule.py: mymodule
2.0
```
The __name__ variable now takes the path of the file, which, in this case, is mymodule. 

Where does python look for the files and code that we ask it to import? The sys module helps us answer this question.
```
import sys

print(sys.path)
```
This will print out a list of paths that python will look at to find the file that we are asking it to import. When Python does not find the file we asking it to import, Python will throw us an error
```
ModuleNotFoundError: No module named '<modulename>'
```
The first path in the sys.path list will always be the path from which the code ran. 

We can also import a file inside another folder that is in the same folder level.

```
Import_in_python
    |
    |----libs
    |      |
           |----__init__.py 
    |      |----mylib.py 
    |
    |----code.py
    |----mymodule.py
```

Now, in code.py, if we want to import mylib, then we run
```
import libs.mylib
```
Note that, in some older versions of python, we have to include a __init__.py file in the libs folder. The file does not need to contain any code, even an empty file will do.

To see all the imported modules, we can run
```
import sys
print(sys.modules)
```
When Python imports a module, it runs through the entire module executing all the code inside the module. It then stores the module in sys.modules so that it can be used when required later.


## Relative Imports in Python

Let us take the same file structure we had earlier.

```
Import_in_python
    |
    |----libs
    |      |
           |----__init__.py 
    |      |----mylib.py 
    |
    |----code.py
    |----mymodule.py
```

We will add a new folder in the libs folder called operations which will have file called operator.py

```
Import_in_python
    |
    |----libs
    |      |
    |      |----operations
    |      |        |
    |      |        |----__init__.py
    |      |        |----operator.py
    |      | 
    |      |----__init__.py 
    |      |----mylib.py 
    |
    |----code.py
    |----mymodule.py
```

Lets review the code in each file.

In code.py, we have
```
from mymodule import divide

print('code.py:', __name__)
print(divide(10, 5))
```
When we run this, it will see the import statement and it will immediately move to executing the code inside mymodule.py

In mymodule.py, we have
```
import libs.mylib

def divide(dividend, divisor):
    return dividend / divisor

print('mylib:', __name__)
```
When this starts executing, python will pause at the first line and move to executing mylib.py

In mylib.py, we have 
```
import libs.operations.operator

print('mylib.py:', __name__)
```
When this starts executing, python will pause at the first line and mov to executing operator.py.

In operator.py, we have
```
print('operator.py:', __name__)
```
When this executes, it will print 'operator.py: libs.operators.operator' in the console. Then it will continue from the first line in mylib.py, where it had paused earlier, and will print 'mylib.py: libs.mylib'. Then python will resume from the first line in mymodule.py where it had paused and will print 'mymodule.py: mymodule'. Then we will get back to the file we ran first. Python will then print 'mycode.py: __main__' and then 2.0 which is the result of the divide function we called in code.py.

Let us look at the output
```
operator.py: libs.operations.operator
mylib.py: libs.mylib
mymodule.py: mymodule
mycode.py: __main__
2.0
```
Note that we have not used relative imports yet. These are all absolute imports as we have specified the path in full for each import.

In the output, we see some names seperated by the '.' and some names not seperated by '.'. The right most names with respect to the '.' is the filename. The names to the left of the '.' are folder names. We can do relative imports with files that have folder names. We cannot do relative imports with names that have only filenames. 

To do a relative import, we have to use the following
```
from .mymodule import divide
```

The single '.' refers to the current folder. So the above statement means, from the current folder, look at the mymodule file and import the divide function. Given that this line is in the mycode.py file, this makes sense because the mymodule.py file is located in the same folder as the mycode.py file.

However, this gives an error. Python actually tries to look for a module name '__main__.mymodule'. This is because the name of this file, as seen in the __name__ variable, is '__main__'.
There is no module called mymodule in __main__.

Similarly if we run the following in mymodule.py
```
from .libs import mylib
```
Python will still throw an error, because it searches for a folder, but there is no folder in the __name__ variable in this file. The __name__ variable has the value 'mymodule' and this value does not have a folder in it. 

Lets see what happens when we run this in mylib.py
```
from .operations import operator
```
The __name__ variable in this file has the value 'libs.mylib'. Python removes the filename and then appends operations to libs folder. So we get libs.operations and Python finds this path in its path list and hence is able to access the operator.py module. 

Note that this works only if we run the code.py file. If we run the mylib.py file, then the __name__ variable takes the value .__main__ and hence Python will throw an error because it cannot find __main__.operations.

Lets see what happends when we run the following in operator.py file
```
from ..mylib import *
```
In this case the __name__ variabe in operator.py takes the value libs.operations.operator. When Python seen '..' in the import statement, then it removes the operator and operaations part from the the __name__ value and attached mylib to it. So Python finds libs.mylib in the path and hence Python is able to import the desired code.

## Errors in Python

Let us look at the divide function that we explored earlier.
```
def divide(dividend, divisor):
    if divisor == 0:
        print('Cannot divide by 0')
        return
    return dividend/divisor
```
If we run the following, no error will be thrown. There will be a print statement by the program and it continues as it is.

```
divide(10, 0)
```

Consider a case that will use the divide function above. We have a list of grades and we want the average of all grades.
```
grades = []
average = divide(sum(grades), len(grades))
print(f'The average is {average}')
```
When we run this, first 'Cannot divide by 0' will be printed in the console. Then in the next line, it will print 'The average is None'.

This is not clear to a user who expects to read something about grades. 

We can restructure the grades code to do this.
```
grades = []
if len(grades) == 0:
    print('You dont have any grades yet.')
    exit()

average = divide(sum(grades), len(grades))
print(f'The average grade is {average}')
```
Now, the user gets to read a message related to grades. However, there is a cleaner way to structure this operation by raising an error
```
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    return dividend/divisor

grades = []
average = divide(sum(grades), len(grades))
print(f'The average grade is {average}')
```
In this case, when the divisor is 0, a ZeroDivisorError will be raised a full traceback will be provided.
```
Traceback (most recent call last):
  File "playground.py", line 18, in <module>
    average = divide(sum(grades), len(grades))
  File "playground.py", line 15, in divide
    raise ZeroDivisionError('Divisor cannot be 0.')
ZeroDivisionError: Divisor cannot be 0.
```
Python provides a traceback that points out the file location, the line number of the bug and the reason for the error.
In this case, the error occurred in playground.py, line 15, in divide function. The error is ZeroDivisionError. When error is raised, the execution of the code stops at that point.

Python allows us to catch this error and maintain the flow of the program so that the execution does not stop. It will also provide us the ability to print a relevant message that a user can understand
```
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    return dividend/divisor

grades = []
try:
    average = divide(sum(grades), len(grades))
    print(f'The average grade is {average}')
except ZeroDivisionError as e:
    print('Grades list is empty')
```
The syntax to catch the error/exception is to put the main part of the code in the try block. The except block will contain the code that we want executed when an error/exception is raised. The variable e takes the value of the exception object, which in this case is 'Divisor cannot be 0'. In this case, because the grades list is empty, the error/exception will be raised while using the divide function and hence the except block will run.

Apart from ZeroDivisionErrors, there are a number of built-in errors that we can create for different things. Some examples are TypeError (wrong type), ValueError (unexpected value), RuntimeError. We can even create our own error types.

Another important point to note in the syntax is
```
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    return dividend/divisor

grades = []
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print('Grades list is empty')
else:
    print(f'The average grade is {average}')
```

This will also produce the same outcome as the previous code. The else block will run only if try block runs without any error. This is done in case we dont want to put all of our code int he same block.

```
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    return dividend/divisor

grades = []
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print('Grades list is empty')
else:
    print(f'The average grade is {average}')
finally:
    print('We are done!')
```
The finally block will always run, irrespective of whether an error/exception was raised or not.

Lets look at an elaborate version of the above code.

```
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    return dividend/divisor

students = [
    {'name':'Bob', 'grades':[75, 90]},
    {'name':'Rolf', 'grades':[]},
    {'name':'Jen', 'grades':[100, 90]},
]
try:
    for student in students:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades), len(grades))
        print(f'{name} averaged {average}')
except ZeroDivisionError as e:
    print(f'ERROR: {name} has no grades')
else:
    print('--- All student averages calculated ---')
finally:
    print('--- End of student average calculation ---')
```
When the iteration gets to Rolf, who has no grades, the code in try block will raise error and the except block will execute for Rolf. The else block runs only if the try block runs successfully, which is not the case here. The finally block code runs and the program ends. If Rolf has some grades, then the try block will execute successfuly and then the else block and the finally block runs and the program ends.


## Custom Error Classes

Consider a class called Book.
```
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr(self):
        return (
            f'<Book {self.name}, read {self.pages_read} out of {self.page_count} pages>'
        )

    def read(self, pages: int):
        self.pages_read += pages
        print(f'You have now read {self.pages_read} out of {self.page_count}')
```
There is a bug in this code. Let us see what it is.
```
python101 = Book('Python 101', 50)
python101.read(35)
python101.read(50)
```
In this case, the last output line will be 'You have now read 85 pages out of 50 pages.'
This is clearly not possible. Making changes, we will raise a error when the number of pages read > page count.

```
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr(self):
        return (
            f'<Book {self.name}, read {self.pages_read} out of {self.page_count} pages>'
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f'You tried to read {self.pages_read + pages} pages but this book only has {self.page_count} pages.'
            )
        self.pages_read += pages
        print(f'You have now read {self.pages_read} out of {self.page_count}')
```
The TooManyPagesReadError is not a built-in error type. But we can define our own errors.

```
class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr(self):
        return (
            f'<Book {self.name}, read {self.pages_read} out of {self.page_count} pages>'
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f'You tried to read {self.pages_read + pages} pages but this book only has {self.page_count} pages.'
            )
        self.pages_read += pages
        print(f'You have now read {self.pages_read} out of {self.page_count}')
```

We defined the error and made it inherit from the ValueError class. But we named it something else.
What happens when we try to run this.
```
python101 = Book('Python 101', 50)
python101.read(35)
python101.read(50)
```
The error raised is
```
Traceback (most recent call last):
  File "playground.py", line 60, in <module>
    python101.read(50)
  File "playground.py", line 52, in read
    raise TooManyPagesReadError(
__main__.TooManyPagesReadError: You tried to read 85 pages but this book only has 50 pages.
```
We were able to raise our own custom error messaage.

In order to make error messages specific to the users and what they expect, we can catch the error and using the except block, execute a piece of code that we want for better communication.

In summary, when we want to define our own error class, then we need to make sure that they are inheriting the appropriate error class like ValueError, TypeError etc.

## First Class Functions in Python

First class functions mean that functions are just variables. This means we can pass them as arguments to other functions and in general use them the same way we use variables.
```
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    return dividend/divisor

def calculate(*values, operator):
    return operator(*values)
```
If we wanted to use the divide function using the calculate function, we use
```
result = calculate(20, 4, operator=divide)
```
Here, we are using divide as a variable and passing it to the calculate function. divide is an example of a first class function. Note that when using function as a variable we do not call it, so in this case we do operator = divide and not operator = divide().

Functions in Python just happen to be variables that are callable. Let us look at another example.
```
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RunTimeError(f'Could not find an element with {expected}')

friends = [
    {'name': 'Rolf', 'age': 24},
    {'name': 'Adam', 'age': 30},
    {'name': 'Anne', 'age': 27},
]

def get_friend_name(friend):
    return friend['name']
```
In this case, get_friend_name is the finder function. It runs on each element of the iteration and returns the 'name' property of the element of the sequence. 

When we run
```
print(search(friends, 'Bob Smith', get_friend_name))
```
We will get a RunTimeError. Similarly when run
```
print(search(friends, 'Rolf', get_friend_name))
```
Python will print the first row dictionary in the console.
```
{'name': 'Rolf', 'age': 24}
```
Can you replace the get_friend_name with a lambda function?

There is an itemgetter module in the operator built-in package that will perform the same role.
```
from operator import itemgetter

print(searh(friends, 'Rolf', itemgetter('name')))
```
This works the same way too.

## Decorators in Python

Decorators allow us to modify function easily.

Consider this sceanrio
```
user = {'username':'jose', 'access_level':'guest'}

def get_admin_password():
    return '1234'

print(get_admin_password)
```
We will get the admin password even though the user access level is only guest. We should secure the get_admin_password function because only admins should be able to get the password.

```
user = {'username':'jose', 'access_level':'guest'}

def get_admin_password():
    return '1234'

if user['access_level'] == 'admin':
    print(get_admin_password)
```
In this case the get_admin_password function itself is unsecure. Which means anyone could call the function and receive the admin password.

Let us define a secure function

```
user = {'username':'jose', 'access_level':'guest'}

def get_admin_password():
    return '1234'

def secure_get_admin(): 
    if user['access_level'] == 'admin':
        return '1234'
```
get_admin_password is still there. So we should delete the get_admin_password.
secure_get_admin does protect the password.

However, we will have to add the if statement in every function where we want to secure the access. There is a better way.

We will use a decorator to modify the get_admin_password functon to make it secure.

```
user = {'username':'jose', 'access_level':'guest'}

def get_admin_password():
    return '1234'

def secure_function(func): 
    if user['access_level'] == 'admin':
        return func

get_admin_password = secure_funcion(get_admin_password)
print(get_admin_password())
```

When secure_function is called while passing the get_admin_password, it checks if user's access level is 'admin'. If it is, then the same function get_admin_password is returned. When the get_admin_password function is called, it returns the password. If the access level is not 'admin', then the secure_function returns None and in this case the get_admin_password takes the None object. Calling get_admin_password results in an error as Nonetype objects are not callable.

This is not quite what we want though, because calling the get_admin_password leads to error. Instead, we can make the following change
```
user = {'username':'jose', 'access_level':'guest'}

def get_admin_password():
    return '1234'

def make_secure(func):
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
```

The make_secure function replaces the get_admin_password function with the secure_function defined in the make_secure function. Currently, if the access level is not 'admin', the get_admin_password function call returns None. We can make it descriptive in case the access level is not 'admin'
```
user = {'username':'jose', 'access_level':'guest'}

def get_admin_password():
    return '1234'

def make_secure(func):
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'No admin permissions for {user['username']}'
    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
```

This time, the get_admin_password function call returns the message incase the user level is not 'admin'.

Instead of
```
get_admin_password = make_secure(get_admin_password)
```
we can redesign as
```
user = {'username':'jose', 'access_level':'guest'}

def make_secure(func):
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'No admin permissions for {user['username']}'
    return secure_function

@make_secure
def get_admin_password():
    return '1234'

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
```

Replacing the get_admin_password function with the secure_function changes the name of the get_admin_password function.

If you want to retain the name of the function, we can include the following in our code.
```
import functools
user = {'username':'jose', 'access_level':'guest'}

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'No admin permissions for {user['username']}'
    return secure_function

@make_secure
def get_admin_password():
    return '1234'

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
```

There is an issue in the above design. Imagine if our get_admin_password was replaced by 
```
get_password(panel):
    if panel == 'admin':
        retun '1234'
    elif panel == 'billing':
        return 'super_secure_password'
```
In this case, decorating the get_password with make_secure will result in an error because the secure_function does not take any argument.

If you do the following
```
import functools
user = {'username':'jose', 'access_level':'guest'}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(panel):
        if user['access_level'] == 'admin':
            return func(panel)
        else:
            return f'No admin permissions for {user['username']}'
    return secure_function

@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'super_secure_password'

get_admin_password = make_secure(get_admin_password)
print(get_admin_password('billing'))
```
This is going to tie the make_secure function with the get_password function because of the specific parameter in the secure function called panel. We want a generic decorator that we can use to secure any other function that takes any number or type of paramaters.

```
import functools
user = {'username':'jose', 'access_level':'guest'}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f'No admin permissions for {user['username']}'
    return secure_function

@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'super_secure_password'

get_admin_password = make_secure(get_admin_password)
print(get_admin_password('billing'))
```
This way, we can pass any number and type of arguments to the function that is being replacing the old function. This makes the decorator generic and can be used to secure any function that takes any kind of parameters.

You can even create decorators with parameters that we can pass arguments to while decorating.
```
import functools
user = {'username':'jose', 'access_level':'guest'}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f'No {access_level} permissions for {user['username']}'
        return secure_function
    return decorator

@make_secure('admin')
def get_admin_password():
    return '1234'

@make_secure('guest')
def get_dashboard_password():
    return 'user: user_password'

print(get_admin_password())
print(get_dashboard_password())
```



