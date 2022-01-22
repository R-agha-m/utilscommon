from subprocess import run, STDOUT, PIPE


def run_command(command, raise_error=True):
    completed_process = run(command,
                            shell=False,
                            # capture_output=True,
                            text=True,
                            stdout=PIPE,
                            stderr=STDOUT)

    stdout = completed_process.stdout

    if raise_error:
        completed_process.check_returncode()

    return stdout
