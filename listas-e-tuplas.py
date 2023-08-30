#Criando e inicializando uma lista
pessoas=['Ana','Gabriela','Lucas','Eduardo']

#Modificando a lista
pessoas[1]="Letícia"

#Exibindo itens de uma lista
# print(pessoas[0])
# print(pessoas[3])
# print(pessoas)

# Intervalo fixo
# for i in range(4):
#     print(pessoas[i])

# intervalo variável
# for i in range(len(pessoas)):
#     print(pessoas[i])

# for p in pessoas:
#     print(p)

times=[]#Criando uma lista vazia
#Inserindo elementos no final da lista
times.append('Flamengo')
times.append('Botafogo')
times.append('Fluminense')
times.append('Vasco')
times.append('Bangu')

#Inserção por posição
times.insert(0,'São Paulo')#Inserir novo elemento alterando a estrutura da lista
print(times)

#Removendo itens da lista
times.remove('Bangu')
times.pop(0)
