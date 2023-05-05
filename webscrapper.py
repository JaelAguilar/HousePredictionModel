import bs4
import csv
from tqdm import tqdm

from webscrapperFunctions import checkHouse, checkLink, checkMyIP, isResponseValid,getHeaders

originalLink = 'https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/'
checkMyIP() #Sanity Check
totalPages = 1
houses = []

for i in tqdm(range(1,totalPages+1)):
    print('================================================ PAGE '+str(i)+' ================================================================')
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
            
print(*houses, sep='\n\n')

# Updating the csv
headers = getHeaders()
resultsFile = open('dataTest.tsv','w',newline='')
resultsFileWriter = csv.DictWriter(resultsFile, delimiter='\t', lineterminator='\n\n',fieldnames=headers)
resultsFile.close()

print(headers)
#for house in houses:
#    row = []
#    for header in headers:
        
    
    

