import pandas as pd 
import matplotlib.pyplot as plt
import random 


def simulacion_dados():
    numero_lanzamientos=int(input("¿Cuantas veces lanzara el dado?"))
    list=[] #esta lista contendra los resultados de cada lanzamiento
    for i in range(numero_lanzamientos+1):
        data=random.randint(1,6)
        list.append(data)

    lanzamiento=[i for i in range(numero_lanzamientos+1)if True] #esta lista guardara el numero del lanzamiento

    dic={'Lanzamiento':lanzamiento,'Resultado':list}
    df=pd.DataFrame(dic)
     #se agrupa por cada resultado, se cuenta el numero de resultados y se grafica digrama de barras
    df.groupby('Resultado').count().plot(kind='bar')


simulacion_dados()
