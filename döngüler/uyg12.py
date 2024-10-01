# 1 den 20 ye kadar sayıların karesini ve kareler toplamını yazdıran program
toplam=0
for i in range(1,20):
    print(i,"sayısının karesi=",i**2)
    j=i**2
    toplam=toplam+j
print("bu sayıların toplamı=",toplam)
