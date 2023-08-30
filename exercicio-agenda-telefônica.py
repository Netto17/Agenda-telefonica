import os
agenda=[]
sair=False
while (sair==False):
    print("--------AGENDA--------")
    print("1-Novo contato")
    print("2-Listar contatos")
    print("3-Editar contato")
    print("4-Remover contato")
    print("---------------------")
    opcao=int(input("Digite a opção desejada:"))
    if(opcao==1):
        novo_contato=[]
        nome=input("\nDigite o nome do contato: ")
        novo_contato.append(nome)
        numero=input("Digite o número do contato : ")
        novo_contato.append(numero)
        agenda.append(novo_contato)
        os.system('cls')


