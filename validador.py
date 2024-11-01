def validador(cnpj):

    
    cnpjChars = [] # Criando lista para gerar um split do cnpj
    
    for char in cnpj:
        cnpjChars.append(int(char)) # adicionando o caractere na lista

    print(cnpjChars)

    return True

def main():
    
    # CNPJ será string para fazer o split
    cnpj = input("Digite o CNPJ que será validado (somente os números)")
    
    
    # Verificando se o tamanho do cnpj é válido
    while len(cnpj) < 11:
        print("Cnpj inválido porque é menor que o tamanho padrão")
        cnpj = input("Digite o CNPJ que será validado (somente os números)")
        

    # Armazenando o valor booleano do validador
    resultadoValidacao = validador(cnpj)
    
    if resultadoValidacao == True:
        print(f"O cnpj: {cnpj} é válido")
    else:
        print(f"O cnpj: {cnpj} não é válido")
        
main()