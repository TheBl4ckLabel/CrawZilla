import requests
import json
import time
import argparse
import sys

def get_all_indexes():
    """Fetch all available Common Crawl."""
    url = "https://index.commoncrawl.org/collinfo.json"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return [item["id"] for item in response.json()]
    except Exception as e:
        print(f"Error fetching indexes: {e}")
        return []

def fetch_urls_from_index(domain, index):
    """Fetch URLs from a specific Common Crawl."""
    urls = set()
    api_url = f"https://index.commoncrawl.org/{index}-index?url={domain}/*&output=json"
    try:
        response = requests.get(api_url, timeout=30)
        if response.status_code != 200:
            return urls
        for line in response.text.splitlines():
            try:
                data = json.loads(line)
                url = data.get("url")
                if url:
                    urls.add(url)
            except json.JSONDecodeError:
                continue
    except Exception:
        pass
    return urls

def main():
    parser = argparse.ArgumentParser(description="Fetch URLs from Common Crawl for a given domain.")
    parser.add_argument("-d", "--domain", required=True, help="Domain to search.")
    parser.add_argument("-o", "--output", help="Output file to save URLs.")
    
    args = parser.parse_args()
    domain = args.domain.strip()
    output_file = args.output

    indexes = get_all_indexes()
    if not indexes:
        sys.exit(1)

    all_urls = set()
    for index in indexes:
        urls = fetch_urls_from_index(domain, index)
        for url in urls:
            if url not in all_urls:
                all_urls.add(url)
                print(url)
        time.sleep(1)  # avoid hitting API too hard

    print(f"\nTotal unique URLs found: {len(all_urls)}")

    # Save results to file optional
    if output_file:
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                for url in sorted(all_urls):
                    f.write(url + "\n")
            print(f"Results saved to {output_file}")
        except Exception as e:
            print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
