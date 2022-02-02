import pandas
from sklearn import linear_model

df = pandas.read_csv("enterprises.csv")

X = df[
    [
        'Question1', 
        'Question2',
        'Question3',
        'Question4',
        'Question5',
        'Question6',
        'Question7',
        'Question8',
        'Question9',
        'Question10',
        'Question11',
        'Question12',
        'Question13',
        'Question14',
        'Question15',
    ]]
y = df['NPS']

print(df, '\n')

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedNPS = regr.predict([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])

print(predictedNPS)