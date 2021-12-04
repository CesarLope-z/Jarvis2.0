import random
import webbrowser
from datetime import date, datetime
import cv2
import pyglet
import speech_recognition as sr
import os


#####VARIABLES#################################################################################################
mostrar = ["[ control admin ]", "[ mostrar todo ]", "[ cambiar usuario ]", "[ salir ]", "[ agregar funcion ]", "[ eliminar funcion ]", "[ clases ]", "[ random ]", "[ documento ]", "[ abrir pag web ]"]
clases = ["matematica", "sociales", "lenguaje", "fisica", "biologia","modulo", "ingles", "mucy","informatica",  "religion" ]

MatematicaEnlace = ("https://meet.google.com/pod-hudn-ygu?authuser=0")
SocialesEnlace = ("https://meet.google.com/pea-tqfy-vks")
LenguajeEnlace = ("https://meet.google.com/jrx-ewvn-avn?authuser=0&hl=es")
FisicaEnlace = ("https://meet.google.com/mwp-cjfe-vpw?authuser=0&hl=es")
BiologiaEnlace = ("https://meet.google.com/lookup/bqsvy22nsl")
ModuloEnlace = ("https://meet.google.com/jjj-pojg-dqa")
InglesEnlace = ("")
MucyEnlace = ("https://meet.google.com/pea-tqfy-vks")
InformaticaEnlace = ("https://meet.google.com/xmj-ugxc-mpf")
ReligionEnlace = ("http://meet.google.com/awy-zrwm-xei")

classroomMatematica= "https://classroom.google.com/c/MjY5MzMxMDI0NzM0"
classroomSociales= "https://classroom.google.com/c/MTk3MjQ0ODE2MjI2"
classroomLenguaje= "https://classroom.google.com/c/NjU4MDI4NTk1NTZa"
classroomFisica= "https://classroom.google.com/c/MzI0NDQ2MzkxODc3"
classroomBiologia= "https://classroom.google.com/c/MzI5ODUzOTU4Nzcx"
classroomModulo= "https://classroom.google.com/c/MzcxNDMxODg4MDA1"
classroomIngles= "https://classroom.google.com/c/MjY4MzM0MjE2NTgz"
classroomMucy= "https://classroom.google.com/c/MzIyMTEwNTQxMTEw"
classroomInformatica= "https://classroom.google.com/c/MzU3MzQ3NjAzNDcz"
classroomReligion= "https://classroom.google.com/c/MzIyMzYzMDYwNzg2"

img1 = cv2.imread("imgs\Tperiodica.jpg")
img2 = cv2.imread("imgs\Trigonometricafull.jpg")

enlaceClases = [MatematicaEnlace, SocialesEnlace, LenguajeEnlace, FisicaEnlace, BiologiaEnlace, ModuloEnlace, InglesEnlace, MucyEnlace, InformaticaEnlace, ReligionEnlace]
diasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
seguKey = "9110"
admin = False
doctxt = "recordatorios.txt"

sepLarga = "###################################################################"
sepCorta = "**********************************"

rList = []

today = date.today()
now = datetime.now()

r = sr.Recognizer()

actVoz = False
ActAudio = False
#####VARIABLES FIN#######################################################################################################
def jarvisvaadecir(loquevoyadecir):#nombre del audio

    if(ActAudio):
        jarvis = pyglet.resource.media(loquevoyadecir)
        jarvis.play()

def escuchar():
  if actVoz:
    print("[ Para utilizar el comando de voz ingresa [ x ] ]")
  text = input("Escribe que deseas hacer: ")

  if text == "x":
    with sr.Microphone() as source:
        print("habla.")
        if(actVoz):
          audio = r.listen(source)
          try:
            text =  r.recognize_google(audio, language='es-MX')
            print(text)
            print("[ Se ha escuchado perfectamente... ]")
        
          except:                
              print("Error al escuchar ")
  return text 

def clase(enlaceMeet, enlaceClassroom):
    print("El enlace del Meet es: ")
    print(" ")
    print(enlaceMeet)
    print(" ")
    print(sepCorta)
    print(" ")
    print("El enlace del Classroom es: ")
    print(" ")
    print(enlaceClassroom)
    brow = input("Abrir las paginas web de manera automatica")
    if brow == 'y':
        webbrowser.open_new(enlaceMeet)
        webbrowser.open_new_tab(enlaceClassroom)
    else:
        print()
        print("No se han abierto las paginas")
        print()
        print()
    Qtdv = input("Deseas abrir algun tema?")
    if "tabla per" in Qtdv:
        showImg(img1)
    if "trigonometri" in Qtdv:
        showImg(img2)

def showImg(imgNeed):
    print("abriendo...")
    # cv2.imshow("prueba img 1", img1)
    cv2.imshow("El tema seleccionado aparece en su pantalla:", imgNeed)
    print("abierto")
    cv2.waitKey(0)
    print("cerrado")

#####DEFINICIONES FIN#######################################################################################################

repetirUsr = True
while repetirUsr:
  voz = input("Antes que nada, deseas activar la utilizacion de J.A.R.V.I.S por voz [ RECONOCIMIENTO DE VOZ ] [y]es [n]o: ")
  audio = input("Tambien, deseas activar la utilizacion de J.A.R.V.I.S por audio [ REPRODUCIR VOZ ] [y]es [n]o: ")
  if (voz == 'y'):
      actVoz = True
  else:
      actVoz = False
  if (audio == 'y'):
      ActAudio = True
  else:
      ActAudio = False
  print("Esta es mi primera prueba de sistema operativo ")

  jarvisvaadecir("holasoyjarvis.mp3")
  
  print("Soy J.A.R.V.I.S. Asistente personal de Cesar")
  print("Hola, Mr... ") 
  name = input("ingresa un nombre, porfavor; ")
  print(" ")
  print(sepLarga)
  print(" ")
  print("Hola, Mr." + name)

  permiso = input("Permite preguntarte unos datos, ingresa [Y]yes, [N]No ")
  if permiso != 'Y':
    print("Esta bien, tu decisión es importante")   
  else: 
    telP = input("ingresa tu telefono; ")
    emaP = input("ingresa tu e-mail; ")
    print(sepCorta)
    print(" ")
    print("Gracias " + name )
    print("Esa información me servirá más adelante")
  repetirQdh = True
  print(" ")
  print(sepLarga)
  while repetirQdh:  
    print(" ")
    print(sepLarga)
    print(" ")

    Qdh = escuchar()  
    print(" ")  


    if "admin" in Qdh:
      print("Accediendo para verificacion de administrador")
      print(sepCorta)
      print(" ")
      ingCon = input("INGRESA CONTRASEÑA ")
      if ingCon == seguKey:
        admin = True 
        print(" ")
        print("Acceso Correcto")
        print(name + ", ha accedido como admin")
        print(" ")
        print(sepCorta)

      else:
        print("Contraseña incorrecta o Error")

    elif "todo" in Qdh:
      print("Nombre: ")
      print(name)
      if permiso != 'Y':
        print("No hay registro de telefono ni email")
      else:
        print(sepCorta)
        print("Telefono: ")
        print(telP)
        print(sepCorta)
        print("E-mail: ")
        print(emaP)
      print(sepCorta)
      print("Acceso administrativo: ")
      print(admin)
      print(sepCorta)
      print("Fecha actual: ")
      print(datetime.now())

    elif "sal" in Qdh:
      print("bye, " + name)
      repetirQdh = False
      repetirUsr = False

    elif Qdh == "help":
      print("Las acciones que puedes escribir,son: ")
      for help in mostrar:
        print(help)

    elif "cambiar de usuario" in Qdh:
      repetirQdh = False
      admin = False
      
    elif "agregar funcion" in Qdh:
      if admin == False:
        print("Necesitas permiso administrativo ")
        print("para agregar funcion")
      else:
        name_func = input("Nombre de la funcion")
        mostrar.append("[ " + name_func + " ]")
        print("Que te gustaria qie la funcion hiciera," + name)
        func1 = input("Di imprime para ejecutar algo en pantalla")
        if func1 == "imprime":
          impress = input("Que quieres que imprima ")
   
    elif "eliminar funcion" in Qdh:
      if admin == False:
        print("Necesitas permiso administrativo ")
        print("para agregar funcion")
      else:
        mostrar.pop()
        print("Se ha eliminado correctamente")

    elif "clase" in Qdh:
      print("Accediendo a los elementos")
      # dia = input("Antes que nada, ingresa el dia de hoy: ")
      print(" ")
      print(sepLarga)
      print(" ")
      if "mate" in Qdh: clase(MatematicaEnlace, classroomMatematica)
      elif "sociales" in Qdh: clase(SocialesEnlace, classroomSociales)
      elif "lenguaje" in Qdh: clase(LenguajeEnlace, classroomLenguaje)
      elif "fisica" in Qdh:   clase(FisicaEnlace, classroomFisica)
      elif "bio" in Qdh:      clase(BiologiaEnlace, classroomBiologia)
      elif "modulo" in Qdh:   clase(ModuloEnlace, classroomModulo)
      elif "inglés" in Qdh:   clase(InglesEnlace, classroomIngles)
      elif "moral" in Qdh:    clase(MucyEnlace, classroomMucy)        
      elif "info" in Qdh:     clase(InformaticaEnlace, classroomInformatica)
      elif "reli" in Qdh:     clase(ReligionEnlace, classroomReligion)
      else:
        QdhC = input(" Clase a acceder: ")  
        if QdhC in clases:
          print(" ")
          print(sepLarga)
          print(" ")
          print("[ "+ QdhC + " ]") 
          if "mate" in QdhC: clase(MatematicaEnlace, classroomMatematica)
          elif "sociales" in QdhC: clase(SocialesEnlace, classroomSociales)
          elif "lenguaje" in QdhC: clase(LenguajeEnlace, classroomLenguaje)
          elif "fisica" in QdhC:   clase(FisicaEnlace, classroomFisica)
          elif "bio" in QdhC:      clase(BiologiaEnlace, classroomBiologia)
          elif "modulo" in QdhC:   clase(ModuloEnlace, classroomModulo)
          elif "ingles" in QdhC:   clase(InglesEnlace, classroomIngles)
          elif "moral" in QdhC:    clase(MucyEnlace, classroomMucy)        
          elif "info" in QdhC:     clase(InformaticaEnlace, classroomInformatica)
          elif "reli" in QdhC:     clase(ReligionEnlace, classroomReligion)
        else:
            print("Error, Clase no encontrada o Incorrecta")

    elif "random" in Qdh:
      QdhR = input("Adquirir un valor numerico o palabra, Ingresa [n]numero o [p]palabra ")
      if QdhR == 'n':
          print("Ingresando un numero aleatorio: ")
          numInit = int(input("Ingresa numero [ inicial ] : "))
          numFn = int(input("Ingresa numeros [ limite ] : "))
          numRan = random.randint(numInit, numFn)
          print(numRan)
      elif QdhR == 'p':
          print("Ingresando una palabra aleatoria:  ")
          r = int(input("Cuantos valores asignaras: "))
          for ra in range(r):
              ran = input("ingresa uno de los valores a escoger: ")
              rList.append(ran)
          print("Los valores que se han asignado son: ")
          print(rList)
          palRan = random.choice(rList)
          print("La palabra sorteada es: ")
          print("[ " + palRan + " ]")

    elif "Google" in Qdh:
      if "Word" in Qdh:
        print("Se ha abierto: [ Word ]")                  
        webbrowser.open_new_tab("https://docs.google.com/document/u/0/")
      elif "Excel" in Qdh:
        print("Se ha abierto: [ Excel ]")                  
        webbrowser.open_new_tab("https://docs.google.com/spreadsheets/u/0/")
      elif "Powerpoint" in Qdh:
        print("Se ha abierto: [ PowerPoint ]")                  
        webbrowser.open_new_tab("https://docs.google.com/presentation/u/0/")
      elif "classroom" in Qdh:
        print("Se ha abierto: [ Classroom ]")                  
        webbrowser.open_new_tab("https://classroom.google.com/h?hl=es")
      else:
          pagWeb = input("Que pagina deseas buscar: ")
          lin  = ("https://www.google.com/search?q="+pagWeb+"&rlz=1C1CHBF_esSV908SV908&oq="+pagWeb+"&aqs=chrome..69i57j0i512l9.3442j0j7&sourceid=chrome&ie=UTF-8")
          webbrowser.open_new(lin)
          print()
          print("Se ha abierto: [ " + pagWeb + " ]")
          print()
          print(sepCorta)

    elif "doc" in Qdh:
      print("Entrando a documento...")
      print("")
      loopdoc = True
      if "leer" in Qdh:
        doc = open(doctxt, "r")
        contenido = doc.read()
        print(contenido)
      elif "agregar" in Qdh:
        doc = open(doctxt, "a")
        QdA = input("agrega texto: ")
        doc.write(QdA +  "\n")
        doc.close()
      elif "borrar" in Qdh:
        doc = open(doctxt, "w")
        QdA = input("agrega texto: ")
        doc.write(QdA +  "\n")
        doc.close()
      else:
        while loopdoc:
          QdhD = input("Deseas agregar, Leer o Borrar el documento: ")
          print("")
          if QdhD == "leer":
            doc = open(doctxt, "r")
            contenido = doc.read()
            print(contenido)
            doc.close()
          elif QdhD == "agregar":
            doc = open(doctxt, "a")
            QdA = input("agrega texto: ")
            doc.write(QdA +  "\n")
            doc.close()
          elif QdhD == "borrar":
            doc = open(doctxt, "w")
            QdA = input("agrega texto: ")
            doc.write(QdA +  "\n")
            doc.close()
          elif QdhD == "salir":
            loopdoc = False
 
    elif "Apaga" in Qdh:
      if admin:
        print()
        print("Apagando sistema...")
        os.system('shutdown -s')
      else:
        print()
        print("No tienes acceso para apagar el sistema")
        print("Ve a [ Control Administrativo ] y digital la contraseña")
        print()

    else: 
      print("Creo que no tengo configurada esa opcion") 
      print("intenta nuevamente")
