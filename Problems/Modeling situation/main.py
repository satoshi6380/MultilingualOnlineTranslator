try:
    exception_test()
except ZeroDivisionError:
    print("ZeroDivisionError ")
except AssertionError:
    print("AssertionError ")
except ArithmeticError:
    print("ArithmeticError ")