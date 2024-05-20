import Pyro4

# Cria um proxy para se conectar ao servidor Pyro
def main():
    calculadora = Pyro4.Proxy("URI_Server")  # Substitua 'obj_123456' pelo URI do servidor
    resultado = calculadora.somar(85, 3)
    print("A soma é:", resultado)

     resultado_subtracao = calculadora.subtrair(85, 3)
    print("A subtração é:", resultado_subtracao)

    resultado_multiplicacao = calculadora.multiplicar(85, 3)
    print("A multiplicação é:", resultado_multiplicacao)

if __name__ == "__main__":
    main()
