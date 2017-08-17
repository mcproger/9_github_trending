import requests
import argparse
from datetime import date, timedelta


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('top_size', type=int,
                        help='Number of repositories that should be returned')
    parser.add_argument('time_delta', type=int,
                        help='Time for searching create date of repository')
    args = parser.parse_args()
    return args


def get_trending_repositories(top_size, time_delta):
    max_page_count = 100
    if top_size > max_page_count:
        return None
    time_ago_date = date.today() - timedelta(days=time_delta)
    github_api_url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'created:>=%s' % week_ago_date,
        'sort': 'stars',
        'per_page': '100'
    }
    response = requests.get(github_api_url, params=params).json()
    repositories = response['items'][:top_size]
    return repositories


def get_repository_info(repo_url, repo_stars, repo_issues):
    repository_info = '{repo_url} {repo_stars} {repo_issues}'.format(
        repo_url=repo_url,
        repo_stars=repo_stars,
        repo_issues=repo_issues
    )
    return repository_info


if __name__ == '__main__':
    args = get_argparser()
    repositories = get_trending_repositories(args.top_size, args.time_delta)
    for repository in repositories:
        print(get_repository_info(repository['url'], repository['stargazers_count'], repository['open_issues_count']))