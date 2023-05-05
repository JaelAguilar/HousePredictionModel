import traceback
import bs4
import csv
import requests
from tqdm import tqdm

from webscrapperFunctions import checkHouse, checkLink, checkMyIP, isResponseValid,getHeaders

originalLink = 'https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/'
originalLinks = [
    "https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/?sorting=newest",
    "https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/?sorting=price-high",
    "https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/?sorting=price-low",
    "https://www.lamudi.com.mx/nuevo-leon/apodaca/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/guadalupe-1/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/monterrey/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/monterrey/casa/for-sale/?sorting=newest",
    "https://www.lamudi.com.mx/nuevo-leon/san-pedro-garza-garcia/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/santa-catarina-1/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/san-nicolas-de-los-garza/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/garcia/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/santiago/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/general-escobedo/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/juarez-4/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/cadereyta-jimenez/casa/for-sale/",
    "https://www.lamudi.com.mx/nuevo-leon/pesqueria/casa/for-sale/"]

places = [
    "Nuevo León nuevas",
    "Nuevo León caras",
    "Nuevo León baratas",
    "Apodaca",
    "Guadalupe",
    "Monterrey",
    "Monterrey nuevas"
    "San pedro",
    "Santa catarina",
    "San nicolás",
    "García",
    "Santiago",
    "General escobedo",
    "Juarez",
    "Cadereyta jimenez",
    "Pesqueria"]

checkMyIP() #Sanity Check
#totalPages = 100
houses = []
cLoop = 0
try:
    for originalLink in (pbar :=tqdm(originalLinks)):
        city = places.pop(0)
        pbar.set_description("Current city -> "+city)
        r = checkLink(originalLink)
        s = bs4.BeautifulSoup(r.text,'html.parser')
        totalPages = int(s.find('select',{'class':'js-pagination-dropdown'})['data-pagination-end']) #Obtain the actual total pages
        
        for i in (pbar2:=tqdm(range(1,totalPages+1))):
            cLoop=i
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
        #Update tsv
        headers = getHeaders()
        resultsFile = open('Data/dataUpdated.tsv','a',newline='')
        resultsFileWriter = csv.DictWriter(resultsFile, delimiter='\t', lineterminator='\n',fieldnames=["titulo","direccion","precio"]+list(headers))
        #resultsFileWriter.writeheader()
        #print(headers)
        for house in tqdm(houses):
            resultsFileWriter.writerow(house)
        resultsFile.close()
except Exception as e:
    print("Loop {}: {}".format(cLoop,e))
    print(traceback.format_exc())
    requests.post('https://api.mynotifier.app', {
    "apiKey": 'cc66dedc-04cd-42ac-b502-2efb81b98419', # Sign up for your own api key
    "message": "Error obteniendo datos", # Could be anything
    "description": "City {} Loop {} Error: {}".format(city,cLoop,e), # Optional
    "body": traceback.format_exc(), # Optional
    "type": "error", # info, error, warning or success
    "project": "" # Optional if you want to specify the project
  })
#print(*houses, sep='\n\n')

requests.post('https://api.mynotifier.app', {
    "apiKey": 'cc66dedc-04cd-42ac-b502-2efb81b98419', # Sign up for your own api key
    "message": "Success!!", # Could be anything
    "description": "Se lograron obtener todos los datos", # Optional
    "body": "", # Optional
    "type": "success", # info, error, warning or success
    "project": "" # Optional if you want to specify the project
  })
    
    

