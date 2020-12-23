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
print(df_PDA)
print("Hola funciono")

