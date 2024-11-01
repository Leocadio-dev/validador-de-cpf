def main():
    
    # CNPJ será string para fazer o split
    cnpj = input("Digite o CNPJ que será validado (somente os números)")
    
    
    # Verificando se o tamanho do cnpj é válido
    while len(cnpj) != 11:
        print("Cnpj inválido porque é menor que o tamanho padrão")
        cnpj = input("Digite o CNPJ que será validado (somente os números)")
        

    # Armazenando o valor booleano do validador
    
    resultadoValidacao = validador(cnpj)
    
    if resultadoValidacao == True:
        print(f"O cnpj: {cnpj} é válido")
    else:
        print(f"O cnpj: {cnpj} não é válido")


def validador(cnpj: str):

    
    listNumerosCnpj = [] # Criando lista para gerar um split do cnpj
    listaAux = [] # Lista com os números multiplicados

    for char in len(cnpj) :
        listNumerosCnpj.append(int(char)) # Adicionando o caractere na lista
        if len(listNumerosCnpj) == 9: 
            break # Precisa parar o laço para verificar 
    listNumerosCnpj.reverse() # Revertendo a lista 

    multiplicadorAuxiliar = 2 # Começa multiplicando por 2
    somaNumeros = 0
    for i in range(len(listNumerosCnpj)):
        listaAux.append(listNumerosCnpj[i] * multiplicadorAuxiliar) # Adicionando os números já multiplicados
        multiplicadorAuxiliar += 1
        somaNumeros += listaAux[i]

    calcularDoisUltimosDigitos(listNumerosCnpj, listaAux, somaNumeros)
    print(listaAux)
    return 1

def calcularDoisUltimosDigitos(listlistNumerosCnpj: list, listaAux: list, somaNumeros: int):

    return 
       
main()