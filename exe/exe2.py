loja_carros = {
'gol': {
'preco': 20000,
'cor': 'vermelho'
},
'corsa':{
'preco': 30000,
'cor': 'vermelho'
},
'fiatUno':{
'preco': 100000,
'cor': 'cinza'
},
}

for k,y in loja_carros.items():
loja_carros.get(k)['preco']*=1.15
print(loja_carros)

# função get: método usado para acessar o valor em um dicionário
preco_gol = loja_carros.get('gol',{})
print('gol:', preco_gol)

# função update: método usado para atualizar os valores do dicionário
loja_carros.update({'gol': 20000, 'ferrari': 56700})
print(loja_carros, '#ferrari adicionado')

loja_carros.pop('ferrari')
print(loja_carros, '#ferrari removido')

for chave, valor in loja_carros.items():
print(f'key: {chave}: value: {valor}')
	
