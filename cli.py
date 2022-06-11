from crawler import *
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from prettytable import PrettyTable
import sys

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0"}
def main():
    parser = argparse.ArgumentParser(prog="Crawler", description="Crawl a website and get all links")
    parser.add_argument('--url', '-u', dest="url", type=str, required=True, help="This is the URL you want to crawl")
    parser.add_argument('--export', dest="export", type=argparse.FileType('w', encoding='UTF-8'), required=False, help="Export output to a file, give it a file name")
    parser.add_argument('--404', dest="error_404", action='store_true', help="Return links with 404 error")
    parser.add_argument('--external-url', action='store_true', dest="ext_url", required=False, help="Return links with external domain name")
    parser.add_argument('--protected-url', action='store_true', dest="pro_url", required=False, help="Return links with login page")
    # url = "https://cnpp.com"
    args = parser.parse_args()
    url = args.url
    if url.endswith('/'):
        url = url[:-1]

    r = requests.get(url, headers=headers)
    domain = urlparse(url).netloc
    soup = BeautifulSoup(r.content,'lxml')
    links = soup.find_all('a', href=True)
       
    lsd= links_in_same_domain(url, links)
    led= links_external_domain(domain, links=links)
    unq = unique_links(lsd, led)

    columns = ["Unique", "Same domain", "External domain", "Forms", "Protected", "404 error"]

    my_table = PrettyTable()
    
    if args.ext_url:
        my_table.add_column(columns[2], led)
        print(my_table)

    elif args.export:
        print("Please wait, this may take few minutes..", file=sys.stdout)
        print("Crawling links with forms...", file=sys.stdout)
        frm = links_with_form(unq)
        print("Crawling protected links...", file=sys.stdout)
        pro = links_protected(unq)
        print("Crawling links with 404 error...", file=sys.stdout)
        err = links_with_404error(unq)
        print("Finished..", file=sys.stdout)
        column_pad(unq, lsd, led, frm, pro, err)
        my_table.add_column(columns[0], unq)
        my_table.add_column(columns[1], lsd)
        my_table.add_column(columns[2], led)
        my_table.add_column(columns[3], frm)
        my_table.add_column(columns[4], pro)
        my_table.add_column(columns[5], err)
        print(my_table, file=args.export)

    elif args.pro_url:
        print("Crawling protected links...", file=sys.stdout)
        pro = links_protected(unq)
        my_table.add_column(columns[4], pro)
        print(my_table)

    elif args.error_404:

        print("Crawling links with 404 error...", file=sys.stdout)
        err = links_with_404error(unq)
        my_table.add_column(columns[5], err)
        print(my_table)

    elif not args.ext_url and not args.pro_url and not args.export and not args.error_404:
        
        print("Please wait, this may take few minutes..", file=sys.stdout)
        print("Crawling links with forms...", file=sys.stdout)
        frm = links_with_form(unq)
        print("Crawling protected links...", file=sys.stdout)
        pro = links_protected(unq)
        print("Crawling links with 404 error...", file=sys.stdout)
        err = links_with_404error(unq)
        print("Finished..", file=sys.stdout)
        column_pad(unq, lsd, led, frm, pro, err)
        my_table.add_column(columns[0], unq)
        my_table.add_column(columns[1], lsd)
        my_table.add_column(columns[2], led)
        my_table.add_column(columns[3], frm)
        my_table.add_column(columns[4], pro)
        my_table.add_column(columns[5], err)
        print(my_table)
   
    
    

main()