import random
from dadosGerais import matchClasses, matchClasses2, listaClasses
from dadosGerais import dicionarioRacas as dRacas
from nomePersonagem import nomePersonagem

# Funcao que retorna a posicao de 'r' na lista
def posicao(r, lista):
    contPos = 0
    for classe in lista:
        if classe == r:
            return contPos
        contPos+=1

# Funcao que ira retornar a tupla do match da raca e a posicao na lista M
def match(raca, M):
    pos = 0
    for rc in M:
        if raca == rc[1]:
            return rc, pos
        pos += 1
        
    return False

# Funcao para ver se alguma classe nao possui um match e nao propos a todas as racas
def unmatched(match, matchBool):
    # Percorrendo o dicionario em busca da primeira classe sem um match
    for chave, dic in match.items():
        # Caso nao possua um match
        if matchBool[chave] == False:
            # Entao, percorre-se o outro dicionario em busca de uma raca que nao recebeu uma proposta
            for chaveDois, valor in dic.items():
                if valor == False:
                    return chave, chaveDois
                
    return False

''' Funcao que ira organizar o dicionario matchClasses2 para se adaptar a quantidade de jogadores
    Ela recebera uma posicao aleatoria (pos) e (16 - N). Com isso a funcao ira transformar em True as 'n' posicoes
    seguintes. Por conta disso, so sobrarao 'N' classes sem match e o algoritmo so utilizara essa quantidade.
'''
def organizarClasses(pos, n):
    cont = 0
    
    while cont != n:
        matchClasses2[listaClasses[pos]] = True
        if (pos+1) == len(listaClasses):
            pos = 0
        else:
            pos += 1
        cont += 1

# Algoritmo de Gale-Shapley
def GaleShapley():
    
    # Inicializando uma lista que armazenara os matches
    M = []
    
    # Enquanto alguma classe estiver sozinha e nao tiver feito uma proposta a todoas as racas
    while unmatched(matchClasses, matchClasses2):
        # c <- primeira classe que nao possui match e nao fez todas propostas possiveis
        # r <- primeira raca que nao teve uma proposta recebida por 'c'
        c, r = unmatched(matchClasses, matchClasses2)
        
        # indica que 'r' ja recebeu uma proposta
        matchClasses[c][r] = True
        
        # se o 'r' nao possuir match
        if not match(r, M):
            M.append((c, r))
            matchClasses2[c] = True
        # caso nao
        else: 
            # armazena-se entao a tupla que representa o match de 'r' e a posicao na lista de matches (M)
            # entao e checado entre o 'c' e o atual parceiro de 'r', qual possui maior prioridade
            matchR, pos = match(r, M)
            
            # novo <- posicao do 'c' na lista
            novo = posicao(c, dRacas[r])
            
            # atual <- posicao do match atual de 'r' na lista
            atual = posicao(matchR[0], dRacas[r])
            
            # Se a posicao de 'c' for prioritaria a do atual match, entao substitui-se o parceiro de 'r' 
            if novo < atual:
                # novo match
                M[pos] = ((c, r))
                
                # remove-se o match do antigo parceiro
                matchClasses2[matchR[0]] = False
                
                # aplica-se o match em 'c'
                matchClasses2[c] = True
        
    return M

#=====================================================
#       ENTRADAS E SAIDAS
#=====================================================
# Entrada com a quantidade N de jogadores
# O valor precisa ser maior que 0 e menor que 17
N = int(input('Insira a quantidade de jogadores '))
while N <= 0 or N > 16:
    N = int(input('Valor invalido, insira novamente '))

# Lista que armazenara o nome dos jogadores que irao jogar
listaJogadores = []
for i in range(N):
    listaJogadores.append(input())

# Uma posicao aleatoria gerada para ser passada a funcao 'organizarClasses'
pos = random.randrange(1, 16)

# Chamada da funcao
organizarClasses(pos, 16-N)

# Variavel para armazenar a lista de matches
Match = GaleShapley()

# Gerando N nomes aleatorios
listaNomes = []
contador = 0
while contador < N:
    nome = nomePersonagem()
    if nome not in listaNomes:
        listaNomes.append(nome)
        contador += 1

# Imprimindo as informacoes de cada jogador
for i in range(len(Match)):
    print('===============================================================')
    print('Nome do Personagem:', listaNomes[i], '- Jogador:', listaJogadores[i]) 
    print('Raca:', Match[i][1], '- Classe:', Match[i][0])
print('===============================================================')
