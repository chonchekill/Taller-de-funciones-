def factorial(num):
    t=2
    factorial=1
    for x in range (num-1):
        factorial=factorial*t
        t+=1
    return factorial
num=int(input("Ingrese el numero= "))
print("El factorial es= ",factorial(num))
