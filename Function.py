a = 10;
b = 2;
c = "nope";
def greater(x, y):
    if x > y:
        return " is true"
    else:
        return " is false"

c = greater(a, b);
print ("The statement " + str(a) + " is greater than " + str(b) + c);
