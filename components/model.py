import pandas as pd
import pickle
from sklearn import linear_model
import json


VariablesACambiar={'ESTU_TRABAJA':1,'FAMI_TIENECOMPUTADOR':0.9,'COBERTURA_NETA':0.9}
Municipio='Medellín'
datos_defecto = pd.read_csv('data/model/datos_defecto.csv')

with open('data/model/CodigoMunicipio.json', 'r') as fp:
    CodigoMunicipio = json.load(fp)

#municipios names
df = pd.DataFrame.from_dict(CodigoMunicipio, orient='index')
df.reset_index(level=0, inplace=True)
df.rename(columns={"index": "MUNICIPIO"}, inplace=True)

MUNICIPIOS = list(df.MUNICIPIO.unique())


with open('data/model/standarization_Dict.json', 'r') as fp:
    standarization_Dict = json.load(fp)


loaded_model = pickle.load(open('data/model/ElasticNetIcfes.sav', 'rb'))



def PredecirMunicipio(Municipio,datos_defecto=datos_defecto,VariablesACambiar=VariablesACambiar,
                     modelo=loaded_model):
    colstodrop=['PERIODO','COLE_COD_MPIO_COLEGIO','PUNTAJE_NORM']
    X2=datos_defecto[datos_defecto['COLE_COD_MPIO_COLEGIO']==CodigoMunicipio[Municipio]].drop(colstodrop,axis=1).reset_index(drop=True)

    for col in VariablesACambiar.keys():
        if col in standarization_Dict.keys():
            X2[col]=(VariablesACambiar[col]-standarization_Dict[col][0])/(standarization_Dict[col][1]-standarization_Dict[col][0])
        else:
            X2[col]=VariablesACambiar[col]
            
    norm_prediction=loaded_model.predict(X2)[0]
    Saber11Score=norm_prediction*standarization_Dict['PUNTAJE_NORM'][0]+standarization_Dict['PUNTAJE_NORM'][1]
    if Saber11Score > 500 : Saber11Score = 500
    if Saber11Score < 0 : Saber11Score = 0
    return(Saber11Score)

# predicted = PredecirMunicipio(Municipio)
# print(predicted)