# 500 ile 1000 arasındaki çift sayıların 4 e bölünenlerinin kareköklerini
# alan ve ekrana yazdıran programı yazınız.

import math

for i in range(500,1000):
    if i%4==0:
        print(math.sqrt(i))
