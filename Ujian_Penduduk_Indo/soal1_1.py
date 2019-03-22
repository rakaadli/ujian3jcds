import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

databps1 = pd.read_excel('indo_12_1.xls',skiprows=3,skipfooter = 2)
df = pd.DataFrame(databps1)
df.columns = ['Provinsi','1971','1980','1990','1995','2000','2010']
df.replace('-', int(0), inplace=True)

#logicnya ea
indo=df['Provinsi'][df['2010']==df['2010'].max()]
Indonesia=indo.index.tolist()[0]

#df baru biar ga pusing
df1=df
df1.dropna(inplace = True)
terbesar = df1.nlargest(2, '2010') 
Jawabarat=terbesar['Provinsi'].index.tolist()[1] 
#print(jawabarat)

kecil=df1['Provinsi'][df1['1971']==df1['1971'].min()] 
Bengkulu=kecil.index.tolist()[0] 

#untuk di plot
x=np.array([1971,1980,1990,1995,2000,2010])
kolomy=['1971','1980','1990','1995','2000','2010']
yindonesia=df.loc[Indonesia,kolomy]
yjawabarat=df.loc[Jawabarat,kolomy]
ybengkulu=df.loc[Bengkulu,kolomy]

#PLOTnya bray
plt.figure(figsize=(9,6))
plt.style.use('ggplot')
plt.plot(x,yjawabarat,color='g',label=df1.Provinsi[Jawabarat],linestyle='-')
plt.plot(x,ybengkulu,color='b',label=df1.Provinsi[Bengkulu],linestyle='-')
plt.plot(x,yindonesia,color='r',label=df1.Provinsi[Indonesia],linestyle='-')

plt.legend()

plt.scatter(x,yindonesia,color='r')
plt.scatter(x,yjawabarat,color='g')
plt.scatter(x,ybengkulu,color='b')

plt.grid(True)

plt.xlabel('Tahun',fontsize=12)
plt.ylabel('Jumlah penduduk (ratus juta jiwa)',fontsize=12)
plt.title('Jumlah Penduduk INDONESIA (1971-2010)',fontsize=14)
plt.show()
