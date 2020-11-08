# Numeros Primos
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            #print(n, "e igual", x,  "*", n//x)
            print('{} e igual {} * {}'.format(n, x, n//x))
            break
        else:
            # O Ciclo pula pra ca sem encontrar um fator
            #print(n, "e um numero primo")
            print('{} e um numero primo'.format(n))
