# git_cli


# REQUIREMENTS
git_cli needs the git executable to be installed on the system and available in your 
PATH.

# INSTALL
If you have donwloaded source code:
python setup.py install

# API Documentation

# cli tool Documentation
Make sure that run_cli.py has the correct PYTHONPATH or is in same directory with src code
Alternatively you can install run_cli.py in your bashrc script or whatever helps you with your daily job. 
To run cli tool

$python run_cli.py

Run "help" command to check available commands for cli tool
Starting git command line interface...
gitcli> help

Documented commands (type help <topic>):
========================================
gitclone  gitcommit  gitpull  gitpush  help  quit

Run quit command to exit the tool:
gitcli> quit
Quitting.

Run gitclone command (Make sure you have git installed):
A bad result...
gitcli> gitclone git@github.com:sakellar/git_cli.git
Running git clone.
fatal: destination path 'git_cli' already exists and is not an empty directory.
Command '['git', 'clone', 'git@github.com:sakellar/git_cli.git']' returned non-zero exit status 128

A good result...
gitcli> gitclone git@github.com:sakellar/git_cli.git
Running git clone.
Cloning into 'git_cli'...
remote: Counting objects: 48, done.
remote: Compressing objects: 100% (41/41), done.
remote: Total 48 (delta 7), reused 27 (delta 1), pack-reused 0
Receiving objects: 100% (48/48), 13.96 KiB | 0 bytes/s, done.
Resolving deltas: 100% (7/7), done.
Checking connectivity... done.
Successfully cloned repository git@github.com:sakellar/git_cli.git

Run gitpush command (Make sure you are inside the repository you want to push):
gitcli> gitpush git@github.com:sakellar/git_cli.git
Running git push.
Everything up-to-date
Successfully pushed to repository git@github.com:sakellar/git_cli.git

Run gitpull command (Make sure you are inside the repository you want to pull from):
gitcli> gitpull git@github.com:sakellar/git_cli.git
Running git pull.
From github.com:sakellar/git_cli
 * branch            HEAD       -> FETCH_HEAD
Already up-to-date.
Successfully pulled from repository git@github.com:sakellar/git_cli.git


# Testing
