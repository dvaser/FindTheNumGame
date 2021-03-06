
import os, random, time, datetime, ControlManager, Manager

class _Main:
    
    def start():
        wellcome = " Oyuna Hos Geldin "
        wellcome = wellcome.center(50,'-')
        print("\n"+"-"*(len(wellcome))+"\n"+wellcome+"\n"+"-"*(len(wellcome)))
        _Methods.timer(seconds=2)

    def numOfGamer():
        isBool = True
        while isBool:    
            global numberOfUser
            try:
                numberOfUser = input("\nOyunu kaç kişi oynayacak: ")
                ControlManager._ControlMenu.checkNumOfUser(numOfUser=numberOfUser)
            except Exception as ex:
                print(f"\n Dikkat !!\n\n Hatalı karakter girdiniz... Error: {ex} Tekrar deneyiniz.")
                print("\n"+"-"*50)
            else:
                isBool = False

    def menu():
        isBool = True
        while isBool:    
            try:
                helloMenu = int(input("\nMENU\n\n Kayit olusturmak icin         1\n Giris yapmak icin             2\n Misafir girisi icin           3\n Oyun hakkinda bilgi icin      4\n Cikis yapmak icin             5\n\n                                Tuslayiniz: "))
                ControlManager._ControlMenu.checkMenu(helloMenu=helloMenu)
            except Exception as ex:
                print(f'\nHatali deger girdiniz...\nError !! {ex}')
                _Methods.timer(seconds=2)
            else:
                isBool = False
                if helloMenu == 1:
                    os.system('cls')
                    print("\n"+"-"*50)
                    Manager._Register.userRegister()
                    _Methods.timer(seconds=2, writer="Kayit Basarili...")
                    choose = input("\n\nMenuye devam etmek icin herhangi tuslama yapiniz: ")
                    _Main.menu()
                elif helloMenu == 2:
                    os.system('cls')
                    print("\n"+"-"*50)
                    Manager._Login.userLogin()
                    _Methods.timer(seconds=2, writer="Giris Basarili...")
                elif helloMenu == 3:
                    _Main.numOfGamer()
                    Manager._Register.guestRegister(numberOfUser=numberOfUser)
                    _Methods.timer(seconds=2, writer=f"Kayit Basarili... {int(numberOfUser)} kullanıcıya da başarılar.")
                    _Main.gameMenu()
                elif helloMenu == 4:
                    os.system('cls')
                    aboutGameFile = open("AboutGameFile.txt", "r", encoding='utf-8')
                    aboutGameFile.seek(0)
                    print(aboutGameFile.read())
                    aboutGameFile.close()
                    choose = input("\n\nMenuye devam etmek icin herhangi tuslama yapiniz: ")
                    _Methods.timer(seconds=0.1)
                    _Main.menu()
                elif helloMenu == 5:
                    _Methods.ScreenWriter(seconds=2.5, writer='Tekrar Bekleriz... Hosca kal...')

    def gameMenu():
        isBool = True
        while isBool:    
            try:
                gameMenu = int(input("\nGAME MENU\n\n Oyuna baslamak icin            1\n Oyun hakkinda bilgi icin       2\n Menuye donmek icin             3\n\n                                 Tuslayiniz: "))
                ControlManager._ControlMenu.checkGameMenu(gameMenu=gameMenu)
            except Exception as ex:
                print(f'\nHatali deger girdiniz...\nError !! {ex}')
                _Methods.timer(seconds=2)
            else:
                isBool = False
                if gameMenu == 1: 
                    Manager._Game.gameGuest()
                elif gameMenu == 2:
                    os.system('cls')
                    aboutGameFile = open("AboutGameFile.txt", "r", encoding='utf-8')
                    aboutGameFile.seek(0)
                    print(aboutGameFile.read())
                    aboutGameFile.close()
                    choose = input("\n\nOyun Menusune donmek icin herhangi tuslama yapiniz: ")
                    _Methods.timer(seconds=0.1)
                    _Main.gameMenu()
                elif gameMenu == 3:
                    _Main.menu()


class _Methods:

    def timer(seconds=2.5, writer=''):
        then = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        print(f'\n{writer}')
        while then > datetime.datetime.now():
            time.sleep(1)
        else:
            os.system('cls')

    def ScreenWriter(seconds=2.5, writer=''):
        os.system('cls')
        then = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        print(f'\n{writer}')
        while then > datetime.datetime.now():
            time.sleep(1)
        else:
            os.system('cls')

    def cupMassage(massage=' '):
        print(f"{len(massage)*' '} BBBBBB     RRRRRR             AA  VV              VV   OOOOOOO         ##############")
        print(f"{len(massage)*' '} BB   BB    RR    RR          AAAA  VV            VV  OO       OO        ## WINNER ## ")
        print(f"{len(massage)*' '} BB   BB    RR    RR         AA  AA  VV          VV  OO         OO        ##########  ")
        print(f"{len(massage)*' '} BBBBBB     RRRRRRR         AA    AA  VV        VV   OO         OO           ####     ")
        print(f"{len(massage)*' '} BB   BB    RR    RR       AAAAAAAAAA  VV      VV    OO         OO            ##      ")
        print(f"{len(massage)*' '} BB     BB  RR     RR     AA        AA  VV    VV     OO         OO            ##      ")
        print(f"{len(massage)*' '} BB     BB  RR      RR   AA          AA  VV  VV       OO       OO            ####     ")
        print(f"{len(massage)*' '} BBBBBBBB   RR       RR AA            AA  VVVV          OOOOOOO           ##########  ")



