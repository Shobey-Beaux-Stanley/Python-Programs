import pandas, scipy , matplotlib, numpy, json
from statsmodels.formula.api import ols
import statsmodels.api as sm
from Classes import Day

days_list = []#Holds objects of type Day
with open("input_data.json") as json_data:
    data = json.load(json_data)
print(data.keys())
print(data['days'][35])
for temp_day in data['days']:
    newDay = Day()
    newDay.date = temp_day['date']
    newDay.assigned = temp_day['assigned']
    newDay.returned = temp_day['returned']
    newDay.abandoned = temp_day['abandoned']
    newDay.paid = temp_day['paid']
    newDay.approved = temp_day['day']['approved']
    newDay.rejected = temp_day['day']['rejected']
    newDay.submitted = temp_day['day']['submitted']
    newDay.pending = temp_day['day']['pending']
    newDay.hit_rewards = temp_day['day']['hits_rewards']
    newDay.bonus_rewards = temp_day['day']['bonus_rewards']
    newDay.earnings = temp_day['day']['earnings']
    days_list.append(newDay)
'''
print("hello world")
data = pandas.read_csv("data_input.csv", sep=",")
print(data.shape)#prints num of rows, num of columns
print(data.columns)#prints column names

data.plot(x = "DA", y = "R", kind = "scatter")
model = ols("DA ~ R", data).fit()#Find Regression from dataframe
print(model.summary())


data_subset = data.dropna(subset=['DA','R'])
#data_subset = data_subset[data_subset]
x = data_subset['DA']
y = data_subset['R']

#matplotlib.pyplot.show()
'''
