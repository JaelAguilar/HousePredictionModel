import requests
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
    
def checkLink(houseLink):
    response = requests.get(houseLink,headers=header)
    return response
    
def checkMyIP():
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip)) 
       