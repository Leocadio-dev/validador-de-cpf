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

# Função principal do validador
def validador(cpf: str):

    listNumerosCpf = []
    digitoValidado = False 

    # Laço pra dividir todo o cpf
    for char in cpf:
        listNumerosCpf.append(int(char))
    
    # Fazendo a soma dos números baseado no tamanho do cpf (será somado para depois validar o décimo código)
    somaNumeros = somarNumerosCpf(cpf = cpf, tamanhoCpf = 9)
    
    # Primeiro dígito a ser validado
    digitoCorreto = calcularDigito(somaNumeros = somaNumeros)
    
    if listNumerosCpf[9] == digitoCorreto:
        digitoValidado = True
    else:
        return False
        
        
    # Fazendo a soma de todos os números novamente para descobrir o décimo primeiro número
    somaNumeros = somarNumerosCpf(cpf = cpf, tamanhoCpf = 10)
    
    digitoCorreto = calcularDigito(somaNumeros = somaNumeros)
    if listNumerosCpf[10] == digitoCorreto: 
        if digitoValidado == True: # Primeira validação feita retornou True, basta só verificar o segundo e não precisa gravar nada mais
            return True
    else:
        return False
        

    segundoDigito = calcularDigito(somaNumeros = somaNumeros)
    
# Função para reverter e multiplicar os números - inserido em uma função para que não tenha código repetido
def somarNumerosCpf(cpf: str, tamanhoCpf: int):
    
    listNumerosCpfModificado = [] # Criando lista para gerar um split do cpf
    listaAux = [] # Lista com os números multiplicados
    
    # Laço pra reverter a lista
    for char in cpf :
        listNumerosCpfModificado.append(int(char)) # Adicionando o caractere na lista
        
        if len(listNumerosCpfModificado) == tamanhoCpf: 
            break # Precisa parar o laço para verificar os dois últimos dígitos
        
    listNumerosCpfModificado.reverse() # Revertendo a lista 

    multiplicadorAuxiliar = 2 # Começa multiplicando por 2
    somaNumeros = 0
    
    for i in range(len(listNumerosCpfModificado)):
        listaAux.append(listNumerosCpfModificado[i] * multiplicadorAuxiliar) # Adicionando os números já multiplicados
        multiplicadorAuxiliar += 1
        somaNumeros += listaAux[i]
    return somaNumeros

# Calcula os dois últimos dígitos
def calcularDigito(somaNumeros: int):

    validadoresUltimosDigitos = [] # Lista que vai guardar o resultado da divisão e o resto
    digito = 0 # Últimos dígitos do cpf (na ordem normal)

    validadoresUltimosDigitos.append(somaNumeros / 11)   # Valor da divisão (divisão por 11 porque é o tamanho padrão do cpf)
    validadoresUltimosDigitos.append(somaNumeros % 11)   # Resto da divisão 
    
    if validadoresUltimosDigitos[1] < 2:
        digito = 0
    else:
        digito = 11 - validadoresUltimosDigitos[1]

    # Limpando a lista após a execução:
    validadoresUltimosDigitos = []
    return digito
       
main()