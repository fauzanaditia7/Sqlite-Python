import os
from database import Database

db = Database()
pilihan = {
    1: ["Tampilkan Data", db.show],
    2: ["Masukkan Data", db.insert],
    3: ["Keluar", exit]
}

while not False:
    if os.name.lower() == "nt":
        os.system("cls")
    elif any([os.name.lower() == "darwin", os.name.lower() == "posix"]):
        os.system("clear")
    for a, i in enumerate(pilihan, start=1):
        print('%s. %s' % (a, pilihan[i][0]))
    userChoice = input("Masukkan 1 / 2 : ")
    if not userChoice.isdigit():
        userChoice = input("Masukkan hanya angka : ")
        continue
    if int(userChoice) > len(pilihan):
        print("Masukkan hanya 1 / 2")
        continue
    if (int(userChoice) == 1):
        print(pilihan[int(userChoice)][1]())
    elif (int(userChoice) == 2):
        while 1:
            nama = input("Masukkan Nama : ")
            npm = input("Masukkan NPM : ")
            if not npm.isdigit():
                print("Masukkan Hanya Angka")
                continue
            jurusan = input("Masukkan Jurusan : ")
            pilihan[int(userChoice)][1](nama, int(npm), jurusan)
            print("Sukses Masukkan Data")
            break
    elif (int(userChoice) == 3):
        pilihan[int(userChoice)][1]()
    if (input("Lanjutkan Program [Y/N] : ").lower() == "y"):
        continue
    break
