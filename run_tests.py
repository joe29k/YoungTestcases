import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../YoungTableau'))
 

from struc import *
import ytmath
import random
import unittest



errorstr= "Fehlerhafte Ausgabe, erwarteter Output: "

#Wir wollen als gegeben voraus setzen, dass die Eingaben schon korrekt sind (vllt) oder später
class TestWordsPy(unittest.TestCase):
    def test_wordspy_parse_word(self):

        data = "5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5"
        result = parse_word(data)
        self.assertEqual(result, [[1, 2, 2, 3, 3, 5], [2, 3, 5, 5], [4, 4, 6, 6], [5,6]])


        data = "7 8 9 10 11 12 13 14 5 6 4 4 6 1 2 3 5 5 1 2 2 3 3 5"
        self.assertRaises(ValueError, parse_word, data)

        

        self.assertEqual(parse_word(""), [])
        self.assertEqual(parse_word(" "), [])

        self.assertRaises(ValueError, parse_word, "1 2 2 3 3 5 2 3 5 5 4 4 6 6 5 6")
        self.assertEqual(parse_word(" 1  2 3 4       5"), [[1,2,3,4,5]])

        #TESTS AUS DER ttest.txt ABER KOPIERT
        data = "5 6 7 8 5 5 6 7 8"
        self.assertRaises(ValueError, parse_word, data)

        data = "100 50 82 83 40 40 40 55 58 12 12 30 50 50 4 12 13 20 21 3 3 3 5 20 20 1 2 2 3 3 4 6 20" #die "letzte" davon die wie wir ja wissen falsch ist
        self.assertRaises(ValueError, parse_word, data)


        
    def test_wordspy_parse(self):

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
    def testvispy(self):
        #Diese sind in der Visual_tests.py Datei!!!!

        
        #print_tex([[1, 2, 2, 3, 3, 5], ['2', '3', '5', '5'], ['4', '4', '6', '6'], ['5', '6']], 1)
        #print_tex([[1, 2, 3]], 1)
        #verschiedene boxlengths testen
        #verschiedene matrizen testen
        #latex file pruefen
        #pdf pruefen
        pass

class TestK_relationsoperations(unittest.TestCase):

    #TODO: pruefen kleinergl operation!!!


    #TEIL A - TEST IN YTMATH
    def test_k1_ytmath(self):
        self.assertEqual(ytmath.K1([4,2,3,1,5],1), "4 2 1 3 5")
        self.assertEqual(ytmath.K1([6,6,3],0), "6 3 6")
        self.assertRaises(ValueError, ytmath.K1, [3,6,3],0)
        
    def test_k1_inv_ytmath(self):
        self.assertEqual(ytmath.K1_inv([4,2,1,3,5],1), "4 2 3 1 5")
        self.assertRaises(ValueError, ytmath.K2, [3,3,6],0)
        
    def test_k2_ytmath(self):
        self.assertEqual(ytmath.K2([2,4,3,1,5],0), "4 2 3 1 5")
        self.assertRaises(ValueError, ytmath.K2, [3,6,6],0)
        

        
    def test_k2_inv_ytmath(self):
        self.assertEqual(ytmath.K2_inv([4,2,3,1,5], 0), "2 4 3 1 5")
        self.assertRaises(ValueError, ytmath.K2_inv, [6,6,3],0)
        self.assertEqual(ytmath.K2_inv([6,3,3],0), "3 6 3")
        self.assertRaises(ValueError, ytmath.K2_inv, [6,3,6],0)

    def test_k_grenzfaelle_ytmath(self):
        self.assertEqual(ytmath.K1_inv([4,2,3,1,5],2), "4 2 3 5 1")
        self.assertRaises(ValueError, ytmath.K1, [4,2,3,1,5], 3)
        self.assertRaises(ValueError, ytmath.K1_inv, [1,2], 0)
        self.assertRaises(ValueError, ytmath.K2, [1,2], 0)
        self.assertRaises(ValueError, ytmath.K2_inv, [1,2], 0)
        self.assertEqual(ytmath.K1([2,3,1],0), "2 1 3")

    def test_k_kleinergl_grenzfaelle(self):
        self.assertEqual(ytmath.K1([2,3,1],0), "2 1 3")
        self.assertRaises(ValueError, ytmath.K1, [1,1,1],0)
        self.assertRaises(ValueError, ytmath.K1, [1,1,2],0)
        self.assertRaises(ValueError, ytmath.K1, [1,2,1],0)
        self.assertRaises(ValueError, ytmath.K1, [1,0,1],0)
        self.assertRaises(ValueError, ytmath.K1, [2,1,3],0)
        self.assertEqual(ytmath.K1([1,1,0],0), "1 0 1")

    #TEIL B - TEST IN WORD CLASS ALSO ANALOG ABER BISSL VEREINFACHT
    def test_k_op_struc_wordclass(self):
        self.assertEqual(word("4 2 3 1 5").K1(1), "4 2 1 3 5")
        self.assertEqual(word("4 2 1 3 5").K1_inv(1), "4 2 3 1 5")
        self.assertEqual(word("2 4 3 1 5").K2(0), "4 2 3 1 5")
        self.assertEqual(word("4 2 3 1 5").K2_inv(0), "2 4 3 1 5")
    def test_k_op_struc_wordclass_grenzfaelle(self):
        self.assertEqual(word("4 2 3 1 5").K1_inv(2), "4 2 3 5 1")
        self.assertRaises(ValueError, word("4 2 3 1 5").K1, 3)
        self.assertRaises(ValueError, word("1 2").K1, 0)
        self.assertEqual(word("2 3 1").K1(0), "2 1 3")

        

class TestYoungTableau(unittest.TestCase):
    #METHODE ZUM TESTEN VON VISUAL -> SIEHE VISUAL_TESTS.py
    def test_row_ins(self):
        yt = youngtableau("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5")
        self.assertEqual(yt.row_insert(1).matrix, [[1, 1, 2, 3, 3, 5], [2, 2, 5, 5], [3, 4,6, 6],[4,6],[5]])

        yt = youngtableau("")
        self.assertEqual(yt.row_insert(1).matrix, [[1]])

        #GRENZFALL "ECHT GROESSER"
        yt = youngtableau("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5")
        self.assertEqual(yt.row_insert(5).matrix, [[1, 2, 2, 3, 3, 5, 5], [2, 3, 5, 5], [4, 4,6, 6],[5,6]])
        

    def test_getword(self):

        for word in ["5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5", ""]:
            yt = youngtableau(word)
            self.assertEqual(yt.word().wort, word)


class TestWordClass(unittest.TestCase):
    #K operationen oben abgehandelt
    def test_ytfunc(self):

        #zunaechst woerter die bereits funktionierende young tableaux sind.
        w1 = word("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5")
        self.assertEqual(w1.youngtableau().word().wort, w1.wort)
        self.assertEqual(w1.youngtableau().matrix, [[1,2,2,3,3,5],[2,3,5,5],[4,4,6,6],[5,6]])

        w2 = word("")
        self.assertEqual(w2.youngtableau().matrix, [])

        #jetz fehlerhafte die dann eine funktionierende (eindeutige) ergeben:


        
class TestStruc(unittest.TestCase):
    def test_createfrom(self):
        self.assertRaises(ValueError, create_from, 3, "ttest.txt")
        self.assertRaises(ValueError, create_from, 4, "ttest.txt")
        self.assertRaises(ValueError, create_from, 9, "ttest.txt")

        self.assertEqual(create_from(8, "ttest.txt").matrix, parse(8, "ttest.txt"))
        self.assertEqual(create_from(8, "ttest.txt").matrix, [[1, 2, 2, 3, 3, 4, 6, 20]
                                                              ,[3 ,3, 3, 5, 20, 20],[4 ,12, 13, 20, 21],[ 12, 18 ,30 ,50 ,50 ],[40, 40 ,40, 55, 58],[50, 82, 83],[100]])   
                         

            
    def test_multclasses(self):

        self.assertEqual(mult_classes(word("3 4 9 3 7"), word("1 3 1 9")).youngtableau().wort, "9 4 7 3 3 1 1 3 9")

    def test_equiv(self):
        self.assertTrue(are_equiv(word("4 2 1 3 5"), word("2 4 3 1 5")))
        self.assertTrue(are_equiv(word(""), word("  ")))
        self.assertFalse(are_equiv(word("4 0"), word("0 4")))
    def test_multiply(self):

        #test easy
        data= youngtableau("2 1 3")
        result = multiply(data, data).wort
        self.assertEqual(result, "3 2 2 1 1 3")
        
        data1= youngtableau("100 50 82 83 40 40 40 55 58 12 18 30 50 50 4 12 13 20 21 3 3 3 5 20 20 1 2 2 3 3 4 6 20")
        data2= youngtableau("100 50 82 83 40 40 40 55 58")
        result = multiply(data1, data2).wort
        self.assertEqual(result, "100 50 82 83 40 40 40 55 58 12 18 30 50 50 4 12 13 20 21 100 3 3 3 5 20 20 50 82 83 1 2 2 3 3 4 6 20 40 40 40 55 58")

        data1= youngtableau("100 50 82 83 40 40 40 55 58 12 18 30 50 50 4 12 13 20 21 3 3 3 5 20 20 1 2 2 3 3 4 6 20")
        data2= youngtableau("100 50 82 83 40 40 40 55 58 12 18 30 50 50")
        result = multiply(data1, data2).wort
        self.assertEqual(result, "100 50 82 83 40 40 40 55 58 12 18 30 50 50 100 4 12 13 20 21 50 82 83 3 3 3 5 20 20 20 40 40 55 58 1 2 2 3 3 4 6 12 18 30 40 50 50")


        data1 = youngtableau("18 16 9 11 24")
        data2 = youngtableau("20 25 2 14 20")
        result = multiply(data1, data2).wort
        self.assertEqual(result, "18 16 24 9 20 25 2 11 14 20")


        data1 = youngtableau("18 11 15 8 11")
        data2 = youngtableau("7 8 1 3 11")
        result = multiply(data1, data2).wort
        self.assertEqual(result, "18 11 15 8 11 7 8 1 3 11")

        data1 = youngtableau("11 10 20 6 19")
        data2 = youngtableau("14 11 12 15 20")
        result = multiply(data1, data2).wort
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
        yt1 = word(wort1).youngtableau()
        yt2 = word(wort2).youngtableau()
        #print(vgl_wort1, vgl_wort2)
        
        result = multiply(yt1, yt2).wort
        self.assertEqual(result, (mult_classes(word(wort1), word(wort2)).youngtableau().wort))

class ComplexTests(unittest.TestCase):
    def test_multiply_createfrom_visual(self):
        multiply(create_from(8, "ttest.txt"), create_from(8, "ttest.txt")).visual(1,"Y01_complex.tex")
    def multclasses_equiv(self):
        self.assertTrue(are_equiv(mult_classes(word("3 4 9 3 7"), word("1 3 1 9")), word("9 4 7 3 3 1 1 3 9")))
    def multi_ks(self):
        self.assertEqual(K2(K1(K1_inv(K2_inv("7 1 4 9 3 6 3", 0), 1), 1),4), "1 7 4 9 3 6 6")
if __name__ == '__main__':
    unittest.main()
    
#parse1()
#print(parse_word("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5"))
##print("Everything passed")


