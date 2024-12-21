import pandas as pd
import json

recipe_dataframe = pd.read_csv('C:/Users/diamo/Desktop/recipes_test/recipes3.csv')
recipes1 = recipe_dataframe.to_dict(orient='records')

json_data = {}
data = []
for record in recipes1:
    this_record = {}
    for item in record:
        if str(record[item]).lower() != 'nan':
            this_record[item] = str(record[item])
        else:
            this_record[item] = ''
        x = 2
    data.append(this_record)
json_data['data'] = data

with open(file='recipes4.json', mode='w') as f:
    json.dump(obj=json_data, fp=f)
x = 2