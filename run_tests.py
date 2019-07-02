import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../YoungTableau'))
 

from struc import *
import unittest



errorstr= "Fehlerhafte Ausgabe, erwarteter Output: "

#Wir wollen als gegeben voraus setzen, dass die Eingaben schon korrekt sind (vllt) oder später
class TestWords(unittest.TestCase):
    def test_parse_word(self):

        data = "5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5"
        result = parse_word(data)
        self.assertEqual(result, [[1, 2, 2, 3, 3, 5], [2, 3, 5, 5], [4, 4, 6, 6], [5,6]])


        data = "7 8 9 10 11 12 13 14 5 6 4 4 6 1 2 3 5 5 1 2 2 3 3 5"
        self.assertRaises(ValueError, parse_word, data)


        #TESTS AUS DER ttest.txt ABER KOPIERT
        data = "5 6 7 8 5 5 6 7 8"
        self.assertRaises(ValueError, parse_word, data)

        data = "100 50 82 83 40 40 40 55 58 12 12 30 50 50 4 12 13 20 21 3 3 3 5 20 20 1 2 2 3 3 4 6 20" #die "letzte" davon die wie wir ja wissen falsch ist
        self.assertRaises(ValueError, parse_word, data)


        
    def test_parse(self):
        
        result = parse(0, "testcases/words.txt")
        self.assertEqual(result, [[1, 2, 2, 3, 3, 5], [2, 3, 5, 5], [4, 4, 6, 6], [5,6]])

        #result = parse(1, "testcases/words.txt")
        #self.assertEqual(result, [[1, 2, 2, 3, 3, 5], [2, 3, 5, 5], [4, 4, 6, 6], [5,6]])

        
        
        #assert parse_word() == erg, errorstr + str(wort[1])
        #assert parse(0, "testcases/words.txt") == erg, errorstr + str(erg)
        #assert parse(1, "testcases/words.txt") == erg, errorstr + str(erg)

        #Test cases zum hinzufuegen:
        #A) Value Errors
        #B) parse from file
        
        #for i in range(0, 4):
        #    print(parse(i, "testcases/words.txt"))



class TestVisual(unittest.TestCase):
    def testsheet(self):
        pass

class TestStruc(unittest.TestCase):
    def test_multiply(self):

        #test easy
        data= "2 1 3"
        result = multiply(parse_word(data), parse_word(data)).word
        self.assertEqual(result, "3 2 2 1 1 3")
        
        data1= "100 50 82 83 40 40 40 55 58 12 18 30 50 50 4 12 13 20 21 3 3 3 5 20 20 1 2 2 3 3 4 6 20"
        data2= "100 50 82 83 40 40 40 55 58"
        result = multiply(parse_word(data1), parse_word(data2)).word
        self.assertEqual(result, "100 50 82 83 40 40 40 55 58 12 18 30 50 50 4 12 13 20 21 100 3 3 3 5 20 20 50 82 83 1 2 2 3 3 4 6 20 40 40 40 55 58")

        data1= "100 50 82 83 40 40 40 55 58 12 18 30 50 50 4 12 13 20 21 3 3 3 5 20 20 1 2 2 3 3 4 6 20"
        data2= "100 50 82 83 40 40 40 55 58 12 18 30 50 50"
        result = multiply(parse_word(data1), parse_word(data2)).word
        self.assertEqual(result, "100 50 82 83 40 40 40 55 58 12 18 30 50 50 100 4 12 13 20 21 50 82 83 3 3 3 5 20 20 20 40 40 55 58 1 2 2 3 3 4 6 12 18 30 40 50 50")

        #auch nochmal analog mit createfrom
        #multiply(create_from(8, "ttest.txt"), create_from(8, "ttest.txt")).visual(1,"777.tex")
        
if __name__ == '__main__':
    unittest.main()
    
parse1()
print(parse_word("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5"))
multiply(create_from(8, "ttest.txt"), create_from(8, "ttest.txt")).visual(1,"777.tex")
print("Everything passed")

