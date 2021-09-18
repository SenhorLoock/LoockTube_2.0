import os
import pytube
def Banner():
     os.system('clear')
     print ('Download Video')
     print ('--------------')
     print ('LoockTube 2.0')
     os.system('sleep 1.0')
Banner()
url = input('Insert Url:')
os.system('clear')
print ("Loading...")
os.system('sleep 3.0')
print ("Resolution")
print ("[01]-Max")
print ("[02]-Min")
resolution = input(">>>")
if resolution == "01" or resolution == "1":
          resultado = pytube.YouTube(url)
          video = resultado.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first().download()
          print (f"Exelente!!!\nName_Video:{resultado.title}")
          volt = input("You Want Exit? Y/yes or N/no:")
          if volt == "Y" or volt == "y":
              exit()
          else:
              os.system('python3 main.py')
elif resolution == "02" or resolution == "2":
          resultado = pytube.YouTube(url)
          video = resultado.streams.first().download()
          print (f"Exelente!!!\nName_Video:{resultado.title}")
          volt = input("You Want Exit? Y/yes or N/no:")
          if volt == "Y" or volt == "y":
              exit()
          else:
              os.system('python3 main.py')
           
else:
    os.system("clear")
    print ('Erro')
