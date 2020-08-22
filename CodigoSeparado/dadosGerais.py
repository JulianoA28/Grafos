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

# Lista para armazenar o nome de todas as racas - so e utilizada para facilitar a vizualicao
listaRacas = ['humano', 'anao', 'dahllan', 'elfo', 'goblin', 'lefou', 'minotauro', 'qareen', 'golem', 'hynne', 
              'kliren', 'medusa', 'osteon', 'tritao', 'silfide', 'suraggel', 'trog']

'''
Dicionario = se a raca possui um match
Lista com o nome das racas
Preferencias de cada raca
'''
matchRacas = {
'humano': {'bruxo' : False, 'mago' : False, 'feiticeiro' : False, 'barbaro' : False, 'bardo' : False, 'bucaneiro' : False, 'cacador' : False, 'cavaleiro' : False, 'clerigo' : False, 'druida' : False, 'guerreiro' : False, 'inventor' : False, 'ladino' : False, 'lutador' : False, 'nobre' : False, 'paladino': False},
'anao': {'clerigo' : False, 'barbaro' : False, 'druida' : False, 'cacador' : False, 'guerreiro' : False, 'lutador' : False, 'paladino' : False, 'cavaleiro' : False, 'inventor' : False, 'ladino' : False, 'bruxo' : False, 'mago' : False, 'feiticeiro' : False, 'bardo' : False, 'bucaneiro' : False, 'nobre': False},
'dahllan': {'druida' : False, 'cacador' : False, 'clerigo' : False, 'ladino' : False, 'bucaneiro' : False, 'bardo' : False, 'lutador' : False, 'barbaro' : False, 'guerreiro' : False, 'paladino' : False, 'inventor' : False, 'mago' : False, 'feiticeiro' : False, 'bruxo' : False, 'cavaleiro' : False, 'nobre': False},
'elfo': {'mago' : False, 'bruxo' : False, 'inventor' : False, 'ladino' : False, 'bardo' : False, 'cacador' : False, 'bucaneiro' : False, 'cavaleiro' : False, 'guerreiro' : False, 'feiticeiro' : False, 'nobre' : False, 'paladino' : False, 'clerigo' : False, 'druida' : False, 'lutador' : False, 'barbaro' : False},
'goblin': {'ladino' : False, 'inventor' : False, 'cacador' : False, 'bruxo' : False, 'mago' : False, 'bucaneiro' : False, 'bardo' : False, 'druida' : False, 'guerreiro' : False, 'lutador' : False, 'barbaro' : False, 'cavaleiro' : False, 'clerigo' : False, 'paladino' : False, 'nobre' : False, 'feiticeiro' : False},
'lefou': {'bruxo' : False, 'mago' : False, 'barbaro' : False, 'cacador' : False, 'cavaleiro' : False, 'clerigo' : False, 'druida' : False, 'guerreiro' : False, 'inventor' : False, 'ladino' : False, 'lutador' : False, 'bucaneiro' : False, 'nobre' : False, 'paladino' : False, 'feiticeiro' : False, 'bardo' : False},
'minotauro' : {'barbaro' : False, 'guerreiro' : False, 'lutador' : False, 'cavaleiro' : False, 'paladino' : False, 'clerigo' : False, 'druida' : False, 'ladino' : False, 'cacador' : False, 'bardo' : False, 'bucaneiro' : False, 'bruxo' : False, 'mago' : False, 'inventor' : False, 'feiticeiro' : False, 'nobre' : False},
'qareen' : {'bardo' : False, 'feiticeiro' : False, 'bruxo' : False, 'mago' : False, 'bucaneiro' : False, 'nobre' : False, 'paladino' : False, 'inventor' : False, 'clerigo' : False, 'ladino' : False, 'cacador' : False, 'druida' : False, 'barbaro' : False, 'guerreiro' : False, 'lutador' : False, 'cavaleiro' : False},
'golem' : {'barbaro' : False, 'guerreiro' : False, 'lutador' : False, 'cavaleiro' : False, 'paladino' : False, 'druida' : False, 'clerigo' : False, 'cacador' : False, 'ladino' : False, 'bucaneiro' : False, 'inventor' : False, 'bruxo' : False, 'mago' : False, 'feiticeiro' : False, 'nobre' : False, 'bardo' : False},
'hynne' : {'bucaneiro' : False, 'bardo' : False, 'ladino' : False, 'feiticeiro' : False, 'nobre' : False, 'cacador' : False, 'paladino' : False, 'druida' : False, 'clerigo' : False, 'mago' : False, 'bruxo' : False, 'inventor' : False, 'cavaleiro' : False, 'guerreiro' : False, 'barbaro' : False, 'lutador' : False},
'kliren' : {'inventor' : False, 'mago' : False, 'bruxo' : False, 'feiticeiro' : False, 'nobre' : False, 'bardo' : False, 'paladino' : False, 'bucaneiro' : False, 'ladino' : False, 'clerigo' : False, 'druida' : False, 'cacador' : False, 'cavaleiro' : False, 'guerreiro' : False, 'barbaro' : False, 'lutador' : False},
'medusa' : {'bucaneiro' : False, 'bardo' : False, 'feiticeiro' : False, 'nobre' : False, 'ladino' : False, 'cacador' : False, 'paladino' : False, 'clerigo' : False, 'bruxo' : False, 'mago' : False, 'inventor' : False, 'druida' : False, 'guerreiro' : False, 'barbaro' : False, 'lutador' : False, 'cavaleiro' : False},
'osteon' : {'bruxo' : False, 'mago' : False, 'feiticeiro' : False, 'bardo' : False, 'bucaneiro' : False, 'cacador' : False, 'clerigo' : False, 'druida' : False, 'inventor' : False, 'ladino' : False, 'nobre' : False, 'paladino' : False, 'cavaleiro' : False, 'guerreiro' : False, 'lutador' : False, 'barbaro' : False},
'tritao' : {'bruxo' : False, 'mago' : False, 'feiticeiro' : False, 'barbaro' : False, 'bardo' : False, 'bucaneiro' : False, 'cacador' : False, 'cavaleiro' : False, 'clerigo' : False, 'druida' : False, 'guerreiro' : False, 'inventor' : False, 'ladino' : False, 'lutador' : False, 'nobre' : False, 'paladino' : False},
'silfide' : {'bardo' : False, 'feiticeiro' : False, 'nobre' : False, 'bucaneiro' : False, 'paladino' : False, 'ladino' : False, 'cacador' : False, 'druida' : False, 'bruxo' : False, 'mago' : False, 'inventor' : False, 'clerigo' : False, 'guerreiro' : False, 'cavaleiro' : False, 'lutador' : False, 'barbaro' : False},
'suraggel' : {'clerigo' : False, 'druida' : False, 'cacador' : False, 'ladino' : False, 'bardo' : False, 'bucaneiro' : False, 'feiticeiro' : False, 'nobre' : False, 'paladino' : False, 'bruxo' : False, 'mago' : False, 'inventor' : False, 'guerreiro' : False, 'cavaleiro' : False, 'lutador' : False, 'barbaro' : False},
'trog' : {'barbaro' : False, 'guerreiro' : False, 'lutador' : False, 'cavaleiro' : False, 'paladino' : False, 'druida' : False, 'clerigo' : False, 'cacador' : False, 'ladino' : False, 'bucaneiro' : False, 'feiticeiro' : False, 'nobre' : False, 'bardo' : False, 'inventor' : False, 'bruxo' : False, 'mago' : False}
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
