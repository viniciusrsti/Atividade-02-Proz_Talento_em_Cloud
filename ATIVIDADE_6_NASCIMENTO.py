nome = input("Digite seu nome:")
ano_nac = int (input("Digite o ano do seu nascimento:"))
ano_at = int (input("Digite o ano atual: "))
res = ano_at-ano_nac
if ano_nac < 1922  and ano_nac > 2021:
    print('Nao e possivel computar, pf digite o ano entre 1922 e 2021')
if (ano_nac > 1922):
    print('Seu nome e: {} E sua idade e: {} '.format(nome, res)) 
else:
    print('Valor não encontrado')
