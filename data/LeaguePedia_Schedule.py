import requests
from bs4 import BeautifulSoup
# from datetime import datetime

class LeaguePedia_Schedule:
    def __init__(self):
        self.url_schedule = ""
        self.schedule_raw = []

    def scape_schedule(self):
        try:
            response = requests.get(self.url_schedule)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            # Locate all shcedule table
            schedule_raw = soup.find("div", class_ = "ml-normal-pred-and-results")

            rows = schedule_raw.find_all("tr")
            for row in rows[1:]:
                # row_data = [data.text.strip() for data in row.find_all('td')]
                row_data = []
                for data in row.find_all('td'):
                    data.text.strip()
                    row_data.append(data.text.replace("\u2060", ""))
                if len(row_data) == 3:
                    self.schedule_raw.append(row_data)

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
    
    def schedule_data_output(self):
        with open(r'data\schedule.txt', "w", encoding="utf-8") as file:
            for row in self.schedule_raw:
                row_str = "\t|".join(row) 
                file.write(row_str + "\n")

def scape_LPL_schedule():
    LPL = LeaguePedia_Schedule("https://lol.fandom.com/wiki/LPL/2024_Season/Spring_Season", r'data\shcedule.txt')
    LPL.scape_schedule()

