import requests
import json
from bs4 import BeautifulSoup

class LeaguePeida_Standings:
    def __init__(self):
        self.url_standings = ""
        self.standings_raw = []

    def scrape_standings(self):
    # LPL 2024 schedule URL
    # self.url = "https://lol.fandom.com/wiki/LPL/2024_Season/Spring_Season"
        try:
            response = requests.get(self.url_standings)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            # Locate the standings table
            standings_table = soup.find("table", class_="wikitable2 standings")

            # Extract standings headers
            headers = [header.text.strip() for header in standings_table.find_all('th')]

            # Extract standings rows 
            rows = standings_table.find_all("tr")

            # Extract and process the schedule data
            for row in rows[1:]:
                # row_data = [data.text.strip(), data.text.replace("\\u2060", "") for data in row.find_all('td')]
                row_data = []
                for data in row.find_all('td'):
                    data.text.strip()
                    row_data.append(data.text.replace("\u2060", ""))
                if len(row_data) == 8:
                    self.standings_raw.append(row_data)

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")

    def standings_data_output(self):
        with open(r'data\standings.txt', "w", encoding="utf-8") as file:
            for row in self.standings_raw:
                row_str = "\t".join(row) 
                file.write(row_str + "\n")
    
    def standings_data_processor(self, area="LPL"):
        with open(r'data\config\teams.json', 'r', encoding='utf-8') as file:
            mapping = json.load(file)

        if area == "LPL":
            mapping_LPL = mapping["LPL"]

        for line in self.standings_raw:
            for i in range(len(line)):
                if line[i] in mapping_LPL:
                    mapped_data = mapping_LPL[line[i]]
                    line[i] = mapped_data



    
    
