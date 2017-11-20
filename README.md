# git_cli
A Git binding library, wrapping the Git cli tool, for the following actions:
1.	clone repositories
2.	commit changes to repositories
3.	push to remote repositories
4.	pull from remote repositories

## REQUIREMENTS
Installing on Linux.
If you want to install the basic Git tools on Linux via a binary installer, you can generally do so through the basic package-management tool that comes with your distribution. If you’re on Fedora for example (or any closely-related RPM-based distro such as RHEL or CentOS), you can use dnf:
```
$ sudo dnf install git-all
```
If you’re on a Debian-based distribution like Ubuntu, try apt-get:
```
$ sudo apt-get install git-all
```

Install python mock
```
$ sudo pip install mock
```
## INSTALL
Alternatevely if you have donwloaded source code:
```
python setup.py install
```

## API Documentation

### NAME
gitpush - Wrapper on git push which updates remote refs along with associated objects for a specific repository
### SYNOPSIS
gitpush [reponame]
### DESCRIPTION
Command runs git push with the <repository> argument, branch.*.remote configuration for the current branch is consulted to determine where to push. If the configuration is missing, it defaults to origin.
### gitpush python API
 ```
def run_git(options):
  """ {'type':'gitpush', 'repo':'repositoryname'} -> git push repositoryname command output""" 
 ```

### NAME
gitpull - Wrapper on git pull which fetches from and integrates with a specific repository
### SYNOPSIS
gitpull [reponame]
### DESCRIPTION
Incorporates changes from a remote repository into the current branch. In its default mode, git pull is shorthand for git fetch followed by git merge FETCH_HEAD.
 ```
def run_git(options):
  """ {'type':'gitpull', 'repo':'repositoryname'} -> git pull repositoryname command output""" 
 ```

## cli tool Documentation
Make sure that run_cli.py has the correct PYTHONPATH or is in same directory with src code
Alternatively you can install run_cli.py in your bashrc script or whatever helps you with your daily job. 
To run cli tool
```
$python run_cli.py
```

Run "help" command to check available commands for cli tool
```
Starting git command line interface...
$gitcli> help

Documented commands (type help <topic>):
gitclone  gitcommit  gitpull  gitpush  help  quit
```
Run quit command to exit the tool:
```
$gitcli> quit
Quitting.
```
Run gitclone command (Make sure you have git installed):
A bad result...
```
$gitcli> gitclone git@github.com:sakellar/git_cli.git
Running git clone.
fatal: destination path 'git_cli' already exists and is not an empty directory.
Command '['git', 'clone', 'git@github.com:sakellar/git_cli.git']' returned non-zero exit status 128
```
Run gitpush command (Make sure you are inside the repository you want to push):
```
$gitcli> gitpush git@github.com:sakellar/git_cli.git
Running git push.
Everything up-to-date
Successfully pushed to repository git@github.com:sakellar/git_cli.git
```
Run gitpull command (Make sure you are inside the repository you want to pull from):
```
$gitcli> gitpull git@github.com:sakellar/git_cli.git
Running git pull.
From github.com:sakellar/git_cli
 * branch            HEAD       -> FETCH_HEAD
Already up-to-date.
Successfully pulled from repository git@github.com:sakellar/git_cli.git
```

Run gitcommit command (Make sure you are inside the repository you want to commit):
```
gitcli> gitcommit fixed issues with git commit
Running git commit.
[master 1a3198d] fixed issues with git commit
 1 file changed, 2 insertions(+), 2 deletions(-)
Successfully committed changes with message :  <fixed issues with git commit>
```

## Testing
