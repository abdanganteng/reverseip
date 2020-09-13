import requests
import json
import sys
import time,os
import glob
from time import gmtime, strftime
from pyfiglet import Figlet		
custom_fig = Figlet(font='standard')
def progressbar(it, prefix = "", size = 1000):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "_"*(size-x), _i, count))
        sys.stdout.flush()
    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()
toolbar_width = 30

sys.stdout.write(":%s:" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))
for i in xrange(toolbar_width):
    time.sleep(0.01)

    sys.stdout.write("*")
    sys.stdout.flush()
t = strftime("%H:%M:%S", gmtime())
lists = sys.argv[1]


for i in xrange(toolbar_width):
    time.sleep(0.01)
os.system('cls' if os.name == 'nt' else 'clear')

for site in open(lists, 'r').read().splitlines():
    try:
        if "http" in site:
            site = site.split("/")[2]
        else:
            site = site
        req = requests.get("https://api.viewdns.info/reverseip/?host=" + site + "&apikey=2043639deedcd1d803470e0ef17b0e99d7ef6430&output=json", headers={"User-Agent": "Mozilla"})
        coeg = json.loads(req.text)
        for lookup in coeg["response"]["domains"]:
            print(lookup["name"])
            f = open("remah.txt", 'a+')
            f.write(lookup["name"] + '\n')
            f.close()
	

    except Exception as e:
        print(str(e))

print "["+t+"]"+" Done Save Remah.txt "
def main():
    print(custom_fig.renderText('  M3sicth'))
    print("=============================================")
    print(" Reverse IP By M3 ")
    print(" Big Thanks -> Con7ext - Kyu_Kazami    ")
    print("=============================================\n")    
main()
