loja_fruta={
    'marca':2.40,
    'banana':3.60,
    'uva':7.60

}


# função get: método usado para acessar o valor jem dinheiro ->
preco_uva = loja_fruta.get('uva',{})
print('uva:',preco_uva)
#função update: método usado para atualizar os valores
loja_fruta.update({'uva': 8.90,'tomate':10})
print(loja_fruta,'#tomate adicionado')
# função pop: método para remover uma chave específica de um diciónario e retornar o valor associado a ela.
loja_fruta.pop('tomate')
print(loja_fruta,'#tomateremovido')
#função itemns: método de leitura de um diciónario, que separa Key e value de mesmo.
for chave, valor in loja_fruta.items():
  print(f'key: {chave}: value: {valor}')
