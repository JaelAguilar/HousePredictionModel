import requests,bs4

# The response needs a header to pretend it is an user and not a script, else it returns 403 forbidden error
response = requests.get('https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/',headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})

# If the script can't get tthe response, shows the error in the terminal
try:
    response.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))
    
#Creating the soup with an HTML Parser
soup = bs4.BeautifulSoup(response.text,'html.parser')

#Obtains the HTML objects of eacht on of the cards on the webpage
divHouses = soup.find_all('div',{'class':'row ListingCell-row ListingCell-agent-redesign'})

# Obtain the data from all the houses
for house in divHouses:
    print(house.find('h2',{'class':'ListingCell-KeyInfo-title'}).text)

