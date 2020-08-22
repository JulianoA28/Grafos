import random

#=====================================================
#       ESTRUTURAS DE DADOS
#=====================================================

''' A seguir:
    Duas Listas com nomes retirados dos jogos DotA e Dark Souls III
    Esses nomes serao utilizados para gerar nomes de personagens de forma aleatoria com a funcao 'nomePersonagem'
'''
PrimeiroNome = ['Daelin', 'Rexxar', 'Bradwarden', 'Raigor', 'Purist', 'Mangix', 'Sven', 'Tiny', 'Tauren', 'Io', 'Razzil',
                'Strygwyr', 'Clinkz', 'Anub', 'Mortred', 'Nevermore', 'Mercurial', 'Lesale', 'Magina', 'Kardel', 'Artorias', 
                'Yurnero', 'Syllasbear', 'Luna', 'Moorphling', 'Mirana', 'Jahrakal', 'Aurel', 'Atropos', 'Ishkafel', 
                'Krobelus', 'Lion', 'Darchrow', 'Kel', 'Rotund', 'Pugna', 'Harbinger', 'Akasha', 'Demnok', 'Eredar', 
                'Rylai', 'Aiushtha', 'Puck', 'Chen', 'Ezalor', 'Zeus', 'Furion', 'Nortrom', 'Lina', 'Raijin', 'Alleria', 
                'Thrall', 'Mogul', 'Nessaj', 'Lucifer', 'Naix', 'Abaddon', 'Banehallow', 'Balanar', 'Azgalor', 'Pudge', 
                'King', 'Slardar', 'Traxex', 'Lanaya', 'Shendelzare', 'Darkterror', 'Medusa', 'Arc', 'Knight', 'Rigwarl', 
                'Icarus', 'Ymir', 'Tresdin', 'Rizzrak', 'Kaolin', 'Aggron', 'Barathrum', 'Razor', 'Crixalis', 'Squee', 
                'Jakiro', 'Boush', 'Rhasta', 'Rubick', 'Dragonus', 'Nerif', 'Jinzakk', 'Dazzle', 'Kael', 'Visage', 
                'Leshrac', 'Voljin', 'Kaldr', 'Huskar', 'Terror', 'Greirat', 'Yoel', 'Yuria', 'Siegward', 'Joseph']

# Possui algumas strings vazias para gerar nomes simples, somente com o da primeira lista
SegundoNome = ['Proudmoore', 'Stonehoof', 'Thunderwrath', 'Chieftain', 'Rooftrellen', 'Arak', 'Seran', 'Deathbringer',
               'Viper', 'Meepo', 'Sharpeye', 'Moonfang', 'Slithice', 'Azwraith', 'Nightshade', 'Rikimaru', 'Vlaicu',
               'Thuzad', 'Jere', 'Lannik', 'Lannik', 'Auroth', 'Crestfall', 'Inverse', 'Thunderkeg', 'Kahn', 'Leoric',
               'Dirge', 'Ulfsaar', 'Silkwood', 'Gondar', 'Xin', 'Razor', 'Slark', 'Rattletrap', 'Davion','Leviathan', 
               'Magnus', 'Spleen', 'Blade', 'de Catarina', 'do Assentamento dos Mortos-Vivos', 'do Abismo', 'de Carim', 
               'de Lothric', 'de Lavras', '', '', '', '', '', '', '', '', '', '', '', '', '']

# Lista contendo o nome de todas as classes que sera utilizada pela funcao organizarClasses
listaClasses = ['bruxo', 'feiticeiro', 'mago', 'barbaro', 'bardo', 'bucaneiro', 'cacador', 'cavaleiro', 'clerigo',
               'druida', 'guerreiro', 'inventor', 'ladino', 'lutador', 'nobre', 'paladino']

# Dicionario que representa as propostas de cada classe
# Estrutura:
# Chave : { Outro Dicionario }
# Chave == Classe
# Outro Dicionario -> possui a lista de preferencia e um bool para ver se ja houve uma proposta entre os dois
# Exemplo: Na primeira chave, a classe 'bruxo' nao propos um match para a raca 'elfo' e nem para todas as outras
matchClasses = {
'bruxo' : {'elfo' : False, 'goblin' : False, 'kliren' : False, 'suraggel' : False, 'qareen' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'anao' : False, 'golem' : False, 'hynne' : False, 'medusa' : False, 'silfide' : False, 'minotauro' : False, 'dahllan' : False, 'trog' : False},
'feiticeiro' : {'medusa' : False, 'qareen' : False, 'hynne' : False, 'kliren' : False, 'silfide' : False, 'dahllan' : False, 'anao' : False, 'humano' : False, 'tritao' : False, 'osteon' : False, 'elfo' : False, 'suraggel' : False, 'trog' : False, 'minotauro' : False, 'lefou' : False, 'goblin' : False, 'golem' : False},
'mago' : {'elfo' : False, 'goblin' : False, 'kliren' : False, 'suraggel' : False, 'qareen' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'anao' : False, 'golem' : False, 'hynne' : False, 'medusa' : False, 'silfide' : False, 'minotauro' : False, 'dahllan' : False, 'trog' : False},
'barbaro' : {'minotauro' : False, 'golem' : False, 'trog' : False, 'anao' : False, 'goblin' : False, 'suraggel' : False, 'dahllan' : False, 'medusa' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'qareen' : False, 'elfo' : False, 'hynne' : False, 'silfide' : False, 'kliren' : False},
'bardo' : {'medusa' : False, 'qareen' : False, 'hynne' : False, 'silfide' : False, 'kliren' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'suraggel' : False, 'elfo' : False, 'dahllan' : False, 'anao' : False, 'minotauro' : False, 'trog' : False, 'goblin' : False, 'golem' : False},
'bucaneiro' : {'hynne' : False, 'silfide' : False, 'medusa' : False, 'suraggel' : False, 'goblin' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'dahllan' : False, 'elfo' : False, 'qareen' : False, 'kliren' : False, 'minotauro' : False, 'trog' : False, 'golem' : False, 'anao' : False},
'cacador' : {'goblin' : False, 'hynne' : False, 'silfide' : False, 'suraggel' : False, 'dahllan' : False, 'elfo' : False, 'medusa' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'golem' : False, 'kliren' : False, 'trog' : False, 'minotauro' : False, 'qareen' : False, 'anao' : False},
'cavaleiro' : {'minotauro' : False, 'golem' : False, 'trog' : False, 'anao' : False, 'goblin' : False, 'suraggel' : False, 'dahllan' : False, 'medusa' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'qareen' : False, 'elfo' : False, 'hynne' : False, 'silfide' : False, 'kliren' : False},
'clerigo' : {'anao' : False, 'dahllan' : False, 'golem' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'trog' : False, 'elfo' : False, 'goblin' : False, 'medusa' : False, 'suraggel' : False, 'hynne' : False, 'kliren' : False, 'silfide' : False, 'minotauro' : False, 'qareen' : False},
'druida' : {'dahllan' : False, 'goblin' : False, 'hynne' : False, 'silfide' : False, 'suraggel' : False, 'elfo' : False, 'medusa' : False, 'anao' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'kliren' : False, 'golem' : False, 'trog' : False, 'minotauro' : False, 'qareen' : False},
'guerreiro' : {'minotauro' : False, 'golem' : False, 'trog' : False, 'anao' : False, 'goblin' : False, 'suraggel' : False, 'dahllan' : False, 'medusa' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'qareen' : False, 'elfo' : False, 'hynne' : False, 'silfide' : False, 'kliren' : False},
'inventor' : {'elfo' : False, 'goblin' : False, 'kliren' : False, 'suraggel' : False, 'qareen' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'anao' : False, 'golem' : False, 'hynne' : False, 'medusa' : False, 'silfide' : False, 'minotauro' : False, 'dahllan' : False, 'trog' : False},
'ladino' : {'goblin' : False, 'hynne' : False, 'silfide' : False, 'suraggel' : False, 'dahllan' : False, 'elfo' : False, 'medusa' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'golem' : False, 'kliren' : False, 'trog' : False, 'minotauro' : False, 'qareen' : False, 'anao' : False},
'lutador' : {'minotauro' : False, 'golem' : False, 'trog' : False, 'anao' : False, 'goblin' : False, 'suraggel' : False, 'dahllan' : False, 'medusa' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'qareen' : False, 'elfo' : False, 'hynne' : False, 'silfide' : False, 'kliren' : False},
'nobre' : {'medusa' : False, 'qareen' : False, 'hynne' : False, 'kliren' : False, 'silfide' : False, 'dahllan' : False, 'anao' : False, 'humano' : False, 'tritao' : False, 'osteon' : False, 'elfo' : False, 'suraggel' : False, 'trog' : False, 'minotauro' : False, 'lefou' : False, 'goblin' : False, 'golem' : False},
'paladino' : {'qareen' : False, 'medusa' : False, 'humano' : False, 'lefou' : False, 'tritao' : False, 'osteon' : False, 'minotauro' : False, 'trog' : False, 'hynne' : False, 'kliren' : False, 'anao' : False, 'dahllan' : False, 'elfo' : False, 'suraggel' : False, 'golem' : False, 'goblin' : False, 'silfide' : False} 
}

# Dicionario que representa se a classe possui match ou nao (True para Match)
# Esse dicionario tambem sera utilizado para remover algumas classes para se adequar a quantidade de jogadores
# A remocao sera feita transformando em True, valores aleatorios antes da execucao do algoritmo
matchClasses2 = {
'bruxo': False,
'feiticeiro': False,
'mago': False,
'barbaro': False,
'bardo': False,
'bucaneiro': False,
'cacador': False,
'cavaleiro': False,
'clerigo': False,
'druida': False,
'guerreiro': False,
'inventor': False,
'ladino': False,
'lutador': False,
'nobre': False,
'paladino': False 
}

# Listas de preferencia de cada raca
Humano = ['bruxo', 'mago', 'feiticeiro', 'barbaro', 'bardo', 'bucaneiro', 'cacador', 'cavaleiro', 'clerigo', 'druida', 'guerreiro', 'inventor', 'ladino', 'lutador', 'nobre', 'paladino'] 
Anao = ['clerigo', 'barbaro', 'druida', 'cacador', 'guerreiro', 'lutador', 'paladino', 'cavaleiro', 'inventor', 'ladino', 'bruxo', 'mago', 'feiticeiro', 'bardo', 'bucaneiro', 'nobre']
Dahllan = ['druida', 'cacador', 'clerigo', 'ladino', 'bucaneiro', 'bardo', 'lutador', 'barbaro', 'guerreiro', 'paladino', 'inventor', 'mago', 'feiticeiro', 'bruxo', 'cavaleiro', 'nobre']
Elfo = ['mago', 'bruxo', 'inventor', 'ladino', 'bardo', 'cacador', 'bucaneiro', 'cavaleiro', 'guerreiro', 'feiticeiro', 'nobre', 'paladino', 'clerigo', 'druida', 'lutador', 'barbaro']
Goblin = ['ladino', 'inventor', 'cacador', 'bruxo', 'mago', 'bucaneiro', 'bardo', 'druida', 'guerreiro', 'lutador', 'barbaro', 'cavaleiro', 'clerigo', 'paladino', 'nobre', 'feiticeiro']
Lefou = ['bruxo', 'mago', 'barbaro', 'cacador', 'cavaleiro', 'clerigo', 'druida', 'guerreiro', 'inventor', 'ladino', 'lutador', 'bucaneiro', 'nobre', 'paladino', 'feiticeiro', 'bardo']
Minotauro = ['barbaro', 'guerreiro', 'lutador', 'cavaleiro', 'paladino', 'clerigo', 'druida', 'ladino', 'cacador', 'bardo', 'bucaneiro', 'bruxo', 'mago', 'inventor', 'feiticeiro', 'nobre']
Qareen = ['bardo', 'feiticeiro', 'bruxo', 'mago', 'bucaneiro', 'nobre', 'paladino', 'inventor', 'clerigo', 'ladino', 'cacador', 'druida', 'barbaro', 'guerreiro', 'lutador', 'cavaleiro']
Golem = ['barbaro', 'guerreiro', 'lutador', 'cavaleiro', 'paladino', 'druida', 'clerigo', 'cacador', 'ladino', 'bucaneiro', 'inventor', 'bruxo', 'mago', 'feiticeiro', 'nobre', 'bardo']
Hynne = ['bucaneiro', 'bardo', 'ladino', 'feiticeiro', 'nobre', 'cacador', 'paladino', 'druida', 'clerigo', 'mago', 'bruxo', 'inventor', 'cavaleiro', 'guerreiro', 'barbaro', 'lutador']
Kliren = ['inventor', 'mago', 'bruxo', 'feiticeiro', 'nobre', 'bardo', 'paladino', 'bucaneiro', 'ladino', 'clerigo', 'druida', 'cacador', 'cavaleiro', 'guerreiro', 'barbaro', 'lutador']
Medusa = ['bucaneiro', 'bardo', 'feiticeiro', 'nobre', 'ladino', 'cacador', 'paladino', 'clerigo', 'bruxo', 'mago', 'inventor', 'druida', 'guerreiro', 'barbaro', 'lutador', 'cavaleiro']
Osteon = ['bruxo', 'mago', 'feiticeiro', 'bardo', 'bucaneiro', 'cacador', 'clerigo', 'druida', 'inventor', 'ladino', 'nobre', 'paladino', 'cavaleiro', 'guerreiro', 'lutador', 'barbaro']
Tritao = ['bruxo', 'mago', 'feiticeiro', 'barbaro', 'bardo', 'bucaneiro', 'cacador', 'cavaleiro', 'clerigo', 'druida', 'guerreiro', 'inventor', 'ladino', 'lutador', 'nobre', 'paladino']
Silfide = ['bardo', 'feiticeiro', 'nobre', 'bucaneiro', 'paladino', 'ladino', 'cacador', 'druida', 'bruxo', 'mago', 'inventor', 'clerigo', 'guerreiro', 'cavaleiro', 'lutador', 'barbaro']
Suraggel = ['clerigo', 'druida', 'cacador', 'ladino', 'bardo', 'bucaneiro', 'feiticeiro', 'nobre', 'paladino', 'bruxo', 'mago', 'inventor', 'guerreiro', 'cavaleiro', 'lutador', 'barbaro']
Trog = ['barbaro', 'guerreiro', 'lutador', 'cavaleiro', 'paladino', 'druida', 'clerigo', 'cacador', 'ladino', 'bucaneiro', 'feiticeiro', 'nobre', 'bardo', 'inventor', 'bruxo', 'mago']

# Dicionario que guarda as listas de preferencia de cada raca
dicionarioRacas = {
'humano': Humano,
'anao': Anao,
'dahllan': Dahllan,
'elfo': Elfo,
'goblin': Goblin,
'lefou': Lefou,
'minotauro' : Minotauro,
'qareen' : Qareen,
'golem' : Golem,
'hynne' : Hynne,
'kliren' : Kliren,
'medusa' : Medusa,
'osteon' : Osteon,
'tritao' : Tritao,
'silfide' : Silfide,
'suraggel' : Suraggel,
'trog' : Trog }

#=====================================================
#       FUNCOES
#=====================================================

# Funcao que ira gerar um nome aleatorio a partir das listas ('PrimeiroNome' e 'SegundoNome')
def nomePersonagem():
    primeiro = random.choice(PrimeiroNome)
    segundo = random.choice(SegundoNome)
    
    if segundo == '':
        return primeiro
    else:
        return (primeiro + ' ' + segundo)

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

# Funcao para restaurar todos os valores do dicionario matchClasses2 para False e assim executar novos exemplos
# E utilizada pois as vezes, o matchClasses2 nao e restaurado corretamente
def restaurar():
    for chave in matchClasses2:
        matchClasses2[chave] = False

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
            novo = posicao(c, dicionarioRacas[r])
            
            # atual <- posicao do match atual de 'r' na lista
            atual = posicao(matchR[0], dicionarioRacas[r])
            
            # Se a posicao de 'c' for prioritaria a do atual match, entao substitui-se o parceiro de 'r' 
            if novo < atual:
                # novo match
                M[pos] = ((c, r))
                
                # remove-se o match do antigo parceiro
                matchClasses2[matchR[0]] = False
                
                # aplica-se o match em 'c'
                matchClasses2[c] = True
        
    return M

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
    # Entrada com o nome de N jogadores
    listaJogadores.append(input())
    
# Chamada da funcao
restaurar()

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

# Impressao das informacoes de cada jogador
for i in range(len(Match)):
    print('===============================================================')
    print('Nome do Personagem:', listaNomes[i], '- Jogador:', listaJogadores[i])
    print('Raca:', Match[i][1], '- Classe:', Match[i][0])
print('===============================================================')
