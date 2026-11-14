# project-1 — TimeCraft Historical Explorer

TimeCraft is an English-language educational Streamlit prototype for exploring selected historical events, notable people, and alternative-history questions. It also includes a **World Updates** page that displays recent international headlines from the BBC News World RSS feed.

> TimeCraft is a learning prototype. Its historical summaries and “what if?” prompts are introductory examples, not a sourced reference work or a predictive simulation.

## Features

- A multi-page Streamlit interface for historical events, people, and scenario prompts.
- An interactive Folium map with selected historical locations.
- Searchable figure cards with short biographies and local portrait assets.
- An optional Gemini-powered assistant using Google's current `google-genai` Python SDK. The rest of the app works without a Gemini key.
- A live World Updates page that reads BBC News World RSS, links to original articles, and uses Streamlit's `st.cache_data` with a ten-minute TTL to limit repeated requests.
- A consistent dark-and-gold theme, Git ignore rules, and a GitHub Actions syntax check.

## Requirements and setup

Use Python 3.10 or newer and Streamlit 1.51 or newer.

```bash
# Create a virtual environment
python -m venv .venv

# Activate it on Linux or macOS
source .venv/bin/activate

# On Windows PowerShell:
# .venv\Scripts\Activate.ps1

# Install dependencies and launch from the repository root
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Optional Gemini assistant

The AI Assistant page requires a Google Gemini API key. Other TimeCraft pages do not. Set the key in the process environment or in Streamlit Secrets; never hard-code it in Python or commit it to GitHub.

```bash
# Linux or macOS, for the current shell session
export GOOGLE_API_KEY="your-key"

# Windows PowerShell, for the current shell session
$env:GOOGLE_API_KEY = "your-key"
```

The model name can be overridden with `GEMINI_MODEL`; otherwise the application uses `gemini-flash-latest`. For Streamlit Community Cloud, add `GOOGLE_API_KEY` under the app's Secrets settings. The `.streamlit/secrets.toml` file is ignored by Git.

## World Updates source

World Updates reads [BBC News World RSS](https://feeds.bbci.co.uk/news/world/rss.xml). BBC asks sites displaying its feed to attribute the content as **BBC News** or **bbc.co.uk/news** and prohibits use of BBC logos or trademarks. TimeCraft displays the required attribution, provides links to original stories, and does not include BBC branding. See [BBC guidance for using its news feeds](https://www.bbc.co.uk/news/10628494) and its [Terms of Use](https://www.bbc.co.uk/usingthebbc/terms-of-use/).

This page needs an internet connection. Streamlit caches feed data for up to ten minutes, and users can request a refresh from the page. Headlines, summaries, links, and feed availability are controlled by the publisher and may change.

## Project structure

```text
.
├── app.py                       # Streamlit entry point and navigation
├── pages/                       # Home, history, figures, scenarios, assistant, and news
├── images/                      # Local image assets
├── .streamlit/config.toml        # Application theme
├── .github/workflows/            # Python syntax check
├── requirements.txt              # Python dependencies
└── .env.example                  # Optional configuration names, no secrets
```

## Important limitations

- Sign-in and sign-up are interface demos only. They do not authenticate users or create accounts. Do not enter real passwords.
- The contact form does not send or store messages.
- Some page images are hosted externally and require an internet connection. Check image rights and source terms before reuse.
- Check historical facts against reliable, cited sources before using them in academic or public work.
- No software license is included. Do not assume the code or media may be reused until a license is selected.

## Checks

GitHub Actions validates Python syntax on pushes and pull requests:

```bash
python -m compileall -q app.py pages
```
