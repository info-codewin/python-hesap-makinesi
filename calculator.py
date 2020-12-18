#wincode.ml farkıyla :)
# Buralarla oynamayın fazla :D
def toplama(x, y):
    return x + y

def cikartma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return x / y


print("İşlemi seçin.")
print("1.Toplama")
print("2.Çıkartma")
print("3.Çarpma")
print("4.Bölme")

while True:

    choice = input("Seçimi girin(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("İlk sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))

        if choice == '1':
            print(num1, "+", num2, "=", toplama(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", cikartma(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", carpma(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", bolme(num1, num2))
        break
    else:
        print("Geçersiz Giriş")
