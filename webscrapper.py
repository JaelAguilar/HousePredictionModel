import traceback
import bs4
import csv
import requests
from tqdm import tqdm

from webscrapperFunctions import checkHouse, checkLink, checkMyIP, isResponseValid,getHeaders

originalLink = 'https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/'
checkMyIP() #Sanity Check
totalPages = 100
houses = []
cLoop = 0
try:
    for i in tqdm(range(1,totalPages+1)):
        cLoop=i
        #print('================================================ PAGE '+str(i)+' ================================================================')
        newLink = originalLink +'?page='+str(i)
        # Request the URL       
        response = checkLink(newLink)

        if isResponseValid(response):
            #Creating the soup with an HTML Parser
            soup = bs4.BeautifulSoup(response.text,'html.parser')

            #Obtains the HTML objects of eacht on of the cards on the webpage
            divHouses = soup.find_all('div',{'class':'row ListingCell-row ListingCell-agent-redesign'})

            for house in divHouses:
                houseData = checkHouse(house)
                if houseData is not None:
                    houses.append(houseData)
except Exception as e:
    print("Loop {}: {}".format(cLoop,e))
    print(traceback.format_exc())
    requests.post('https://api.mynotifier.app', {
    "apiKey": 'cc66dedc-04cd-42ac-b502-2efb81b98419', # Sign up for your own api key
    "message": "Error obteniendo datos", # Could be anything
    "description": "Loop {} Error: {}".format(cLoop,e), # Optional
    "body": e, # Optional
    "type": traceback.format_exc(), # info, error, warning or success
    "project": "" # Optional if you want to specify the project
  })
#print(*houses, sep='\n\n')

# Updating the csv
headers = getHeaders()
resultsFile = open('Data/dataTest.tsv','w',newline='')
resultsFileWriter = csv.DictWriter(resultsFile, delimiter='\t', lineterminator='\n',fieldnames=["titulo","direccion","precio"]+list(headers))
resultsFileWriter.writeheader()
#print(headers)
for house in tqdm(houses):
    resultsFileWriter.writerow(house)
resultsFile.close()
        
        
    
    

