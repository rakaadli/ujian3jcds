import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

df=pd.read_excel('indo_12_1.xls')
df.columns=['Provinsi','1971','1980','1990','1995','2000','2010']
df=df.dropna()
df.replace('-', int(0), inplace=True)

#mikir ea
indo=df['Provinsi'][df['2010']==df['2010'].max()]
Indonesia=indo.index.tolist()[0] 

#df baru
df1=df
df1.dropna(inplace = True)
terbesar = df1.nlargest(2, "2010") 
Jawabarat=terbesar['Provinsi'].index.tolist()[1] 


kecil=df1['Provinsi'][df1['1971']==df1['1971'].min()] 
#print(kecil)
bengkulu=kecil.index.tolist()[0] 
#print(bengkulu)

x=np.array([1971,1980,1990,1995,2000,2010])
xr=x.reshape(-1,1)
kolomy=['1971','1980','1990','1995','2000','2010']
yindonesia=df.loc[Indonesia,kolomy]
yjawabarat=df.loc[Jawabarat,kolomy]
ybengkulu=df.loc[bengkulu,kolomy]

from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(xr,yjawabarat)
ypredictjb=model.predict(xr)

print('Prediksi Jumlah Penduduk Jawa Barat di Tahun 2050:', int(round(model.predict([[2050]])[0])))

model.fit(xr,ybengkulu)
ypredictbengkulu=model.predict(xr)
print('Prediksi jumlah Penduduk Bengkulu di Tahun 2050:', int(round(model.predict([[2050]])[0])))

model.fit(xr,yindonesia)
ypredictid=model.predict(xr)
print('Prediksi Jumlah Penduduk Indonesia di Tahun 2050:', int(round(model.predict([[2050]])[0])))

#di plot

plt.figure(figsize=(9,6))
plt.style.use('ggplot')
plt.plot(x,yjawabarat,color='g',label=df1.Provinsi[Jawabarat],linestyle='-')
plt.plot(x,ybengkulu,color='b',label=df1.Provinsi[bengkulu],linestyle='-')
plt.plot(x,yindonesia,color='r',label=df1.Provinsi[Indonesia],linestyle='-')
plt.plot(xr,ypredictjb,'y-',label='Best Fit Line')
plt.plot(xr,ypredictbengkulu,'y-')

plt.plot(xr,ypredictid,'y-')

plt.legend()

plt.scatter(x,yindonesia,color='r')
plt.scatter(x,yjawabarat,color='g')
plt.scatter(x,ybengkulu,color='b')

plt.grid(True)

plt.xlabel('Tahun',fontsize=12)
plt.ylabel('Jumlah penduduk (ratus juta jiwa)',fontsize=12)
plt.title('Jumlah Penduduk INDONESIA (1971-2010)',fontsize=14)
plt.show()

