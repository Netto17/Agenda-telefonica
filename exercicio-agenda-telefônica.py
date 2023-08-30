import os
agenda=[]
sair=False
novo_contato=[]
while (sair==False):
    print("--------AGENDA--------")
    print("1-Novo contato")
    print("2-Listar contatos")
    print("3-Editar último contato")
    print("4-Remover último contato")
    print("---------------------")
    opcao=int(input("Digite a opção desejada:"))
    if(opcao==1):#Add um contato na agenda
        nome=input("\nDigite o nome do contato: ")
        novo_contato.append(nome)
        numero=input("Digite o número do contato : ")
        novo_contato.append(numero)
        agenda.append(novo_contato)
        os.system('cls')
        if(opcao==2):#Lista os contatos presentes na agenda
            os.system('cls')
            for p in agenda:
             print(p)
        if (opcao==3):#Modifica o último contato presente na agenda
                nome=input("\nDigite o nome do contato a ser editado: ")
                for  i in range(len(agenda)):
                    if (agenda[i][0]==nome):
                        novo_nome=input("Digite o novo nome do contato:")
                        novo_numero=input("Digite o novo número do contato: ")
                        agenda[i][0]=novo_nome
                        agenda[i][1]=novo_numero
                        os.system('cls')