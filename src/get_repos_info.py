import json

fn = "/data/cryptokasten/repo/repos.json"

def read_repos_file():
    return json.loads(open(fn, "rt").read())

def calculate_sum(repos, field):
    return sum(map(lambda x: x[field], repos))

def get_statistics(repos):
    res = dict()
    res["stargazers"] = calculate_sum(repos, "stargazers_count")
    res["forks"] = calculate_sum(repos, "forks_count")
    res["watchers"] = calculate_sum(repos, "watchers_count")
    res["open_issues"] = calculate_sum(repos, "open_issues_count")
    res["total_repos"] = len(repos)
    return res

repos = read_repos_file()

print(get_statistics(repos))
