import pandas as pd
import bayespy as bp
import csv

data=pd.read_csv("heart_disease_data1.csv")
heart_disease=pd.DataFrame(data)
print(heart_disease)

from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator,BayesianEstimator

model=BayesianModel([('age','Lifestyle'),('Gender','Lifestyle'),('Family','heartdisease'),('diet','cholestrol'),('Lifestyle','diet'),('cholestrol','heartdisease'),('diet','cholestrol')])
model.fit(heart_disease,estimator=MaximumLikelihoodEstimator)

from pgmpy.inference import VariableElimination
HeartDisease_infer=VariableElimination(model)
print('For age enter SuperSeniorCitizen:0,SeniorCitizen:1,MiddleAged:2,Youth:3,Teen:4')
print('For Gender Enter Male:0 , Female:1')
print('For Family History Enter yes:1,N0:0')
print('For diet Enter High:0,Medium:1')
print('for lifestyle enter Athlete:0,Active:1,Moderate:2,Sedetary:3')
print('for cholestrol enter High:0,BorderLine:1,Normal:2')
q=HeartDisease_infer.query(variables=['heartdisease'],evidence={'age':int(input('enter age :')),'Gender':int(input('enter Gender:')),'Family':int(input('enter Family history: ')),'diet':int(input('enter diet : ')),'Lifestyle':int(input('enter Lifestyle : ')),'cholestrol':int(input('enter cholestrol :'))})
print(q['heartdisease'])