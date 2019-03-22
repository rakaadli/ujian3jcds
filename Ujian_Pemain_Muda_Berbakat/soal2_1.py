import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

df=pd.read_csv('data.csv')

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Read a file
df = pd.read_csv('data.csv')

plt.figure('soal2_1plot',figsize = (10,17))
plot1 = plt.subplot(121)
plt.scatter(
    df['Age'],
    df['Overall'],
    marker = 'o',
    color = 'r'
)
plt.scatter(
    df['Age'][df['Age'] <= 25][df['Overall'] >= 80],
    df['Overall'][df['Age'] <= 25][df['Overall'] >= 80],
    marker = 'o',
    color = 'g'
)
plot1.set_xlabel('Age')
plot1.set_ylabel('Overall')
plot1.set_title(' Age vs Overall')
plot1.legend(['Non-Target','Target'])
plot1.grid()
plot2 = plt.subplot(122)
plt.scatter(
    df['Age'],
    df['Potential'],
    marker = 'o',
    color = 'r'
)
xage=df['Age'][df['Age'] <= 25][df['Potential'] >= 80]
yoverall = df['Potential'][df['Age'] <= 25][df['Potential'] >= 80]
plt.scatter(
    xage,
    yoverall,
    marker = 'o',
    color = 'g'
)
plot2.set_xlabel('Age')
plot2.set_ylabel('Potential')
plot2.set_title('Age vs Potential')
plot2.legend(['Non-Target','Target'])
plot2.grid(True)
plt.show()
