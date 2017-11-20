from cmd import Cmd
from wrapper import Wrapper
import subprocess

class MyPrompt(Cmd):
    branches = []

    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit

    def do_gitclone(self, args):
        """Wrapper for git clone"""
        print "Running git clone."
        if len(args) == 0:
            print "you must enter a repository name as an  argument"
            return
        else:
            repo_name = args
        if len(args.split()) == 1:
            options = dict()
            options['type'] = "gitclone"
            options["repo"] = repo_name
            try:
                if  Wrapper.run_git(options)[0] == 0:
                    print "Successfully cloned repository " + str(repo_name)
            except subprocess.CalledProcessError as e:
                print e
                return
        else:
            print "not valid repository name"
            return

    def do_gitcommit(self, args):
        """Wrapper for git commit"""
        print "Running git commit."
        options = dict()
        options['type'] = "gitclone"
        Wrapper.run_git(options)

    def complete_gitpush(self, text, line, begidx, endidx):
         _AVAILABLE_BRANCHES = ['FETCH_HEAD', 'HEAD', 'master', 'ORIG_HEAD', 'origin/HEAD', 'origin/master']
         return [i for i in _AVAILABLE_BRANCHES if i.startswith(text)]

    def do_gitpush(self, args):
        """Wrapper for git push"""
        print "Running git push."
        if len(args) == 0:
            print "you must enter a repository name as an  argument"
            return
        else:
            repo_name = args
        if len(args.split()) == 1:
            options = dict()
            options['type'] = "gitclone"
            options["repo"] = repo_name
            try:
                if  Wrapper.run_git(options)[0] == 0:
                    print "Successfully cloned repository " + str(repo_name)
            except subprocess.CalledProcessError as e:
                print e
                return
        else:
            print "not valid repository name"
            return

    def complete_gitpull(self, text, line, begidx, endidx):
        _AVAILABLE_BRANCHES = ['FETCH_HEAD', 'HEAD', 'master', 'ORIG_HEAD', 'origin/HEAD', 'origin/master']
        return [i for i in _AVAILABLE_BRANCHES if i.startswith(text)]

    def do_gitpull(self, args):
        """Running git pull"""
        options = {}
        options['type'] = "gitbranchall"

        if len(args) == 0:
            print "you must enter a branch name as an argument"
            return
        else:
            branch = args

        if len(args.split()) == 1:
            options = dict()
            options['type'] = "gitpull"
            options['branch'] = branch
            try:
                if  Wrapper.run_git(options)[0] == 0:
                    print "Successfully pulled from branch" + str(repo_name)
            except subprocess.CalledProcessError as e:
                print e
                return

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'gitcli> '
    prompt.cmdloop('Starting git command line interface...')
