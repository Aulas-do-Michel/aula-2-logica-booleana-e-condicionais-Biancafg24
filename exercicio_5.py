#
### Exercício 5 - Analisador de Variantes Genéticas.

#Você está analisando uma variante genética e precisa saber se ela é relevante para análise ou não.

#Obs: Esse exercício é uma simplificação!

#Você vai receber 5 parametros:

#1) Frequência Populacional: Frequencia da variante na população em porcentagem. Será um float de 0 a 100.
#2) Gene: Gene da variante. Será um texto. Exemplo: "BRCA1", "BOLA1", "HFE", etc.
#3) Impacto: Se ela está numa posição de impacto ALTO ou BAIXO. Será um texto, necessariamente ou "ALTO" ou "BAIXO".
#4) Reads: Quantidade de reads da variante. Será um número inteiro.
#5) Vaf: Frequencia alélica da variante. Será um float de 0 a 100.

#A primeira coisa é tomar cuidado com a qualidade da leitura. 

#Se a variante tiver menos de 10 reads OU uma frequência alélica abaixo de 20% a gente vai dizer que ela não é relevante, pois deve ser um artefato.

#Se ela não for um artefato temos que avaliar as seguintes coisas:

#1) Ela só vai ser relevante se o impacto for ALTO.

#2) Ela não vai ser relevante se a frequência dela for maior que 5%, a não ser que esteja nos seguintes genes de exceção: "HFE", "MEFV" ou "GJB2".

#Obs: Uma resolução desse exercício está no Colab da Aula 02. Tente primeiro fazer sozinho! 
#Se não passar nos testes, qualquer coisa consulte lá depois para ver o que você poderia ter feito diferente.

frequencia_populacional = float(input('Digite a frequencia populacional (em porcentagem):'))
gene = input('Digite o gene:')
impacto = input('Digite o Impacto (ALTO ou BAIXO):')
reads = int(input('Digite os reads:'))
frequencia_alelica = float(input('Digite a frequencia alélica (em porcentagem):'))

if reads < 10 or frequencia alelica < 20:
    print('Não é relevante')
elif impacto == 'ALTO':
    print('É relevante')
elif frequencia_alelica > 5 and gene != "HFE" and gene != "MEFV" and gene =! "GJB2":
    print('Não é relevante')
else:
    ('Não é relevante')


        
