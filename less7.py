# my_list = [1,2,3]
# iterator = iter(my_list)
# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)

# class Counter:
#
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#
#         return self.i
#
# counter = Counter(5)
# for e in counter:
#     print(e)
#
# counter2 = Counter(5)
# print(counter2.__next__())
# print(next(counter2))
#
#
#
# def to_degree(number, degree):
#     i = 0
#     for _ in range(degree):
#         yield number ** i
#         i += 1
#
#
# result = to_degree(10000, 5)
# print(result)
# for i in result:
#     print(i)
#
#
# def to_degree2(number):
#     i = 0
#     while True:
#         x = number ** i
#         yield x
#         if x > 100 ** 20:
#             return
#         i += 1
#
# result = to_degree2(10000)
# print(result)
# for i in result:
#     print(i)

# def helper(work):
#     work_in_memory = work
#
#     def helper(work):
#         return (f'I will help you with your {work_in_memory}.'
#                 f' After I will help with {work}')
#
#     return helper
#
# help_me = helper('homework')
# print(help_me('cleaning'))
# print(help_me('driving'))
# print(
#     helper('homework')('playing the guitar')
# )
#
# def checker(function):
#     def checker(*args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except Exception as err:
#             print(f'we have a problem - {err}')
#         else:
#             print(f'No problems. Result - {result}')
#
#     return checker


# def calculate(expression):
#     return eval(expression)
#
#
# calculate = checker(calculate)
# calculate('2*2')


# @checker
# def calculate(expression):
#     return eval(expression)
#
# calculate('2+2')

def checker(*exc_types):
    def checker(function):
        def checker2(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except (exc_types) as err:
                print(f'we have a problem - {err}')
            else:
                print(f'No problems. Result - {result}')
        return checker2
    return checker

@checker(NameError, TypeError, ZeroDivisionError)
def calculate(expression):
    return eval(expression)

calculate('2+32')