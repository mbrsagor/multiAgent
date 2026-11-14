from src.tools.tools import web_search, scrape_url
from src.pipelines.pipeline import run_research_pipeline


# content = web_search("What the the current news about AI")
# print(content)

# results = scrape_url("https://www.nbcnews.com/artificial-intelligence")
# print(results)


topic = "The impact of AI on the job market in 2027"
run_research_pipeline(topic=topic)

