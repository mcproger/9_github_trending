import requests
import argparse
from datetime import date, timedelta


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('top_size', type=int,
                        help='Number of repositories that should be returned')
    args = parser.parse_args()
    return args


def get_trending_repositories(top_size):
    max_page_count = 100
    if top_size > max_page_count:
        return 'Max page count is 100'
    week_ago_date = date.today() - timedelta(days=7)
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'created:>=%s' % week_ago_date,
        'sort': 'stars',
        'per_page': '100'
    }
    response = requests.get(url, params=params).json()
    repositories = response['items'][:top_size]
    return repositories


def get_open_issues_amount(repositories):
    pass


if __name__ == '__main__':
    args = get_argparser()
    repositories = get_trending_repositories(args.top_size)
    for repository in repositories:
        print(repository['name'], '-', repository['open_issues_count'], repository['stargazers_count'])