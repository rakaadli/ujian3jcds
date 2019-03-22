import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

df=pd.read_csv('data.csv')
df.replace('-', int(0), inplace=True)

df['Target']=0
df['Target_name']='Non-Target'

df['Target'][(df['Age']<=25)&(df['Overall']>=80)&(df['Potential']>=80)]=1
df['Target_name'][(df['Age']<=25)&(df['Overall']>=80)&(df['Potential']>=80)]='Target'

x=df.loc[:,['Age','Overall','Potential']]
y=df['Target']

k = round(len(x) ** .5)
if((k%2) == 0):
    k=k+1
else:
    k=k
knn=KNeighborsClassifier(n_neighbors=k)


#support Vector Machine
SVC = SVC(gamma = 'auto')


# Random Forest
ranfor=RandomForestClassifier(n_estimators=50)


# Decision Tree
dec=DecisionTreeClassifier()


print("Skor KNN: ",round(cross_val_score(knn,x,y,cv=3).mean()*100),' %')
print("Skor Random Forest: ",round(cross_val_score(ranfor,x,y,cv=3).mean()*100),' %')
print("Skor Decision Tree: ",round(cross_val_score(dec,x,y,cv=3).mean()*100),' %')
print("Skor SVM:",round(cross_val_score(SVC,x,y,cv=3).mean()*100),' %')


# Skor KNN:  94.0  %
# Skor Random Forest:  89.0  %
# Skor Decision Tree:  89.0  %
# Skor SVM: 99.0  
