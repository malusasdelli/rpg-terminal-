player = {
    '1': {
        'nome': 'Nilson',
        'idade': 24,
        'ryos': 320.50,
        'classe': 'Mago',
        'familia': 'Loki',
        'habilidades': {
            'ataque': 10,
            'defesa': 5,
            'vida': 10
        },
        'nivel': 100,
        'xp': 0,
        'equipamentos': [2],
        'dungeon':1
    },
    '2': {
        'nome': 'Malu',
        'idade': 15,
        'ryos': 0.0,
        'classe': 'Guerreira',
        'familia': 'Sasdelli',
        'habilidades': {
            'ataque': 15,
            'defesa': 5,
            'vida': 5
        },
        'nivel': 1,
        'xp': 0,
        'equipamentos': [1],
        'dungeon':1
    }
}

equipamentos = {
    '1':{
        'nome': 'Espada de Madeira',
        'classe':'Guerreiro',
        'habilidades': {
            'ataque':1,
            'defesa':1,
            'vida':0,
        },
    },
    '2': {
        'nome': 'Livro Velho',
        'classe': 'Mago',
        'nivel':1,
        'habilidades': {
            'ataque': 1,
            'defesa': 0,
            'vida': 1,
            },
        },
    '3': {
        'nome':'Arco de Madeira',
        'classe':'Arqueiro',
        'habilidades':{
            'ataque': 2,
            'defesa':0,
            'vida':0,
            }
        }
    }

monstros = {
    1:{'nome':'Rato',
       'habilidade':{
           'ataque':1,
           'defesa':0,
           'vida':1}
       },

    2:{'nome':'Formiga',
       'habilidade':{
           'ataque':2,
           'defesa':2,
           'vida':1}
       }
}


def iniciar():
  print('Bem vindo ao RPG Terminal')
  id = str(input('Qual é o seu ID?: '))
  personagem = player[id]
  print(personagem['nome'])

  print('Menu\n1-Dungeon')

  escolha = input('Escolha uma opção:  ')
  if escolha == '1':
    print('Você entrou na Dungeon')
    explorarDungeon(personagem)

def explorarDungeon(player):
  print('Você está explorando a Dungeon no Andar: ',
    player.get11
     2('dungeon'))

iniciar()

def ativar_armas(player):
  if len(player.get('equipamentos')) == 0:
    print('Você não tem equipamentos no seu inventário')
    pass
  for i in player.get ('equipamentos'):
    if equipamentos.get(str(i)) == None:
      print('Você não tem equipamentos válidos no seu inventario')
    elif player.get('classe') == equipamentos.get(str(i)).get('classe'):
      print(f'Seu equipamento é um (a){equipamentos.get(str(i)).get('nome')}')
      for j, k in equipamentos.get (str(i)).get('habilidades').items():
        player.get('habilidades')[j] += k