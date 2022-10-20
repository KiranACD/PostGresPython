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
The return type of the class methods is the class itself. When the return type is class itself, we have to write the return type in quotes. If it is any other class, we do not have to put the class name in quotes.













