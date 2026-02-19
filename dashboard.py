import streamlit as st
import os
from config import COMPETITORS
from scraper import scrape_page
from ai_generator import generate_battle_card

st.set_page_config(page_title="FlytBase Competitor Radar", layout="wide")

st.title("🚀 FlytBase Competitor Kill-Switch Monitor")

st.write("Detect competitor updates and auto-generate marketing content.")

selected = st.selectbox(
    "Select Competitor",
    [c["name"] for c in COMPETITORS]
)

if st.button("Check Competitor Update"):

    competitor = next(c for c in COMPETITORS if c["name"] == selected)

    st.info("Scraping competitor page...")
    text = scrape_page(competitor["url"])

    if not text:
        st.error("Could not scrape page")
    else:
        st.success("Page scraped!")

        st.info("Generating AI battle card...")
        output = generate_battle_card(selected, text)

        st.subheader("📊 AI Generated Content")

        # Render markdown properly
        st.markdown(output)

        # Keep download button for raw text
        st.download_button(
            label="⬇️ Download as .txt",
            data=output,
            file_name="battle_card.txt",
            mime="text/plain"
        )
