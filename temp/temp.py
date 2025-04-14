import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_assets_from_10k(cik: str, user: str, email: str):
    # Get metadata
    metadata_url = f"https://data.sec.gov/submissions/CIK{cik.zfill(10)}.json"
    headers = {"User-Agent": f"{user} ({email})"}
    response = requests.get(metadata_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Metadata fetch failed: {response.status_code}")

    data = response.json()
    filings = pd.DataFrame(data["filings"]["recent"])
    filings["filingDate"] = pd.to_datetime(filings["filingDate"])

    # Get the most recent 10-K
    ten_k = filings[filings["form"] == "10-K"].sort_values("filingDate", ascending=False).iloc[0]
    accession_number = ten_k["accessionNumber"].replace("-", "")
    primary_doc = ten_k["primaryDocument"]

    filing_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession_number}/{primary_doc}"
    print(f"Fetching filing from: {filing_url}")

    filing_response = requests.get(filing_url, headers=headers)
    if filing_response.status_code != 200:
        raise Exception(f"Filing download failed: {filing_response.status_code}")

    soup = BeautifulSoup(filing_response.content, "html.parser")

    # Find all tables after a title mentioning "balance sheet"
    balance_sheet_header = soup.find(string=lambda s: s and "balance sheet" in s.lower())
    if not balance_sheet_header:
        raise Exception("Could not locate a balance sheet section in the document.")

    # Look for multiple tables after header
    tables = []
    current = balance_sheet_header
    while current and len(tables) < 3:  # avoid looping too much
        current = current.find_next()
        if current.name == "table":
            tables.append(current)

    if not tables:
        raise Exception("No tables found following balance sheet section.")

    # Parse the first table with usable format
    for table in tables:
        rows = table.find_all("tr")
        header_cells = rows[0].find_all(["th", "td"])
        columns = [cell.get_text(strip=True) for cell in header_cells]
        expected_col_count = len(columns)

        data = []
        for row in rows[1:]:
            cells = row.find_all("td")
            if len(cells) == expected_col_count:
                row_data = [cell.get_text(strip=True) for cell in cells]
                data.append(row_data)

        if data:
            df = pd.DataFrame(data, columns=columns)
            break
    else:
        raise Exception("Could not find a properly structured table.")

    # Filter rows that look like assets
    asset_rows = df[df.apply(lambda row: any("asset" in str(cell).lower() for cell in row), axis=1)]

    print("Matched rows with 'assets':\n")
    print(asset_rows)
    return asset_rows

if __name__ == "__main__":
    df_assets = fetch_assets_from_10k("0000320193", "Ethan", "eswagstaff@outlook.com")
    print("Done.")