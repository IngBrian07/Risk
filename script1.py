import pandas as pd
import matplotlib.pyplot as pyplot

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



print(df_PDA)

