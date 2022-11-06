from math import sqrt, sin, atan, asin, degrees

"""
In right ABC triangle we add point M in the middle of AC and then divide triangle 
on 2 equal parts: ABM and BMC. This script gets an angle of MBC
"""

ab = int(input())
bc = int(input())
ac = sqrt(ab**2 + bc**2)
cm = ac / 2
# area of abc is ab*ac/2 and bm line divides triangle on 2 equal parts so it's ab*ac/4
area_abm = (ab * bc) / 4
angle_acb = atan(ab / bc)
bm = sqrt(bc**2 + cm**2 - (2 * (sqrt(bc**2 * cm**2 - 4 * (area_abm**2)))))
angle_mbc = cm * sin(angle_acb) / bm
print(f"{round(degrees(asin(angle_mbc)))}\N{DEGREE SIGN}")
