print("Enter The Value Of a & b\n")
a = int(input())
b = int(input())
############### Airthmetic Operations ####################################################################################
def add():
    c = a + b
    print("Addition Result =", c)
    return c
def sub():
    c = a-b
    print("Substraction Result =", c)
    return c
def mult():
    c = a*b
    print("Multiplication Result =", c)
    return c
def div():
    c = a/b
    if b == 0:
        print("Infinite Value\n")
    else:
        print("Division Result =", c)
    return c
###################### Airthmetic Operations Function Finished ############################################################
###################### Airthmetic Function Calling ########################################################################
add()
sub()
mult()
div()
##################### Airthmetic Function Calling Finished ################################################################

