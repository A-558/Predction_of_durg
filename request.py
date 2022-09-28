import requests

url = 'http://127.0.0.1:5000/predict'
r = requests.post(url,json={'Age':23, 'Sex':0, 'BP':1 ,'Cholesterol' : 1 ,"Na_to_K" : 25})

print(r.json())