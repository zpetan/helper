import typer
import os
import subprocess
from getpass import getpass

app = typer.Typer()


def is_root():
    return os.geteuid() == 0


@app.command(name="battery", help="Fixes slow CPU on battery power by adjusting battery settings.")
def fix_slow_cpu_with_battery() -> None:
    """Fixes slow CPU on battery power by adjusting battery settings.
    """
    
    args = "sudo wrmsr 0x1FC value".split()
    kwargs = dict(stdout=subprocess.PIPE,
                  encoding="ascii")
    
    subprocess.run(args, **kwargs)
    
    print("Fixed slow CPU when on battery.")

