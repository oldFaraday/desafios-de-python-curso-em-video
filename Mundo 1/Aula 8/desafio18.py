import math
ang_gr = float(input('Digite um valor: '))
ang_rad = math.radians(ang_gr)
sen = math.asin(ang_rad)
cos = math.acos(ang_rad)
tan = math.atan(ang_rad)
print('Os valore de Seno, Cosseno e Tangente de {:.2f}° são:\nSen: {:.2f}\nCos: {:.2f}\nTan: {:.2f}'.format(ang_gr, sen, cos, tan))