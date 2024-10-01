# 3500 ile 8900 arasındaki 11 e bölünen sayıların toplamı,7400 ile 26987
# arasındaki 231 e bölünen sayıların toplamından kaç fazladır?

topbir=0

for i in range(3500,8900):
    if i%11==0:
        topbir=topbir+i
print("11 e bölünen sayıların toplamı=",topbir)

topiki=0
for i in range(7400,26987):
    if i%231==0:
        topiki=topiki+i
print("231 e bölünen sayıların toplamı=",topiki)
print("farkları=",topbir-topiki)
