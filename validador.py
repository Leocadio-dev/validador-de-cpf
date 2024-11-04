def main():
    
    # CPF será string para fazer o split
    cpf = input("Digite o CPF que será validado (somente os números)")
    
    
    # Verificando se o tamanho do cpf é válido
    while len(cpf) != 11:
        print("Cpf inválido porque é menor que o tamanho padrão")
        cpf = input("Digite o CPF que será validado (somente os números)")
        

    # Armazenando o valor booleano do validador
    
    resultadoValidacao = validador(cpf)
    
    if resultadoValidacao == True:
        print(f"O cpf: {cpf} é válido")
    else:
        print(f"O cpf: {cpf} não é válido")


def validador(cpf: str):

    listNumerosCpf = []
    listNumerosCpfModificado = [] # Criando lista para gerar um split do cpf
    listaAux = [] # Lista com os números multiplicados

    # Laço pra dividir todo o cpf
    for char in cpf:
        listNumerosCpf.append(int(char))

    # Laço pra reverter a lista
    for char in cpf :
        listNumerosCpfModificado.append(int(char)) # Adicionando o caractere na lista
        if len(listNumerosCpfModificado) == 9: 
            break # Precisa parar o laço para verificar os dois últimos dígitos
    listNumerosCpfModificado.reverse() # Revertendo a lista 

    multiplicadorAuxiliar = 2 # Começa multiplicando por 2
    somaNumeros = 0
    for i in range(len(listNumerosCpfModificado)):
        listaAux.append(listNumerosCpfModificado[i] * multiplicadorAuxiliar) # Adicionando os números já multiplicados
        multiplicadorAuxiliar += 1
        somaNumeros += listaAux[i]

    primeiroDigito = calcularDigito(somaNumeros)
    if listNumerosCpf[9] != primeiroDigito:
        print("O cpf é inválido")
    if listNumerosCpf[10] != segundoDigito:
        print("O cpf é inválido")
    

    segundoDigito = calcularDigito(somaNumeros)
    return 1

# Calcula os dois últimos dígitos
def calcularDigito(somaNumeros: int):

    validadoresUltimosDigitos = [] # Lista que vai guardar o resultado da divisão e o resto
    digito = 0 # Últimos dígitos do cpf (na ordem normal)

    validadoresUltimosDigitos[0] = somaNumeros / 11   # Valor da divisão (divisão por 11 porque é o tamanho padrão do cpf)
    validadoresUltimosDigitos[1] = somaNumeros % 11   # Resto da divisão 
    
    if validadoresUltimosDigitos[1] < 2:
        digito = 0
    else:
        digito = 11 - validadoresUltimosDigitos[1]

    return digito
       
main()