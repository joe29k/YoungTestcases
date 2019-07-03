import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../YoungTableau'))
 

from struc import *

#am ende zeitstempel pruefen um zu sehen ob er was gemacht hat


#TEST 01 - Standard von Aufgabenstellung - BoxSize 1
print_tex([['1', '2', '2', '3', '3', '5'], ['2', '3', '5', '5'], ['4', '4', '6', '6'], ['5', '6']], 1, "X01_visual_output.tex")
subprocess.call(['pdflatex', "X01_visual_output.tex"], stdout=subprocess.DEVNULL)

#TEST 02 - Standard von Aufgabenstellung - BoxSize 5
print_tex([['1', '2', '2', '3', '3', '5'], ['2', '3', '5', '5'], ['4', '4', '6', '6'], ['5', '6']], 5, "X02_visual_output.tex")
subprocess.call(['pdflatex', "X02_visual_output.tex"], stdout=subprocess.DEVNULL)

#TEST 03 - Standard von Aufgabenstellung - BoxSize 0.4
print_tex([['1', '2', '2', '3', '3', '5'], ['2', '3', '5', '5'], ['4', '4', '6', '6'], ['5', '6']], 0.4, "X03_visual_output.tex")
subprocess.call(['pdflatex', "X03_visual_output.tex"], stdout=subprocess.DEVNULL)

#TEST 04 - Ganz komplex
print_tex(parse(8, "ttest.txt"), 1, "X04_visual_output.tex")
subprocess.call(['pdflatex', "X04_visual_output.tex"], stdout=subprocess.DEVNULL)

#TEST 05 - Ganz leer
print_tex([], 1, "X05_visual_output.tex")
subprocess.call(['pdflatex', "X05_visual_output.tex"], stdout=subprocess.DEVNULL)

#TEST 06 - FUER YOUNGTABLEAU VISUAL METHODE
yt = youngtableau("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5")
yt.visual(1, "X06_visual_output.tex")
subprocess.call(['pdflatex', "X06_visual_output.tex"], stdout=subprocess.DEVNULL)

#TEST 07 - FUER YOUNGTABLEAU VISUAL METHODE - BOXSIZE 3
yt = youngtableau("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5")
yt.visual(2, "X07_visual_output.tex")
subprocess.call(['pdflatex', "X07_visual_output.tex"], stdout=subprocess.DEVNULL)

        
