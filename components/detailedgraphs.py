import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#sns.set_style('whitegrid')
#plt.style.use('ggplot')
from sklearn import preprocessing
import plotly.graph_objects as go
import gc


puntajes = ['PUNT_C_NATURALES', 'PUNT_IDIOMA', 'PUNT_GLOBAL',
            'PUNT_LECTURA_CRITICA', 'PUNT_MATEMATICAS', 'PUNT_SOCIALES_CIUDADANAS', 'c_puntajes']

#dataset
estu_punt = pd.read_csv('data/estu_punt.csv')

#utility variable
tmp = estu_punt[['COLE_DEPTO_COLEGIO', 'COLE_MPIO_MUNICIPIO']].copy()
tmp = tmp.drop_duplicates(subset='COLE_MPIO_MUNICIPIO', keep="first")
citiesPerDepartment = {}
for i in tmp['COLE_DEPTO_COLEGIO'].unique():
    citiesPerDepartment[i] = [tmp['COLE_MPIO_MUNICIPIO'][j] for j in tmp[tmp['COLE_DEPTO_COLEGIO']==i].index]
###

def filter_estu_punt(estu_punt=estu_punt, var=None,\
                     puntajes=puntajes, dpto=None,\
                    periodo=None, city=None): 
    #Hack to count in aggregate way
    estu_punt['c_puntajes'] = 1
    oper_agg = ['mean', 'mean', 'mean', 'mean', 'mean', 'mean', 'count']
    dagg = dict(zip(puntajes, oper_agg))
    if periodo is None:
        periodo = ['2008-2', '2009-2', '2010-2', '2011-2', '2012-2', '2013-2',
           '2014-2', '2015-2', '2016-2', '2017-2', '2018-2', '2012-1',
           '2009-1', '2010-1', '2011-1', '2019-1', '2013-1', '2014-1',
           '2015-1', '2018-1', '2016-1', '2017-1']
        
    if var is None:
        agrupacion = ['PERIODOestu']
    else:
        agrupacion = ['PERIODOestu'] + [var] 
    
    if dpto is None:
        if city is None:
            agrupacion += ['COLE_DEPTO_COLEGIO'] 
            mask = [-1, periodo]
        else:
            agrupacion += ['COLE_MPIO_MUNICIPIO'] 
            mask = [0, [city], periodo]
    else:
        if city is None:
            agrupacion += ['COLE_DEPTO_COLEGIO', 'COLE_MPIO_MUNICIPIO'] 
            mask = [1, [dpto], periodo]
        else:
            agrupacion += ['COLE_MPIO_MUNICIPIO'] 
            mask = [0, [city], periodo]
    
    temp_df = estu_punt.groupby(agrupacion)[puntajes].agg(dagg).reset_index() 
    #print(mask')'
    if len(mask) == 2:
        mask = temp_df.PERIODOestu.isin(periodo)
    else:
        if mask[0]==0:
            mask = temp_df.PERIODOestu.isin(mask[2]) & temp_df.COLE_MPIO_MUNICIPIO.isin(mask[1])
        else:
            mask = temp_df.PERIODOestu.isin(mask[2]) & temp_df.COLE_DEPTO_COLEGIO.isin(mask[1])
        
    #print(mask[0:5])
    temp_df = temp_df[mask].reset_index(drop=True)    
    gc.collect()
    return temp_df


def puntaje_heatmap(norm_temp_df, puntaje):
    fig = go.Figure(data=go.Heatmap(
            z=norm_temp_df.values,
            x=norm_temp_df.columns,
            y=norm_temp_df.index,
            opacity = 0.8,
            xgap = 0.7,
            ygap = 0.7,
            reversescale=True
            ))

    fig.update_layout(
        width=600,
        height=800,
        template='none',
        yaxis = {'categoryorder':"total ascending"},
        xaxis = {'type':'category'},
        title = puntaje
    )

    return fig


def scatter_Plot(temp_df, x_col, puntaje, var=None):
    fig = go.Figure()

    if var is None:
        fig.add_trace(go.Scatter(
            x=temp_df[x_col],
            y = temp_df[puntaje],
            name = puntaje,
            mode = 'lines+markers',
            line_shape='spline'
            ))    
        
    else:
        var_values = temp_df[var].unique()
        for i,e in enumerate(var_values):
            fig.add_trace(go.Scatter(
                x=temp_df[temp_df[var]==e][x_col],
                y = temp_df[temp_df[var]==e][puntaje],
                name = str(e),
                mode = 'lines+markers',
                line_shape='spline'
                ))  

    
    tickfont = {
                 'family':'Arial',
                 'size':12,
                 'color':'rgb(82, 82, 82)'
            }

    fig.update_layout(

        title = str(var) + ' Evolution by year',

        xaxis = {'type':'category',
                'showline':True,
                'linecolor':'rgb(204, 204, 204)',
                'linewidth':2,
                'ticks':'outside',
                'tickangle':-10,
                'tickfont':tickfont},

        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=True,
            tickfont=tickfont
        ),
        autosize=True,
        margin=dict(
            autoexpand=True,
            l=100,
            r=20,
            t=110,
        ),
        showlegend=True,
        plot_bgcolor='white'

    )

    return fig


def getDetailedScatterByDpto(dpto,var,puntaje):
    temp_df = filter_estu_punt(estu_punt, dpto=dpto, var=var)
    if var is None:
        agrupacion = ['PERIODOestu','COLE_DEPTO_COLEGIO']
    else:
        agrupacion = ['PERIODOestu','COLE_DEPTO_COLEGIO',var]
    temp_df['PUNT_MULTI'] = temp_df[puntaje] * temp_df['c_puntajes']
    new_temp_df = temp_df.groupby(agrupacion)[['PUNT_MULTI', 'c_puntajes']].sum().reset_index()
    new_temp_df[puntaje] = new_temp_df['PUNT_MULTI']/new_temp_df['c_puntajes']
    new_temp_df = new_temp_df[new_temp_df['PERIODOestu'].str.contains('-2')].reset_index(drop=True)
    fig = scatter_Plot(new_temp_df, x_col='PERIODOestu', puntaje=puntaje, var=var)
    return fig

def getDetailedScatterByCity(city, var, puntaje):
    temp_df = filter_estu_punt(estu_punt, city=city, var=var)
    temp_df.head()
    if var is None:
        agrupacion = ['PERIODOestu','COLE_MPIO_MUNICIPIO']
    else:
        agrupacion = ['PERIODOestu','COLE_MPIO_MUNICIPIO',var]
    temp_df['PUNT_MULTI'] = temp_df[puntaje] * temp_df['c_puntajes']
    new_temp_df = temp_df.groupby(agrupacion)[['PUNT_MULTI', 'c_puntajes']].sum().reset_index()
    new_temp_df[puntaje] = new_temp_df['PUNT_MULTI']/new_temp_df['c_puntajes']

    new_temp_df = new_temp_df[new_temp_df['PERIODOestu'].str.contains('-2')].reset_index(drop=True)
    fig = scatter_Plot(new_temp_df, x_col='PERIODOestu', puntaje=puntaje, var=var)
    return fig


def getDetailedScatterAllCountry(var, puntaje):
    temp_df = filter_estu_punt(estu_punt, var=var)
    if var is None:
        agrupacion = ['PERIODOestu']
    else:
        agrupacion = ['PERIODOestu',var]
    temp_df['PUNT_MULTI'] = temp_df[puntaje] * temp_df['c_puntajes']
    new_temp_df = temp_df.groupby(agrupacion)[['PUNT_MULTI', 'c_puntajes']].sum().reset_index()
    new_temp_df[puntaje] = new_temp_df['PUNT_MULTI']/new_temp_df['c_puntajes']
    new_temp_df = new_temp_df[new_temp_df['PERIODOestu'].str.contains('-2')].reset_index(drop=True)
    fig = scatter_Plot(new_temp_df, x_col='PERIODOestu', puntaje=puntaje, var=var)
    return fig
    
def getHeatmapAllCountry(puntaje):
    temp_df= filter_estu_punt(estu_punt)
    min_max_scaler = preprocessing.MinMaxScaler()
    norm_temp_df = temp_df[['PERIODOestu', 'COLE_DEPTO_COLEGIO', puntaje]]
    norm_temp_df = norm_temp_df.pivot('COLE_DEPTO_COLEGIO', 'PERIODOestu', puntaje)
    norm_temp_df = norm_temp_df.loc[:, norm_temp_df.columns.str.contains('-2')].sort_values(by='2014-2', ascending=False)
    x_scaled = min_max_scaler.fit_transform(norm_temp_df.values)
    norm_temp_df[[col for col in norm_temp_df.columns]] = x_scaled
    fig = puntaje_heatmap(norm_temp_df, puntaje)
    return fig


def getHeatmapByDpto(puntaje, dpto):
    temp_df = filter_estu_punt(estu_punt, dpto=dpto)
    min_max_scaler = preprocessing.MinMaxScaler()
    norm_temp_df = temp_df[['PERIODOestu', 'COLE_MPIO_MUNICIPIO', puntaje]]
    norm_temp_df = norm_temp_df.pivot('COLE_MPIO_MUNICIPIO', 'PERIODOestu', puntaje)
    norm_temp_df = norm_temp_df.loc[:, norm_temp_df.columns.str.contains('-2')].sort_values(by='2014-2', ascending=False)

    x_scaled = min_max_scaler.fit_transform(norm_temp_df.values)

    norm_temp_df[[col for col in norm_temp_df.columns]] = x_scaled

    if len(norm_temp_df)>30:
        norm_temp_df = pd.concat([norm_temp_df.head(15), norm_temp_df.tail(15)])

    fig = puntaje_heatmap(norm_temp_df, puntaje)

    return fig


def getHeatmapByCity(puntaje, city):
    min_max_scaler = preprocessing.MinMaxScaler()
    temp_df = estu_punt[estu_punt.COLE_MPIO_MUNICIPIO == city].reset_index()
    temp_df = temp_df.groupby(['PERIODOestu', 'COLE_NOMBRE'])[puntajes].mean().reset_index()
    norm_temp_df = temp_df.sort_values(by=puntaje).reset_index()
    norm_temp_df = norm_temp_df.pivot('COLE_NOMBRE', 'PERIODOestu', puntaje)
    norm_temp_df  =norm_temp_df.loc[:, norm_temp_df.columns.str.contains('-2')].sort_values(by='2014-2', ascending=False)
    x_scaled = min_max_scaler.fit_transform(norm_temp_df.values)
    norm_temp_df[[col for col in norm_temp_df.columns]] = x_scaled
    if len(norm_temp_df)>30:
        norm_temp_df = pd.concat([norm_temp_df.head(15), norm_temp_df.tail(15)])

    fig = puntaje_heatmap(norm_temp_df, puntaje)

    return fig