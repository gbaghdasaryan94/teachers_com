# This is runner script
# User should be able to pass environment, browser name, page(s) arguments
# Give mechanism to get corresponding arguments within tests

import argparse
import os
import subprocess

# have choices to tell about options
parser = argparse.ArgumentParser(description='')
parser.add_argument('--env', type=str, default='new', help='Input environment', choices=['new', 'live'])
parser.add_argument('--browser', type=str, default='chrome', help='Input browser', choices=['firefox', 'chrome'])
parser.add_argument('--page', type=str, default='', help='Input page', choices=['login', 'class', 'add_student'])
parser.add_argument('--group', type=str, default='', help='Input page', choices=['smoke'])
parser.add_argument('--case', type=str, default='', help='Input page')

args = parser.parse_args()

url_add = {"new": "new", "live": "www"}

base_url = 'https://{}.typing.com'.format(url_add[args.env])

os.environ["ENV"] = args.env
os.environ["BROWSER"] = args.browser
os.environ["URL"] = base_url

bashCommand = f"pytest tests/{args.page}_page_test.py --html={args.page}_report.html"
if args.group:
    bashCommand = f'pytest -m {args.group} --html={args.group}_report.html'
if args.case:
    bashCommand = f'pytest -k {args.case} --html={args.case}_report.html'

process = subprocess.call(bashCommand.split(' '))
