#Autores: Mariana Martínez Soto
#04 de marzo 2022
#Análisis y procesamiento de textos. Facultad de Ingeniería, UNAM
#DISTRIBUCIÓN DE PALABRAS EN UN TEXTO
#
import pandas as pd
#What this funtions do is filter puntuation signs
#and digits
def delete_signs(te):
    print ("Hi")
    
def main():
    data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
    print (data)
    texto_entrada = ""
    #texto_entrada = input("Ingresa tu texto de entrada: ")

main()
