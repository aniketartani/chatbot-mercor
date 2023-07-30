import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.moneycontrol.com/stocks/marketstats/sector-scan/bse/today.html"

# Send a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the span elements with the specified class names
name_spans = soup.find_all("span", class_=["SubSectorWeb_w120__1ezEW"])

# Extract the names from the spans and store them in a list
names_list = [span.text.strip() for span in name_spans]

name_spans_per = soup.find_all("td", class_=["SubSectorWeb_grn__13lsS","SubSectorWeb_rd__1lg1i"])

# Extract the names from the spans and store them in a list
names_lis_per = [span.text.strip() for span in name_spans_per]


# Print the list of names
print(names_list)

print(names_lis_per)

data = list(zip(names_list, names_lis_per))

# Specify the file path for the CSV file
csv_file_path = "output_data.csv"

# Write the data to the CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(["Name", "Percentage"])

    # Write the data rows
    csv_writer.writerows(data)