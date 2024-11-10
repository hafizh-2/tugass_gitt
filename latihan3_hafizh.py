#Hafizh iltizam ilham
#2401286
#rpl A


def hitung_selisih_waktu(mulai_jam, mulai_menit, mulai_detik, selesai_jam, selesai_menit, selesai_detik):

    waktu_mulai = mulai_jam * 3600 + mulai_menit * 60 + mulai_detik
    waktu_selesai = selesai_jam * 3600 + selesai_menit * 60 + selesai_detik

    selisih_detik = waktu_selesai - waktu_mulai
    

    selisih_jam = selisih_detik // 3600
    selisih_detik %= 3600
    selisih_menit = selisih_detik // 60
    selisih_detik %= 60
    
    return selisih_jam, selisih_menit, selisih_detik


mulai_jam = 8
mulai_menit = 10
mulai_detik = 20


selesai_jam = 9
selesai_menit = 15
selesai_detik = 30


selisih_jam, selisih_menit, selisih_detik = hitung_selisih_waktu(mulai_jam, mulai_menit, mulai_detik, selesai_jam, selesai_menit, selesai_detik)

print(f"Selisih waktu: {selisih_jam} jam - {selisih_menit} menit - {selisih_detik} detik")