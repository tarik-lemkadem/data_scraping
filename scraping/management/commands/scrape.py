from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import json
from scraping.models import Job




class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command
    def handle(self, *args, **options):
        # collect html
        urls = 'https://www.bkam.ma/Marches/Principaux-indicateurs/Marche-monetaire/Marche-monetaire-interbancaire/'
        dfs = pd.read_html(urls)
        #html = urlopen('https://jobs.lever.co/opencare')
        html = urlopen(urls)
        # convert to soup
        soup = BeautifulSoup(html, 'html.parser')
        # grab all postings
        #postings = soup.find_all("div", class_="block-table")
        columns=[ 'Date','Taux Moyen Pondéré','Volume JJ','Encours']
        
        #header = soup.find_all("th")#.text
        header = soup.find("thead").text
        #data = soup.find_all("td")#.text
        data = soup.find("tbody").text
        data = str(data)
        data.replace("\n"," ")
        header = str(header)
        header.replace("\n"," ")
        #data.replace("<tbody>"," ")
        with open(f"./table.txt", 'w') as f:
            f.write(str(header))
            f.write(str(data))
        '''
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
        '''
        try:
            # save in db
            Job.objects.create(
                data=data,
                header=header,
                #location=location
            )
            print('%s added' % (header,))
        except:
            print('%s already exists' % (header,))
        self.stdout.write( 'job complete' )


