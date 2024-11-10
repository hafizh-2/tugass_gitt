#Hafizh iltizam ilham
#2401286
#rpl A


def fibonacci(n):
    
    hasil = [0, 1]
    for i in range(2, n):
        angka = hasil[-1] + hasil[-2]
        hasil.append(angka)
    return hasil

N = int(input("Masukkan jumlah bilangan Fibonacci yang ingin dihitung: "))

if N > 0:
    hasil = fibonacci(N)
    print(f"Deret Fibonacci sebanyak {N} bilangan adalah: {hasil}")
else:
    print("Masukkan bilangan positifff.")