#LIST 
print ("\n\t*MENGHITUNG NILAI AKHIR MAHASISWA TEKNOLOGI INFORMASI*\n")
mahasiswa= [["Achmad Alief                 |teknologi informasi" ,192104001],
["Nedi Tiara Regifa            |teknologi informasi", 192104002],
["Ahmad Gofiansah              |teknologi informasi", 192104003],
["Bagas Saktiawan Prasojo      |teknologi informasi", 192104004],
["Bambang Sadewo               |teknologi informasi", 192104005],
["Dimas Pratama                |teknologi informasi", 192104006],
["Velisia Amanda Khafid        |teknologi informasi", 192104007]]

#FUNGSI + PERULANGAN
def mahasiswa_tekno():
	print("==================================================================")
	print("|no|       nama mahasiswa          |       prodi       |   nim   |")
	print("==================================================================")
	i=1
	for item in mahasiswa:
		print("|"+str(i)+" |  "+item[0]+"|"+str(item[1])+"|")
		i+=1

#INPUTAN,PERULANGAN, PERCABANGAN,   EXCEPTION HANDLING, DAN OUTPUT
try:
	
	i = 1
	while i <=4:
		mahasiswa_tekno()

		print("==================================================================")
		nim = int(input("Masukkan nim\t\t : "))
		print("==================================================================")
		

		if nim == 192104001:
			print("nama\t\t\t : Achmad Alief")
			print("prodi\t\t\t : teknologi informasi")
			print("==================================================================")
		elif nim == 192104002:
			print("nama\t\t\t : Nedi Tiara Regifa")
			print("prodi\t\t\t : teknologi informasi")
			print("==================================================================")
		elif nim == 192104003:
			print("nama\t\t\t : Ahmad Gofiansah")
			print("prodi\t\t\t : teknologi informasi")
			print("==================================================================")
		elif nim == 192104004:
			print("nama\t\t\t : Bagas Saktiawan Prasojo")
			print("prodi\t\t\t : teknologi informasi")
			print("==================================================================")
		elif nim == 192104005:
			print("nama\t\t\t : Bambang Sadewo")
			print("prodi\t\t\t : teknologi informasi")
			print("==================================================================")
		elif nim == 192104006:
			print("nama\t\t\t : Dimas Pratama")
			print("prodi\t\t\t : teknologi informasi")
			print("==================================================================")
		elif nim == 192104007:
			print("nama\t\t\t : Velisia Amanda Khafid")
			print("prodi\t\t\t : teknologi informasi")
			print("==================================================================")
		else:
			kalimat="bukan mahasiswa prodi teknologi informasi"
			print(kalimat.upper())
			break

		print("Pilihan mata kuliah\t : \n")
		print("1. konsep pemrograman")
		print("2. matematika diskrit")
		print("3. logika informatika")
		print("4. bahasa inggris")
		print("==================================================================")


		matkul = int(input("Masukkan no matkul\t : "))
		print("")
		if matkul == 1:
			print(">> Mata Kuliah Konsep Pemrograman <<")
		elif matkul == 2:
			print(">> Mata kuliah Matematika Diskrit <<")
		elif matkul == 3:
			print(">> Mata Kuliah Logika Informatika <<")
		elif matkul == 4:
			print(">> Bahasa Inggris <<")
		else:
			print(">> Mata Kuliah yang Dimasukan Salah! Silahkan Pilih Yang Ada di Pilihan Mata Kuliah <<")
			break
		
		print("==================================================================")	
		uts = int(input("Masukkan Nilai UTS       : "))
		print("")
		uas = int(input("Masukkan Nilai UAS       : "))
		print("")
		tugas = int(input("Masukkan Nilai Tugas     : "))
		print("")
		presensi = int(input("Masukkan Nilai Kuis\t : "))
		print("")
		kuis = int(input("Masukkan Nilai Presensi  : "))
		print("")
		sikap = int(input("Masukkan Nilai Sikap     : "))
		print("")
		UTS = uts*20/100
		UAS = uas*20/100
		Tugas = tugas*20/100
		Presensi = presensi*15/100
		Kuis = kuis*15/100
		Sikap = sikap*10/100
		Jumlah_Nilai =(uts+uas+tugas+presensi+kuis+sikap)
		print("Jumlah Nilai\t\t :",Jumlah_Nilai)
		print("")
		Rata_rata =(uts+uas+tugas+presensi+kuis+sikap)/6
		print("Rata - rata\t\t : %i"% (Rata_rata))


		if Rata_rata>=85 :
			print ("\nNilai Huruf\t\t : A\n")
		elif Rata_rata>=75 :
			print ("\nNilai Huruf\t\t : B\n")
		elif Rata_rata>=70 :
			print ("\nNilai Huruf\t\t : C\n")
		elif Rata_rata>=60 :
			print ("\nNilai Huruf\t\t : D\n")
		elif Rata_rata<=59 :
			print ("\nNilai Huruf\t\t : E\n")
		i+=1

		if Rata_rata>=70:
			print("\t\t\t+++++++++")
			print("\t\t\t| LULUS |") 
			print("\t\t\t+++++++++")
			output1="\n\t*selamat anda lulus mata kuliah ini!*\n\n"
			print(output1.upper())
		else:
			print("\t\t\t   +++++++++++++++")
			print ("\t\t\t   | TIDAK LULUS |")
			print("\t\t\t   +++++++++++++++")
			output2="\n\t*silahkan mengulang mata kuliah di semester berikutnya!*\n\n"
			print(output2.upper())

except ValueError:
	print("\nData Harus Diisi Dengan Benar!!!")