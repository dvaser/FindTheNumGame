
import os, random, time, datetime, ControlManager, Manager

class _Main:
    
    def start():
        wellcome = " Oyuna Hos Geldin "
        wellcome = wellcome.center(50,'-')
        print("\n"+"-"*(len(wellcome))+"\n"+wellcome+"\n"+"-"*(len(wellcome)))
        _Methods.timer(seconds=2)

    def menu():
        
        try:
            helloMenu = int(input("\nMENU\n\n Kayit olusturmak icin         1\n Giris yapmak icin             2\n Misafir girisi icin           3\n Oyun hakkinda bilgi icin      4"))
            if helloMenu is not 1 or 2 or 3 or 4:
                raise Exception("Tuslamayi dogru yapiniz.")
            if TypeError:
                raise Exception("Rakamsal tuslama yapiniz.")
        except Exception as ex:
            print(F'\nHatali deger girdiniz...\nError !! {ex}')
        else:
            if helloMenu == 1:
                Manager._Register.userRegister()
            elif helloMenu == 2:
                pass
            elif helloMenu == 3:
                pass
            elif helloMenu == 4:
                aboutGameFile = open("AboutGameFile.txt", "r", encoding='utf-8')
                aboutGameFile

        print("\n"+"-"*(len(helloMenu))+"\n"+helloMenu+"\n"+"-"*(len(helloMenu)))       
        
        #! Menu girisi >> Kaydol, giris yap >> Misafir Girisi, Giris , oyun hakkinda.   

    def numOfGamer():
        try:
            numberOfUser = int(input("\nOyunu kaç kişi oynayacak: "))
        except Exception:
            print("\n Dikkat !!\n\n Hatalı karakter girdiniz... Tekrar deneyiniz.")

class _Methods:

    def timer(seconds=2.5, writer=''):
        then = datetime.datetime.now() + datetime.timedelta(seconds)
        print(f'\n{writer}')
        while then > datetime.datetime.now():
            time.sleep(1)
        else:
            os.system('cls')