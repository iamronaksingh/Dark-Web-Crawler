import requests
import random
import string
import sys
import os

def get_tor_session():
    session = requests.session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9150'}
    return session

def torSearcher(url):
    try:
        session = get_tor_session()
        print("Getting ...", url)
        result = session.get(url).text
        filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))

        with open(f"{filename}.txt", "w+", encoding="utf-8") as newthing:
            newthing.write(result)
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to {url}. Skipping. Error: {e}")

def main():
    programname = os.path.basename(sys.argv[0])

    try:
        thelist = "sites.txt"  # Change this to the actual path of your file
        print("Opening ...", thelist)
        
        with open(thelist, "r", encoding="utf-8") as newfile:
            data = newfile.readlines()

            try:
                for k in data:
                    k = k.replace("\n", "")
                    torSearcher(k)
            except Exception as E:
                print(E)
    except:
        print(f"Usage: {programname} <newlineSeparatedList.txt>")

if __name__ == "__main__":
    main()
