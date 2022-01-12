from bs4 import BeautifulSoup
import requests
from sys import argv


print(
    '''
    ███████ ██ ███    ██ ██████  ████████ ██   ██ ███████ ███    ███ 
    ██      ██ ████   ██ ██   ██    ██    ██   ██ ██      ████  ████ 
    █████   ██ ██ ██  ██ ██   ██    ██    ███████ █████   ██ ████ ██ 
    ██      ██ ██  ██ ██ ██   ██    ██    ██   ██ ██      ██  ██  ██ 
    ██      ██ ██   ████ ██████     ██    ██   ██ ███████ ██      ██
    '''
)

help_menu = '''
-h                 Display this menu
-n <name>          Name of target
-r <results>       Number of results to return
OPTIONAL
-s <site>          Site on which to search
-c <custom search> Search for a custom query NOTE: Only -r is allowed (and mandatory) when using custom query

!REMEMBER TO PUT ALL OPTIONS IN DOUBLE QUOTES!
'''

isSite = False
isCustom = False

if len(argv) == 1:
    print(help_menu)
    quit()
else:
    pass

if '-h' in argv:
    print(help_menu)
    quit()
else:
    pass


if '-s' in argv:
    site = argv[argv.index('-s') + 1]
    isSite = True
else:
    pass

if '-c' in argv:
    if len(argv) == 5:
        custom = argv[argv.index('-c') + 1]
        isCustom = True
    else:
        print(help_menu)
        quit()
else:
    pass

if '-n' in argv:
    name = argv[(argv.index('-n') + 1)]
else:
    if isCustom == False:
        print(help_menu)
        quit()
    else:
        pass


if '-r' in argv:
    results = int(argv[argv.index('-r') + 1])
else:
    print(help_menu)
    quit()


def find(isCustom, isSite):
    if isCustom == False:
        query = f'"{name}"'
        query = query.replace(' ', '+')
        if isSite == False:
            page = requests.get(
                f'https://www.google.com/search?q={query}&num={results}')
            soup = BeautifulSoup(page.text, 'html.parser')
            links = soup.findAll('a')
            for link in links:
                link_href = link.get('href')
                if 'url?q=' in link_href and not 'webcache' in link_href:
                    link_href = link_href.replace('/url?q=', ' ')
                    link_head, sep, tail = link_href.partition('&sa')
                    print(f'[HIT] ' + ' ' + link_head + '\n' +
                          '-------------------------------------------------------------------------------------------------')
        else:
            query = f'"{name}" site:"{site}"'
            query = query.replace(' ', '+')
            page = requests.get(
                f'https://www.google.com/search?q={query}&num={results}')
            soup = BeautifulSoup(page.text, 'html.parser')
            links = soup.findAll('a')
            for link in links:
                link_href = link.get('href')
                if 'url?q=' in link_href and not 'webcache' in link_href:
                    link_href = link_href.replace('/url?q=', ' ')
                    link_head, sep, tail = link_href.partition('&sa')
                    print(f'[HIT] ' + ' ' + link_head + '\n' +
                          '-------------------------------------------------------------------------------------------------')
    else:
        page = requests.get(
            f'https://www.google.com/search?q={custom}&num={results}')
        soup = BeautifulSoup(page.text, 'html.parser')
        links = soup.findAll('a')
        for link in links:
            link_href = link.get('href')
            if 'url?q=' in link_href and not 'webcache' in link_href:
                link_href = link_href.replace('/url?q=', ' ')
                link_head, sep, tail = link_href.partition('&sa')
                print(f'[HIT] ' + ' ' + link_head + '\n' +
                      '-------------------------------------------------------------------------------------------------')


# try:
find(isCustom=isCustom, isSite=isSite)
# except:
#     print('No results found')
#     quit()
