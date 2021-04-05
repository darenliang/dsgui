import platform
import subprocess

shell_opt = True if platform.system() == "Windows" else False


def Popen(opts):
    return subprocess.Popen(
        opts,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        universal_newlines=True,
        shell=shell_opt
    )


def run(opts):
    return subprocess.run(
        opts,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        shell=shell_opt
    )
