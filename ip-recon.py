import subprocess
import json
import pyfiglet
import requests
import argparse
import time

subprocess.call('clear', shell=True)
time.sleep(1)

class bcolors:
	r = "\033[1;31;40m"
	g = "\033[1;32;40m"
	b = "\033[1;34;40m"
	white =  "\033[1;37;40m"
	purple = "\033[1;35;40m"

ascii_banner = pyfiglet.figlet_format("ip_recon")



print(bcolors.g + ascii_banner)
print(bcolors.g + "           coded by zer0day")

parser=argparse.ArgumentParser()

parser.add_argument("-i","--ipaddress",help="IP address to track")
args=parser.parse_args()
ip=args.ipaddress
   
url="http://ip-api.com/json/"+str(ip)
response=requests.get(url)
data = json.loads(response.content)
print(bcolors.white)
print("Ip recon at: ", ip)
print("[$] IP:     ",data["query"])
print("[$] LOC:    ",data["country"])
print("[$] CITY:   ",data["city"])
print("[$] REG:    ",data["regionName"])
print("[$] ZIP:    ",data["zip"])
print("[$] LON:    ",data["lon"])
print("[$] TIME:   ",data["timezone"])
print("\n\n")

