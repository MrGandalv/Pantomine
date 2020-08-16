"""In this project we try to build a ML Programm that recognizes certain terms that the user is trying to express by gesture over a camera"""
Richtung = ["oben", "unten", "links", "rechts", "oben links", "oben rechts", "unten links", "unten rechts", "keine"]
GeschKat = ["1", "2", "3", "4", "5"]

dummy_liste = []

#for k in zip(Richtung, GeschKat):
#	dummy_liste.append(k)

for element in Richtung:
	dummy_liste.append(element)

print(dummy_liste)