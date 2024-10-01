# Alan ve çevre isimli iki fonksiyon tanımlayarak bir dikdörtgenin alan ve
# hacimlerini kullanıcının girmiş olduğu değerlerle hesapla,kullanıcının
# girdiği değerler fonksiyonda parametre olarak kullanılsın.


kk=int(input("Dörtgenin kısa kenarını giriniz="))
uk=int(input("Dörtgenin uzun kenarını giriniz="))

def alan(kk,uk):
    sonalan=kk*uk
    print("alan=",sonalan)
def cevre(kk,uk):
    soncevre=2*(uk+kk)
    print("çevre=",soncevre)
alan(kk,uk)
# Parametrelerle oluşturulan fonksiyon parametreyle çağrılır.
cevre(kk,uk)
