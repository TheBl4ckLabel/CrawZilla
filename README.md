# CrawZilla 

Common Crawl Domain URL Extractor
<img width="1011" height="384" alt="image" src="https://github.com/user-attachments/assets/b875fbb0-ea9c-48df-8f9a-826b148d0b3d" />

This Python script fetches archived URLs for a given domain from the [Common Crawl](https://commoncrawl.org/) dataset.  
It queries all available Common Crawl indexes and extracts unique URLs related to the specified domain.  

---

## 🚀 Features
- Fetches all available Common Crawl indexes automatically.
- Extracts archived URLs for a given domain.
- Deduplicates results (ensures unique URLs).
- Saves results to a file (`urls.txt`).
- Prints URLs in real time as they are discovered.
- Provides the total count of unique URLs found.

---

## 📦 Requirements
- Python 3.7+
- `requests` library (for HTTP requests)

Install dependencies with:

pip install -r requirements.txt


## 📂 Installation

git clone https://github.com/yourusername/CrawZilla.git
cd CrawZilla

## 🛠 Usage

python crawler.py
