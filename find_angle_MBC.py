from math import sqrt, sin, atan, pi, asin, degrees
#input1 = int(input())
#input2 = int(input())
ab = 10
bc = 10
ac = sqrt(ab ** 2 + bc ** 2)
cm = ac/2
area_abm = (ab*bc)/4 # area of abc is ab*ac/4 and bm line divides triangle on 2 equal parts
angle_acb = atan(ab/bc)
bm = sqrt(bc**2 + cm**2 - (2*(sqrt(bc**2*cm**2 - 4*(area_abm**2)))))
angle_mbc  = cm*sin(angle_acb)/bm
print(round(degrees(asin(angle_mbc))))