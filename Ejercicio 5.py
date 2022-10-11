def cant_numeros_primos(num):
    cuenta=0
    while num>0:
        ultimo_digito=num%10
        num=num//10
        if ultimo_digito==2 or ultimo_digito==3 or ultimo_digito==5 or ultimo_digito==7:
            cuenta += 1
    return cuenta          
num=int(input("Ingrese el numero= "))
print("La cantidad de numeros primos es= ",cant_numeros_primos(num))