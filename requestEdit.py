import requests
import base64

myURL="" #I've removed the URL for pruvacy purposes.
email={'email':'david.adr.elizalde@hpe.com'}

people = []
payload = ""
mycodefile ="code.py"
ageAverage = 0

def get_token():
    r = requests.get(myURL,email)
    data = r.json()
    token = data['token']
    return token

def get_people():
    keepgoing = True
    global ageAverage
    while keepgoing:
      r = requests.get(myURL+"/data",{'token': token})
      if(r.status_code == 404):
        print("404 encountered, exiting")
        keepgoing = False 
      else:
        print(r.status_code)
        data = r.json()
        print(data)
        people.append( data['name'] )
        ageAverage += int( data['age'] )

token = get_token()
get_people()
ageAverage = ageAverage // len(people)

people.sort()
for person in people:
    payload += person.split(' ')[1][0]

with open("code.py", "rb") as text_file:
  encoded_bytes = base64.b64encode(text_file.read())
  encoded_string = encoded_bytes.decode('utf-8')
  #print(encoded_string)

myfinaljson = {'age': ageAverage, "payload": payload, "code": encoded_string }
#Final Post
r = requests.post(myURL+"/result?token="+token, json=myfinaljson)
print(r.url)
print(r.json())