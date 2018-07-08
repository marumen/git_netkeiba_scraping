### import
import urllib.request
from bs4 import BeautifulSoup
import sys
import time
from datetime import datetime

### define
sleeptime = 5    # sleep time[s]
###

### def: print description of this file
def description():
    u"""
    Description:
    Get urls of race from [year]* to this year
    Output file name is "url_list.txt"
    * The [year] is possible to set from 1975 to this year

    usage(example):
    # python html_scraping.py 2017[year]
    """
### end of def

### def: get urls of race
### arg1(urls): base url
def get_url_list(urls):
    html = urllib.request.urlopen(urls)
    soup = BeautifulSoup(html,"html.parser")
    #print(soup)
    
    ## get race date
    race_date_list = []
    date = soup.find("div",class_="race_calendar")
    for tmp in date.find_all("td"):
        tmp = tmp.find("a")
        if tmp is not None:
            race_date_list.append("http://db.netkeiba.com" + tmp.get("href"))
    #print(race_date)

    ## file open for storaging to text file
    fp = open("url_list.txt","a")

    ## get urls of race and output it to file
    for race_date_url in race_date_list:
        race_date_html = urllib.request.urlopen(race_date_url)
        date_soup = BeautifulSoup(race_date_html,"html.parser")
        #print(soup_date)
        for tmp in date_soup.find_all("dl",class_="race_top_data_info fc"):
            tmp = tmp.find("a")
            fp.write("http://db.netkeiba.com")
            fp.write(tmp.get("href"))
            fp.write("\n")

    ## file close
    fp.close()
### end of def

### def: main function
### arg: none
def main():
    ## check argment
    args = sys.argv

    year = int(args[1])
    thisyear = datetime.now().year

    ## check for exception
    if year > thisyear:
        raise Exception("year(argment) range of from 1975 to this year")

    ## output file reset
    fp = open("url_list.txt","w")
    fp.close()

    ## get urls of race
    while year <= thisyear:
        month = 1
        if year == thisyear:
            month_end = datetime.now().month
        else:
            month_end = 12
        while month <= month_end:
            print("Get urls of " + str(year) + "/" + str(month))
            get_url_list("http://db.netkeiba.com/race/list/" + str(year) + str("{0:02d}".format(month)) + "01/")
            time.sleep(sleeptime)
            month += 1
        year += 1
### end of def

### run main function
if __name__ == '__main__':
    print(description.__doc__)
    main()
    
# for debug
#urls = "http://db.netkeiba.com/race/list/20170301/"
#get_url_list(urls)
#urls = "http://db.netkeiba.com/race/list/20180301/"
#get_url_list(urls)
# debug end
