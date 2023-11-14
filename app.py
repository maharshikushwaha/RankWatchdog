import argparse
from googlesearch import search

def track_rank(url, keywords, num_results, country_code):
    try:
        print(f"Tracking rankings for '{url}' with keywords: {', '.join(keywords)} in {country_code}\n")

        for keyword in keywords:
            print(f"Keyword: {keyword}")
            query = f"{url} {keyword} country:{country_code}"
            results = list(search(query=query, num=num_results, stop=min(num_results, 100), pause=2))
            
            for idx, result in enumerate(results, start=1):
                print(f"{idx}. {result}")

            print("\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Simple Rank Tracker with Country')
    parser.add_argument('--url', required=True, help='Target website URL')
    parser.add_argument('--keywords', required=True, help='Comma-separated list of keywords')
    parser.add_argument('--num_results', type=int, default=5, help='Number of search results to fetch for each keyword')
    parser.add_argument('--country', required=True, help='Country code for country-specific ranking tracking')

    args = parser.parse_args()
    keywords = [kw.strip() for kw in args.keywords.split(',')]

    track_rank(args.url, keywords, args.num_results, args.country)

if __name__ == "__main__":
    main()
