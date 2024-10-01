# 40 ile 1600 arasındaki çift sayıların toplamının %10'u,6780 ile 7400
# arasındaki 5 ile bölünebilen sayıların toplamının yarısından kaç eksiktir?

topbir=0
for i in range(40,1600,2):
    topbir=topbir+i
topiki=0

for i in range(6780,7400,5):
    topiki=topiki+i
sontoplam=(topbir*10/100)-(topiki/2)
print(sontoplam)
