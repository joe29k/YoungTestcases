import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../YoungTableau'))
 

from struc import *
import random
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

        self.assertEqual(parse_word(""), [])
        self.assertEqual(parse_word(" "), [])
        self.assertEqual(parse_word(" 1  2 3 4       5"), [[1,2,3,4,5]])

        #TESTS AUS DER ttest.txt ABER KOPIERT
        data = "5 6 7 8 5 5 6 7 8"
        self.assertRaises(ValueError, parse_word, data)

        data = "100 50 82 83 40 40 40 55 58 12 12 30 50 50 4 12 13 20 21 3 3 3 5 20 20 1 2 2 3 3 4 6 20" #die "letzte" davon die wie wir ja wissen falsch ist
        self.assertRaises(ValueError, parse_word, data)


        
    def test_parse(self):

        #TESTS MIT WOERTERN AUS DATEI words.txt
        #IN ZEILE 1/4 EIN GUELTIGES WORT, ZEILE 2-4 und 6 IST KEIN YOUNG TABL.
        #ZEILE 5 ist das leere wort
        #IN PYTHON HAT 1. ZEILE INDEX 0
        
        result = parse(0, "words.txt")
        self.assertEqual(result, [[1, 2, 2, 3, 3, 5], [2, 3, 5, 5], [4, 4, 6, 6], [5,6]])

        result = parse(4, "words.txt")
        self.assertEqual(result, [])


        self.assertRaises(ValueError, parse, 1, "words.txt")
        self.assertRaises(ValueError, parse, 2, "words.txt")
        self.assertRaises(ValueError, parse, 3, "words.txt")
        self.assertRaises(ValueError, parse, 5, "words.txt")
        
        
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
        #Diese sind in der Visual_tests.py Datei!!!!

        
        #print_tex([[1, 2, 2, 3, 3, 5], ['2', '3', '5', '5'], ['4', '4', '6', '6'], ['5', '6']], 1)
        #print_tex([[1, 2, 3]], 1)
        #verschiedene boxlengths testen
        #verschiedene matrizen testen
        #latex file pruefen
        #pdf pruefen
        pass

class TestK_relationsoperations(unittest.TestCase):
    def testsheet(self):
        pass

class TestYoungTableau(unittest.TestCase):
    def test_row_ins(self):
        pass
    def test_visual(self):
        pass
    def test_getword(self):
        pass
    
class TestStruc(unittest.TestCase):
    def test_createfrom(self):
        pass

    def test_multclasses(self):
        pass
    def test_equiv(self):
        pass
    def test_multiply(self):

        #test easy
        data= "2 1 3"
        result = multiply(parse_word(data), parse_word(data)).wordstring
        self.assertEqual(result, "3 2 2 1 1 3")
        
        data1= "100 50 82 83 40 40 40 55 58 12 18 30 50 50 4 12 13 20 21 3 3 3 5 20 20 1 2 2 3 3 4 6 20"
        data2= "100 50 82 83 40 40 40 55 58"
        result = multiply(parse_word(data1), parse_word(data2)).wordstring
        self.assertEqual(result, "100 50 82 83 40 40 40 55 58 12 18 30 50 50 4 12 13 20 21 100 3 3 3 5 20 20 50 82 83 1 2 2 3 3 4 6 20 40 40 40 55 58")

        data1= "100 50 82 83 40 40 40 55 58 12 18 30 50 50 4 12 13 20 21 3 3 3 5 20 20 1 2 2 3 3 4 6 20"
        data2= "100 50 82 83 40 40 40 55 58 12 18 30 50 50"
        result = multiply(parse_word(data1), parse_word(data2)).wordstring
        self.assertEqual(result, "100 50 82 83 40 40 40 55 58 12 18 30 50 50 100 4 12 13 20 21 50 82 83 3 3 3 5 20 20 20 40 40 55 58 1 2 2 3 3 4 6 12 18 30 40 50 50")


        data1 = "18 16 9 11 24"
        data2 = "20 25 2 14 20"
        result = multiply(parse_word(data1), parse_word(data2)).wordstring
        self.assertEqual(result, "18 16 24 9 20 25 2 11 14 20")


        data1 = "18 11 15 8 11"
        data2 = "7 8 1 3 11"
        result = multiply(parse_word(data1), parse_word(data2)).wordstring
        self.assertEqual(result, "18 11 15 8 11 7 8 1 3 11")

        data1 = "11 10 20 6 19"
        data2 = "14 11 12 15 20"
        result = multiply(parse_word(data1), parse_word(data2)).wordstring
        self.assertEqual(result, "20 11 19 10 14 6 11 12 15 20")
         

        
        #auch nochmal analog mit createfrom
        #multiply(create_from(8, "ttest.txt"), create_from(8, "ttest.txt")).visual(1,"777.tex")
    def test_multipyCmpWord(self):
        for i in range(0,20):
            wort1 = ""
            wort2 = ""
            for j in range(0,5):
                wort1 = wort1 + str(random.randint(1,25)) + " "
                wort2 = wort2 + str(random.randint(1,25)) + " "
            wort1 = wort1[:-1]
            wort2 = wort2[:-1]

        

        #Geht nur, wenn:
        #bei mult_classes der Repraesentant das Wort ist, das in eine Young Matrix ueberfuehrt werden kann UND
        #die klasse Youngtableau muss das Attribut word besitzen, in dem das uebergebene wort gespeichert ist.7
        #analog muss in der word klasse, das attribut wordstring enthalten sein, dass das wort als string enthaelt
        #get_wyt(wort - string) ist funktion, die das zu wort aequival. wort zurueckgibt, dass in eine young matrix ueberfuehrt
        #werden kann!
        vgl_wort1 = get_wyt(wort1)
        vgl_wort2 = get_wyt(wort2)
        #print(vgl_wort1, vgl_wort2)
        
        result = (multiply(parse_word(vgl_wort1), parse_word(vgl_wort2)).wordstring)
        self.assertEqual(result, get_wyt(mult_classes(word(wort1), word(wort2)).wordstring))

if __name__ == '__main__':
    unittest.main()
    
#parse1()
#print(parse_word("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5"))
#multiply(create_from(8, "ttest.txt"), create_from(8, "ttest.txt")).visual(1,"777.tex")
#print("Everything passed")

