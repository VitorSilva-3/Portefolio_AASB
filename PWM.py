from typing import List, Dict, Optional
import math
import re

class AnalisadorSequencias:
    """
    @brief Uma classe para analisar sequências de ADN ou proteínas e calcular várias matrizes.
    
    Esta classe fornece funcionalidades para:
    - Calcular tabelas de contagens para alinhamentos de sequências
    - Computar Position Weight Matrices (PWM)
    - Calcular Position-Specific Scoring Matrices (PSSM)
    - Encontrar sequências mais prováveis
    """
    
    ALFABETO_ADN = "ACGT"
    ALFABETO_PROTEINA = "ARNDCQEGHILKMFPSTWYVBZX_"
    
    @staticmethod
    def tabela_contagens(sequencias: List[str], alfabeto: str = ALFABETO_ADN, 
                        pseudocontagem: float = 0) -> List[Dict[str, float]]:
        """
        @brief Calcula a tabela de contagens para cada coluna de um alinhamento.
        
        @param sequencias Lista de sequências alinhadas
        @param alfabeto Conjunto de caracteres permitidos
        @param pseudocontagem Valor a adicionar a cada contagem para evitar valores nulos
        
        @return Lista de dicionários onde cada dicionário corresponde às contagens
                de cada carácter do alfabeto numa coluna do alinhamento
        
        @throws AssertionError se as sequências tiverem comprimentos diferentes
        """
        return [{b: occ.count(b) + pseudocontagem for b in alfabeto} 
                for occ in zip(*sequencias)]

    @staticmethod
    def pwm(sequencias: List[str], tipo: str = "ADN", 
           pseudocontagem: float = 0) -> List[Dict[str, float]]:
        """
        @brief Calcula a Position Weight Matrix (PWM).
        
        @param sequencias Lista de sequências alinhadas
        @param tipo "ADN" ou "PROTEINA", define o alfabeto permitido
        @param pseudocontagem Valor a adicionar às contagens para evitar zeros
        
        @return Lista de dicionários representando frequências relativas normalizadas
                para cada coluna do alinhamento
        
        @throws AssertionError se as sequências tiverem comprimentos diferentes ou tipo inválido
        """
        assert all(len(sequencias[0]) == len(s) for s in sequencias), \
            "As sequências devem ter comprimentos iguais!"
        tipo = tipo.upper()
        assert tipo in ["ADN", "PROTEINA"], f"Tipo inválido: {tipo}!"
        
        alfabeto = AnalisadorSequencias.ALFABETO_ADN if tipo == "ADN" \
            else AnalisadorSequencias.ALFABETO_PROTEINA
        
        tabela = AnalisadorSequencias.tabela_contagens(sequencias, alfabeto, pseudocontagem)
        L = len(sequencias[0])
        A = len(alfabeto)
        
        return [{k: v / (L + A * pseudocontagem) 
                for k, v in linha.items()} for linha in tabela]

    @staticmethod
    def imprime_matriz(pwm: List[Dict[str, float]], casas_decimais: int = 2) -> str:
        """
        @brief Formata e imprime a PWM ou a PSSM como uma matriz tabular.

        @param pssm Position-Specific Scoring Matrix
        @param pwm Position Weight Matrix
        @param casas_decimais Número de casas decimais para arredondar
    
        @return String formatada representando a matriz PWM ou PSSM
        """
        alfabeto = pwm[0].keys()
        linhas = []

        for base in alfabeto:
            linha = [base] + [round(coluna[base], casas_decimais) for coluna in pwm]
            linhas.append(linha)

        matriz_str = "\n".join(["  ".join(map(str, linha)) for linha in linhas])
        print(matriz_str)
        return matriz_str
    
    
    @staticmethod
    def prob_gerar_sequencia(sequencia: str, 
                           pwm: List[Dict[str, float]]) -> float:
        """
        @brief Calcula a probabilidade de gerar uma sequência com base numa PWM.
        
        @param sequencia Sequência para calcular a probabilidade
        @param pwm Position Weight Matrix
        
        @return Probabilidade de gerar a sequência
        
        @throws AssertionError se os comprimentos da sequência e do motivo não coincidirem
        """
        assert len(sequencia) == len(pwm), \
            "Os comprimentos da sequência e do motivo devem ser iguais!"

        prob = 1
        for letra, coluna in zip(sequencia, pwm):
            prob *= coluna[letra]
        return prob

    @staticmethod
    def seq_mais_provavel(sequencia: str, 
                         pwm: List[Dict[str, float]]) -> List[str]:
        """
        @brief Encontra a(s) subsequência(s) mais provável(eis) numa sequência maior.
        
        @param sequencia Sequência maior onde procurar
        @param pwm Position Weight Matrix
        
        @return Lista ordenada das subsequências mais prováveis
        
        @throws AssertionError se a sequência for mais curta que o comprimento do motivo
        """
        assert len(sequencia) >= len(pwm), \
            "O comprimento da sequência deve ser maior ou igual ao do motivo!"
            
        L = len(pwm)
        R = '.' * L
        probs: Dict[str, float] = {}
        
        for s in re.findall(f'(?=({R}))', sequencia):
            probs[s] = AnalisadorSequencias.prob_gerar_sequencia(s, pwm)
            
        maior_prob = max(probs.values())
        return sorted(set([k for k, v in probs.items() if v >= maior_prob]))

    @staticmethod
    def calcula_pssm(pwm: List[Dict[str, float]], 
                     alfabeto: str = ALFABETO_ADN,
                     frequencias_base: Optional[Dict[str, float]] = None) -> List[Dict[str, float]]:
        """
        @brief Calcula a Position-Specific Scoring Matrix (PSSM) a partir de uma PWM.
        
        @param pwm Position Weight Matrix
        @param alfabeto Conjunto de caracteres permitidos
        @param frequencias_base Dicionário com frequências de base para cada símbolo
        
        @return PSSM como lista de dicionários com pontuações logarítmicas
        
        @throws AssertionError se os alfabetos da PWM e das frequências base não coincidirem
        """
        if frequencias_base is None:
            frequencias_base = {base: 1 / len(alfabeto) for base in alfabeto}
            
        assert set(frequencias_base.keys()) == set(alfabeto), \
            "O alfabeto das frequências base deve coincidir com o da PWM!"
            
        pssm = []
        for coluna in pwm:
            pssm_coluna = {}
            for base, prob in coluna.items():
                if prob > 0:
                    pssm_coluna[base] = math.log2(prob / frequencias_base[base])
                else:
                    pssm_coluna[base] = float('-inf')
            pssm.append(pssm_coluna)
        return pssm