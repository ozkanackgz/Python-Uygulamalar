# Bir ürünün satışında alışfiyatı,kar oranı,adeti ve KDV si girilerek ürünün
# son fiyatını yazdıran fonksiyonu oluşturunuz.

af=int(input("Ürünün alış fiyatını giriniz="))
ko=int(input("Ürünün kar oranını giriniz="))
sa=int(input("Ürünün kaç tane satıldığını giriniz="))
kdv=int(input("Ürünün KDV oranını giriniz="))

def ciro(af,ko,sa,kdv):
    toplamciro=sa*(af+(af*ko/100)+(af*kdv/100))
    print("toplamciro=",toplamciro)
    print("toplamkar=",toplamciro-(af*sa))
ciro(650,18,9,236)
