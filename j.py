import json

f = open("test.txt","w")
tyss = {"ceo":"Girish","MQAS":"Raju","MPS":"Kishore"}
data = json.dumps(tyss)
f.write(data)
print(json.loads(data))




