import random
import webbrowser
from datetime import date, datetime
import time
import cv2
import pyglet
import speech_recognition as sr
import os
import tkinter 
import pyautogui
from tkinter import Tk, Label, Button, Entry
from pytube import YouTube
from os import path
try:
    import pywhatkit as kit
except:
    print("No hay conexion a internet...")

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

mama = "+50375797010"
karen = "+50373709725"
diego = "+50377424811"
duri = "+50371750557"
cesar = "+50375469957"

today = date.today()
now = datetime.now()

r = sr.Recognizer()

blanco = "#FFFFFF"
negro = "#000000"

rojo = "#F0012D"
amarillo = "#FFBE01"
anaranjado = "#EE6A2B"
verde = "#2CD133"
azul = "#01FFFA"

cntra = "9110"
admn = False

pagLista = []
youT = []
list3 = {}
ventana = tkinter.Tk()
ventana.geometry("300x550")
ventana.title("J.A.R.V.I.S")
#ventana.iconbitmap(r'C:\Users\Paty\Documents\Csar_2021\python\imgs\logoJ.ico')

def jarvisvaadecir(loquevoyadecir):#nombredelaudio
    try:
        jarvis = pyglet.resource.media(loquevoyadecir)
        jarvis.play()
    except:
        print("Error al reproducir el audio...")
jarvisvaadecir("iniciandoSistema.mp3")
def label(colorFondo, texto, colorTexto, padX, padY, tamX, tamY):

    etiqueta = Label(ventana, bg= colorFondo, text= texto, fg= colorTexto)
    etiqueta.place(relx=padX, rely=padY, relwidth= tamX, relheight= tamY)

def boton(colorFondo, texto, colorTexto, comando, padX, padY, tamX, tamY):
    boton1 = Button(ventana, text= texto, command= comando, bg= colorFondo, fg= colorTexto)
    boton1.place(relx=padX, rely=padY, relwidth= tamX, relheight= tamY)
    # boton1.pack() #al agregar comandos no creo que se pueda utilizar de esta manera

def cajaTexto():
    ingresaTexto = Entry(ventana)
    ingresaTexto.pack()

def cerrar():
    jarvisvaadecir("bye.mp3")
    ventana.quit()
def borrar():
        label(negro, " ", negro, 0.07, 0.25, 0.86, 0.68)
        ingresaTexto.delete(0, "end") 

def voz():
    with sr.Microphone() as source:
        
        print("habla.")
        
        audio = r.listen(source)
        try:
            text =  r.recognize_google(audio, language='es-MX')
            text = text.lower()
            # print(text)
            print("[ Se ha escuchado perfectamente... ]")
            jarvisvaadecir("enseguida.mp3")
    
        except:                
            print("Error al escuchar ")
            jarvisvaadecir("errorescuchar.mp3")

    Qdh(text) 
    ingresaTexto.insert(0, text)
def enviar():
    text = ingresaTexto.get()
    jarvisvaadecir("enseguida.mp3")
    Qdh(text)

def enviar2(caja):
    text = caja.get()
    return text

def Qdh(quehacer):
    print(quehacer)
    if "admin" in quehacer:
        admin(quehacer)
    elif "google" in quehacer:
        google(quehacer)
    elif "word" in quehacer:
        word()
    elif "excel" in quehacer:
        excel()
    elif "point" in quehacer:
        point()
    elif "clase" in quehacer:
        clases(quehacer)
    elif "apaga" in quehacer:
        apagar()
    elif "whatsapp" in quehacer:
        whatsapp(quehacer)
    elif "youtube" in quehacer:
        if "descarg" in quehacer:
            installYoutube()
        else:
            youtube(quehacer)
    elif "actuali" in quehacer:
        actualizar()
    elif "gmail" in quehacer:
        gmail(quehacer)
    elif "escrib" in quehacer:
        escribir(quehacer)
    else:
        nada()
    
def admin(x):
    time.sleep(1)
    label(anaranjado, " ", negro, 0.07, 0.25, 0.86, 0.68)
    label(negro, " ", negro, 0.075, 0.255, 0.845, 0.67)
    label(negro, "Control Administrativo", anaranjado, 0.08, 0.26, 0.4, 0.04)
    time.sleep(1)
    label(anaranjado, "Ingresa Contraseña", negro, 0.2, 0.5, 0.6, 0.04)
    ingresaTexto2 = Entry(ventana, bg=negro, fg=anaranjado)
    ingresaTexto2.place(relx=0.2, rely=0.55, relwidth= 0.6, relheight= 0.04)
    boton(rojo, "[   ]", negro, ingresaTexto2.get(), 0.2, 0.6, 0.29, 0.04)
    boton(verde, "[   ]", negro, ingresaTexto2.get(), 0.5, 0.6, 0.3, 0.04)

def google(x):
    googleAuto(x)
    label(blanco, " ", negro, 0.07, 0.25, 0.86, 0.68)
    label(negro, " ", negro, 0.075, 0.255, 0.845, 0.67)
    label(negro, "GOOGLE", blanco, 0.09, 0.26, 0.3, 0.04)
    time.sleep(1)
    label(blanco, "Pagina a Abrir", negro, 0.2, 0.5, 0.6, 0.04)
    ingresaTexto2 = Entry(ventana, bg=negro, fg=blanco)
    ingresaTexto2.place(relx=0.2, rely=0.55, relwidth= 0.6, relheight= 0.04)
    boton(rojo, "[   ]", negro, " ", 0.2, 0.6, 0.29, 0.04)
    boton(verde, "[   ]", negro, lambda: googleOpen(ingresaTexto2.get()), 0.5, 0.6, 0.3, 0.04)
def googleOpen(pag):
    print(pag)
    lin  = ("https://www.google.com/search?q="+pag+"&rlz=1C1CHBF_esSV908SV908&oq="+pag+"&aqs=chrome..69i57j0i512l9.3442j0j7&sourceid=chrome&ie=UTF-8")
    webbrowser.open_new(lin)
def googleAuto(x):
    pagLista = x.split("busca ")
    #elimino la primera objeto
    pagLista.pop(0)
    numeros = int(len(pagLista))
    for i in pagLista:
        webbrowser.open_new_tab("https://www.google.com/search?q="+ i + "&rlz=1C1CHBF_esSV908SV908&oq=" + i + "&aqs=chrome..69i57j0i512l9.3442j0j7&sourceid=chrome&ie=UTF-8")

def actualizar():
    pyautogui.moveTo(88, 43)
    pyautogui.click()

def nada():
    label(negro, " ", negro, 0.07, 0.25, 0.86, 0.68)
    label(rojo, "Error, no tengo configurada esa opcion", negro, 0.1, 0.26, 0.8, 0.06 )
    jarvisvaadecir("error.mp3")

def word():
    label(azul, "Se ha abierto [  WORD  ]", negro, 0.1, 0.26, 0.8, 0.06 )
    pyautogui.moveTo(450, 740)
    pyautogui.click()
    time.sleep(5)
    jarvisvaadecir("listo.mp3")
def excel():
    label(verde, "Se ha abierto [  EXCEL  ]", negro, 0.1, 0.26, 0.8, 0.06 )
    pyautogui.moveTo(500, 740)
    pyautogui.click()
    time.sleep(5)
    jarvisvaadecir("listo.mp3")
def point():
    label(anaranjado, "Se ha abierto [ Power Point ]", negro, 0.1, 0.26, 0.8, 0.06 )
    pyautogui.moveTo(570, 740)
    pyautogui.click()
    time.sleep(5)
    jarvisvaadecir("listo.mp3")

def clases(x):
    clasesAuto(x)
    label(negro, " ", negro, 0.07, 0.25, 0.86, 0.68)
    label(negro, "Accediendo a clases:", verde, 0.08, 0.26, 0.4, 0.04)
    time.sleep(1)
    boton(rojo, 
        "Matematica",
        negro,lambda: clases2(rojo,"Matematica", 
        classroomMatematica, 
        MatematicaEnlace),
        0.09, 0.35, 0.25, 0.06)
    boton("green", "Ciencias", negro,lambda: clases2("green"," hola ", " ", " "), 0.37, 0.35, 0.25, 0.06)
    boton("blue", "Sociales", negro,lambda: clases2("blue","Sociales", classroomSociales, SocialesEnlace), 0.65, 0.35, 0.25, 0.06)

    boton("purple", "Modulo", negro,lambda: clases2("purple","Modulo", classroomModulo, ModuloEnlace), 0.09, 0.45, 0.25, 0.06)
    boton(anaranjado, "Lenguaje", negro,lambda: clases2(anaranjado,"Lenguaje", classroomLenguaje, LenguajeEnlace), 0.37, 0.45, 0.25, 0.06)
    boton("blue", "Ingles", negro,lambda: clases2("blue","Ingles", classroomIngles, InglesEnlace), 0.65, 0.45, 0.25, 0.06)

    boton("purple", "Religion", negro,lambda: clases2("purple","Religion", classroomReligion, ReligionEnlace), 0.09, 0.55, 0.25, 0.06)
    boton(azul, "Informatica", negro,lambda: clases2(azul,"Informatica", classroomInformatica, InformaticaEnlace), 0.37, 0.55, 0.25, 0.06)
    boton("blue", "MUYC", negro,lambda: clases2("blue","MUYC", classroomMucy, MucyEnlace), 0.65, 0.55, 0.25, 0.06)

    # label(rojo, "Matematica", negro, 0.069, 0.3, 0.27, 0.06)
def clases2(color, clas, classroom, meet):
    label(color, " ", negro, 0.07, 0.25, 0.86, 0.68)
    label(negro, " ", negro, 0.075, 0.255, 0.845, 0.67)
    label(negro, "Accediendo a clases:", color, 0.08, 0.26, 0.4, 0.04)

    label(color, clas, negro, 0.069, 0.3, 0.27, 0.06)
    boton(negro, "Classroom", color,lambda: webbrowser.open_new_tab(classroom), 0.35, 0.37, 0.25, 0.06)
    boton(negro, "meet", color,lambda: webbrowser.open_new(meet), 0.61, 0.44, 0.15, 0.06)
    boton(negro, "otros", color, " ", 0.77, 0.44, 0.13, 0.06)
    # label(rojo, "Matematica", negro, 0.069, 0.3, 0.27, 0.06)
    # boton(negro, "Classroom", rojo, " ", 0.35, 0.3, 0.25, 0.06)
    # boton(negro, "meet", rojo, " ", 0.61, 0.3, 0.15, 0.06)
    # boton(negro, "otros", rojo, " ", 0.77, 0.3, 0.13, 0.06)
def clasesAuto(x):
    if "mate" in x:
        if "classroom" in x:
            webbrowser.open_new_tab(classroomMatematica)
        elif "meet" in x:
            webbrowser.open_new_tab(MatematicaEnlace)
    elif "sociales" in x:
        if "classroom" in x:
            webbrowser.open_new_tab(classroomSociales)
        elif "meet" in x:
            webbrowser.open_new_tab(SocialesEnlace)
    elif "lenguaje" in x:
        if "classroom" in x:
            webbrowser.open_new_tab(classroomLenguaje)
        elif "meet" in x:
            webbrowser.open_new_tab(LenguajeEnlace)
    elif "modulo" in x:
        if "classroom" in x:
            webbrowser.open_new_tab(classroomModulo)
        elif "meet" in x:
            webbrowser.open_new_tab(ModuloEnlace)
    elif "ingles" in x:
        if "classroom" in x:
            webbrowser.open_new_tab(classroomIngles)  
        elif "meet" in x:
            webbrowser.open_new_tab(InglesEnlace)
    elif "informatica" in x:
        if "classroom" in x:
            webbrowser.open_new_tab(classroomInformatica) 
        elif "meet" in x:
            webbrowser.open_new_tab(InformaticaEnlace)
    elif "religion" in x:
        if "classroom" in x:
            webbrowser.open_new_tab(classroomReligion)
        elif "meet" in x:
            webbrowser.open_new_tab(ReligionEnlace)
    elif "moral" in x:
        if "classroom" in x:
            webbrowser.open_new_tab(classroomMucy)
        elif "meet" in x:
            webbrowser.open_new_tab(MucyEnlace)

def randon():
    print("x")

def apagar():
    label(rojo, " ", negro, 0.07, 0.25, 0.86, 0.68)
    label(negro, " ", negro, 0.075, 0.255, 0.845, 0.67)
    label(rojo, "Para apagar el sistema\nDigite la contraseña:", negro, 0.1, 0.26, 0.8, 0.06 )
    jarvisvaadecir("accesodenegado.mp3")
    ingresacontra = Entry(ventana, bg=blanco, fg=rojo)
    ingresacontra.place(relx=0.2, rely=0.35, relwidth= 0.6, relheight= 0.04)
    boton(rojo, "[   ]", negro,lambda: apagar2(ingresacontra), 0.2, 0.4, 0.29, 0.04)
    boton(verde, "[   ]", negro,lambda: apagar2(ingresacontra), 0.5, 0.4, 0.3, 0.04)
def apagar2(x):
    c = x.get()
    if c == cntra:
        label(verde, "Contrasena correcta\nApagando sistema", negro, 0.2, 0.46, 0.6, 0.06 )
        jarvisvaadecir("bye.mp3")
        os.system('shutdown -s')
    else:
        label(rojo, "Contrasena incorrecta", negro, 0.2, 0.46, 0.6, 0.06 )

def whatsapp(x):
    # kit.sendwhatmsg_instantly("+50375797010", "hola estoy enviando este mensaje instantaneamente")
    what = x.split("diciendo")
    what.pop(0)
    print(what[0])
    if "karen" in x:
        kit.sendwhatmsg_instantly(karen, what[0])
    if "diego" in x:
        kit.sendwhatmsg_instantly(diego, what[0])
    if "mamá" in x:
        kit.sendwhatmsg_instantly(mama, what[0])
    if "duri" in x:
        kit.sendwhatmsg_instantly(duri, what[0])
    if "auto" in x:
        kit.sendwhatmsg_to_group("Cesar", what[0],now.hour , now.minute+1)
    jarvisvaadecir("listo.mp3")
def youtube(x):

    youT = x.split("youtube")
    youT.pop(0)
    print(youT[0])
    kit.playonyt(youT[0])
    label(azul, "Se ha abierto [  YOUTUBE  ]", negro, 0.1, 0.26, 0.8, 0.06 )
def installYoutube():
    label(rojo, " ", negro, 0.07, 0.25, 0.86, 0.68)
    label(negro, " ", negro, 0.075, 0.255, 0.845, 0.67)
    label(rojo, "Deseas Descargar\nEl video de youtube?:", negro, 0.1, 0.26, 0.8, 0.06 )
    ingresalink = Entry(ventana, bg=blanco, fg=rojo)
    ingresalink.place(relx=0.2, rely=0.35, relwidth= 0.6, relheight= 0.04)
    
    boton(rojo, "[   ]", negro," ", 0.2, 0.4, 0.29, 0.04)
    boton(verde, "[   ]", negro,lambda: installYoutube2(ingresalink.get()), 0.5, 0.4, 0.3, 0.04)
def installYoutube2(x):
    link = x
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()
    jarvisvaadecir("instalando.mp3")

def gmail(x):
    if "gmail" in x:
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    if "mandar" in x:
        time.sleep(5)
        pyautogui.moveTo(100, 200)
        pyautogui.click()
    if "doc" in x:
        webbrowser.open("https://docs.google.com/document/u/0/")
    if "excel" in x:
        webbrowser.open("https://docs.google.com/spreadsheets/u/0/")
    if "presentacion" in x:
        webbrowser.open("https://docs.google.com/presentation/u/0/")
    if "reuni" in x:
        webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")
    if "chat" in x:
        webbrowser.open("https://mail.google.com/chat/u/0/#chat/welcome")

def escribir(x):

    list3 = x.split("coloca ")
    list3.pop(0)
    a=list(list3[0])
    time.sleep(5)

    pyautogui.press(a)


label(negro, " ", "white" , 0,0, 1, 1)
# label(celeste, " ", "black", 0,0, 1, 0.06)
# label(blanco, "J.A.R.V.I.S", "black", 0.02, 0.01, 0.3, 0.04)
boton(rojo,     " ", "black", cerrar, 0.12, 0.02, 0.04, 0.02)
boton(amarillo, " ", "black", borrar, 0.07, 0.02, 0.04, 0.02)
boton(verde,    " ", "black", "", 0.02, 0.02, 0.04, 0.02)

label(negro, "Que deseas hacer: ?", verde, 0.3, 0.01, 0.4, 0.04)
label(verde, " ", "black", 0.07, 0.06, 0.86, 0.001)

boton(negro, "VOZ", verde, voz, 0.07, 0.08, 0.11, 0.04)

ingresaTexto = Entry(ventana, bg=negro, fg=verde)
ingresaTexto.place(relx=0.07, rely=0.13, relwidth= 0.86, relheight= 0.04)

boton(negro, "[    ]" , verde, enviar, 0.82, 0.185, 0.11, 0.04)
label(verde, " ", "black", 0.07, 0.94, 0.86, 0.001)

# label(verde, " ", negro, 0.07, 0.25, 0.86, 0.68)

label(verde, " ", "black", 0.07, 0.24, 0.86, 0.001)
boton(negro, "CONFIG", verde, " ", 0.07, 0.95, 0.3, 0.04)

ventana.mainloop()
