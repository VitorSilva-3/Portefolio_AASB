
import unittest

class TestDNAFunctions(unittest.TestCase):

    def test_validacao_dna(self):
        self.assertEqual(validacao_dna("ATCG"), "É uma sequência válida de DNA")
        self.assertEqual(validacao_dna("atcg"), "É uma sequência válida de DNA")
        self.assertEqual(validacao_dna("ATXG"), "Não é uma sequência válida de DNA")
        self.assertEqual(validacao_dna(""), "Não é uma sequência válida de DNA")

    def test_contar_bases(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        contar_bases("ATCGATCG")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "A: 2\nC: 2\nG: 2\nT: 2")

    def test_frequencia_bases(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        frequencia_bases("ATCGATCG")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "A: 0.25\nC: 0.25\nG: 0.25\nT: 0.25")

    def test_complemento_inverso(self):
        self.assertEqual(complemento_inverso("ATCG"), "CGAT")
        self.assertEqual(complemento_inverso("aatt"), "AATT")
        self.assertEqual(complemento_inverso(""), "")

    def test_dna_para_rna(self):
        self.assertEqual(dna_para_rna("ATCG"), "AUCG")
        self.assertEqual(dna_para_rna("aattccgg"), "AAUUCCGG")
        self.assertEqual(dna_para_rna(""), "")

    def test_dividir_codoes(self):
        self.assertEqual(dividir_codoes("ATCGTACGAT"), ["ATC", "GTA", "CGA"])
        self.assertEqual(dividir_codoes("AATTGG"), ["AAT", "TGG"])
        self.assertEqual(dividir_codoes("AATTC"), ["AAT"])
        self.assertEqual(dividir_codoes(""), [])

    def test_dna_para_proteina(self):
        self.assertEqual(dna_para_proteina("AGCGATGCAGCTGATAG"), "SDAAD_")
        self.assertEqual(dna_para_proteina("ATGAAATAA"), "MK_")
        self.assertEqual(dna_para_proteina(""), "")

    def test_obter_orfs(self):
        self.assertEqual(obter_orfs("ATGAAATAG"), [['ATG', 'AAA', 'TAG'], ['TGA', 'AAT'], ['GAA', 'ATA'], ['CTA', 'TTT', 'CAT'], ['TAT', 'TTC'], ['ATT', 'TCA']])

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
