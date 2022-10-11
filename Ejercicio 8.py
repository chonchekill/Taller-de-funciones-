def numero_fobonacci(num):
    aux=1
    fibo=0
    aux_2=0
    y=0
    lista=[]
    for x in range (30):
        fibo=aux+fibo
        aux_2=aux
        aux=fibo
        fibo=aux_2
        lista.append(fibo)
    for t in range (30):
        if lista[t]==num:
            aux_3=1
            return aux_3
    for m in range(30):
        if lista[m]!=num:
            aux_3=0
            return aux_3
num=int(input("Ingrese el numero= "))
print("Si el numero es 1 esta dentro de los primeros 30 numeros fobonacci si no el resultado es 0")
print(numero_fobonacci(num))