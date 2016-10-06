from datetime import datetime, timedelta
from github import Github

gh = Github("nikhilm", open("token.cfg").read().strip())
repo = gh.get_repo("iron-io/go")

howlong = timedelta(days=30)
deadline = datetime.now() - howlong
print "Deadline", deadline
for pr in repo.get_pulls():
    mtime = pr.updated_at
    if mtime < deadline:
        pr.create_issue_comment('Closing this since it was last modified more than %s days ago. This is an automated message.' % howlong.days)
        pr.edit(state='closed')
        print pr.number, pr.title, "closed", mtime
