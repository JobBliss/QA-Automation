import firebase_admin
import datetime
import json,csv
from firebase_admin import credentials, db

# Fetch the service account key JSON file contents
cred = credentials.Certificate("./qaresults-a35ee-firebase-adminsdk-lam61-ec5d1e12d3.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://qaresults-a35ee-default-rtdb.firebaseio.com/"
})

ref = db.reference('jobBlissAlpha')

#Convert results csv to json
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

def results():
    csvFilePath = r'./prodAutomationQA_Summary.csv'
    jsonFilePath = r'prodresults.json'

    csv_to_json(csvFilePath, jsonFilePath)


    #push json to firebase
    with open("prodresults.json", "r") as f:
        file_contents = json.load(f)
    ref.set(file_contents)

results()



