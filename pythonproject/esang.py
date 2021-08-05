l = ["medicine","electronics items","house items","food items","drinks","mobile phones","vegetables","fruits"]
def esang():
    # print("To Buy Medicines  = Press 1    To Buy Electronics Items = Press 2\nTo Buy House Items = Press 3    To Food Items = Press 4\n"
    #       "To Buy Drinks = Press 5    To Buy Mobile Phones = Press 6\nTo Buy Vegetables = Press 7    To Buy Fruits = Press 8")
    # n = int(input("Enter Your Category\n"))
    for m in enumerate(l):
        print("Items Booked =",m)
    print("Do You Want to Cancel any Items(y/n)")
    n = str(input())
    if n == 'y':
        print("Which Item You Want to Cancel")
        n1 = str(input())
        if n1=='0':
            del l[0]
            print("Updated List\n",l)
    else:
        print("Order Confirmed(All Items)")
esang()