from autoscraper import AutoScraper
import subprocess
import webbrowser
from googlesearch import *


url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en'
searchlist=[]
wanted_list = ['Max Hospital retracts earlier statement of not taking new patient admissions in Delhi-NCR']
scraper= AutoScraper()
result = scraper.build(url, wanted_list)
click=int(input("Enter your choice\n"))
chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
print("1. Start your day with what you want to do?\n2. open youtube\n3. Open google calender")
if click == 1:
    query=input("So what should I search Today? \n")
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        webbrowser.open("https://google.com/search?q=%s" % query)
elif click==2:
    webbrowser.open("https://youtube.com/")
elif click == 3:
    webbrowser.open("https://calendar.google.com/calendar?tab=rc&authuser=0")
else:
    print("i have error")