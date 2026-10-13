

try:
      import pyfiglet
      import requests
      from rich import print
      import cloudscraper
      from bs4 import BeautifulSoup as bs
      import socket
      import time
      import sys
        


#install missing libraries


except Exception:
      print('some required libraries are missing. would you like to install them now? (y/n)')
      Q = input('').strip().lower()
    
      if Q == 'y':
          try:
                      try:
                            import os
                            os.system('pip install requests rich cloudscraper beautifulsoup4 pyfiglet')
                      except Exception:
                            print('error.')
                    
          except Exception:
              import os
              os.system('python -m pip install requests rich cloudscraper beautifulsoup4 pyfiglet')
      elif Q == 'n':
          print('ok')
          exit()
    
      else:
          print('Syntax Error.')


#welcome message
welcome = 'welcome to info grabber V1.4, made by A>MyneX Dev'
for wel in welcome:
    print('[purple]' + wel, end='', flush=True)
    time.sleep(0.05)
time.sleep(1.5)
for wel in range(len(welcome)):
      sys.stdout.write('\b \b')
      sys.stdout.flush()
      time.sleep(0.02)

#logo
print(pyfiglet.figlet_format('Info Grabber', font='slant'))
cloud = cloudscraper.create_scraper()


#get url
print('[purple]enter your URL: ')
url = input('')

#url filtering
if ' ' in url:
      print('[yellow]bro, dont write spaces.')
      url = url.replace(' ', '')
if not url.startswith(('http://', 'https://')):
      url = 'http://' + url



try:

      #get data for url

      qrl = cloud.get(url)
      soup = bs(qrl.text, 'html.parser')
      print(f'[purple]Title :[u #4B0082] {soup.title.text}')
      print(f'[purple]status :[u #4B0082] {qrl.status_code}')
      print(f'[purple]server :[u #4B0082] {qrl.headers.get('Server', '[yellow]not found')}')
      print(f'[purple]server speed :[u #4B0082] {qrl.elapsed.total_seconds()}')
      print(f'[purple]latest update :[u #4B0082] {qrl.headers.get('Last-Modified', '[yellow]not found')}')
      print(f'[purple]file type :[u #4B0082] {qrl.headers.get('Content-Type', '[yellow]not found')}')

      if not url.endswith('/'):
            url = url + '/robots.txt'
            qrl2 = cloud.get(url)
            if qrl2.status_code > 299:
                  print('[purple]robots.txt :[u #4B0082] False')
            if qrl2.status_code < 300:
                  print('[purple]robots.txt :[u #4B0082] True')
      elif url.endswith('/'):
            url = url + 'robots.txt'
            qrl2 = cloud.get(url)
            if qrl2.status_code > 299:
                  print('[purple]robots.txt :[u #4B0082] False')
            if qrl2.status_code < 300:
                  print('[purple]robots.txt :[u #4B0082] True')
      else:
            print('[red]error')
      url = url.replace('http://', '').replace('https://', '')
      url = url.split('/')[0]
      print(f'[purple]IP :[u #4B0082] {socket.gethostbyname(url)}' + '  [#1e1e1e](The IP  might belong to the server, not website itself)')
except Exception as e:
      print(f'[bold red]error : {e}')