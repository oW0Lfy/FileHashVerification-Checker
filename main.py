#libs
import hashlib
import os
import time
from datetime import date ,datetime
os.system('cls')
#functs
def checker(fname, val):
    ta = False
    h_md5=hashlib.md5()
    h_sha256=hashlib.sha256()
    h_sha512=hashlib.sha512()
    h_sha384=hashlib.sha384()
    try:
        open(fname, "rb")
    except:
        ta = True
    while ta == True:
        fname=input('No path/file found.\nInsert PATH or FILE again:')
        try:
            open(fname,"rb")
        except:
            print("Sorry.")
        else:
            ta = False
    if val == "1":
        with open(fname, "rb") as f:
            for i in iter(lambda: f.read(4096),b""):
                h_sha256.update(i)
        return h_sha256.hexdigest()
    if val == "2":
        with open(fname, "rb") as f:
            for i in iter(lambda:f.read(4096),b""):
                h_md5.update(i)
        return h_md5.hexdigest()
    if val == "3":
        with open (fname, "rb") as f:
            for i in iter(lambda: f.read(4096),b""):
                h_sha384.update(i)
        return h_sha384.hexdigest()
    if val == "4":
        with open (fname, "rb") as f:
            for i in iter(lambda: f.read(4096),b""):
                h_sha512.update(i)
        return h_sha512.hexdigest()
def save(htype, hash0, fname):
    yn=input(str('Save Data?(Y/N)\n>'))
    while yn not in ["Y","N","y","n"]:
        yn=input(str('Save Data?(Y/N)\n>'))
    if yn in ["N",'n']:
        time.sleep(0.5)
    else:
        if htype == "1":
            its="SHA-256"
        if htype == "2":
            its="MD5"
        if htype == "3":
            its="SHA-384"
        if htype == "4":
            its="SHA-512"
        os.system('cls')
        print("Saving Data.")
        time.sleep(0.5)
        print('/')
        time.sleep(0.5)
        print('-')
        time.sleep(0.5)
        print('\\')
        
        now = datetime.now()
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        ct=now.strftime("%H:%M:%S")
        if "DataHash" in os.listdir():
            try:
                dta = open ("DataHash/Data.txt", "a")
            except:
                dta = open ("DataHash/Data.txt","w")
            dta.write("\n\nFileName->"+fname+'\nType->'+its+'\nHash->'+hash0+'\nDate:'+d2+'  Time:'+ct)
            dta.close()
        else:
            os.mkdir("DataHash")
            dta = open ("DataHash/Data.txt", "w")
            dta.write("\n\nFileName->"+fname+'\nType->'+its+'\nHash->'+hash0+'\nDate:'+d2+'  Time:'+ct)
            dta.close()
        #dta = open ("../New folder/data.txt", "a")
        #dta.write("\n\nFileName->"+fname+'\nType->'+its+'\nHash->'+hash0+'\nDate:'+d2+'  Time:'+ct)
        #dta.close()

#cogs
sw = False
lop = 1
questi0=["1","2","0"]
questi2=["1","2","3","0","4"]
#TypesVars
mdV = ""
sha256V = ""
sha512V = ""
sha384 = ""
#Interface-Menu
print("This is a program Made by Wolfy. iykyk.\n\n\n")
quest = input(str('Select an option.\n(1)File Hash Verification.\n(2)File Hash Checker.\n\n(0)Exit\n>'))
while quest not in questi0:
    quest = input(str('Invalid Option!\n\nSelect an option.\n(1)File Hash Verification.\n(2)File Hash Checker.\n\n(0)Exit\n>'))
if quest == "0":
    lop = 0
while lop == 1:
    #FILE HASH CHECKER
    if quest == "2":
        os.system('cls')
        print('File Hash Checker.(A program made by W0Lfy)\n\n')
        q2=input(str('Choose Hash Type:\n(1)SHA-256\n(2)MD5\n(3)SHA-384\n(4)SHA-512\n\n(0)Exit\n>'))
        while q2 not in questi2:
            q2=input(str('Invalid Input.\nChoose Hash Type:\n(1)SHA-256\n(2)MD5\n(3)SHA-384\n(4)SHA-512\n\n(0)Exit\n>'))
        if q2 == "0":
            exit()
        if q2 == "1":
            os.system('cls')
            print('File Hash Checker\n\nType Selected--->SHA-256')
            fname2 = input(str("Give File's Path(or name if inside the Folder)\n>"))
            hash2=checker(fname2, q2)
            os.system('cls')
            print ("File Hash Checker\n\nType Selected-->SHA-256\nFile Path-->",fname2,"\nFile Hash-->",hash2)
        if q2 == "2":
            os.system('cls')
            print('File Hash Checker\n\nType Selected--->MD5')
            fname2 = input(str("Give File's Path(or name if inside the Folder)\n>"))
            hash2=checker(fname2, q2)
            os.system('cls')
            print ("File Hash Checker\n\nType Selected-->MD5\nFile Path-->",fname2,"\nFile Hash-->",hash2)
        if q2 == "3":
            os.system('cls')
            print('File Hash Checker\n\nType Selected--->SHA-384')
            fname2 = input(str("Give File's Path(or name if inside the Folder)\n>"))
            hash2=checker(fname2, q2)
            os.system('cls')
            print ("File Hash Checker\n\nType Selected-->SHA-384\nFile Path-->",fname2,"\nFile Hash-->",hash2)
        if q2 == "4":
            os.system('cls')
            print('File Hash Checker\n\nType Selected--->SHA-512')
            fname2 = input(str("Give File's Path(or name if inside the Folder)\n>"))
            hash2=checker(fname2, q2)
            os.system('cls')
            print ("File Hash Checker\n\nType Selected-->SHA-512\nFile Path-->",fname2,"\nFile Hash-->",hash2)
        sve=save(q2,hash2,fname2)
        
    if quest == "1":
        #FILE HASH VERIFICATION
        os.system('cls')
        print('File Hash Verification. (A program made by W0Lfy)\n\n')
        time.sleep(1)
        typh = input (str('Choose Hash Type:\n(1)SHA-256\n(2)MD5\n(3)SHA-384\n(4)SHA-512\n\n(0)Exit\n>'))
        while typh not in questi2:
            os.system('cls')
            typh = input (str('Invalid Number.\n\nChoose Hash Type:\n(1)SHA-256\n(2)MD5\n(3)SHA-384\n(4)SHA-512\n\n(0)Exit\n>'))
        #HashType Interface
        if typh == "3":
            os.system('cls')
            print('File Hash Verification (A program made by W0Lfy)\n\nHash Type-->SHA-384')
        if typh == "4":
            os.system('cls')
            print('File Hash Verification (A program made by W0Lfy)\n\nHash Type-->SHA-512')
        if typh == "2":
            os.system('cls')
            print('File Hash Verification (A program made by W0Lfy)\n\nHash Type-->MD5')
            
        if typh == "1":
            os.system('cls')
            print('File Hash Verification (A program made by W0Lfy)\n\nHash Type-->SHA-256')
        if typh == "0":
            exit()


        #Learn REAL hash
        urhash = input(str("\nInsert Verification Hash.\n-->"))
        #---------------------SPACE CHECKER----------------------------
        for i in range (len(urhash)):
            if " " == urhash[i]:
                sw = True
        while sw == True:
            print("SPACE found in hash. COPY/PASTE CAREFULLY!!!")
            urhash = input(str("Insert REAL hash(from website).\n-->"))
            for i in range (len(urhash)):
                if " " == urhash[i]:
                    sw = True
                else:
                    sw= False
        #-------------------SPACE CHECKER END--------------------------
        #md5 character checking
        if typh == "2":
            while len(urhash) != 32:
                if len(urhash) != 32:
                    urhash=input(str("Check your hash again.\n--->"))

        #sha256 character checking
        if typh == "1":
            while len(urhash) != 64:
                if len(urhash) != 64:
                    urhash=input(str("Check your hash again.\n--->"))
        #sha384
        if typh == "3":
            while len(urhash) != 96:
                if len(urhash) != 96:
                    urhash=input(str("Check your hash again.\n--->"))
        #sha512
        if typh == "4":
            while len(urhash) != 128:
                if len(urhash) != 128:
                    urhash=input(str("Check your hash again.\n--->"))

        #Real hash INterface
        os.system('cls')
        print("Data Collected.\nHash Type-->",typh,"\nReal Hash-->",urhash)
        #File name
        flname=input("\n\nInsert File Path...\n-->")
        #HashVerificationPerType
        if typh == "2":
            mdV = checker(flname, typh)
            if mdV == urhash:
                os.system('cls')
                print('Processing...')
                time.sleep(5)
                os.system('cls')
                print('Hash Type-->MD5\nREAL Hash:',urhash,"\nFile Hash:",mdV,"\nEverything seems normal. Nothing to worry about.")
            else:
                os.system('cls')
                print('Processing...')
                time.sleep(5)
                os.system('cls')
                print('Hash Type-->MD5\nREAL Hash:',urhash,"\nFile Hash:",mdV,"\nHASH IS CHANGED. DELETE FILE IMMEDIATELY.")

        if typh == "1":
            sha256V = checker(flname, typh)
            if sha256V == urhash:
                os.system('cls')
                print('Processing...')
                time.sleep(5)
                os.system('cls')
                print('Hash Type-->SHA-256\nREAL Hash:',urhash,"\nFile Hash:",sha256V,"\nEverything seems normal. Nothing to worry about.")
            else:
                os.system('cls')
                print('Processing...')
                time.sleep(5)
                os.system('cls')
                print('Hash Type-->SHA-256\nREAL Hash:',urhash,"\nFile Hash:",sha256V,"\nHASH IS CHANGED. DELETE FILE IMMEDIATELY.")
        if typh == "3":
            sha384V = checker(flname, typh)
            if sha384V == urhash:
                os.system('cls')
                print('Processing...')
                time.sleep(5)
                os.system('cls')
                print('Hash Type-->SHA-384\nREAL Hash:',urhash,"\nFile Hash:",sha384V,"\nEverything seems normal. Nothing to worry about.")
            else:
                os.system('cls')
                print('Processing...')
                time.sleep(5)
                os.system('cls')
                print('Hash Type-->SHA-384\nREAL Hash:',urhash,"\nFile Hash:",sha384V,"\nHASH IS CHANGED. DELETE FILE IMMEDIATELY.")
        if typh == "4":
            sha512V = checker(flname, typh)
            if sha512V == urhash:
                os.system('cls')
                print('Processing...')
                time.sleep(5)
                os.system('cls')
                print('Hash Type-->SHA-512\nREAL Hash:',urhash,"\nFile Hash:",sha512V,"\nEverything seems normal. Nothing to worry about.")
            else:
                os.system('cls')
                print('Processing...')
                time.sleep(5)
                os.system('cls')
                print('Hash Type-->SHA-512\nREAL Hash:',urhash,"\nFile Hash:",sha512V,"\nHASH IS CHANGED. DELETE FILE IMMEDIATELY.")

    quest = input(str('\n\nSelect an option.\n(1)File Hash Verification.\n(2)File Hash Checker.\n\n(0)Exit\n>'))
    if quest == "0":
        lop = 0

