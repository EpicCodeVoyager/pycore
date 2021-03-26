# add two number if non numeric raise exception

def add_number(num1, num2):
    # get input from the cli
    # if it is all digits/float
    try:
        if (str(num1).isnumeric() or str(num2).isnumeric):
            return num1 + num2
        raise Exception
    except Exception as e:
        print('Error not a number')


out = add_number(1, 2)
print(out)
