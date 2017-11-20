from cmd import Cmd
from wrapper import Wrapper
import subprocess

class MyPrompt(Cmd):
    """
    Class for Cli
    """

    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit

    def do_gitpull(self, args):
        """Wrapper for git pull"""
        print "Running git pull."
        options = dict()
        options['type'] = "gitpull"
        options['repo'] = args
        try:
            if Wrapper.run_git(options)[0] == 0:
                print "Successfully pulled from repository " + str(options['repo'])
        except subprocess.CalledProcessError as e:
            print e
            print e.output
            return
        except Exception as gen:
            print gen
            return

    def do_gitcommit(self, args):
        """Wrapper for git commit"""
        print "Running git push."
        options = dict()
        options['type'] = "gitpush"
        options['message'] = args
        try:
            if Wrapper.run_git(options)[0] == 0:
                print "Successfully committed changes " + str(options['message'])
        except subprocess.CalledProcessError as e:
            print e
            print e.output
            return
        except Exception as gen:
            print gen
            return

    def do_gitpush(self, args):
        """Wrapper for git push"""
        print "Running git push."
        options = dict()
        options['type'] = "gitpush"
        options['repo'] = args
        try:
            if Wrapper.run_git(options)[0] == 0:
                print "Successfully pushed to repository " + str(options['repo'])
        except subprocess.CalledProcessError as e:
            print e
            print e.output
            return
        except Exception as gen:
            print gen
            return

    def do_gitclone(self, args):
        """Wrapper for git clone"""
        print "Running git clone."
        options = dict()
        options['type'] = "gitclone"
        options['repo'] = args
        try:
            if Wrapper.run_git(options)[0] == 0:
                print "Successfully cloned repository " + str(options['repo'])
        except subprocess.CalledProcessError as e:
            print e
            print e.output
            return
        except Exception as gen:
            print gen
            return

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'gitcli> '
    prompt.cmdloop('Starting git command line interface...')
