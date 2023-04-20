import requests,bs4

from webscrapperFunctions import checkLink, checkMyURL, isResponseValid

# Request the URL       
response = checkLink('https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/')
checkMyURL()

if isResponseValid(response):
    #Creating the soup with an HTML Parser
    soup = bs4.BeautifulSoup(response.text,'html.parser')

    #Obtains the HTML objects of eacht on of the cards on the webpage
    divHouses = soup.find_all('div',{'class':'row ListingCell-row ListingCell-agent-redesign'})

    # Obtain the data from all the houses
    # TODO: Recámaras
    # TODO: Estacionamientos
    # TODO: Baños
    # TODO: Construidos (m2)
    # TODO: Terreno (m2)
    # TODO: Amueblado (yes,no)
    # TODO: Precio
    # TODO: Short description
    # TODO: Condiciones de precio
    # TODO: Calificación del vecindario
    # TODO: Amenidades

    for house in divHouses:
        # For every data, obtain the text and remove the surrounding whitespace
        title = house.find('h2',{'class':'ListingCell-KeyInfo-title'}).text.strip()
        address = house.find('span', {'class':'ListingCell-KeyInfo-address-text'}).text.strip()
        link = house.find('a',{'class':'js-listing-link'})['href']
    
        print('='*40)
        print(title)
        print(address)
        print(link)


