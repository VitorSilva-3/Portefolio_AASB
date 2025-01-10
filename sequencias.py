
def validacao_dna(sequencia):
    """
    Função que valida se uma determinada sequência é uma sequência de DNA
    
    """
    if not sequencia:
        return "Não é uma sequência válida de DNA"       #averigua se a sequência está vazia

    sequencia = sequencia.upper()                        #converte os caracteres da sequência em maiúsculas
    bases = ["A", "T", "C", "G"]                         #lista com todas as bases azotadas do DNA

    for base in sequencia:                               #averigua se as bases estão na sequência
        if base not in bases:
            return "Não é uma sequência válida de DNA"
    return "É uma sequência válida de DNA"

def contar_bases(sequencia):
    """
    Função que recebe uma sequência de DNA e imprime o número de ocorrências de A, C, G e T.

    """
    bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}            #dicionário que contém as bases
    
    for base in sequencia.upper():                      #contar as ocorrências de cada base
        if base in bases:
            bases[base] += 1
    
    for base, quantidade in bases.items():              #imprimir o número de cada base
        print(f"{base}: {quantidade}")

def frequencia_bases(sequencia):
    """
    Função que recebe uma sequência de DNA e imprime a frequência de A, C, G e T.

    """
    bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}                            #dicionário que contém as bases
    
    tamanho = len(sequencia)
    
    for base in sequencia.upper():                                      #contar as ocorrências de cada base
        if base in bases:
            bases[base] += 1
    
    for base, quantidade in bases.items():                              #imprimir a frequência de cada base
        frequencia = quantidade / tamanho if tamanho > 0 else 0
        print(f"{base}: {frequencia:.2f}")

def complemento_inverso(sequencia):
    """
    Função que recebe uma sequência de DNA e retorna o seu complemento inverso

    """
    complementares = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}               #dicionário com as bases complementares de cada base

    sequencia_inversa = sequencia.upper()[::-1]                             #inverte a sequência e muda para maiúsculas

    return ''.join(complementares[base] for base in sequencia_inversa)      #gera o complemento inverso 

def dna_para_rna(sequencia):
    """
    Função que recebe uma sequência de DNA  e retorna a cadeia de RNA correspondente

    """
    rna = sequencia.upper().replace("T", "U")        #mete a sequência em maiúsculas e substitui a Timina por Uracilo
    
    return rna

def dividir_codoes(sequencia):
    """
    Função que recebe uma sequência de DNA e retorna uma lista de codões

    """
    seq_maiusculas = sequencia.upper()             #mete a sequência em maiúsculas
    codoes = []                                    #lista para armazenar os codões
    
    for i in range(0, len(seq_maiusculas), 3):     #percorre a sequência de em passos de 3
        codao = seq_maiusculas[i:i+3]              #pega o codão de 3 nucleotídeos
        if len(codao) == 3:                        #adiciona o codão à lista se tiver 3 nucleotídeos
            codoes.append(codao)
    
    return codoes

def dna_para_proteina(sequencia):
    """
    Função que recebe uma sequência de DNA e retorna os respetivos aminoácidos de cada codão de forma a formar uma proteína

    """
    codigo_genetico = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                       "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                       "TAT":"Y", "TAC":"Y", "TAA":"_", "TAG":"_",
                       "TGT":"C", "TGC":"C", "TGA":"_", "TGG":"W",
                       "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                       "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                       "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                       "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                       "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                       "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                       "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                       "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                       "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                       "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                       "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                       "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}                    #tabela representativa do códio genético
    
    seq_maiusculas = sequencia.upper()                                                #mete a sequência em maiúsculas

    codoes = [seq_maiusculas[i:i+3] for i in range(0, len(seq_maiusculas), 3)]        #percorre a sequência em passos de 3, extraindo os codões  

    proteina = [codigo_genetico.get(codao, "_") for codao in codoes]                  #tradução de cada codão para o seu aminoácido correspondente                                                    

    resultado = "".join(proteina)                                                     #junta os aminoácidos formando uma proteína            

    return resultado
