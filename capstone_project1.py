#define beginning database - dictionary
database_karyawan = {
    1 : {
        'Nama' : 'Kevin',
        'Usia' : 26,
        'Posisi' : 'Head',
        'Department' : 'IT'
    },
    2 : {
        'Nama' : 'Angga',
        'Usia' : 30,
        'Posisi' : 'Mngr',
        'Department' : 'IT'
    },
    3 : {
        'Nama' : 'Agus',
        'Usia' : 35,
        'Posisi' : 'SPV',
        'Department' : 'IT'
    }
}

#define main menu - perlu run
def main_menu() : 
    try:
        input_main_menu = int(input('''
        Selamat datang di menu database karyawan PT Megah Abadi
        Main Menu :
        1. Lihat data karyawan
        2. Modifikasi data karyawan
        3. Summary data karyawan
        4. Keluar program
        Masukkan menu yang anda inginkan: '''))
        if (input_main_menu == 1):
            lihat_data_karyawan()
        elif (input_main_menu == 2):
            modifikasi_data_karyawan()
        elif (input_main_menu == 3):
            summary_data_karyawan()
        elif (input_main_menu == 4):
            keluar_program()
        elif (input_main_menu <1 or input_main_menu >4):
            print('\nMenu {} tidak tersedia! Silahkan masukkan angka 1-4'.format(input_main_menu))
            main_menu()
    except ValueError :
        print('\nAnda tidak memasukkan angka! Harap masukkan angka 1-4')
        main_menu()

#define options on main menu - perlu run
def lihat_data_karyawan() :
    try:
        input_lihat_data_karyawan = int(input('''
        Anda memilih menu "Lihat Data Karyawan"
        Berikut opsi dari menu ini :
        1. Tampilkan seluruh data karyawan
        2. Cari karyawan berdasarkan nomor
        3. Kembali ke menu utama
        4. Keluar program
        Opsi yang anda pilih : '''))
        if (input_lihat_data_karyawan == 1):
            tampilkan_data()
            main_menu()
        elif (input_lihat_data_karyawan == 2):
            cari_data()
        elif (input_lihat_data_karyawan == 3):
            main_menu()
        elif (input_lihat_data_karyawan == 4):
            keluar_program()
        elif (input_lihat_data_karyawan < 1 or input_lihat_data_karyawan > 4):
            print('\nMenu {} tidak tersedia! Silahkan masukkan angka 1-4'.format(input_lihat_data_karyawan))
            lihat_data_karyawan()
    except ValueError :
        print('\nAnda tidak memasukkan angka! Harap masukkan angka 1-4')
        lihat_data_karyawan()


#define Tampilkan Data - checked
def tampilkan_data():
    print('Daftar Seluruh Karyawan: \n')
    print('|No\t|Nama\t|Usia\t|Posisi\t|Department\t|')
    for key in database_karyawan :
        print('|{}\t|{}\t|{}\t|{}\t|{}\t\t|'.format(key,database_karyawan[key]['Nama'],database_karyawan[key]['Usia'],database_karyawan[key]['Posisi'],database_karyawan[key]['Department']))

#cari data - checked
def cari_data():
    tampilkan_data()
    try:
        nomor_input = int(input('''
            Masukkan nomor karyawan yang dicari:
            Atau masukkan 0 untuk kembali pada menu sebelumnya'''))
        if nomor_input in range(1,len(database_karyawan)+1) :
            print('Karyawan yang anda cari terdaftar!')
            print('|No\t|Nama\t|Usia\t|Posisi\t|Department\t|')
            print('|{}\t|{}\t|{}\t|{}\t|{}\t\t|'.format(nomor_input,database_karyawan[nomor_input]['Nama'],database_karyawan[nomor_input]['Usia'],database_karyawan[nomor_input]['Posisi'],database_karyawan[nomor_input]['Department']))
            main_menu()
        elif nomor_input == 0:
            lihat_data_karyawan()
        elif nomor_input not in range(1,len(database_karyawan)+1) :
            print('Nomor yang anda masukkan tidak ada. Harap masukkan sesuai dengan list yang tersedia')
            cari_data()
    except:
        print('Anda hanya boleh input angka!')
        cari_data()

def modifikasi_data_karyawan():
    try:
        opsi_modifikasi = int(input('''
        Anda memilih menu "Modifikasi Data Karyawan"
        Berikut opsi dari menu ini :
        1. Tambah data
        2. Hapus data
        3. Update / Ubah data
        4. Kembali ke menu utama
        Opsi yang anda pilih : '''))
        if (opsi_modifikasi == 1):
            tambah_data()
        elif (opsi_modifikasi == 2):
            hapus_data()
        elif (opsi_modifikasi == 3):
            update_data()
        elif (opsi_modifikasi == 4):
            main_menu()
        elif (opsi_modifikasi < 1 or opsi_modifikasi > 4):
            print('\nOpsi {} tidak tersedia! Silahkan masukkan angka 1-4'.format(opsi_modifikasi))
            modifikasi_data_karyawan()
    except ValueError :
        print('\nAnda tidak memasukkan angka! Harap masukkan angka 1-4')
        modifikasi_data_karyawan()

def tambah_data_nama():
    global nama_baru
    nama_baru = input('Masukkan nama baru: ')
    if nama_baru.isnumeric():
        print('Hanya boleh alphabet!')
        tambah_data_nama()
    elif nama_baru.isalpha():
        print('Berhasil input nama!')
    else:
        print('Harap masukkan alphabet')
        tambah_data_nama()

def tambah_data_usia():
    global usia_baru
    usia_baru = input('Masukkan usia baru: ')
    if usia_baru.isalpha():
        print('Hanya boleh angka!')
        tambah_data_usia()
    elif usia_baru.isnumeric():
        print('Berhasil input usia!')
    else:
        print('Harap masukkan angka')
        tambah_data_usia()

def tambah_data_posisi():
    global posisi_baru
    posisi_baru = input('Masukkan posisi baru (Stff / SPV / Mngr / Head): ')
    posisi_baru = posisi_baru.lower()
    if (posisi_baru != 'stff' and posisi_baru != 'spv' and posisi_baru != 'mngr' and posisi_baru != 'head'):
        print('Posisi tidak tersedia')
        tambah_data_posisi()
    elif (posisi_baru == 'stff' or posisi_baru == 'spv' or posisi_baru == 'mngr' or posisi_baru == 'head'):
        if (posisi_baru == 'stff' or posisi_baru == 'mngr' or posisi_baru == 'head'):
            posisi_baru = posisi_baru.capitalize()
            print('Berhasil input posisi!')
        else:
            posisi_baru = posisi_baru.upper()
            print('Berhasil input posisi!')
    else:
        pass

def tambah_data_department():
    global department_baru
    department_baru = input('Masukkan department baru: ')
    if type(department_baru) != str:
        print('Hanya boleh alphabet!')
        tambah_data_department()
    elif type(department_baru) == str:
        print('Berhasil input department!')
    else:
        pass

def tambah_data():
    try:
        opsi_tambah = int(input('''
        Anda memilih menu "Tambah Data Karyawan"
        Berikut opsi dari menu ini :
        1. Tambah data
        2. Kembali ke menu utama
        Opsi yang anda pilih : '''))
        if (opsi_tambah == 1):
            tampilkan_data()
            global tambah_nomor
            tambah_nomor = int(input('Masukkan no baru: '))
            if type(tambah_nomor) != int:
                print('Hanya boleh masukkan angka!')
                tambah_data()
            elif tambah_nomor <= len(database_karyawan):
                print('Nomor {} sudah ada. Silahkan input nomor lain yang belum ada'.format(tambah_nomor))
                tambah_data()
            elif tambah_nomor > len(database_karyawan):
                print('Nomor dapat digunakan')
                tambah_data_nama()
                tambah_data_usia()
                tambah_data_posisi()
                tambah_data_department()
                print('Data berhasil ditambah!')
                database_karyawan[tambah_nomor] = {'Nama' : nama_baru, 'Usia' : usia_baru, 'Posisi' : posisi_baru, 'Department' : department_baru}
                tampilkan_data()
                modifikasi_data_karyawan()
        elif (opsi_tambah == 2):
            modifikasi_data_karyawan()
        elif (opsi_tambah < 1 or opsi_tambah > 2):
            print('\nOpsi {} tidak tersedia! Silahkan masukkan angka 1-2'.format(opsi_tambah))
            tambah_data()
    except ValueError :
        print('\nAnda tidak memasukkan angka! Harap masukkan angka 1-2')
        tambah_data()

def hapus_data():
    try:
        opsi_hapus = int(input('''
        Anda memilih menu "Hapus Data Karyawan"
        Berikut opsi dari menu ini :
        1. Hapus data
        2. Kembali ke menu utama
        Opsi yang anda pilih : '''))
        if opsi_hapus == 1:
            tampilkan_data()
            nomor_input = int(input('''
            Masukkan nomor karyawan yang ingin dihapus:
            Atau masukkan 0 untuk kembali pada menu sebelumnya'''))
            if nomor_input in range(1,len(database_karyawan)+1) :
                print('Karyawan yang anda akan hapus! {}'.format(database_karyawan[nomor_input]))
                print('Anda yakin?')
                jawaban = input('Anda yakin? (yes or no)')
                jawaban = jawaban.lower()
                if jawaban == 'yes':
                    del database_karyawan[nomor_input]
                    print('Karyawan berhasil dihapus!')
                    tampilkan_data()
                    main_menu()
                elif jawaban == 'no':
                    print('Anda batal untuk hapus data')
                    main_menu()
                else:
                    print('''Jawaban hanya boleh 'yes' atau 'no' ''')
                    hapus_data()
            elif nomor_input not in range(1,len(database_karyawan)+1) :
                print('Nomor yang anda masukkan tidak ada. Harap masukkan sesuai dengan list yang tersedia')
                hapus_data()
        elif opsi_hapus == 2:
            modifikasi_data_karyawan()
        elif opsi_hapus > 2:
            print('Menu tidak tersedia! Harap masukkan angka 1-2')
            hapus_data()
        else:
            print('Input anda tidak sesuai')
            modifikasi_data_karyawan()
    except :
        print('\nAnda tidak memasukkan angka! Harap masukkan angka 1-2')
        hapus_data()

def ubah_nama():
    nama_baru = input('Masukkan nama baru: ')
    if type(nama_baru) != str:
        print('Hanya boleh alphabet!')
        ubah_nama()
    elif type(nama_baru) == str:
        database_karyawan[nomor_input]['Nama'] = nama_baru
        print('Nama berhasil diubah!')
    else:
        print('Input anda tidak sesuai')
        ubah_nama()

def ubah_usia():
    usia_baru = input('Masukkan usia baru: ')
    if usia_baru.isalpha():
        print('Hanya boleh angka!')
        ubah_usia()
    elif usia_baru.isnumeric():
        usia_baru = int(usia_baru)
        database_karyawan[nomor_input]['Usia'] = usia_baru
        print('Usia berhasil diubah!')
    else:
        print('Input anda tidak sesuai')
        ubah_usia()

def ubah_posisi():
    posisi_baru = input('Masukkan posisi baru (Stff / SPV / Mngr / Head) :')
    posisi_baru = posisi_baru.lower()
    if (posisi_baru != "stff" and posisi_baru != "spv" and posisi_baru != "mngr" and posisi_baru != "head"):
        print('Posisi tidak tersedia, harap masukkan sesuai pilihan')
        ubah_posisi()
    elif (posisi_baru == "stff" or posisi_baru == "spv" or posisi_baru == "mngr" or posisi_baru == "head"):
        if (posisi_baru == "stff" or posisi_baru == "mngr" or posisi_baru == "head"):
            posisi_baru = posisi_baru.capitalize()
        elif (posisi_baru == "spv"):
            posisi_baru = posisi_baru.upper()
        database_karyawan[nomor_input]['Posisi'] = posisi_baru
        print('Posisi berhasil diubah')
    else:
        print('Input anda tidak sesuai')
        ubah_posisi()

def ubah_department():
    department_baru = input('Masukkan department baru :')
    if type(department_baru) != str:
        print('Hanya boleh alphabet!')
        ubah_department()
    elif type(department_baru) == str:
        database_karyawan[nomor_input]['Department'] = department_baru
        print('Department berhasil diubah!')
    else:
        print('Input anda tidak sesuai')
        ubah_department()

def update_data():
    try:
        tampilkan_data()
        global nomor_input
        nomor_input = int(input('''
            Masukkan nomor karyawan yang ingin diubah:
            Atau masukkan 0 untuk kembali pada menu utama'''))
        if nomor_input in range(1,len(database_karyawan)+1) :
            ubah_nama()
            ubah_usia()
            ubah_posisi()
            ubah_department()
            tampilkan_data()
            main_menu()
        elif nomor_input == 0:
            main_menu()
        else:
            print('Input anda tidak sesuai, masukkan angka sesuai yang tersedia')
            update_data()
    except:
        print("Input tidak valid, kembali ke menu sebelumnya")
        modifikasi_data_karyawan()
            
def summary_data_karyawan():
    try :
        menu_summary = int(input('''
        Pilihan menu summary :
        1. Jumlah karyawan
        2. Kembali ke menu utama
        Masukkan pilihan yang anda inginkan : '''))
        if (menu_summary == 1):
            print('Jumlah karyawan adalah : {} orang'.format(len(database_karyawan)))
            main_menu()
        elif (menu_summary == 2):
            main_menu()
    except:
        print("Anda tidak memasukkan angka")
        summary_data_karyawan()

#keluar program
def keluar_program():
    print('\nTerima kasih telah menggunakan program ini')
    print('Sampai jumpa lagi ~')

main_menu()