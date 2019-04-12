from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

s_url = "https://www.rottentomatoes.com/"
#request the page, read it and close connection

uClient = uReq(s_url)

p_html = uClient.read()

uClient.close()


#html parser
page_soup = soup(p_html, "html.parser")

#grab the left column data

div_listings = page_soup.findAll("div", {"class":"listings"})

moviesOfTheWeek = div_listings[0]

left_col = moviesOfTheWeek.table.findAll("td", {"class": "left_col"})

middle_col = moviesOfTheWeek.table.findAll("td", {"class": "middle_col"})





#Loop throught data

percentage_list = []
title_list = []

for items in left_col:
    try:
        Percentage = items.findAll("span",{"class":"tMeterScore"})
        moviePercentage = Percentage[0].text
        moviePercentage = moviePercentage.replace("%","")
        percentage_list.append(int(moviePercentage))

    except:
        percentage_list.append(0)

for items in middle_col:
    title = items.a.text
    title_list.append(title)

#create df

data = {"Movies": title_list, "Percentage": percentage_list}

df = pd.DataFrame.from_dict(data)

df.to_csv("moviesOpeningThisWeek.csv")

print("wrote to CSV")

print(percentage_list,title_list)


#get box office rating

boxOffice = div_listings[1]

left_col = boxOffice.table.findAll("td", {"class": "left_col"})
middle_col = boxOffice.table.findAll("td", {"class": "middle_col"})
right_col = boxOffice.table.findAll("td", {"class": "right_col"})

percentage_list = []
title_list = []
gross_list = []

for items in left_col:
    try:
        Percentage = items.findAll("span",{"class":"tMeterScore"})
        moviePercentage = Percentage[0].text
        moviePercentage = moviePercentage.replace("%","")
        percentage_list.append(int(moviePercentage))

    except:
        percentage_list.append(0)

for items in middle_col:
    title = items.a.text
    title_list.append(title)

for items in right_col:
    gross = items.a.text
    gross = gross.replace("M","")
    gross = gross.replace("$","")
    gross_list.append(gross)

data = {"Movies": title_list, "Percentage": percentage_list, "Gross": gross_list}

df = pd.DataFrame.from_dict(data)

df.to_csv("boxoffice.csv")

print("wrote to box Office CSV")

print(percentage_list,title_list, gross_list)





