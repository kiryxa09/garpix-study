import requests

def get_repo_counts(languages):
    result = []
    for language in languages:
        response = requests.get(f'https://api.github.com/search/repositories?q=language:{language}')
        repo_count = response.json()['total_count']
        result.append([language, repo_count])
    return result

languages = ['python', 'c++', 'java', 'javascript', 'ruby', 'c#']
repo_counts = get_repo_counts(languages)
print(repo_counts)

