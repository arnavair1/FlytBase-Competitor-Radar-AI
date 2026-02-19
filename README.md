# 🚀 FlytBase Competitor Kill-Switch Monitor

An AI-powered competitive intelligence agent that monitors competitor updates and automatically generates FlytBase-ready marketing content.

Built as part of the FlytBase AI Marketing Roundtable demo.

---

## ✨ What This Project Does

When a competitor launches a feature or announces an update, the agent automatically generates:

- Sales battle card
- Comparison blog outline
- LinkedIn post
- Email pitch
- Video script

All in FlytBase brand voice.

> "When Competitor X launched Y yesterday, my agent woke up and wrote a sales email before I had my coffee."

---

## 🧠 Why This Matters

Marketing teams spend hours tracking competitors manually. This tool reduces that to seconds.

It enables:

- ✅ Faster sales response
- ✅ Better positioning
- ✅ Independent AI-driven marketing
- ✅ Real-time competitor intelligence

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python |
| Web Scraping | BeautifulSoup |
| AI Generation | Gemini AI |
| Frontend | Streamlit |
| Change Detection | MD5 Snapshot Diffing |
| Scheduling | Python `time` loop |

---

## 📂 Project Structure

```
kill-switch-agent/
│
├── app.py                 # Background agent + scheduler
├── dashboard.py           # Streamlit UI
├── ai_generator.py        # Gemini AI content generation
├── scraper.py             # Web scraping logic
├── database.py            # Snapshot save/load/hash
├── change_detector.py     # Detects page changes
├── config.py              # Competitor config list
├── .env                   # API keys (not committed)
└── snapshots/             # Stored competitor page snapshots
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone <repo-url>
cd kill-switch-agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your API Key

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_key_here
```

---

## ▶️ Run the Background Agent

Monitors competitors on a schedule and prints AI output to terminal:

```bash
python app.py
```

## ▶️ Run the Dashboard

Interactive UI to manually trigger competitor checks:

```bash
streamlit run dashboard.py
```

---

## 🎯 Demo Script

1. Delete any existing file inside `snapshots/`
2. Run the dashboard with `streamlit run dashboard.py`
3. Select a competitor from the dropdown
4. Click **"Check Competitor Update"**
5. The AI generates a full battle card instantly

---

## 🚀 Deployment

### Streamlit Cloud (Recommended — Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo, set main file to `dashboard.py`
4. Add your secret under **Settings → Secrets**:
   ```
   GEMINI_API_KEY = "your_key_here"
   ```
5. Click **Deploy** — you get a live public URL

### Railway.app (For running agent + dashboard together)

1. Push to GitHub → Go to [railway.app](https://railway.app)
2. Add env variable: `GEMINI_API_KEY`
3. Dashboard start command:
   ```
   streamlit run dashboard.py --server.port $PORT --server.address 0.0.0.0
   ```
4. Agent start command (separate service):
   ```
   python app.py
   ```

---

## 🔮 Future Improvements

- LinkedIn competitor monitoring
- G2 review sentiment analysis
- Slack / email alerts on change detection
- Auto SEO optimization for blog posts
- Multi-language marketing content generation

---

## 👨‍💻 Author

Built by a software engineer passionate about AI automation and real-world product engineering.

Target role: AI-native product engineering & marketing automation at FlytBase.

---

## ⭐ Inspiration

FlytBase AI Marketing Roundtable — where marketers build world-class content independently using AI.