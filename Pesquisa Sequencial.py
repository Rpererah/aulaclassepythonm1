
# def busca_sequencial(registros,alunos,registro_aluno):
#     indice = 0
#     while indice <= (len(registros)-1):
#         if registro_aluno == registros[indice]:
#             return indice
#         indice = indice + 1
#     return -1


# registro_aluno = int(input("Digite seu RA:"))
# posicao = busca_sequencial(registros,alunos,registro_aluno)


# if posicao == -1:
#     print('RA não encontrado')
# else:
#     print(f"Posição:{posicao}")
#     print(f"Aluno:{alunos[posicao]}")

pessoas = ['Adrian', 'Bernardo', 'Rogerio', 'Helder(feijoada)', 'Neymar']
registros = [12345, 12346, 12347, 12348, 12310]

def pesquisa_sequencial(pessoas,registros,chave):
    posicao = 0
    while posicao <= (len(registros)-1):
        if registros[posicao] == chave:
            print(f'{pessoas[posicao]}')
            return True
        else:
            posicao = posicao+1
    return False

chave=12347
pesquisa_sequencial(pessoas,registros,chave)

