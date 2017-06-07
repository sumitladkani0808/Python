# # Decorators class without Arguments
#
#
# class DecoratorWithoutArguments(object):
#     def __init__(self, f):
#         """
#         If there are no decorator arguments, the function
#         to be decorated is passed to the constructor.
#         """
#         print("Inside __init__()")
#         self.f = f
#
#     def __call__(self, *args):
#         """
#         The __call__ method is not called until the
#         decorated function is called.
#         """
#         print("Inside __call__()")
#         self.f(*args)
#         print("After self.f(*args)")
#
#
# @DecoratorWithoutArguments
# def sayhello(a1, a2, a3, a4):
#     print('sayHello arguments: {}, {}, {}, {}'.format(a1, a2, a3, a4))
#
# print("After decoration")
# print("Preparing to call sayHello()")
# sayhello("say", "hello", "argument", "list")
# print("After first sayHello() call")
# sayhello("a", "different", "set of", "arguments")
# print("After second sayHello() call")



# # Decorators class with Arguments
#
#
# class DecoratorWithArguments(object):
#     def __init__(self, arg1, arg2, arg3):
#         """
#         If there are decorator arguments, the function
#         to be decorated is not passed to the constructor!
#         """
#         print("Inside __init__()")
#         self.arg1 = arg1
#         self.arg2 = arg2
#         self.arg3 = arg3
#
#     def __call__(self, f):
#         """
#         If there are decorator arguments, __call__() is only called
#         once, as part of the decoration process! You can only give
#         it a single argument, which is the function object.
#         """
#         print("Inside __call__()")
#
#         def wrapped_f(*args):
#             print("Inside wrapped_f()")
#             print("Decorator arguments: {}, {}, {}".format(self.arg1, self.arg2, self.arg3))
#             f(*args)
#             print("After f(*args)")
#         return wrapped_f
#
#
# @DecoratorWithArguments("hello", "world", 42)
# def sayhello(a1, a2, a3, a4):
#     print('sayHello arguments: {}, {}, {}, {}'.format(a1, a2, a3, a4))
#
# print("After decoration")
#
# print("Preparing to call sayHello()")
# sayhello("say", "hello", "argument", "list")
# print("after first sayHello() call")
# sayhello("a", "different", "set of", "arguments")
# print("after second sayHello() call")



# Decorator Functions with Decorator Arguments


def decoratorFunctionWithArguments(arg1, arg2, arg3):

    def wrap(f):
        print("Inside wrap()")

        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments: {}, {}, {}".format(arg1, arg2, arg3))
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap


@decoratorFunctionWithArguments("hello", "world", 42)
def sayhello(a1, a2, a3, a4):
    print('sayHello arguments: {}, {}, {}, {}'.format(a1, a2, a3, a4))

print("After decoration")

print("Preparing to call sayHello()")
sayhello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayhello("a", "different", "set of", "arguments")
print("after second sayHello() call")
