# Faça um programa qua leia uma Frase palo teclado e mostra:
# Quantas vezas aparaca a latra "A"
# Em qual posição ela aparece a primeira vez.
# Em qual posição ela aparace a última vez.

frase = str(input('Digite uma frase: ')).upper()
print('a letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição: {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição: {}'.format(frase.rfind('A')+1))
