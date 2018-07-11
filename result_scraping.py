### import
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import os

### define
sleeptime = 5    # sleep time[s]

### public
current_dir = os.getcwd()
output_dir = ""

### def: print description of this file
def description():
    u"""
    Description:
    Get result of race from urls of "url_list.txt"
    The "url_list.txt" is output file of Function.1

    The output files are named from urls
    They are made to "output" directory

    ex.
    url : http://db.netkeiba.com/race/201806010101/
    output file : output/201806010101.csv

    usage:
    $ python result_scraping.py
    """
### end of def

### def: scraping of race data
### arg1(urls): url of race
def scraping_racedata(urls):
    print("scraping of " + urls.strip("\n"))

    ## check urls
    try:
        html = urllib.request.urlopen(urls)
    except urllib.error.URLError:
        print("Skip!! url does not expect")
        return -1
    
    ## storage to csv file
    output_file = urls.split("/")

    ## check exist of file
    if os.path.isfile(output_dir + "/" + output_file[-2] + ".csv"):
        print("Skip!! Already exist the result file")
        return -1
    
    fp = open(output_dir + "/" + output_file[-2] + ".csv","w")
    fp_writer = csv.writer(fp)

    ## scraping data of urls
    soup = BeautifulSoup(html,"html.parser")
    
    ## get area data
    ## ex. 東京
    area_tmp = soup.find("div",class_="race_head_inner")
    area_tmp = area_tmp.find("a",class_="active")
    area_tmp = area_tmp.get_text().strip("\xa0")

    ## get condition/race number data
    ## ex. condition ダ右1800m / 天候 : 晴 / ダート : 良 / 発走 : 13:10
    ## ex. race number 7R
    cond_race_tmp = soup.find("dl",class_="racedata fc")
    cond_tmp = cond_race_tmp.find("span")
    cond_tmp = cond_tmp.get_text().replace("\xa0","").split("/")

    ## exclude race of "障害"
    if ("障" in cond_tmp[0]) == True:
        print("Skip!! exclude race of 障害")
        return -1
        
    race_tmp = cond_race_tmp.find("dt")
    race_tmp = race_tmp.get_text().strip()

    ## get result of race
    result_data = soup.find("table",class_="race_table_01 nk_tb_common")
                            
    result_item = []
    result = []

    # get item of race
    for tmp in result_data.find_all("th"):
        result_item.append(tmp.get_text())
    result_item.append("会場")
    result_item.append("距離")
    result_item.append("天気")
    result_item.append("競走種別")
    result_item.append("状態")
    result_item.append("発走時間")
    result_item.append("レース")
    fp_writer.writerow(result_item)

    # get result of race
    for result_tmp in result_data.find_all("tr"):
        for tmp in result_tmp.find_all("td"):
            result.append(tmp.get_text().strip().replace("\n",""))
        if len(result) != 0:
            result.append(area_tmp)
            dist_tmp = cond_tmp[0].find("m")
            result.append(cond_tmp[0][dist_tmp-4:dist_tmp])
            result.append(cond_tmp[1][-1:])
            result.append(cond_tmp[2][:1])
            result.append(cond_tmp[2][-1:])
            result.append(cond_tmp[3][-5:])
            result.append(race_tmp)
            fp_writer.writerow(result)
        result = []

    fp.close()

    return 0
### end of def

### def: main function
### arg: none
def main():
    global output_dir
    
    ## open urls file
    fp = open(current_dir + "/url_list.txt","r")

    ## make "output" directory
    output_dir = current_dir + "/output"
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    ## Get result of race
    while True:
        url = fp.readline()
        if not url:
            break
        scraping_racedata(url)
        time.sleep(sleeptime)
    fp.close()
### end of def

### run main function
if __name__ == '__main__':
    print(description.__doc__)
    main()
