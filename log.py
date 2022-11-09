#início função dimensoesObjeto
def dimensoesObjeto():
while True:
try:
altura = float(input('Digite a altura do objeto (em cm): '))
comp = float(input('Digite o comprimento do objeto (em cm): '))
larg = float(input('Digite a largura do objeto (em cm): '))
volume = altura * comp * larg
print('O volume do objeto é (em cm³): {}'.format(volume))
if (volume = 1) and (volume = 1000):
return 10 #valores retornados conforme a tabela em R$
elif (volume > 1001) and (volume = 10000):
return 20
elif (volume > 10001) and (volume = 30000):
return 30
elif (volume > 30001) and (volume = 100000):
return 50
else:
print('Não aceitamos objetos com essas dimensões.')
#Qualquer objeto acima de 100.000 de volume, conforme a tabela 1
continue
except ValueError: #Caso digite algum caractere que não seja número
print('Caractere inválido. Tente novamente.')
continue
#fim da função dimensoesObjeto
#início função pesoObjeto
def pesoObjeto():
while True:
try:
pesoO = float(input('Digite o peso do objeto (em kg): '))
if (pesoO = 0.1):
return 1.0 #retornando os multiplicadores conforme a tabela
2
elif (pesoO = 0.11) and (pesoO = 1):
return 1.5
elif (pesoO = 1.10) and (pesoO = 10):
return 2.0
elif (pesoO = 10.1) and (pesoO = 30):
return 3.0
else:
print('Não aceitamos objetos tão pesados.\nEntre com o peso
desejado novamente.') #Objetos acima de 30kg não serão aceitos
continue
except ValueError:
print('Você digitou o peso do objeto com valor não numérico
\nPor favor entre com o peso desejado novamente.')
continue
#fim da função pesoObjeto
#início função rotaObjeto
def rotaObjeto():
while True:
rotaO = input('Selecione a rota:\nBR - De Brasília para Rio de
Janeiro\nBS - De Brasília para São Paulo\nRB - De Rio de Janeiro para
Brasília\nRS - De Rio de Janeiro para São Paulo\nSR - De São Paulo para Rio
de Janeiro\nSB - De São Paulo Para Brasília\n >')
if (rotaO = 'BR'):
return 1.5 #Multiplicador conforme a tabela 3
elif (rotaO = 'BS'):
return 1.2
elif (rotaO = 'RB'):
return 1.5
elif (rotaO = 'RS'):
return 1
elif (rotaO = 'SR'):
return 1
elif (rotaO = 'SB'):
return 1.2
else:
print('Você Digitou uma rota que não existe\nPor favor entre com
a rota novamente')
#fim função rotaObjeto
#início programa
nico4022326 = 'Nícolas Vinícius Lobo Morais'
print('Bem Vindo a Compainha de Logística {}.'.format(nico4022326))
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota #Equação dada no enunciado
print('Total a pagar: R$ {:.2f}'.format(total), '(dimensões: {} * peso: {}
* rota: {})'.format(dimensoes, peso, rota))
