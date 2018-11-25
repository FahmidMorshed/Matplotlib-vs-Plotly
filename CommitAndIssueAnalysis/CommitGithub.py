from github import Github
g = Github("access_token")
g = Github("e04e9ced4aaf9c221067a5f4e65b3fc30607ee19")

repo=g.get_repo("matplotlib/matplotlib")

paginated_obj=repo.get_commits()
for singleCommit in paginated_obj:
    gitCommitObj=singleCommit.commit
    gitAuthor=gitCommitObj.author
    dateTime=gitAuthor.date
    print(dateTime)
    
    

