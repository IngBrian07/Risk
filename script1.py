import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi

#if __name__=="main":
#Files paths
p_guru="./../../../../../Dropbox/PMO/Proyectos/DAE200701" #Guruli
p_PDA="./../../../../../Dropbox/PMO/Proyectos/DAE200901-PDA" #PDA

#File names
guruli="/PMO 01006 Control Riesgos y Problemas.xlsx"
PDA="/PMO_01006_Control_Riesgos_y_Problemas_DAE.xlsx"

#Reading of the datafame 
df_guru=pd.read_excel(p_guru + guruli, sheet_name='PMO 01006 Control Riesgos y Pro', skiprows=2, index_col=1)
df_PDA=pd.read_excel(p_PDA+PDA, sheet_name="Riesgos", header=1, index_col=1)


#-------------------------------*************Cleaning dataset of guruly******************-------------------------------

df_guru.drop(columns=["Unnamed: 0", "Index Promedio Mensual","Mes"], axis=1, inplace=True) #Dropped unnecessary columns 
df_guru['Proyecto']='Guruli' # Added new column to identify each project

#Added an identifier
dict_Gu={}
for i in range(1, df_guru.shape[0]+1):
    dict_Gu[i]="Gu-"+str(i)
df_guru.rename(index=dict_Gu, inplace=True)


#-------------------------------*************Cleaning dataset of PDA******************-------------------------------

df_PDA.rename(columns={"Unnamed: 7":"Calidad","Unnamed: 8":"Tiempo","Unnamed: 9":"Ppto","Impacto":"Alcance"}, inplace=True)
df_PDA.drop(["Unnamed: 0"], axis=1, inplace=True)
df_PDA=df_PDA.reset_index().drop([0,23])
df_PDA["Proyecto"]='PDA'
df_PDA.drop(['#'],axis=1, inplace=True)

#Added an identifier
dict_PDA={}
for i in df_PDA.index:
    dict_PDA[i]="PDA-"+str(int(i))
df_PDA.rename(index=dict_PDA, inplace=True)


#-------------------------------*************Doing the merge******************-------------------------------
df=df_guru.append(df_PDA)


#-------------------------------*************Working with dataset******************-------------------------------
df[["Alcance","Calidad","Tiempo","Ppto"]]=df[["Alcance","Calidad","Tiempo","Ppto"]].astype(int)
df[['Fecha Compromiso']]=df['Fecha Compromiso'].apply(pd.to_datetime)


#-------------------------------*************Working only with important data******************-------------------------------
df.notnull().sum()/df.shape[0]*100  #Table with the percentage of amount of complete
df_analysis=df.drop(["Fecha Compromiso","Plan de Acción"], axis=1)

"""
Independent values
.- Riesgo / Detonador
.- Categoria
.- Estatus
.- Responsable
.- Proyecto
 """

df_A1= df_analysis[["Riesgo / Detonador","Categoría","Estatus","Responsable","Proyecto"]]
df_A1["Riesgo / Detonador"].value_counts().count()/df_A1.shape[0]*100 #Numbers uniques in the column Riesgos
dict1= df_A1["Responsable"].value_counts()/df_A1.shape[0]*100 #Number of risks for area; It's a dictionary 

keys=dict(dict1).keys()
values=dict(dict1).values()

"""Defining labels size 
"""

title=18
label_text=14
colors=['green','blue','orange','gray','#33f9ff','#339cFF','#5e33ff']

#-------------------------------*************Make figures******************-------------------------------
#Pie graph Incidencias
ls_ax=[0.1 for x in values]
explod=tuple(ls_ax)

fig1, ax1= plt.subplots(figsize=(6,6), subplot_kw=dict(aspect="equal"))
ax1.pie(values, explode=explod,
        labels=keys, autopct='%1.2f%%', 
        shadow=True, textprops={'size':label_text, 'backgroundcolor': 'w'},
       colors=colors, labeldistance=0.9)

plt.title('Incidencias', size=title, )

plt.savefig('./imagenes/inc1.png',transparent=True)


#***********Bar graph********
#Bar graph 
plt.figure(figsize=(8,4))

#Plotting 
plt.bar(keys,values, width = 0.5,color=colors)

plt.xlabel('Área', size=label_text)
plt.ylabel('Frecuencia', size=label_text)
plt.title('Incidencias oor área', size=title)
plt.savefig('.\imagenes\IncTiemp1.png', transparent=True)




#***********Risk Table********
G_bars=df_A1[["Riesgo / Detonador"]]
dfi.export(G_bars.sample(10), './imagenes/table_Risk.png')


#***********Plotting a pie graph******** 
dict2=df_A1['Proyecto'].value_counts().to_dict()
keys2=dict2.keys()
value2=dict2.values()


fig, ax= plt.subplots(figsize=(4,4))

ax.pie(value2, labels=keys2, autopct= '%1.2f%%',
      shadow=True, textprops={'size':label_text},
      colors=['brown','green'])

plt.savefig('.\imagenes\Risk_by_proj.png', transparent=True)
