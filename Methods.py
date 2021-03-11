
import os, random, time, datetime, ControlManager

class _Main:
    
    def start():
        wellcome = " Oyuna Hos Geldin "
        wellcome = wellcome.center(50,'-')
        print("\n"+"-"*(len(wellcome))+"\n"+wellcome+"\n"+"-"*(len(wellcome)))
        _Methods.timer('')

    def numOfGamer():
        try:
            numberOfUser = int(input("\nOyunu kaç kişi oynayacak: "))
        except TypeError:
            print("\n Dikkat !!\n\n Hatalı karakter girdiniz... Tekrar deneyiniz.")

class _Methods:

    def timer(seconds=2.5, writer=''):
        then = datetime.datetime.now() + datetime.timedelta(seconds)
        print(f'\n{writer}')
        while then > datetime.datetime.now():
            time.sleep(1)
        else:
            os.system('cls')