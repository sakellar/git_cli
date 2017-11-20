import subprocess
from subprocess import (
    call,
    Popen,
    PIPE
)
import argparse


class Parser:
     pass

class CommandExecutor:

    def __init__(self):
        parser = argparse.ArgumentParser(description='Process some integers.')

process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print output
process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
output = process.communicate()[0]
