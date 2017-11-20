from ExecuteCommand import call_popen


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
        git_command = ['git']
        return git_command

    @staticmethod
    def _add_git_argument(git_command, options, argument):
        if argument in options:
            git_command.append(formated_arg)
            git_command.append(options[argument])

    @staticmethod
    def gitpush(options):
        git_command = Wrapper.git_cmd()[:]

        git_command.append('push')
        git_command.append('origin')
        git_command.append(options["branch"])

    @staticmethod
    def gitpull(options):
        git_command = Wrapper.git_cmd()[:]

        git_command.append('pull')
        git_command.append('origin')
        git_command.append(options["branch"])

    @staticmethod
    def gitcommit(options):
        git_command = Wrapper.git_cmd()[:]

        git_command.append('commit')
        git_command.append(options['file'])
        git_command.append('-m')
        git_command.append("message")

    @staticmethod
    def gitclone(options):
        """
        Calls git backup
        """
        git_command = Wrapper.git_cmd()[:]

        git_command.append('clone')
        git_command.append(options["repo"])

        return call_popen(git_command)
