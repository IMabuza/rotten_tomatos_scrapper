from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

s_url = "https://www.rottentomatoes.com/"
#request the page, read it and close connection

uClient = uReq(s_url)

p_html = uClient.read()

uClient.close()


#html parser
page_soup = soup(p_html, "html.parser")

print(page_soup.table)
