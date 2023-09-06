import git as gitpython
gitpython.Git().custom_binary('/path/to/git')
import os
os.environ['GIT_PYTHON_GIT_EXECUTABLE'] = '/path/to/git'


repo_url = 'https://github.com/thatgreedydude/Personal-Projects/tree/main'
repo = gitpython.Repo.clone_from(repo_url, 'local_directory')

# Pull latest changes
repo.git.pull()

# Rename the directory
repo.git.mv("loc_track", "Location_Track_using_Phonenumbers")

# Commit the changes
repo.index.commit('Renamed directory')

# Push the changes
repo.remotes.origin.push()