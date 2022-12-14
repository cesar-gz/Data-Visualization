import requests

"""
https://api.github.com/search/repositories?q=language:python&sort=stars
search all the respositories that use Python and sort the projects by the number of stars given
"""

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") #status code of 200 means it was successful

# Store API response in a variable
response_dict = r.json()

# Process results
print(response_dict.keys())

# Print the total amount of Python repositories on GitHub
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")  # print the length to see how many repositories we have information for

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

# Examine the information in the repositories
print("\nSelectred information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}\n")