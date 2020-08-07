import os
import sys
import argparse

from django.core.management import execute_from_command_line

os.environ['DJANGO_SETTINGS_MODULE'] = 'wagtail_text_to_speech.tests.demosite.settings'

def runtests():
    args, rest = argparse.ArgumentParser().parse_known_args()

    argv = [sys.argv[0], 'test'] + rest
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
