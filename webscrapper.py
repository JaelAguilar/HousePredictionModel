import bs4

from webscrapperFunctions import checkHouse, checkLink, checkMyIP, isResponseValid

# Request the URL       
response = checkLink('https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/')
checkMyIP() #Sanity Check

if isResponseValid(response):
    #Creating the soup with an HTML Parser
    soup = bs4.BeautifulSoup(response.text,'html.parser')

    #Obtains the HTML objects of eacht on of the cards on the webpage
    divHouses = soup.find_all('div',{'class':'row ListingCell-row ListingCell-agent-redesign'})

    for house in divHouses:
        checkHouse(house)


