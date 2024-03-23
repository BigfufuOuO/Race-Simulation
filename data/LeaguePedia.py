import requests
from bs4 import BeautifulSoup

class LeaguePeida:
    def __init__(self, url, output_filename):
        self.data = []
        self.url = url
        self.filename = output_filename

    def scrape_lpl_standings(self):
    # LPL 2024 schedule URL
    # self.url = "https://lol.fandom.com/wiki/LPL/2024_Season/Spring_Season"
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            # Locate the standings table
            standings = soup.find("table", class_="wikitable2 standings")

            # Extract standings headers
            headers = [header.text.strip() for header in standings.find_all('th')]

            # Extract standings rows 
            rows = standings.find_all("tr")

            # Extract and process the schedule data
            for row in rows[1:]:
                row_data = [data.text.strip() for data in row.find_all('td')]
                self.data.append(row_data)

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")

    def data_processor(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for row in self.data:
                row_str = "\t".join(row)  # 假设数据是以制表符分隔的文本
                file.write(row_str + "\n")  # 写入数据并添加换行符

if __name__ == "__main__":
    LPL = LeaguePeida("https://lol.fandom.com/wiki/LPL/2024_Season/Spring_Season", r'data\standings.txt')
    LPL.scrape_lpl_standings()
    LPL.data_processor()
    
    
