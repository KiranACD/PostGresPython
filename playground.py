# def double(x):
#     return x*2

# sequence = [1, 3, 5, 9]
# doubled = map(double, sequence)
# print(list(doubled))

# def add(**kwargs):
#     return kwargs['x']+kwargs['y']
# nums = {'x':15, 'y':25}
# print(add(**nums))

# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError('Divisor cannot be 0.')
#     return dividend/divisor

# students = [
#     {'name':'Bob', 'grades':[75, 90]},
#     {'name':'Rolf', 'grades':[]},
#     {'name':'Jen', 'grades':[100, 90]},
# ]
# try:
#     for student in students:
#         name = student['name']
#         grades = student['grades']
#         average = divide(sum(grades), len(grades))
#         print(f'{name} averaged {average}')
# except ZeroDivisionError as e:
#     print(f'ERROR: {name} has no grades')
# else:
#     print('--- All student averages calculated ---')
# finally:
#     print('--- End of student average calculation ---')

# class TooManyPagesReadError(ValueError):
#     pass

# class Book:
#     def __init__(self, name: str, page_count: int):
#         self.name = name
#         self.page_count = page_count
#         self.pages_read = 0
    
#     def __repr(self):
#         return (
#             f'<Book {self.name}, read {self.pages_read} out of {self.page_count} pages>'
#         )

#     def read(self, pages: int):
#         if self.pages_read + pages > self.page_count:
#             raise TooManyPagesReadError(
#                 f'You tried to read {self.pages_read + pages} pages but this book only has {self.page_count} pages.'
#             )
#         self.pages_read += pages
#         print(f'You have now read {self.pages_read} out of {self.page_count}')

# python101 = Book('Python 101', 50)
# python101.read(35)
# python101.read(50)


# def search(sequence, expected, finder):
#     for elem in sequence:
#         if finder(elem) == expected:
#             return elem
#     raise RuntimeError(f'Could not find an element with {expected}')

# friends = [
#     {'name': 'Rolf', 'age': 24},
#     {'name': 'Adam', 'age': 30},
#     {'name': 'Anne', 'age': 27},
# ]

# def get_friend_name(friend):
#     return friend['name']

# print(search(friends, 'Rolf', get_friend_name))

# import functools
# user = {'username':'jose', 'access_level':'guest'}

# def make_secure(access_level):
#     def decorator(func):
#         @functools.wraps(func)
#         def secure_function(*args, **kwargs):
#             if user['access_level'] == access_level:
#                 return func(*args, **kwargs)
#             else:
#                 return f'No {access_level} permissions for {user["username"]}.'
#         return secure_function
#     return decorator

# @make_secure('admin')
# def get_admin_password():
#     return '1234'

# @make_secure('guest')
# def get_dashboard_password():
#     return 'user: user_password'

# print(get_admin_password())
# print(get_dashboard_password())

import datetime
today_timestamp = datetime.datetime.today().timestamp()
condition = ['release_timestamp', '>', today_timestamp]
print(' '.join(condition[:-1]))