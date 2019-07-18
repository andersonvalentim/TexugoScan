import whois
import tldextract
import socket
import json
from ipwhois import IPWhois
from pprint import pprint
result={}
def WhoisCollect(URL):

    domainURL = AdequacyURL(URL)
    print(domainURL)
    try:
        IP=socket.gethostbyname(domainURL)
        obj = IPWhois(IP)
        results = obj.lookup_whois()
        result=results['nets']
        return(result)
    except socket.error as e :
        return "None"
    

     

def AdequacyURL(URL):
    domainDetected = tldextract.extract(URL)
    URLFormated = ".".join(domainDetected[:3])
    if URLFormated[0]==".":

                newUrl= list(URLFormated)
                newUrl[0]=""
                URLFormated=''.join(newUrl)
                return (URLFormated)
    else:
                return (URLFormated.replace("www.",""))

