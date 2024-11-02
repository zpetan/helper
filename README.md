# helper

A CLI tool to run shell scripts for convenience.

- `helper fix battery`: Runs `sudo wrmsr 0x1FC value` to fix slow CPU when on battery power (using third party battery on Thinkpad X270)

## Install
Build package (e.g. using `uv`):
`uv build`

Install wheel file
`pip install --user dist/...whl`

Check installation:
`helper fix --help`
