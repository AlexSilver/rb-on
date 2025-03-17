import os
import requests
from bs4 import BeautifulSoup
import tabulate

from score_row import ScoreRow

TMP_FILE_PATH = "cache.html"
URL = "https://www.sport5.co.il/liga.aspx?FolderID=44"

def fetch_data(with_cache = True):
    ## for dev purpose caching the data in local disk
    ## remove in production
    if with_cache and os.path.exists(TMP_FILE_PATH):
        with open(TMP_FILE_PATH, "r", encoding="utf-8") as file:
            return file.read()

    try:
        response = requests.get(URL)
        response.raise_for_status()
        content = response.text

        if with_cache:
            with open(TMP_FILE_PATH, "w", encoding="utf-8") as file:
                file.write(content)

        return content
    except:
        print("Error fetching " + URL)
        return None

def extract_score_table(content):
    soup = BeautifulSoup(content, "html.parser")

    league_table = None

    for table in soup.find_all("table"):
        headers = [th.text.strip() for th in table.find_all("th")]
        if "קבוצה" in headers and "נק’" in headers:
            league_table = table
            break

    if not league_table:
        print("Error: No appropriate table found")
        return None

    result = []
    rows = league_table.find_all("tr")[1:]

    for row in rows:
        cols = row.find_all("td")

        if len(cols) < 9:
            continue

        team = ScoreRow(
            position=cols[0].text.strip(),
            team=cols[1].text.strip(),
            matches_played=cols[2].text.strip(),
            wins=cols[3].text.strip(),
            draws=cols[4].text.strip(),
            losses=cols[5].text.strip(),
            goals=cols[6].text.strip(),
            diff=cols[7].text.strip(),
            points=cols[8].text.strip()
        )

        result.append(team)

    return result

def print_table(teams):
    headers = ["Position", "Team", "Matches", "Wins", "Draws", "Losses", "Goal Diff", "Diff", "Points"]
    data = [team.as_row() for team in teams]
    print(tabulate.tabulate(data, headers=headers, tablefmt="pretty"))

if __name__ == "__main__":
    content = fetch_data()
    teams = extract_score_table(content)
    print_table(teams)