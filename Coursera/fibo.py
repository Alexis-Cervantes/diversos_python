# modulo de números Fibonacci
def fib(n): # escribe la serie de Fibonacci hasta n.
    a, b = 0, 1
    while b < n:
        print(b, end='  ')
        a, b = b, a+b
    print()

def fib2(n):  # devuelve la serie de Fibonacci hasta n.
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado

    if __name__ == "__main__":
        import sys
        fib(int(sys.argv[1]))
