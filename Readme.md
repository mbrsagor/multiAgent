# Multi-Agent Research Assistant

A Streamlit app that researches a topic with a sequence of specialized AI
agents and produces a report with a separate critique. The project also
includes a command-line entry point for running the same research pipeline.

## What it does

For a given research topic, the pipeline:

1. Uses Tavily to search the web for recent information.
2. Selects a relevant result and extracts page content.
3. Writes a structured research report from the search results and extracted
   content.
4. Reviews the report and returns a score, strengths, and areas to improve.

The Streamlit app shows the pipeline outputs and provides the final report as a
Markdown download. Search and extracted-page outputs are available in
expandable sections.

## Requirements

- Python 3.10 or later
- An OpenAI API key
- A Tavily API key

The app uses `gpt-4o-mini` through LangChain's `ChatOpenAI` integration.

## Setup

Clone or download the project, then from its root directory create and activate
a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configure API keys

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

The application loads these variables with `python-dotenv`. Keep the `.env`
file private and do not commit real API keys to version control.

## Run the application

Start the Streamlit interface from the project root:

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit, enter a research topic, and select
**Run Research Pipeline**.

## Run from the command line

Run the included script with:

```bash
python main.py
```

`main.py` currently runs the pipeline for a topic defined directly in that
file. To use a different topic from the command line, edit the `topic` value
there.

The pipeline can also be called from Python:

```python
from src.pipelines.pipeline import run_research_pipeline

results = run_research_pipeline("The impact of AI on the job market")
print(results["report"])
```

The returned dictionary contains `search_results`, `scraped_content`, `report`,
and `feedback`.

## Project structure

```text
.
├── app.py                  # Streamlit web interface
├── main.py                 # Command-line example
├── requirements.txt        # Python dependencies
└── src/
    ├── agents/
    │   └── agents.py       # Search/reader agents and writer/critic chains
    ├── pipelines/
    │   └── pipeline.py     # Sequential research pipeline
    └── tools/
        └── tools.py        # Tavily search and web-page extraction
```

## Notes

- The search tool returns up to five results.
- Page extraction tries Trafilatura first, then Readability and BeautifulSoup;
  extracted text is limited to 5,000 characters.
- The pipeline makes external API and web requests. Results depend on those
  services, network availability, and the quality/accessibility of source pages.
- The generated report and its critique are AI-produced; verify important
  claims against the cited sources before relying on them.
