Simple script to close all open PRs last modified > 30 days ago.
No configurability whatsoever. Just modify values in the script as required.
Only token is kept in token.cfg so I don't accidentally leak it into version
control.
Source should be explanatory.

### Installation

1. Clone repo
2. cd into repo
3. `virtualenv env`
4. `source env/bin/activate`
5. `pip install pygithub`
6. edit script with your values.
7. create `token.cfg` file that either has a password or a Personal Access
   Token.
8. `python closeprs.py`
9. Profit!
