import matplotlib.pyplot as plt
import pandas as pd
import numpy as np1

def kernel(point,xmat, k):
    m,n= np1.shape(xmat)
    weights = np1.mat(np1.eye((m)))
    for j in range(m):
        diff = point - X[j]
        weights[j,j] = np1.exp(diff*diff.T/(-2.0*k**2))
    return weights
 
def localWeight(point,xmat,ymat,k):
    wei = kernel(point,xmat,k)
    W = (X.T*(wei*X)).I*(X.T*(wei*ymat.T))
    return W
     
def localWeightRegression(xmat,ymat,k):
    m,n = np1.shape(xmat)
    ypred = np1.zeros(m)
    for i in range(m):
        ypred[i] = xmat[i]*localWeight(xmat[i],xmat,ymat,k)
    return ypred
       
# load data points
data = pd.read_csv('tips1.csv')
bill = np1.array(data.total_bill)
tip = np1.array(data.tip)
 
#preparing and add 1 in bill
mbill = np1.mat(bill)  # mat treats array as matrix
mtip = np1.mat(tip)
m= np1.shape(mbill)[1]
print("******",m)
one = np1.mat(np1.ones(m))
X= np1.hstack((one.T,mbill.T))    #Stack arrays in sequence horizontally (column wise).
 
#set k here
ypred = localWeightRegression(X,mtip,2)
SortIndex = X[:,1].argsort(0)
xsort = X[SortIndex][:,0]
     
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(bill,tip, color='blue')
ax.plot(xsort[:,1],ypred[SortIndex], color = 'red', linewidth=1)
plt.xlabel('Total bill')
plt.ylabel('Tip')
plt.show();








