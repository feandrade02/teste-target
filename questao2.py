def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
def main():
    x = int(input("Entre com um número inteiro:"))
    if x < 0:
        print("O número informado não pertence a sequência de Fibonacci!")
    else:
        seq = []
        for i in range(x+10): #Calcular a sequencia de fibonacci algumas posicoes a frente do numero informado para garantir sua inclusao caso esteja na sequencia
            seq.append(fibo(i))
        if x in seq:
            print("O número informado pertence a sequência de Fibonacci!")
        else:
            print("O número informado não pertence a sequência de Fibonacci!")
    return

if __name__ == "__main__":
    main()     