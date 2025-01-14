import unittest
from exemplo import revcomp                #TESTAR
class TestRevComp(unittest.TestCase):

  def test_empty_string(self):
      self.assertEqual("", revcomp(""))
  def teste_one_char(self):
      self.assertEqual("T",revcomp ("A"))
      self.assertEqual("A",revcomp ("T"))
      self.assertEqual("G",revcomp ("C"))
      self.assertEqual("C",revcomp ("G"))

  def test_general_case(self):
      self.assertEqual("TGAC",revcomp("ACGT")

if __name__ == "__main__":
  unittest.main()
