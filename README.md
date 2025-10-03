# OSINT Pipeline 🔍

A comprehensive Open Source Intelligence (OSINT) data collection and analysis pipeline that aggregates data from multiple social media platforms and online sources.

## 📋 Overview

This OSINT pipeline automates the collection, cleaning, sentiment analysis, and visualization of data from various social media platforms. It provides a unified framework for gathering intelligence from multiple sources and storing it in a centralized database.

## ✨ Features

- **Multi-Platform Data Collection**: Collect data from 11+ platforms
  - Twitter
  - Reddit
  - Facebook
  - Instagram
  - GitHub
  - LinkedIn
  - Quora
  - TikTok
  - VK
  - Telegram
  - Discord
  - Mastodon

- **Data Processing**
  - Text cleaning and normalization
  - Language detection and filtering (English)
  - Sentiment analysis using TextBlob
  - Automatic timestamp parsing

- **Data Storage**
  - SQLite database for efficient storage
  - Structured data schema with platform, user, timestamp, text, URL, and sentiment fields

- **Visualization**
  - Sentiment analysis charts by platform
  - Post frequency over time graphs
  - Interactive matplotlib visualizations

- **Automation**
  - Scheduled data collection with configurable intervals
  - Automated pipeline execution

## 📁 Project Structure

```
OSINT-main/
├── osint_pipeline/
│   ├── main.py                 # Main pipeline orchestrator
│   ├── automate.py            # Scheduled automation script
│   ├── collectors/            # Platform-specific data collectors
│   │   ├── twitter_collector.py
│   │   ├── reddit_collector.py
│   │   ├── facebook_collector.py
│   │   ├── instagram_collector.py
│   │   ├── github_collector.py
│   │   ├── linkedin_collector.py
│   │   ├── quora_collector.py
│   │   ├── tiktok_collector.py
│   │   ├── vk_collector.py
│   │   ├── telegram_collector.py
│   │   ├── discord_collector.py
│   │   └── mastodon_collector.py
│   ├── utils/                 # Utility modules
│   │   ├── cleaner.py        # Text cleaning and filtering
│   │   ├── database.py       # Database operations
│   │   ├── sentiment.py      # Sentiment analysis
│   │   └── visualizer.py     # Data visualization
│   └── data/
│       └── osint.db          # SQLite database
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- API keys for various platforms (see Configuration section)

### Setup

1. **Clone the repository**
   ```bash
   cd OSINT-main
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On macOS/Linux
   # or
   myenv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data** (required for text processing)
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

## ⚙️ Configuration

Create a `.env` file in the project root with your API credentials:

```env
# Twitter API
TWITTER_BEARER=your_twitter_bearer_token

# Reddit API
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_user_agent

# GitHub API
GITHUB_TOKEN=your_github_token

# VK API
VK_ACCESS_TOKEN=your_vk_token

# Discord Bot
DISCORD_TOKEN=your_discord_token

# Telegram API
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE=your_phone_number

# LinkedIn (if using unofficial API)
LINKEDIN_EMAIL=your_email
LINKEDIN_PASSWORD=your_password

# Facebook (if available)
FACEBOOK_ACCESS_TOKEN=your_facebook_token
```

### Getting API Keys

- **Twitter**: [Twitter Developer Portal](https://developer.twitter.com/)
- **Reddit**: [Reddit Apps](https://www.reddit.com/prefs/apps)
- **GitHub**: [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
- **VK**: [VK Developers](https://vk.com/dev)
- **Discord**: [Discord Developer Portal](https://discord.com/developers/applications)
- **Telegram**: [Telegram API](https://my.telegram.org/apps)

## 💻 Usage

### Basic Usage

Run the pipeline once:

```bash
cd osint_pipeline
python main.py
```

### Automated Collection

Run the pipeline on a schedule (every hour by default):

```bash
cd osint_pipeline
python automate.py
```

Press `Ctrl+C` to stop the scheduler.

### Visualization

Generate visualizations from collected data:

```bash
cd osint_pipeline/utils
python visualizer.py
```

This will display:
- Average sentiment by platform
- Post frequency over time

### Customizing Collection

Edit `main.py` to customize queries and limits:

```python
def run_pipeline():
    data = []
    data.extend(fetch_twitter("cybersecurity", 50))  # Custom query and limit
    data.extend(fetch_reddit("netsec", 100))
    # Add or remove platforms as needed
    # ...
```

## 📊 Data Schema

Each collected record contains:

| Field      | Type   | Description                           |
|------------|--------|---------------------------------------|
| platform   | TEXT   | Source platform (e.g., "twitter")     |
| user       | TEXT   | Username or user ID                   |
| timestamp  | TEXT   | Post timestamp                        |
| text       | TEXT   | Cleaned post content                  |
| url        | TEXT   | Link to original post                 |
| sentiment  | REAL   | Sentiment score (-1.0 to 1.0)        |

## 🛠️ Advanced Features

### Custom Collectors

Create custom collectors by following the template:

```python
def fetch_platform(query="default", limit=10):
    results = []
    # Your collection logic here
    for item in collected_items:
        results.append({
            "platform": "platform_name",
            "user": item.user,
            "timestamp": item.timestamp,
            "text": item.text,
            "url": item.url
        })
    print(f"Platform: Fetched {len(results)} items")
    return results
```

### Sentiment Analysis

The pipeline uses TextBlob for sentiment analysis:
- **Positive sentiment**: Score > 0
- **Neutral sentiment**: Score ≈ 0
- **Negative sentiment**: Score < 0

### Text Cleaning

Automatic text preprocessing:
- HTML tag removal
- URL removal
- Special character normalization
- Whitespace cleanup
- Language detection and filtering

## 🔧 Troubleshooting

### Common Issues

**1. Import errors**
```bash
# Make sure you're in the correct directory
cd osint_pipeline
python main.py
```

**2. Database not found (when running visualizer)**
- The path is now automatically resolved
- Make sure `data/osint.db` exists in the `osint_pipeline` directory

**3. API Rate Limits**
- Twitter: Free tier has monthly limits
- Reduce the `count` parameter in collector functions
- Add delays between requests

**4. Missing API credentials**
- Check your `.env` file is in the correct location
- Verify all required credentials are set
- Some collectors may fail silently if credentials are missing

### Enable Debug Mode

Add error handling to see detailed errors:

```python
import traceback

try:
    run_pipeline()
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
```

## 📈 Performance Tips

1. **Limit collection sizes** during testing
2. **Use specific queries** to reduce noise
3. **Schedule off-peak hours** to avoid rate limits
4. **Monitor database size** and archive old data
5. **Add error handling** for production use

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional platform collectors
- Enhanced sentiment analysis models
- More visualization types
- Export to different formats (JSON, CSV, Excel)
- Web dashboard interface
- Real-time streaming data collection

## ⚠️ Legal and Ethical Considerations

- **Terms of Service**: Ensure compliance with each platform's ToS
- **Rate Limits**: Respect API rate limits
- **Privacy**: Handle user data responsibly
- **Purpose**: Use for legitimate research and security purposes only
- **Attribution**: Credit data sources appropriately

## 📝 License

This project is for educational and research purposes. Ensure compliance with:
- Platform APIs terms of service
- Local data protection laws (GDPR, CCPA, etc.)
- Ethical guidelines for OSINT research

## 🙏 Acknowledgments

Built with:
- [Tweepy](https://www.tweepy.org/) - Twitter API wrapper
- [PRAW](https://praw.readthedocs.io/) - Reddit API wrapper
- [Instaloader](https://instaloader.github.io/) - Instagram data loader
- [PyGithub](https://pygithub.readthedocs.io/) - GitHub API wrapper
- [TextBlob](https://textblob.readthedocs.io/) - Sentiment analysis
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [Matplotlib](https://matplotlib.org/) - Data visualization

## 📧 Contact

For questions, issues, or suggestions, please open an issue on GitHub.

---

**Note**: This tool is intended for legitimate OSINT research, security analysis, and academic purposes. Users are responsible for ensuring their use complies with all applicable laws and platform policies.
