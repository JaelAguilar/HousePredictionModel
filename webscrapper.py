import requests,bs4

# The response needs a header to pretend it is an user and not a script, else it returns 403 forbidden error
header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

def isResponseValid(response):
    """If the script can't get tthe response, shows the error in the terminal

    Args:
        response (Response): Response of a request
        
    Returns:
        isValid (boolean): There was not a problem in the request
    """    
    try:
        response.raise_for_status()
        return True
    except Exception as exc:
        print("There was a problem: %s" % (exc))
        return False
    
def checkHouseLink(houseLink):
    response = requests.get(houseLink,headers=header)
    
def checkMyURL():
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip)) 
       
# Request the URL       
response = requests.get('https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/',headers=header)
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


