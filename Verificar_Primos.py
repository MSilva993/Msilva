# Função para verificar se um número é primo
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Função principal para imprimir números primos até um valor máximo
def imprimir_numeros_primos():
    max_value = int(input("Digite um valor máximo: "))
    print(f"Números primos até {max_value}:")
    for n in range(2, max_value + 1):
        if is_prime(n):
            print(n, end=' ')
    print()

# Chama a função principal
imprimir_numeros_primos()


    

