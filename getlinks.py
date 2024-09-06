from bs4 import BeautifulSoup, SoupStrainer
import requests

class Scraper:
    def CourseCatalog(self):
        firstpage = "https://catalog.kennesaw.edu/content.php?catoid=72&catoid=72&navoid=6895&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D="
        part2 = "#acalog_template_course_filter"
        links = []
        for i in range(1,32):
            links.append(firstpage + str(i) + part2)
        rows_full = []
        output = []
        for link in links:
            data = requests.get(link).text
            soup = BeautifulSoup(data, 'html.parser')
            tables = soup.find_all('table')
            for table in tables:
                output.append(table.text)

        for o in output:
            print(o)

    # only for undergrad
    def majorRequirements(self):
        basepage = "https://www.kennesaw.edu/degrees-programs/bachelor-degrees/index.php" 
        page = requests.get(basepage).text
        majors = []
        for link in BeautifulSoup(page, 'html.parser', parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                if "degrees-programs" in link['href'] and not "assistive" in link['href'] and not "omniupdate" in link['href']:
                    majors.append(link['href'])

        # first link is weird
        majors = majors[1:]
        major_requirements_links = []
        
        for major in majors:
            page = requests.get(major).text
            for link in BeautifulSoup(page, 'html.parser', parse_only=SoupStrainer('a')):
                if link.has_attr('href'):
                    if "preview_program" in link['href']: 
                        major_requirements_links.append(link['href'])         
                        break
        print(major_requirements_links)
         
        # this is much faster...
        for link in major_requirements_links:
            page = requests.get(link).text
            soup = BeautifulSoup(page, 'html.parser')
            # tables = soup.find_all('table')
            table = soup.find('table', class_='block_content')
            print(table.text)

s = Scraper
Scraper.majorRequirements(s)
