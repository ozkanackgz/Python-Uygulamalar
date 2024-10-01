# 1 den 100 e kadar 5 ile bölünen sayıların toplamı,1 den 100 e kadar 10 ile
# bölünen sayıların toplamından kaç fazladır?

topbes=0
for i in range(0,100,5):
    topbes=topbes+i
topon=0
for i in range(0,100,10):
    topon=topon+i
print("5 ile bölünenlerin toplamı=",topbes)
print("10 ile bölünenlerin toplamı=",topon)
print(topbes,"-",topon,"=",topbes-topon)
