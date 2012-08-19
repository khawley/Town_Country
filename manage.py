#!/usr/bin/env python
import os
os.environ.setdefault('LANG','en_US')

import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Town_Country.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
