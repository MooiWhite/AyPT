#Autores: Mariana Martínez Soto
#18 de Febrero 2022
#Análisis y procesamiento de textos. Facultad de Ingeniería, UNAM
#PROTOTIPO DE SOLUCIONADOR DE WORDLE
#
#Es una versión beta que aún no tiene los correctos
#comandos aplicados con excepciones
#Así como falta el ordenamiento por probabilidad de letras una vez filtrados los resultadps
#Y defectos cuando hay una misma pista proporcionada en dos colores
#(Por ejmplo. s como pista amarilla y gris)
filename = "D:\MarJo\Documents\Semestre 2022-2\AyPT\palabras_todas.txt"
fname = "D:\MarJo\Documents\Semestre 2022-2\AyPT\Fpalabras_todas.txt"

#Función extra si usar
def check_string(str):#Busca una palabra en la lista, a ver si existeS
    with open(fname, encoding='utf-8') as tem_f:
        dfile = tem_f.readlines()
    for line in dfile:
        if (str+'\n').__eq__(line):
            print(str)
            return True 
    print("La palabra no se encuentra")
    return False

def string_5(): #Delimita a palabras de 5 caracteres (se aplica una vez al archivo)
    with open(filename, encoding='utf-8') as temp_f:
        datafile = temp_f.read()
        WORDS = datafile.splitlines()
        WORDS_5 = list(filter(lambda x: len(x) == 5, WORDS))
        return WORDS_5
         
def menu(words_5):
    print("Longitud de principal list: "+str(len(words_5)))
    respuesta = input("¿Tienes pistas verdes? S/N: ")
    while respuesta != 'N':
        verde = input("Ingresa la letra verde: ")
        pos= int(input("Ingresa su posición: "))
        words_5=filtro_verde(words_5,verde,pos)
        respuesta = input("¿Aún hay pistas verdes? S/N: ")
    respuesta = input("¿Tienes pistas amarillas? S/N: ")
    while respuesta != 'N':
        amarillo = input("Ingresa la letra amarilla: ")
        pos= int(input("Ingresa su posición: "))
        words_5=filtro_amarillo(words_5,amarillo,pos)
        respuesta = input("¿Aún hay pistas amarillas? S/N: ")
    respuesta = input("¿Tienes pistas grises? S/N: ")
    while respuesta != 'N':
        gris = input("Ingresa la letra gris: ")
        words_5=filtro_gris(words_5,gris)
        respuesta = input("¿Aún hay pistas grises? S/N: ")
    print("Longitud de principal list: "+str(len(words_5)))
    return words_5
    
def filtro_verde(lista,letter,pos):
    nueva_lis = []
    for x in lista:
        if x[pos-1] == letter:
            nueva_lis.append(x)    
    return nueva_lis

def filtro_amarillo(lista,letter,pos):
    nueva_lis = []
    for x in lista:
        if x[pos-1] != letter and letter in x:
            nueva_lis.append(x)    
    return nueva_lis

def filtro_gris(lista,letter):
    prueba_lis = []
    for x in lista:
        if letter not in x:
            prueba_lis.append(x)
    return prueba_lis

def filter_acc(lista):
    for x in lista:
        if "á" in x:
            lista.remove(x)
        elif "é" in x:
            lista.remove(x)
        elif "í" in x:
            lista.remove(x)
        elif "ó" in x:
            lista.remove(x)
        elif "ú" in x:
            lista.remove(x)
    return lista
        
def probability(lista_filtrada):
    new_list=[]
    for x in lista_filtrada:
        if "a" in x:
            lista_filtrada.insert(0,lista_filtrada.pop(x))
            

def main():
    words_5=string_5()
    words_5 = filter_acc(words_5)
    #print(words_5)
    for i in range(6):
        words_5=menu(words_5)
        print(words_5)
                    
main()

