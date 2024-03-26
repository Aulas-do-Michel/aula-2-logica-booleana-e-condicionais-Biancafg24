"""
#### Exercício 3 - Identificar se a variante está no gene BRCA1 - Versão 2.

Receba 3 inputs do usuário:
1) O cromossomo de uma variante. Ele virá escrito como texto e da seguinte forma "chr1", "chr2", etc.
2) A posição dessa variante. Será um número inteiro.
3) O genoma de referência dessa variante. Considere só 2 opções possíveis, "hg19" e "hg38".

Responda:
"Sim" se ela estiver no BRCA1.
"Não" se ela não estiver.

Considere que a variante está no gene BRCA1 se estiver no cromossomo 17 (chr17), e:
1) Se a posição estiver no intevalo de 41196312 a 41277500, caso o genoma de referência seja o "hg19".
2) Se a posição estiver no intevalo de 43044295 a 43125483, caso o genoma de referência seja o "hg38".

Obs: Tirei a Location daqui: https://grch37.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012048;r=17:41196312-41277500

cromossomo = input("Digite o cromossomo da variante (ex: chr17): ")
posicao = int(input("Digite a posição da variante: "))
genoma_referencia = input("Digite o genoma de referência da variante (hg19 ou hg38): ")

if cromossomo == "chr17":
    if genoma_referencia == "hg19" and 41196312 <= posicao <= 41277500:
        print("Sim, a variante está no gene BRCA1.")
    elif genoma_referencia == "hg38" and 43044295 <= posicao <= 43125483:
        print("Sim, a variante está no gene BRCA1.")
else:
        print("Não, a variante não está no gene BRCA1.")
