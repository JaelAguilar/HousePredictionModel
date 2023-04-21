import bs4

from webscrapperFunctions import checkHouse, checkLink, checkMyIP, isResponseValid

originalLink = 'https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/'
checkMyIP() #Sanity Check
totalPages = 2

for i in range(1,totalPages+1):
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
            checkHouse(house)


