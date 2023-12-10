import os

def input_kalimat():
  input_kalimat = input('Masukkan Kalimat: ')
  kalimat.append(input_kalimat)
  
def cek_kata():
  kata_list = []
  jumlah_kata = []
  for kata in kalimat:
    ambil_kata = kata.split()
    for hitung_kata in ambil_kata:
      if hitung_kata.isalpha():
        lower_kata = hitung_kata.lower()
        if lower_kata not in kata_list:
          kata_list.append(lower_kata)
          jumlah_kata.append(1)
        else:
          index = kata_list.index(lower_kata)
          jumlah_kata[index] += 1

  print("\nJumlah Kemunculan Setiap Kata:")
  for kata, jumlah in zip(kata_list, jumlah_kata):
      panjang_kata_list = len(ambil_kata)
      persentase = (jumlah / panjang_kata_list) * 100
      print(f"{kata}: {jumlah} kali ({persentase:.2f}%)")

def cek_huruf():
  huruf_list = []
  jumlah_huruf = []
  for ambil_kalimat in kalimat:
    for huruf in ambil_kalimat:
      if huruf.isalpha():
        lower_huruf = huruf.lower()
        if lower_huruf not in huruf_list:
          huruf_list.append(lower_huruf)
          jumlah_huruf.append(1)
      else:
        index = huruf_list.index(lower_huruf)
        jumlah_huruf[index] += 1
  
  print("\nJumlah Kemunculan Setiap Kata:")
  total_huruf = sum(jumlah_huruf)
  for huruf, jumlah in zip(huruf_list, jumlah_huruf):
      persentase = (jumlah / total_huruf) * 100
      print(f"{huruf}: {jumlah} kali ({persentase:.2f}%)")
  
if __name__ == '__main__':
  sistem_operasi = os.name
  while True:
    kalimat = []
    match sistem_operasi:
      case 'posix': os.system('clear')
      case 'nt': os.system('cls')

    print(f"{'SELAMAT DATANG DI PROGRAM':^30}")
    print(f"{'MENGANALISIS KALIMAT':^30}")
    print('-'*30)
    print('1. Input Kalimat')
    print('2. Keluar')
    option = input('Masukkan Nomer Menu: ')
    match option:
      case '1': 
        os.system("cls")
        print(f"{'SELAMAT DATANG DI PROGRAM':^30}")
        print(f"{'MENGANALISIS KALIMAT':^30}")
        print('-'*30)
        while True:
          try:
            if not kalimat:
              input_kalimat()
            else:
              os.system("cls")
              print(f"{'SELAMAT DATANG DI PROGRAM':^30}")
              print(f"{'MENGANALISIS KALIMAT':^30}")
              print('-'*30)
              print('1. Mengecek Kemunculan Setiap Kata')
              print('2. Mengecek Kemunculan Setiap Huruf')
              print('3. Keluar')
              option = input('Masukkan Nomer Menu: ')
              match option:
                case '1':
                  cek_kata()
                  is_done = input("Selesai Melihat? ")
                  if is_done:
                    continue
                case '2':
                  cek_huruf()
                  is_done = input("Selesai Melihat? ")
                  if is_done:
                    continue
                case '3':
                  break
          except:
            print('\nIsi terlebih dahulu')
      case '2':
        break