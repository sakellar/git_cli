from ExecuteCommand import call_popen
import subprocess

class Wrapper(object):
    """
    Wrapper class for git
    """
    @staticmethod
    def run_git(options):
        """
        Checks git type and calls the right git method
        """
        command = {
            'gitcommit': Wrapper.gitcommit,
            'gitpush': Wrapper.gitpush,
            'gitpull': Wrapper.gitpull,
            'gitclone': Wrapper.gitclone,
        }

        try:
            return command[options['type']](options)
        except KeyError:
            message = 'type %s provided in options is not valid' % options['type']

    @staticmethod
    def git_cmd():
        """
        Gitcmd helper function
        """
        git_command = ['git']
        return git_command

    @staticmethod
    def check_args_repo(options):
        """
        Checks for the number of arguments for repository
        """
        if len(options['repo']) == 0:
            raise subprocess.CalledProcessError(-1, options['type'], output="You must enter a repository name as an  argument")
        if len(options['repo'].split()) == 1:
            return
        else:
            raise subprocess.CalledProcessError(-2, options['type'], output="Number of arguments should be 1")

    @staticmethod
    def check_args_message(options):
        """
        Checks for the number of arguments for message to commit
        """
        if len(options['message']) == 0:
            raise subprocess.CalledProcessError(-1, options['type'], output="You must enter a message in order to commit")
        else:
            return

    @staticmethod
    def gitcommit(options):
        """
        Calls git commit
        """
        Wrapper.check_args_message(options)
        git_command = Wrapper.git_cmd()[:]

        git_command.append('commit')
        git_command.append('-a')
        git_command.append('-m')
        git_command.append(options["message"])

        return call_popen(git_command)

    @staticmethod
    def gitpull(options):
        """
        Calls git pull
        """
        Wrapper.check_args_repo(options)
        git_command = Wrapper.git_cmd()[:]

        git_command.append('pull')
        git_command.append(options["repo"])

        return call_popen(git_command)

    @staticmethod
    def gitpush(options):
        """
        Calls git push
        """
        Wrapper.check_args_repo(options)
        git_command = Wrapper.git_cmd()[:]

        git_command.append('push')
        git_command.append(options["repo"])

        return call_popen(git_command)

    @staticmethod
    def gitclone(options):
        """
        Calls git clone
        """
        Wrapper.check_args_repo(options)
        git_command = Wrapper.git_cmd()[:]

        git_command.append('clone')
        git_command.append(options["repo"])

        return call_popen(git_command)
