def gcd(x,y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x
 
n1 = int(input("Give me an integer: "))
n2 = int(input("Give me another integer: "))
 
print("The greatest common denominator of",n1,"and",n2,"is",gcd(n1,n2))
