import subprocess

def call_popen(command, live_logging=True):
    """
    Calls subprocess Popen command args passed as an array
    Example: command = ['ls', '-la']
    """
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = []
    for line in iter(process.stdout.readline, ''):
        if line.strip():
            output.append(line)
            if live_logging:
                print line,
    output = "".join(output)
    process.wait()
    ret_code = process.poll()
    if ret_code:
        raise subprocess.CalledProcessError(ret_code, command, output=output)
    return ret_code, command, output

#command = ['git', 'branch', '-a']
#call_popen(command)
