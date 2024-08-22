#!/usr/bin/python
try:
    import requests, re, validators, os, time
    from bs4 import BeautifulSoup
    from alive_progress import alive_bar
except ModuleNotFoundError:
    os.system("pip install requests validators bs4 alive-progress")

curl = requests.Session()
curl.trust_env = False
print("""

    search domain by name

""")
keyword = input("list keyword : ")
print("[💕] Please wait...")

with open("keydomain.txt", "a+") as output_file:
    with open(keyword, "r") as list_file:
        for line in list_file:
            word = line.strip()
            sites = "https://crt.sh/"
            source = curl.get(f"{sites}?q={word}").content
            html = re.sub("<BR>", "\n", source.decode('UTF-8'))

            pocket = set()
            counter = 0
            for site in BeautifulSoup(html, "html.parser").find_all("td"):
                if validators.domain(site.text):
                    if site.text not in pocket:
                        counter += 1
                        pocket.add(site.text)
                        output_file.write(re.sub("$", "\n", site.text))

            result = [counter]
            print(f"[❗] Found: {result} domain")
            for x in result:
                with alive_bar(x) as bar:
                    for i in range(x):
                        time.sleep(.01)
                        bar()

    print("[✅] Tersimpan di keydomain.txt")
# coded by ./meicookies
