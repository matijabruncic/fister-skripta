import os

from src.parsing import LineParsers
from src.model.Log import Log
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input_file', type=str, help='Input file')
parser.add_argument('output_file', type=str, help='Output file')
parser.add_argument("-v", "--verbose", help="modify output verbosity", action = "store_true")
args = parser.parse_args()

input_file = open(os.path.abspath(args.input_file), 'r')
output_file = open(os.path.abspath(args.output_file), "w+")

lines_in_file = input_file.readlines()

logs = []
count = 0
filters = LineParsers.get_all_filters()
for line in lines_in_file:
    if any(ext in line for ext in filters):
        try:
            parser = LineParsers.create_parser(line)
            count = count + 1
            logs.append(Log(count, parser))
        except Exception as e:
            print(line)
            raise

logs.sort(key=lambda x: x.action, reverse=False)

for log in logs:
    if args.verbose:
        print('%s %s %s %s %s %s' % (log.get_date(), log.action, log.get_hour(), log.user, log.ip_address, log.get_description_without_spaces()))
    output_file.write('%s %s %s %s %s %s' % (log.get_date(), log.action, log.get_hour(), log.user, log.ip_address, log.get_description_without_spaces()))
    output_file.write("\n")
output_file.close()
