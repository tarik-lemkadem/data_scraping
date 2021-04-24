from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import json
from scraping.models import Job

from tabula import read_pdf
from tabulate import tabulate
  
import camelot

class Command(BaseCommand):
    help = "extract table"
    # define  command
    def handle(self, *args, **options):
        #reads table from pdf file
        #file = "files\\foo.pdf"
        file = "files\CDM_RFS.pdf"
        table_areas = None
        tables = camelot.read_pdf(file,pages='all',
                                flavor='stream',
                                row_tol=8,table_areas=table_areas,
                                split_text=False,
                                layout_kwargs={'char_margin':2.0,
                                            'line_margin':1,#0.5,
                                            'word_margin':0.1,
                                            #'line_overlap':0.5,
                                            #'boxes_flow':0.5,
                                            'detect_vertical':False,
                                            'all_texts':False})
        print("Total tables extracted:", tables.n)
        if tables.n >0 :
            print(tables[0].df)
            tables[0].parsing_report
        # or export all in a zip
        #tables.export("tables\\tables2.csv", f="csv", compress=True)
        #for t in tables:
        #    t.df.dropna(inplace=True)
        
        #tables.export("tables\\tab.csv", f="csv", compress=False)
        tables.export("tables\\txt\\tab.txt", f="csv", compress=False)
        camelot.plot(tables[0], kind='text').show()
        #camelot.plot(tables[0], kind='grid').show()
        '''

        
        reader = PyPDF2.PdfFileReader('files\CDM_RFS.pdf')

        print(reader.documentInfo)

        num_of_pages = reader.numPages
        print('Number of pages: ' + str(num_of_pages))

            try:
            # save in db
                #Job.objects.update_or_create(
            
                Job.objects.create(
                    date =  tds[0].text,
                    taux = tds[1].text,
                    volume = tds[2].text,
                    encours = tds[3].text
                    )
                
                print('data added' )
            except:
                print('data already exists' )
        
        #header = soup.find_all("th").text
        #header = soup.find("thead").text#[4]
        #data = soup.find_all("td").text
        #data = soup.find("tbody").text
        #data = str(data)
        #data.replace('\n ',' ')
        #header = str(header)
        #header.replace('\n',' ')
        #data.replace("<tbody>"," ")
        
        
        with open(f"./table.txt", 'w') as f:
            f.write(str(header))
            f.write(str(data))
        for p in header:
            data = p.find('th')#.text
        for p in data:
            #url = p.find('a', class_='posting-btn-submit')['href']
            #url = p.find('td').text
            title = p.find('td')#.text
            #location = p.find('span', class_='sort-by-location').text
            # check if url in db
            try:
                # save in db
                Job.objects.create(
                    data=data,
                    title=title,
                    #location=location
                )
                print('%s added' % (title,))
            except:
                print('%s already exists' % (title,))
        
        df = pd.DataFrame(data,columns=columns)
        df.to_csv("./table.csv")
        '''
        #self.stdout.write( 'job complete' )

