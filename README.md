### Overview
Scraping from netkeiba(http://www.netkeiba.com/)

### My enviroment
+ Python v3.5.3

### Preparation
+ install the package of "beautifulsoup4"

```
$ pip3 install beautifulsoup4
....
Successfully installed beautifulsoup4-4.6.0
```

### Function
<b>1. Get urls of race</b>

+ Description

```
Get urls of race from [year] to this year  
Output file name is "url_list.txt"  
The [year] is possible to set from 1975 to this year
```

+ usage(example)

```
$ python html_scraping.py 2017[year]
```

<b>2. Get result of race</b>

+ Description

```
Get result of race from urls of "url_list.txt"
The "url_list.txt" is output file of Function.1

The output files are named from urls
They are made to "output" directory

ex.
url : http://db.netkeiba.com/race/201806010101/
output file : output/201806010101.csv
```

+ usage

```
$ python result_scraping.py
```