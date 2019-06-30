import whois
import tldextract
import socket
from ipwhois import IPWhois
from pprint import pprint
def WhoisCollect(URL):

    domainURL = AdequacyURL(URL)
    print(domainURL)
    IP=socket.gethostbyname(domainURL)
    obj = IPWhois(IP)
    results = obj.lookup_rdap(depth=1)
    pprint(results)
    

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

