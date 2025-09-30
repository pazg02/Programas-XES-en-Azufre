# Archivo de Funciones (Coef. Atenuación y Absorción)
#En este archivo de python voy a definir funciones que representan los coeficientes de atenuación 
# y absorción de distintos elementos.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'-------------'
'MANGANESO'
'-------------'

datosMn=pd.DataFrame(pd.read_excel(r"C:\Users\guadi\OneDrive\Escritorio\UNI\5to año\interaccion de la radiacion con la materia\lab 2 algoritmo\datosNIST\Mn NIST.xlsx"))
datosMn['Energy'] = datosMn['Energy'] * 1000  #pasé las energías a KeV
dfMn = datosMn.apply(np.log, axis=0) #tomé el log de todo
peak_index = 8 #absorption edge
dfMn_before_peak = dfMn.iloc[:peak_index]
dfMn_after_peak = dfMn.iloc[peak_index + 1:]
#absorción
slope1, intercept1 = np.polyfit(dfMn_before_peak['Energy'], dfMn_before_peak['Absorb.'], 1)
slope2, intercept2 = np.polyfit(dfMn_after_peak['Energy'], dfMn_after_peak['Absorb.'], 1)
#atenuación
slope1c, intercept1c = np.polyfit(dfMn_before_peak['Energy'], dfMn_before_peak['Attenuation'], 1)
slope2c, intercept2c = np.polyfit(dfMn_after_peak['Energy'], dfMn_after_peak['Attenuation'], 1)

#funciones:
def AtenuacionMn(x):
    if x<= 6.539: #energía del borde de absorción.
        y=slope1c*np.log(x)+intercept1c
    else:
        y=slope2c*np.log(x)+intercept2c
    return np.exp(y)

def AbsorcionMn(x):
    if x<= 6.539:
        y=slope1*np.log(x)+intercept1
    else:
        y=slope2*np.log(x)+intercept2
    return np.exp(y)


'-------------'
'''COBRE'''
'-------------'

datosCu=pd.DataFrame(pd.read_excel(r"C:\Users\guadi\OneDrive\Escritorio\UNI\5to año\interaccion de la radiacion con la materia\lab 2 algoritmo\datosNIST\Cu NIST.ods"))
datosCu['Energy']=datosCu['Energy']*1000 #pasé las energías a KeV
#aplicamos log
dfCu = datosCu.apply(np.log, axis=0)
#--------ojo, esto está definido varias veces con el mismo nombre.
peak_index_Cu= 12 #absorption edge
dfCu_before_peak = dfCu.iloc[:peak_index_Cu]
dfCu_after_peak = dfCu.iloc[peak_index_Cu + 1:]
#----------
#absorcion
a_Cu_1, b_Cu_1 = np.polyfit(dfCu_before_peak['Energy'], dfCu_before_peak['Absorb.'], 1)
a_Cu_2, b_Cu_2 = np.polyfit(dfCu_after_peak['Energy'], dfCu_after_peak['Absorb.'], 1)
#atenuación
a_Cu_3, b_Cu_3 = np.polyfit(dfCu_before_peak['Energy'], dfCu_before_peak['Attenuation'], 1)
a_Cu_4, b_Cu_4 = np.polyfit(dfCu_after_peak['Energy'], dfCu_after_peak['Attenuation'], 1)
#funciones:
def AbsorcionCu(x):
    if x<datosCu['Energy'][peak_index_Cu]: #energía del borde de absorción.
        y=a_Cu_1*np.log(x)+b_Cu_1
    else:
        y=a_Cu_2*np.log(x)+b_Cu_2
    return np.exp(y)

def AtenuacionCu(x):
    if x<datosCu['Energy'][peak_index_Cu]: #energía del borde de absorción.
        y=a_Cu_3*np.log(x)+b_Cu_3
    else:
        y=a_Cu_4*np.log(x)+b_Cu_4
    return np.exp(y)


'-------------'
'OXIGENO'
'-------------'
datosO=pd.DataFrame(pd.read_excel(r"C:\Users\guadi\OneDrive\Escritorio\UNI\5to año\interaccion de la radiacion con la materia\lab 2 algoritmo\datosNIST\O NIST.ods"))
datosO['Energy']=datosO['Energy']*1000 #pasé las energías a KeV
#aplicamos log
dfO = datosO.apply(np.log, axis=0)
#NO HAY ABSORPTION EDGE!!
#absorcion
a_O_1, b_O_1 = np.polyfit(dfO['Energy'], dfO['Absorb.'], 1)
#ahora para la atenuación
a_O_3, b_O_3 = np.polyfit(dfO['Energy'], dfO['Attenuation'], 1)
#funciones
def AbsorcionO(x):
    y=a_O_1*np.log(x)+b_O_1
    return np.exp(y)

def AtenuacionO(x):
    y=a_O_3*np.log(x)+b_O_3
    return np.exp(y)


'-------------'
'AZUFRE'
'-------------'

datosS=pd.DataFrame(pd.read_excel(r"C:\Users\guadi\OneDrive\Escritorio\UNI\5to año\interaccion de la radiacion con la materia\lab 2 algoritmo\datosNIST\S NIST.ods"))
datosS['Energy']=datosS['Energy']*1000 #pasé las energías a KeV
#aplicamos log
dfS = datosS.apply(np.log, axis=0)
peak_index_S= 4 #absorption edge
dfS_before_peak = dfS.iloc[:peak_index_S]
dfS_after_peak = dfS.iloc[peak_index_S + 1:]
#absorcion
a_S_1, b_S_1 = np.polyfit(dfS_before_peak['Energy'], dfS_before_peak['Absorb.'], 1)
a_S_2, b_S_2 = np.polyfit(dfS_after_peak['Energy'], dfS_after_peak['Absorb.'], 1)
#atenuación
a_S_3, b_S_3 = np.polyfit(dfS_before_peak['Energy'], dfS_before_peak['Attenuation'], 1)
a_S_4, b_S_4 = np.polyfit(dfS_after_peak['Energy'], dfS_after_peak['Attenuation'], 1)
#funciones
def AbsorcionS(x):
    if x<datosS['Energy'][peak_index_S]: #energía del borde de absorción.
        y=a_S_1*np.log(x)+b_S_1
    else:
        y=a_S_2*np.log(x)+b_S_2
    return np.exp(y)

def AtenuacionS(x):
    if x<datosS['Energy'][peak_index_S]: #energía del borde de absorción.
        y=a_S_3*np.log(x)+b_S_3
    else:
        y=a_S_4*np.log(x)+b_S_4
    return np.exp(y)


'-------------'
'LITIO'
'-------------'

datosLi=pd.DataFrame(pd.read_excel(r"C:\Users\guadi\OneDrive\Escritorio\UNI\5to año\interaccion de la radiacion con la materia\lab 2 algoritmo\datosNIST\Li NIST.ods"))
datosLi=datosLi.iloc[:-3]
datosLi=datosLi.iloc[1:]
datosLi['Energy']=datosLi['Energy']*1000 #pasé las energías a KeV
#aplicamos log
dfLi = datosLi.apply(np.log, axis=0)
#NO HAY ABS EDGE
#absorcion
a_Li_1, b_Li_1 = np.polyfit(dfLi['Energy'], dfLi['Absorb.'], 1)
#ahora para la atenuación
a_Li_3, b_Li_3 = np.polyfit(dfLi['Energy'], dfLi['Attenuation'], 1)
#funciones
def AbsorcionLi(x):
    y=a_Li_1*np.log(x)+b_Li_1
    return np.exp(y)

def AtenuacionLi(x):
    y=a_Li_3*np.log(x)+b_Li_3
    return np.exp(y)




'-------------'
'-------------'
