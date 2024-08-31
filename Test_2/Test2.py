# Fução para recuperar sequência de Fibonacci, onde 'n' é o limite final da sequência.
def sequencia_de_fibonacci(n):
    sequencia = [0, 1]  # Inicia a sequência com 0 e 1.
    while sequencia[-1] < n:  # Gera a sequência até o último valor ser maior ou igual ao número informado.
        proximo_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_valor)
    return sequencia

# Função para validar se um número pertence a sequência de fibonacci, retorna um valor boolean, 'True' caso pertenca, e 'False' caso não.
def validar_fibonacci(n):
    sequencia = sequencia_de_fibonacci(n)
    if n in sequencia:
        return True
    else:
        return False

# MAIN
numero = int(input("Informe um número: "))
if validar_fibonacci(numero) == True:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")