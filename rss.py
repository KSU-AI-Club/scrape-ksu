# title gives every event title
# link gives a link to owl life
# <description> is formatted in html, so that will need further parsing... I bet the tags could just be stripped out of it and new lines removed.
# then <start xmlns="events"> is the event date, this can be parsed into a datetime format or just left as is
# then <end xmlns="events"> is the end date

import xml.etree.ElementTree as ET

class RSSparser:
    class event:
        title = ""
        description = ""
        startDate = "" # could be some kind of datetime?
        endDate = ""
        link = ""

        # make SURE we pass an empty string as a method param if there's something missing
        def __init__(self, params):
            title = params[0]
            description = params[1]
            startDate = params[2] # could be some kind of datetime?
            endDate = params[3]
            link = params[4]

    # we will store them all in here
    events = []
#    def __init__(self):
         

    def scrape(self):
        tree = ET.parse("./events.rss")
        parser = ET.XMLPullParser(['start', 'end'])
        parser.feed('<mytag>sometext')
        list(parser.read_events())
        root = tree.getroot()
        for neighbor in root.iter('item'):
            print(neighbor.find('title').text)
        
r = RSSparser()
r.scrape()
