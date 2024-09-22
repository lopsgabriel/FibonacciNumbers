def fibonacci(x):
    #Calcula até o numero escolhido pelo Usuário
    numbers = [0,1]
    while numbers[-1] <= x:
        next_number = numbers[-1] + numbers[-2]
        numbers.append(next_number)
    return numbers

while True:
    number = input("Digite um número para saber se ele pertence a sequência de Fibonacci \t")
    try:
        #Garante que o usuario digite um numero valido
        number = int(number)
        sequence = fibonacci(number)
        if number in sequence:
            #Confere se o numero está presente na sequencia de Fibonacci
            print(f"o numero {number} está presente na sequencia de Fibonacci\n")
        else:
            print(f"o numero {number} não existe na sequencia de Fibonacci\n")
    except ValueError:
        print('Digite um numero válido \n')


