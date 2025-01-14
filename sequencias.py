
def validacao_dna(sequencia: str) -> str:
    """
    @brief Verifica se uma sequência fornecida é uma sequência válida de DNA.

    @details Uma sequência de DNA é considerada válida se:
             - Não estiver vazia.
             - Contiver apenas os caracteres 'A', 'T', 'C' e 'G', que representam as bases azotadas do DNA.

    @param sequencia Uma string representando a sequência de DNA a ser validada.

    @return Uma string indicando se a sequência é válida ou não.
            - "É uma sequência válida de DNA" se todos os critérios forem atendidos.
            - "Não é uma sequência válida de DNA" caso contrário.

    @note A validação é insensível a maiúsculas e minúsculas, pois a sequência é convertida para letras maiúsculas antes da verificação.

    @code
    // Exemplos de uso:
    validacao_dna("ATCG"); // Retorna "É uma sequência válida de DNA"
    validacao_dna("atcg"); // Retorna "É uma sequência válida de DNA"
    validacao_dna("ATXG"); // Retorna "Não é uma sequência válida de DNA"
    validacao_dna("");     // Retorna "Não é uma sequência válida de DNA"
    @endcode
    """
    if not sequencia:
     return "Não é uma sequência válida de DNA"          #averigua se a sequência está vazia

    sequencia = sequencia.upper()                        #converte os caracteres da sequência em maiúsculas
    bases = ["A", "T", "C", "G"]                         #lista com todas as bases azotadas do DNA

    for base in sequencia:                               #averigua se as bases estão na sequência
        if base not in bases:
            return "Não é uma sequência válida de DNA"
    return "É uma sequência válida de DNA"

def contar_bases(sequencia: str):
    """
    @brief Conta as ocorrências de cada base nitrogenada (A, C, G, T) em uma sequência de DNA e exibe os resultados.

    @details A função percorre a sequência fornecida, converte todos os caracteres para maiúsculas,
             e contabiliza a frequência de cada base nitrogenada válida ('A', 'C', 'G', 'T').
             Bases não reconhecidas são ignoradas.

    @param sequencia Uma string representando a sequência de DNA a ser analisada.

    @return Nenhum valor é retornado, mas os resultados são exibidos no formato:
            - A: número de ocorrências de adenina
            - C: número de ocorrências de citosina
            - G: número de ocorrências de guanina
            - T: número de ocorrências de timina

    @note Esta função diferencia apenas as bases nitrogenadas padrão. Qualquer caractere fora de 'A', 'C', 'G', 'T' será ignorado.

    @code
    // Exemplos de uso:
    contar_bases("ATCGATCG");
    // Saída:
    // A: 2
    // C: 2
    // G: 2
    // T: 2

    contar_bases("ATXG");
    // Saída:
    // A: 1
    // C: 0
    // G: 1
    // T: 1
    @endcode
    """
    bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}            #dicionário que contém as bases
    
    for base in sequencia.upper():                      #contar as ocorrências de cada base
        if base in bases:
            bases[base] += 1
    
    for base, quantidade in bases.items():              #imprimir o número de cada base
        print(f"{base}: {quantidade}")

def frequencia_bases(sequencia: str):
    """
    @brief Calcula e exibe a frequência de cada base azotada (A, C, G, T) em uma sequência de DNA.

    @details A função percorre a sequência fornecida, converte todos os caracteres para maiúsculas,
             e calcula a frequência de cada base nitrogenada válida ('A', 'C', 'G', 'T').
             Bases não reconhecidas são ignoradas na contagem.

    @param sequencia Uma string representando a sequência de DNA a ser analisada.

    @return Nenhum valor é retornado, mas as frequências são exibidas no formato:
            - A: frequência de adenina
            - C: frequência de citosina
            - G: frequência de guanina
            - T: frequência de timina

    @note Se a sequência estiver vazia, as frequências serão exibidas como 0.00 para todas as bases.

    @code
    // Exemplos de uso:
    frequencia_bases("ATCGATCG");
    // Saída:
    // A: 0.25
    // C: 0.25
    // G: 0.25
    // T: 0.25

    frequencia_bases("AATTGG");
    // Saída:
    // A: 0.33
    // C: 0.00
    // G: 0.33
    // T: 0.33

    frequencia_bases("");
    // Saída:
    // A: 0.00
    // C: 0.00
    // G: 0.00
    // T: 0.00
    @endcode
    """
    bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}                            #dicionário que contém as bases
    
    tamanho = len(sequencia)
    
    for base in sequencia.upper():                                      #contar as ocorrências de cada base
        if base in bases:
            bases[base] += 1
    
    for base, quantidade in bases.items():                              #imprimir a frequência de cada base
        frequencia = quantidade / tamanho if tamanho > 0 else 0
        print(f"{base}: {frequencia:.2f}")

def complemento_inverso(sequencia: str) -> str:
    """
    @brief Calcula o complemento inverso de uma sequência de DNA.

    @details A função recebe uma sequência de DNA, inverte a ordem das bases,
             e substitui cada base pela sua base complementar de acordo com as seguintes regras:
             - 'A' é complementada por 'T'.
             - 'T' é complementada por 'A'.
             - 'C' é complementada por 'G'.
             - 'G' é complementada por 'C'.

    @param sequencia Uma string representando a sequência de DNA a ser processada.

    @return Uma string contendo o complemento inverso da sequência fornecida.

    @note A função é insensível a maiúsculas e minúsculas, pois converte a sequência para letras maiúsculas antes do processamento.

    @code
    // Exemplos de uso:
    complemento_inverso("ATCG");
    // Retorna: "CGAT"

    complemento_inverso("aatt");
    // Retorna: "AATT"

    complemento_inverso("");
    // Retorna: ""
    @endcode
    """
    complementares = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}               #dicionário com as bases complementares de cada base

    sequencia_inversa = sequencia.upper()[::-1]                             #inverte a sequência e muda para maiúsculas

    return ''.join(complementares[base] for base in sequencia_inversa)      #gera o complemento inverso 

def dna_para_rna(sequencia: str) -> str:
    """
    @brief Converte uma sequência de DNA em uma cadeia de RNA correspondente.

    @details A função recebe uma sequência de DNA, converte todas as letras para maiúsculas 
             e substitui cada ocorrência de Timina ('T') pelo Uracilo ('U'), gerando a sequência de RNA.

    @param sequencia Uma string representando a sequência de DNA a ser convertida.

    @return Uma string contendo a cadeia de RNA correspondente à sequência de DNA fornecida.

    @note A função é insensível a maiúsculas e minúsculas, pois converte a sequência para letras maiúsculas antes do processamento.

    @code
    // Exemplos de uso:
    dna_para_rna("ATCG");
    // Retorna: "AUCG"

    dna_para_rna("aattccgg");
    // Retorna: "AAUUCCGG"

    dna_para_rna("");
    // Retorna: ""
    @endcode
    """
    rna = sequencia.upper().replace("T", "U")        #mete a sequência em maiúsculas e substitui a Timina por Uracilo
    
    return rna

def dividir_codoes(sequencia: str) -> list[str]:
    """
    @brief Divide uma sequência de DNA em uma lista de codões.

    @details A função recebe uma sequência de DNA, converte todas as letras para maiúsculas,
             e divide a sequência em blocos de três nucleotídeos (codões). Apenas blocos completos
             com exatamente três nucleotídeos são incluídos na lista de saída.

    @param sequencia Uma string representando a sequência de DNA a ser dividida em codões.

    @return Uma lista de strings, onde cada string é um codão (grupo de 3 nucleotídeos) da sequência.

    @note Sequências com comprimento não múltiplo de 3 terão os nucleotídeos restantes ignorados.

    @code
    // Exemplos de uso:
    dividir_codoes("ATCGTACGAT");
    // Retorna: ["ATC", "GTA", "CGA"]

    dividir_codoes("AATTGG");
    // Retorna: ["AAT", "TGG"]

    dividir_codoes("AATTC");
    // Retorna: ["AAT"]

    dividir_codoes("");
    // Retorna: []
    @endcode
    """
    seq_maiusculas = sequencia.upper()             #mete a sequência em maiúsculas
    codoes = []                                    #lista vazia para armazenar os codões
    
    for i in range(0, len(seq_maiusculas), 3):     #percorre a sequência de em passos de 3
        codao = seq_maiusculas[i:i+3]              #pega o codão de 3 nucleotídeos
        if len(codao) == 3:                        #adiciona o codão à lista se tiver 3 nucleotídeos
            codoes.append(codao)
    
    return codoes

def dna_para_proteina(sequencia: str) -> str:
    """
    @brief Converte uma sequência de DNA em uma cadeia de aminoácidos que formam uma proteína.

    @details A função utiliza o código genético padrão para traduzir a sequência de DNA em uma sequência de aminoácidos.
             Cada tripla de nucleotídeos (codão) é mapeada para seu respectivo aminoácido. 
             Codões de parada (TAA, TAG, TGA) são representados pelo caractere '_'. 
             Se um codão não for reconhecido, ele também será traduzido para '_'.

    @param sequencia Uma string representando a sequência de DNA a ser traduzida.

    @return Uma string contendo a sequência de aminoácidos correspondente.

    @note A função ignora nucleotídeos extras no final da sequência que não formam um codão completo.

    @code
    // Exemplos de uso:
    dna_para_proteina("ATGTTCGAA");
    // Retorna: "MF_"

    dna_para_proteina("ATGAAATAA");
    // Retorna: "MK_"

    dna_para_proteina("");
    // Retorna: ""
    @endcode
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
                       "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}                    #dicionário representativa do códio genético
    
    seq_maiusculas = sequencia.upper()                                                #mete a sequência em maiúsculas

    codoes = [seq_maiusculas[i:i+3] for i in range(0, len(seq_maiusculas), 3)]        #percorre a sequência em passos de 3, extraindo os codões  

    proteina = [codigo_genetico.get(codao, "_") for codao in codoes]                  #tradução de cada codão para o seu aminoácido correspondente                                                    

    resultado = "".join(proteina)                                                     #junta os aminoácidos formando uma proteína            

    return resultado

def obter_orfs(sequencia: str):
    """
    @brief Calcula todas as 6 possíveis Open Reading Frames (ORFs) de uma sequência de DNA.

    @param Sequência de DNA em formato de string. A sequência deve ser composta apenas pelas bases A, T, C e G.
    
    @return Lista com 6 ORFs, sendo 3 da cadeia direta e 3 da cadeia reversa. Cada ORF é representada como uma lista de codões.

    @details A função gera 3 ORFs a partir da cadeia direta e 3 ORFs a partir da cadeia reversa do DNA. Para isso, a sequência é dividida em codões 
    (grupos de 3 nucleotídeos) a partir de três posições iniciais (0, 1, 2), tanto na sequência original quanto na sequência complementar inversa. 
    As ORFs geradas podem representar potenciais regiões de tradução para proteínas.

    @note A função assume que a sequência de DNA fornecida está em letras maiúsculas. A função também lida com a inversão e complemento da cadeia para calcular as ORFs da sequência reversa reversa.

    @code
    // Exemplo de uso:
    dna = "ATGAAATAGATGTTTTAATGA"
    orfs = get_orfs(dna)
    for orf in orfs:
        print(orf)
    @endcode

    @see dividir_codoes
    @see complemento_inverso
    """
    def dividir_orfs(sequencia):
        """
        Gera 3 ORFs a partir de uma única sequência de DNA.
        
        """
        return [dividir_codoes(sequencia[i:]) for i in range(3)]     #retorna uma lista de codões

    orfs_direta = dividir_orfs(sequencia.upper())                    #ORFs da sequência
    orfs_reversa = dividir_orfs(complemento_inverso(sequencia))      #ORFs da sequência reversa
    
    return orfs_direta + orfs_reversa
