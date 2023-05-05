import bs4
import requests
# The response needs a header to pretend it is an user and not a script, else it returns 403 forbidden error
header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
csvHeader = {"titulo","direccion","precio"}

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
    
def checkLink(link):
    """Obtains the request of the link

    Args:
        link (string): URL

    Returns:
        _type_: _description_
    """    
    response = requests.get(link,headers=header)
    return response

def checkHouse(htmlHouse):
    """Returns a dictionary with all the values of the house

    Args:
        htmlHouse (PageElement): The html Element of the current house
    """    
    # Obtain the data from all the houses
    # TODO: Short description
    # TODO: Calificación del vecindario

    # For every data, obtain the text and remove the surrounding whitespace
    results = {}
    
    title = htmlHouse.find('h2',{'class':'ListingCell-KeyInfo-titulo'}).text.strip()
    print(title)
    try:
        link = htmlHouse.find('a',{'class':'js-listing-link'})['href']
        otherData=checkHouseLink(link)
        results["titulo"]=title
        results["direccion"]=htmlHouse.find('span', {'class':'ListingCell-KeyInfo-direccion-text'}).text.strip()
        results |= otherData
        results["precio"]=htmlHouse.find('span', {'class':'priceSection-Firstprice'}).text.strip()
        return results|otherData
    except Exception as ex:
        print("There was an error retrieving the data from %s: %s"%{title,ex})
        return None
    
    
def checkHouseLink(link):
    """Obtains the data of the individual page of a house

    Args:
        link (string): The link of the house

    Returns:
        dict: Dictionary with the data of every house
    """    
    global csvHeader
    response = requests.get(link,headers=header)
    results = {}
    if isResponseValid(response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        houseDetails = checkHouseDetails(soup)
        houseAmenities = [i.text for i in soup.find_all('span',{'class':'listing-amenities-name'})]
        csvHeader|=set(houseAmenities)
        #print("House Details -> ",houseDetails)
        csvHeader|=houseDetails.keys()
        #print("CSV HEADER -> ",csvHeader)
        #print(houseAmenities)
        results.update(houseDetails)
        results.update([(i,True) for i in houseAmenities])
        #print("House Extra Results -> ",results)
    return results|houseDetails
    
def checkHouseDetails(detailSoup):
    """Obtains the data of the Details section in the webpage

    Args:
        detailSoup (HTMLParse): The html of the Details section of the webpage

    Returns:
        dict: Dictionary with details and its values
    """    
    details={}
    detailsNames = detailSoup.find_all('div',{'class':'ellipsis'})
    detailsValues = detailSoup.find_all('div',{'class':'last'})
    for i in range(len(detailsNames)):
        name=detailsNames[i].text.strip()
        value = detailsValues[i].text.strip()
        details[name]=value
    #print(details)
    return details
        
def checkMyIP():
    """Shows the current IP
    """    
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    print('My public IP direccion is: {}'.format(ip)) 
       
def getHeaders():
    return csvHeader