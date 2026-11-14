from datetime import timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import re
import xml.etree.ElementTree as ET

import streamlit as st


st.set_page_config(page_title="TimeCraft | World Updates", page_icon="🌐", layout="wide")
FEED_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"
MAX_ARTICLES = 20


class TextOnlyHTMLParser(HTMLParser):
    """Extract readable text from RSS descriptions that contain HTML markup."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain_text(value: str) -> str:
    parser = TextOnlyHTMLParser()
    parser.feed(value or "")
    return re.sub(r"\s+", " ", " ".join(parser.parts)).strip()


def format_date(value: str) -> str:
    try:
        date = parsedate_to_datetime(value)
        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)
        return date.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    except (TypeError, ValueError, OverflowError):
        return value or "Publication date unavailable"


@st.cache_data(ttl=600, max_entries=1, show_spinner=False)
def load_world_news():
    request = Request(
        FEED_URL,
        headers={"User-Agent": "TimeCraft/1.0 (educational prototype; RSS reader)"},
    )
    with urlopen(request, timeout=12) as response:
        feed_bytes = response.read(1_000_000)

    root = ET.fromstring(feed_bytes)
    channel = root.find("channel")
    if channel is None:
        raise ValueError("The RSS response did not contain a channel.")

    articles = []
    for item in channel.findall("item")[:MAX_ARTICLES]:
        title = plain_text(item.findtext("title", default=""))
        summary = plain_text(item.findtext("description", default=""))
        link = item.findtext("link", default="").strip()
        parsed_link = urlparse(link)
        if not title or parsed_link.scheme not in {"http", "https"} or not parsed_link.netloc:
            continue
        articles.append(
            {
                "title": title,
                "summary": summary,
                "link": link,
                "published": format_date(item.findtext("pubDate", default="")),
            }
        )

    if not articles:
        raise ValueError("No valid articles were found in the RSS feed.")
    return articles, format_date(channel.findtext("lastBuildDate", default=""))


st.title("🌐 World Updates")
st.write("Recent international headlines from BBC News. Select a story to open its original article.")
st.caption("Headlines are provided by BBC News. This page links to the original publisher and does not reproduce full articles.")

if st.button("Refresh headlines", help="Clear the ten-minute cache and request the feed again."):
    load_world_news.clear()

try:
    with st.spinner("Loading international headlines..."):
        articles, feed_built = load_world_news()
    st.caption(f"Feed last built: {feed_built} · Headlines are cached for up to 10 minutes.")
    for article in articles:
        with st.container(border=True):
            st.subheader(article["title"])
            st.caption(article["published"])
            if article["summary"]:
                st.write(article["summary"])
            st.link_button("Read the full story on BBC News", article["link"])
except (URLError, TimeoutError, OSError, ET.ParseError, ValueError) as error:
    st.error("World updates are temporarily unavailable. Please try again later.")
    with st.expander("Technical details"):
        st.code(str(error))

st.divider()
st.caption("Source: BBC News World RSS feed · External headlines and links may change without notice.")
