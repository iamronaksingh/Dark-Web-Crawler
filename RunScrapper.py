import requests
url = "http://ip-api.com/json/"
key = requests.get(url)

if "India" or "New Delhi" in key.text :
    print("Your VPN might not be on!!")
    safe = False
else:
    safe = True

if safe == True:
    # Changhed to true
    import ahmiascraper
    ahmiascraper.Scraper()
else:
    print("IP change failed, try again later")