#Hafizh iltizam ilham
#2401286
#rpl A


username = "Daspro2023"
password = "Latihan"

def login():
    for kesempatan in range(3):
        print(f"kesempatan {kesempatan + 1} sampai 3")
        
        pw_username = input("Masukan Username kamu: ")
        pw_password = input(f"Masukan Password kamu: ")
        
        if pw_username == username and pw_password == password:
            print("Login Berhasil!!")
            return True
        
        else:
            print(f"Username dan password kamu salah")
            
    print("Kamu telah melakukan 3 kali percobaan. coba lagi nanti")
    return False

login()