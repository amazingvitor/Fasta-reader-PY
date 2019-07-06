def fileCheck(fileName):
    try:
        # Var do arquivo ja verificado
        file = open(fileName)
        # Fechando o arquivo
        file.close()
    except IOError:
        print ('Arquivo nao achado, tente de novo.')
        main()

def main():

    desc = []
    seq = []
    soma = 0
    sums = []

    # Nome do arquivo FASTA
    fileName = raw_input('Coloque o nome do arquivo, incluindo o .fasta: ')
    fileCheck(fileName)

    content = open(fileName, 'r')
    line = content.readline()

    while line:
        line = line.rstrip('\n')
        if '>' in line:
            desc.append(line)
        else:
            seq.append(line)
        line = content.readline()

    content.close()

    for word in seq:
        for letters in word:
            if letters == "A":
                soma += 71.037
            elif letters == "R":
                soma += 156.101
            elif letters == "N":
                soma += 114.042
            elif letters == "D":
                soma += 115.026
            elif letters == "C":
                soma += 103.009
            elif letters == "E":
                soma += 129.042
            elif letters == "Q":
                soma += 128.058
            elif letters == "G":
                soma += 57.021
            elif letters == "H":
                soma += 137.058
            elif letters == "I":
                soma += 113.084
            elif letters == "L":
                soma += 113.084
            elif letters == "K":
                soma += 128.094
            elif letters == "M":
                soma += 131.040
            elif letters == "F":
                soma += 147.068
            elif letters == "P":
                soma += 97.052
            elif letters == "S":
                soma += 87.032
            elif letters == "T":
                soma += 101.047
            elif letters == "W":
                soma += 186.079
            elif letters == "Y":
                soma += 163.063
            elif letters == "V":
                soma += 99.068
        sums.append(soma)
        soma = 0

    tamanhoLista = len(sums)

    for i in range(0, tamanhoLista):
        print (str(sums[i]) + ' | ' + str(desc[i]) + ' | ' + str(seq[i]))







# Run
main()
