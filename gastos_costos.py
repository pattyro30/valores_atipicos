import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfgc= pd.read_excel('gastos_costos_20_23.xlsx', index_col=0)
#print(df.head())

valores_nulos=dfgc.isnull().sum()
#print(valores_nulos)

fig = plt.figure(figsize =(7, 3))
plt.hist(x=dfgc["IVA"], color='red', rwidth=0.50)
plt.title('Hist IVA con outliers')
plt.xlabel('IVA')
plt.ylabel('Frecuencia')
#plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(dfgc["IVA"]) 
plt.title("Outliers de IVA con outliers")
#plt.show()

y=dfgc['IVA']
print(y)

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
print(percentile25)
print(percentile75)
iqr= percentile75 - percentile25
print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
print("Limite superior permitido", Limite_Superior_iqr)
print("Limite inferior permitido", Limite_Inferior_iqr)

# Datos limpios
data_clean_iqr= dfgc[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
print(data_clean_iqr)

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["IVA"]) 
plt.title("Outliers de IVA")
#plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["IVA"], color='red', rwidth=0.50)
plt.title('Hist IVA sin outliers')
plt.xlabel('IVA')
plt.ylabel('Frecuencia')
#plt.show()

# Con desviación estándar
data_clean_iqr["IVA"].to_csv('IVA.csv')

y=dfgc["IVA"]
Limite_Superior_dev_std= y.mean() + 3*y.std()
Limite_Inferior_dev_std= y.mean() - 3*y.std()
print("Limite superior permitido usando desv estandar", Limite_Superior_dev_std)
print("Limite inferior permitido usando desv estandar", Limite_Inferior_dev_std)

# Datos limpios
data_clean_dev_std= dfgc[(y<=Limite_Superior_dev_std)&(y>=Limite_Inferior_dev_std)]
print(data_clean_dev_std)

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["IVA"], color='red', rwidth=0.50)
plt.title('Hist IVA sin outliers- desv std')
plt.xlabel('IVA')
plt.ylabel('Frecuencia')
#plt.show()

# column: total MX
fig2 = plt.figure(figsize =(7, 3))
plt.hist(x=dfgc["TOTAL MX"], color='red', rwidth=0.50)
plt.title('Hist total MX con outliers')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()

fig2 = plt.figure(figsize =(5, 3))
plt.boxplot(dfgc["TOTAL MX"]) 
plt.title("Outliers de total MX con outliers")
#plt.show()

y2=dfgc['TOTAL MX']
print(y2)

percentile25=y2.quantile(0.25) #Q1
percentile75=y2.quantile(0.75) #Q3
print(percentile25)
print(percentile75)
iqr2= percentile75 - percentile25
print(iqr2)

Limite_Superior_iqr2= percentile75 + 1.5*iqr2
Limite_Inferior_iqr2= percentile25 - 1.5*iqr2
print("Limite superior permitido", Limite_Superior_iqr2)
print("Limite inferior permitido", Limite_Inferior_iqr2)

# Datos limpios
data_clean_iqr2= dfgc[(y2<=Limite_Superior_iqr2)&(y2>=Limite_Inferior_iqr2)]
print(data_clean_iqr2)

fig2 = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr2["TOTAL MX"]) 
plt.title("Outliers de TOTAL MX")
#plt.show()

fig2 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr2["TOTAL MX"], color='red', rwidth=0.50)
plt.title('Hist total MX sin outliers')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()

# Con desviación estándar
data_clean_iqr2["TOTAL MX"].to_csv('TOTAL MX.csv')

y2=dfgc["TOTAL MX"]
Limite_Superior_dev_std2= y2.mean() + 3*y2.std()
Limite_Inferior_dev_std2= y2.mean() - 3*y2.std()
print("Limite superior permitido usando desv estandar", Limite_Superior_dev_std2)
print("Limite inferior permitido usando desv estandar", Limite_Inferior_dev_std2)

# Datos limpios
data_clean_dev_std2= dfgc[(y2<=Limite_Superior_dev_std2)&(y>=Limite_Inferior_dev_std2)]
print(data_clean_dev_std2)

fig2 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["TOTAL MX"], color='red', rwidth=0.50)
plt.title('Hist total MX sin outliers - desv std')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()


# column : importe
fig3 = plt.figure(figsize =(7, 3))
plt.hist(x=dfgc["IMPORTE"], color='red', rwidth=0.50)
plt.title('Hist importe con outliers')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

fig3 = plt.figure(figsize =(5, 3))
plt.boxplot(dfgc["IMPORTE"]) 
plt.title("Outliers de importe con outliers")
#plt.show()

y3=dfgc['IMPORTE']
print(y3)

percentile25=y3.quantile(0.25) #Q1
percentile75=y3.quantile(0.75) #Q3
print(percentile25)
print(percentile75)
iqr3= percentile75 - percentile25
print(iqr3)

Limite_Superior_iqr3= percentile75 + 1.5*iqr3
Limite_Inferior_iqr3= percentile25 - 1.5*iqr3
print("Limite superior permitido", Limite_Superior_iqr3)
print("Limite inferior permitido", Limite_Inferior_iqr3)

# Datos limpios
data_clean_iqr3= dfgc[(y3<=Limite_Superior_iqr3)&(y3>=Limite_Inferior_iqr3)]
print(data_clean_iqr3)

fig3 = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr3["IMPORTE"]) 
plt.title("Outliers de importe")
#plt.show()

fig3 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr3["IMPORTE"], color='red', rwidth=0.50)
plt.title('Hist importe sin outliers')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

# Con desviación estándar
data_clean_iqr3["IMPORTE"].to_csv('IMPORTE.csv')

y3=dfgc["IMPORTE"]
Limite_Superior_dev_std3= y3.mean() + 3*y3.std()
Limite_Inferior_dev_std3= y3.mean() - 3*y3.std()
print("Limite superior permitido usando desv estandar", Limite_Superior_dev_std3)
print("Limite inferior permitido usando desv estandar", Limite_Inferior_dev_std3)

# Datos limpios
data_clean_dev_std3= dfgc[(y3<=Limite_Superior_dev_std3)&(y>=Limite_Inferior_dev_std3)]
print(data_clean_dev_std3)

fig3 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr3["IMPORTE"], color='red', rwidth=0.50)
plt.title('Hist importe sin outliers- desv std')
plt.xlabel('IMPORTE')
plt.ylabel('IMPORTE')
#plt.show()