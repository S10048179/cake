from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
from colorama import init, Fore, Back, Style
from time import sleep
import os
init()

def printCake():
    print(Fore.RED + """            ,:/+/-
                /M/              .,-=;//;-
           .:/= ;MH/,    ,=/+%$XH@MM#@:
          -$##@+$###@H@MMM#######H:.    -/H#
     .,H@H@ X######@ -H#####@+-     -+H###@X
      .,@##H;      +XM##M/,     =%@###@X;-
    X%-  :M##########$.    .:%M###@%:
    M##H,   +H@@@$/-.  ,;$M###@%,          -
    M####M=,,---,.-%%H####M$:          ,+@##
    @##################@/.         :%H##@$-
    M###############H,         ;HM##M$=
    #################.    .=$M##M$=
    ################H..;XM##M$=          .:+
    M###################@%=           =+@MH%
    @#################M/.         =+H#X%=
    =+M###############M,      ,/X#H+:,
      .;XM###########H=   ,/X#H+:;
         .=+HM#######M+/+HM@+=.
             ,:/%XM####H/.
                  ,.:=-.""" + Style.RESET_ALL)

def introStart():
    os.system('cls')
    printCake()
    print(Fore.GREEN + "COMMENCING BACKGROUND MUSIC IN")
    print(Fore.YELLOW + "3...")
    sleep(2)
    print("2...")
    sleep(2)
    print("1..." + Style.RESET_ALL)
    sleep(2)

def songTextStart():
    os.system('cls')
    printCake()
    print(Fore.GREEN + "MUSIC DEPLOYED. THANK YOU FOR YOUR TIME." + Style.RESET_ALL)

introStart()
PlaySound("portal-radio.wav", SND_FILENAME|SND_LOOP|SND_ASYNC)
songTextStart()
while True:
    pass
