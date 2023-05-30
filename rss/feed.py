__doc__ = """
Hier werden die RSS Feeds eingelesen und verarbeitet.
"""

# Importe
from xml.etree import ElementTree as ET
from urllib3 import PoolManager

def read_rss_feed(rss_url):
    """
    Lese einen RSS Feed ein.
    """
    if rss_url is None:
        return KeyError("RSS_URL is not set")
    http = PoolManager()
    response = http.request('GET', rss_url)
    return response.data

def parse_rss_feed(rss_feed):
    """
    Verarbeite einen RSS Feed und gebe die einzelnen Einträge zurück.
    """
    root = ET.fromstring(rss_feed)
    items = root.findall('./channel/item')
    entries = []
    for i in range(len(items)-1, -1, -1):
        item = items[i]
        # Create an Index for the entry
        index = len(items) - i - 1
        # Get the title, link and pubDate
        title_elem = item.find('title')
        title = title_elem.text if title_elem is not None else ''
        link_elem = item.find('link')
        link = link_elem.text if link_elem is not None else ''
        pub_date_elem = item.find('pubDate')
        pub_date = pub_date_elem.text if pub_date_elem is not None else ''
        entry = {"Index": str(index), "Title": title, "Link": link, "PubDate": pub_date}
        entries.append(entry)
    return entries
        