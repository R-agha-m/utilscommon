from subprocess import run, STDOUT, PIPE


def run_command(command,
                raise_error=True,
                shell=False):
    completed_process = run(command,
                            shell=shell,
                            # capture_output=True,
                            text=True,
                            stdout=PIPE,
                            stderr=STDOUT)

    stdout = completed_process.stdout

    if raise_error:
        completed_process.check_returncode()

    return stdout
