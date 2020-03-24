f = True
o = True
x = True
y = True
p = False
p1 = False
k = False
k1 = False
g = False
g1 = False
m = False
m1 = False
t = False
t1 = False
while f:
    while o:
        try:
            weight = int(input("weight :=> "))
            o = False
        except ValueError:
            print("type an integer")
            o = True
    while y:
        unit1 = input("From which unit :=> ")
        if unit1.lower() == "kilo" or unit1.lower() == "kg" or unit1.lower() == "kilogram":
            k = True
            y = False
        elif unit1.lower() == "ton" or unit1.lower() == "tonne" or unit1.lower() == "tn":
            t = True
            y = False
        elif unit1.lower() == "gram" or unit1.lower() == "gm" or unit1.lower() == "g":
            g = True
            y = False
        elif unit1.lower() == "mg" or unit1.lower() == "milligram" or unit1.lower() == "milli gram":
            m = True
            y = False
        elif unit1.lower() == "pound" or unit1.lower() == "lbs" or unit1.lower() == "pounds" or unit1.lower() == "lb":
            p = True
            y = False
        else:
            print('''
    please type a valid unit
        tonne     ==> ton
        gram      ==> gm
        milligram ==> mg
        pound     ==> lbs  
            ''')
            y = True

    while x:
        unit2 = input("To which unit :=> ")
        if unit2.lower() == "kilo" or unit2.lower() == "kg" or unit2.lower() == "kilogram":
            k1 = True
            x = False
        elif unit2.lower() == "gram" or unit2.lower() == "gm" or unit2.lower() == "g":
            g1 = True
            x = False
        elif unit2.lower() == "ton" or unit2.lower() == "tonne" or unit2.lower() == "tn":
            t1 = True
            x = False
        elif unit2.lower() == "mg" or unit2.lower() == "milligram" or unit2.lower() == "milli gram":
            m1 = True
            x = False
        elif unit2.lower() == "pound" or unit2.lower() == "lbs" or unit2.lower() == "pounds" or unit2.lower() == "lb":
            p1 = True
            x = False
        else:
            print('''
        please type a valid unit
            tonne     ==> ton
            gram      ==> gm
            milligram ==> mg
            pound     ==> lbs  
                ''')
            x = True

    # conversion starts here
    if p == True and p1 == True:
        print(f"weight : {weight}pound")
        f = False
    elif k == True and k1 == True:
        print(f"weight : {weight}kg")
        f = False
    elif g == True and g1 == True:
        print(f"weight : {weight}gm")
        f = False
    elif t == True and t1 == True:
        print(f"weight : {weight}ton")
        f = False
    elif m == True and m1 == True:
        print(f"weight : {weight}mg")
        f = False



    elif p == True and k1 == True:
        conv = weight * 0.453592
        print(f"weight : {conv}kg")
        f = False
    elif p == True and g1 == True:
        conv = weight * 453.592
        print(f"weight : {conv}gm")
        f = False
    elif p == True and m1 == True:
        conv = weight * 453592
        print(f"weight : {conv}mg")
        f = False
    elif p == True and t1 == True:
        conv = weight * 0.000453592
        print(f"weight : {conv}ton")
        f = False


    elif k == True and p1 == True:
        conv = weight * 2.20462
        print(f"weight : {conv}pound")
        f = False
    elif k == True and t1 == True:
        conv = weight * 0.001
        print(f"weight : {conv}ton")
        f = False
    elif k == True and g1 == True:
        conv = weight * 1000
        print(f"weight : {conv}gm")
        f = False
    elif k == True and m1 == True:
        conv = weight * 1000000
        print(f"weight : {conv}mg")
        f = False


    elif t == True and p1 == True:
        conv = weight * 2204.62
        print(f"weight : {conv}pound")
        f = False
    elif t == True and k1 == True:
        conv = weight * 1000
        print(f"weight : {conv}kg")
        f = False
    elif t == True and g1 == True:
        conv = weight * 1000000
        print(f"weight : {conv}gm")
        f = False
    elif t == True and m1 == True:
        conv = weight * 1000000000
        print(f"weight : {conv}mg")
        f = False



    elif g == True and p1 == True:
        conv = weight * 0.00220462
        print(f"weight : {conv}pound")
        f = False
    elif g == True and k1 == True:
        conv = weight * 0.001
        print(f"weight : {conv}kg")
        f = False
    elif g == True and t1 == True:
        conv = weight * 0.000001
        print(f"weight : {conv}ton")
        f = False
    elif g == True and m1 == True:
        conv = weight * 1000
        print(f"weight : {conv}mg")
        f = False


    elif m == True and p1 == True:
        conv = weight / 453592
        print(f"weight : {conv}pound")
        f = False
    elif m == True and k1 == True:
        conv = weight * 0.000001
        print(f"weight : {conv}kg")
        f = False
    elif m == True and t1 == True:
        conv = weight * 0.000000001
        print(f"weight : {conv}ton")
        f = False
    elif m == True and g1 == True:
        conv = weight * 0.001
        print(f"weight : {conv}gm")
        f = False
    else:
        f = True
print("Thank you for using our service")
