import requests
import csv

api_key = "403e0b7a629746408001e435af8a0283"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)
data = response.json()

articles = data["articles"]

print(f"Total news found: {len(articles)}")
print("---")

with open("C:/Users/dell/Desktop/news.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Source", "Published At", "URL"])
    
    for article in articles:
        writer.writerow([
            article["title"],
            article["source"]["name"],
            article["publishedAt"],
            article["url"]
        ])

print("Done! news.csv has been created on your Desktop!")