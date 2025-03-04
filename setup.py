from __future__ import annotations

from setuptools import setup
import re


def derive_version() -> str:
    with open('pyvolt/__init__.py') as f:
        match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
        if match is None:
            raise RuntimeError('Version was not found')
        version: str = match.group(1)

    if not version:
        raise RuntimeError('Version is not set')

    if version.endswith(('a', 'b', 'rc')):
        # Append version identifier based on commit count
        try:
            import subprocess

            p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, _ = p.communicate()

            if out:
                version += out.decode('utf-8').strip()

            p = subprocess.Popen(
                ['git', 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            out, _ = p.communicate()
            if out:
                version += '+g' + out.decode('utf-8').strip()
        except Exception:
            pass

    return version


with open('README.rst', 'r') as fp:
    long_description = fp.read()

setup(version=derive_version(), long_description=long_description)
