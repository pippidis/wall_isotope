import urllib
import os
import pandas as pd


market = '.OSE'

# check that  folder exist
try: 
    os.makedirs('_historical')
except OSError:
    if not os.path.isdir('_historical'):
        raise
        
# get a list of all papers for selected market    
fullfilename = os.path.join('_historical', 'tickers.csv')
            
url = 'http://hopey.netfonds.no/kurs.php?exchange=' + market + '&sec_types=&sectors=&ticks=&table=tab&sort=alphabetic'
urllib.request.urlretrieve(url, fullfilename)
  
stockPapers = pd.read_csv("_historical/tickers.csv", encoding = 'ISO-8859-1', delimiter=r"\t+", engine='python')
stockPapers = stockPapers['paper']

#download historical file for papers
for paper in stockPapers:
        filename = paper + '_Historical.csv'
        fullfilename = os.path.join('_historical', filename)
        
        url = 'http://hopey.netfonds.no/paperhistory.php?paper=' + paper + market + '&csv_format=csv'
        urllib.request.urlretrieve(url, fullfilename)        
        print(paper)
