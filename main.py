from src.tools.tools import web_search, scrape_url


# content = web_search("What the the current news about AI")
# print(content)

results = scrape_url("https://www.nbcnews.com/artificial-intelligence")
print(results)
