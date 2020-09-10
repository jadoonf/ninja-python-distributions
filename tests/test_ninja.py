
import pytest
import subprocess

import ninja

from . import push_argv


def _run(program, args):
    func = getattr(ninja, program)
    args = ["%s.py" % program] + args
    with push_argv(args), pytest.raises(SystemExit) as excinfo:
        func()
    assert 0 == excinfo.value.code


def test_ninja_module():
    _run("ninja", ["--version"])


def test_ninja_package():
    subprocess.check_call(["python", "-m", "ninja", "--version"])
