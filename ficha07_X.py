# Leitura do ficheiro e atribuição do em lista de dicionarios dos nomes e numeros macanograficos

f = open("dados.txt", "r")  # Abre o ficheiro dado
txt = f.read()
documentacao = list(map(str, txt.split("\n")))  # Distribui o ficheiro em lista

n = int(documentacao[0])

del documentacao[:2*n+1]

n = int(documentacao[0])
del documentacao[0]

alunos_dic = []

for k in range(0, 2*n, 2):
    alunos_dic.append({'nome': documentacao[k], 'numero': documentacao[k+1][:10]})

##----------##-----##----------##

def anoaluno(x):

    y = str(x)
    return int(y[:4])

def cursoaluno(x):
    y = str(x)
    return int(y[5:7])
