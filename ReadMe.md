# Job-Scout

![Job-Scout](https://img.shields.io/badge/remote-jobs-brightgreen) ![ML](https://img.shields.io/badge/machine-learning-blue) ![Stars](https://img.shields.io/github/stars/shreeshabhat1004/Job-Scout)

**Job-Scout** is a Python-based tool that aggregates remote job postings in Machine Learning and Data Science from multiple sources, including Hacker News and Twitter (X). The tool takes your resume in PDF format, analyzes it, and ranks job listings based on how well they match your skills and experience. With easy customization, you can also set it up to search for internships or specific job roles!

## 🌟 Features
- **Multi-Source Aggregation**: Pulls remote job listings from Twitter and Hacker News.
- **Machine Learning Focus**: Primarily searches for Machine Learning, Data Science, and AI roles.
- **Resume Matching**: Uses your PDF resume to rank job listings based on relevance.
- **Remote Job Targeting**: Specifically searches for remote positions.
- **Customizable Search Queries**: Easily modify search criteria for internships or other roles.

## 🔧 Tech Stack
- **Python** for scripting
- **Tweepy** for Twitter API access
- **sklearn** for TF-IDF vectorization and cosine similarity
- **PyMuPDF** for PDF text extraction

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+**
- **Twitter Developer Account** to obtain API credentials ([Sign up here](https://developer.twitter.com/en))

### Installation

1. **Clone the repository**:
   ```powershell
   git clone https://github.com/yourusername/Job-Scout.git
   cd Job-Scout
   ```

2. **Install the dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Set up API keys**:
   - Open `config.py`.
   - Replace the placeholders with your Twitter API credentials.
   - Optionally, adjust the search parameters to customize job types (e.g., internships).

---

## 🔑 Setting Up Twitter (X) API Keys

1. **Create a Twitter Developer Account**: Go to [Twitter Developer](https://developer.twitter.com/en) and create an account.
2. **Create a Project and an App**:
   - After logging in, go to **Developer Portal** > **Projects & Apps** > **Create App**.
   - Name your app, and choose appropriate permissions (usually "Read" access is sufficient for fetching job tweets).
3. **Generate API Keys**:
   - In your app's settings, go to **Keys and Tokens** to generate your **API Key**, **API Key Secret**, **Bearer Token**, **Access Token**, and **Access Token Secret**.
4. **Store Keys in `config.py`**:
   - Open `config.py` in the repository and add your keys as shown below.

```python
# config.py

# Twitter API credentials
API_KEY = "YOUR_API_KEY"
API_KEY_SECRET = "YOUR_API_KEY_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"
BEARER_TOKEN = "YOUR_BEARER_TOKEN"

# Specify search parameters for Twitter API
SEARCH_QUERY = """
("Machine Learning" OR "ML Engineer" OR "Data Scientist" OR "AI Engineer" OR "Deep Learning") 
(#hiring OR #job OR #jobopening OR #nowhiring OR #remote OR "work from home") 
lang:en -is:retweet
"""
MAX_TWEET_RESULTS = 10  # Number of tweets to fetch
```

---

## ⚙️ Usage

1. **Provide a Resume PDF**:
   - Place your resume in the project folder or specify its full path when prompted.

2. **Run the Script**:
   ```powershell
   python main.py
   ```

3. **View Recommendations**:
   - The script will display the top-ranked Machine Learning remote jobs based on how well they match your resume.

---

## Customizing the Search Query

To modify the search query for specific job roles or types (e.g., internships), update the `SEARCH_QUERY` parameter in `config.py`. For example:

- **Machine Learning Internships**:
   ```python
   SEARCH_QUERY = """
   ("Machine Learning Intern" OR "ML Intern" OR "Data Science Internship" OR "AI Intern") 
   (#hiring OR #job OR #internship OR #nowhiring OR #remote OR "work from home") 
   lang:en -is:retweet
   """
   ```

- **General Data Science Roles**:
   ```python
   SEARCH_QUERY = """
   ("Data Scientist" OR "Data Analyst" OR "Machine Learning Engineer") 
   (#hiring OR #job OR #jobopening OR #nowhiring OR #remote) 
   lang:en -is:retweet
   """
   ```

This customization allows you to filter Twitter job results to focus on internships, specific roles, or different fields within Machine Learning and Data Science.

---

## 📁 Project Structure

```
Job-Scout/
├── README.md                # Project documentatio
├── requirements.txt         # List of dependencies
├── config.py                # Configuration for API keys and tokens
├── main.py                  # Main script to run the job search and matching process
├── utils/                   # Utility scripts for modularity
│   ├── twitter_search.py    # Fetches ML job tweets from Twitter
│   ├── hackernews_scraper.py # Scrapes ML remote jobs from Hacker News
│   └── pdf_extractor.py     # Extracts text from the PDF resume
```

---

## 📊 Example Output

When you run the script, you’ll see output similar to the following:

```plaintext
Top Machine Learning Remote Job Recommendations:

Job Title: Machine Learning Engineer at XYZ Corp
Job URL: https://example.com/job/1234
Similarity Score: 0.92

Job Title: Data Scientist - Remote
Job URL: https://example.com/job/5678
Similarity Score: 0.89

...
```

---

## 💬 Contact

For any questions or feedback, please reach out via [email](srbhat1004@gmail.com), contributions are welcome.

**Happy Job Hunting! 🚀**

---
