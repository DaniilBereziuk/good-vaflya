#
# try:
#     print('start code')
#     print(10/0)
#     print('no errors')
# except (NameError, ZeroDivisionError):
#     print('We have an error')
# else:
#     print('All is ok!')
# finally:
#     print('I work if we have error or not')
#
# print('Code after try-expect')


# def checker(value):
#     if type(value) != str:
#         raise TypeError(
#             f"Sorry, we can't work with this type - {type(value)}."
#             f"we need STR"
#         )
#     else:
#         return value
#
# try:
#     checker(10)
# except TypeError as error:
#     print(error)
#     print('Try again!')
#
#
# class BuildingError(Exception):
#
#     def __str__(self):
#         return 'With this materials we cannot build the house'
#
# def check_materials(amount, limit):
#     if amount >= limit:
#         return 'Enogh materials'
#     else:
#         raise BuildingError()
#
# limit = 100
# print(
#     check_materials(80, limit)
# )


import warnings

warnings.simplefilter('always', SyntaxWarning)
warnings.simplefilter('error', ImportWarning)

warnings.warn('Warning, no code here', SyntaxWarning)
warnings.warn('Warning, wrong module', ImportWarning)

print(1000)
















