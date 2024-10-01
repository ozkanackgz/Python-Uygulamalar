# 1 den 200 e kadar olan sayıların toplamı,40 dan 165 e kadar olan sayıların
# toplamından kaç fazladır?

topbir=0
for i in range(1,200):
    topbir=topbir+i
print("1-200 arası sayılar toplamı=",topbir)

topiki=0
for j in range(40,165):
    topiki=topiki+j
print("40-165 arası sayıların toplamı=",topiki)
print("Fark=",topbir-topiki)
