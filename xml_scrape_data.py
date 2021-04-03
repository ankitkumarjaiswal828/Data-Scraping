import os, pandas as pd
import xml.etree.ElementTree as ET
file = '/home/astirmind/Documents/Ankit_DS/Beautifulsoup/rss.xml'

path = os.path.abspath(os.path.join('data', file))
parse = ET.parse(path)

cols = ["title",  "link", "description", "guid", "pubDate", "url"]
rows = []
channel = parse.findall('channel')

for c in channel:
    title = c.find("title").text
    link = c.find("link").text
    rows.append({"title": title,"link": link})
item = parse.findall('channel/item')

for i in item:
    guid = i.find("guid").text
    pubDate = i.find("pubDate").text
    desc = i.find("description").text
    link = i.find("link").text
    rows.append({"guid": guid,"pubDate": pubDate,"description": desc,"url": link})

df = pd.DataFrame(rows, columns=cols)
df.to_csv('xml_scrape_data.csv')



