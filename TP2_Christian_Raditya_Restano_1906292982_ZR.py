# Fungsi yang digunakan untuk mengumpulkan pesan dari user
def pengumpulan_pesan():
    # Meminta user memasukkan user dan menyimpannya ke dalam list
    kumpulan_pesan = []
    pesan = "Tersedia"
    while pesan :
        pesan = input("Pesan: ")
        kumpulan_pesan.append(pesan)

    # Memanggil fungsi yang akan mengumpulkan kata(belum murni) dari sebuah pesan
    pengumpulan_kata(kumpulan_pesan)

# Fungsi yang digunakan untuk mengambil kata
def pengumpulan_kata(kumpulan_pesan):
    #Mengambil kata-kata dari pesan yang dimasukkan dan disimpan dalam list
    kumpulan_kata = []
    for pesan in kumpulan_pesan :
        kata_kata = pesan.split()
        for kata in kata_kata :
            kumpulan_kata.append(kata)

    # Memanggil fungsi yang akan membuang tanda baca pada kata
    pembuangan_tanda_baca(kumpulan_kata)

# Fungsi yang digunakan untuk membuang tanda baca dari suatu kata
def pembuangan_tanda_baca(kumpulan_kata):
    # Menyiapkan list kosong dan memeriksa per kata
    kata_kata = []
    for kata in kumpulan_kata :
        
            # Memeriksa masing-masing karakter dalam kata
            word = ""
            for karakter in kata :
                
                # Memeriksa apakah karakter tersebut alfanumerik atau tidak
                if not karakter.isalnum():
                    if karakter == "-":
                        
                        # Memeriksa apakah sebelum dan sesudah karakter "-" adalah alfabet atau numerik
                        if kata[kata.index("-")-1].isalnum() and kata[kata.index("-")+1].isalnum():
                            word += karakter 
                            
                else :
                    word += karakter

            # Memasukkan kata yang sudah dibuang tanda bacanya ke dalam list 
            if len(word) != 0 :
                kata_kata.append(word.lower())

    # Memanggil fungsi yang akan membuang stop word
    pembuangan_stop_word(kata_kata)

# Fungsi yang digunakan untuk membuang stop word dari list kata yang akan dihitung          
def pembuangan_stop_word(kata_kata):
    # Membuka dan menutup file serta menyimpan isi file ke dalam list
    stop_word = open("TP2-stopword.txt", "r")
    kumpulan_stop_word = stop_word.read().split("\n")
    stop_word.close()

    # Memeriksa dan membuang setiap kata yang terdapat stop word
    for kata in kata_kata :
        if kata in kumpulan_stop_word :
            kata_kata.remove(kata)

    # Memanggil fungsi yang akan menghitung frekuensi kata
    penghitungan_kata(kata_kata)

# Fungsi yang digunakkan untuk menghitung frekuensi dari suatu kata
def penghitungan_kata(kata_kata):
    # Membuat variabe global agar dapat dipanggil pada fungsi lainnya
    global daftar_kata, jumlah_kata
    daftar_kata, jumlah_kata = [],[]

    # Membuat daftar kata agar tidak terdapat kata yang sama
    for kata in kata_kata :
        if kata not in daftar_kata :
            daftar_kata.append(kata)      
            
    # Membuat daftar jumlah frekuensi per kata
    for kata in daftar_kata :
        jumlah_kata.append(kata_kata.count(kata))

# Fungsi yang digunakan untuk membuat tampilan grafik dari data yang sudah ada
def pembuatan_grafik():
    # Mengimport module yang dibutuhkn
    import matplotlib.pyplot as plt, numpy as np
    
    # Mengatur item yang akan ditampilkan pada sumbu x dan y
    y_pos = np.arange(len(daftar_kata))
    plt.barh(y_pos, jumlah_kata[::-1], align = "center")
    plt.yticks(y_pos, daftar_kata[::-1])
    
    # Mengatur ukuran grafik
    fig = plt.gcf()
    fig.set_size_inches(7,10)
    
    # Membuat judul serta keterangan pada sumbu x dan y
    plt.title("Frekuensi Kemunculan Kata")
    plt.xlabel("Frekuensi")
    plt.ylabel("Daftar Kata")
    
    # Memunculkan grafik
    plt.show()
    
# Fungsi utama yang akan menginisiasi jalannya semua fungsi
def main():
    # Membuat perintah agar user dapat tau harus melakukan apa
    print("="*70)
    print("Masukkan pesan: (untuk berhenti masukkan string kosong)")
    print("="*70)

    # Memanggil fungi yang akan mengumpulkan pesan
    pengumpulan_pesan()

    # Membuat tabel yang berisi daftar kata dan frekuensinya
    print("Distribusi frekuensi kata: ")
    print("-"*35)
    print("{:>3s}  {:17s}  {}".format("No", "Kata", "Frekuensi"))
    print("-"*35)
    for indeks in range(len(daftar_kata)) :
        print("{:3d}  {:17s}  {:2d}".format(indeks + 1, daftar_kata[indeks], jumlah_kata[indeks]))
    print("-"*35)
    
    # Memanggil fungsi yang akan membuat grafik
    pembuatan_grafik()
 
# Pemanggilan fungsi utama
if __name__ == "__main__" :
    main()