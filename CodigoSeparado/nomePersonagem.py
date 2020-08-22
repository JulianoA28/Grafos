import random

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


# Funcao que ira gerar um nome aleatorio a partir das listas ('PrimeiroNome' e 'SegundoNome')
def nomePersonagem():
    primeiro = random.choice(PrimeiroNome)
    segundo = random.choice(SegundoNome)
    
    if segundo == '':
        return primeiro
    else:
        return (primeiro + ' ' + segundo)
    