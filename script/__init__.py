from script import LineParsers
from script.model.Log import Log

file1 = open('/home/mbruncic/PycharmProjects/fister-skripta/resources/input/16-4.txt', 'r')
lines_in_file = file1.readlines()

filtered_lines = [
    'Session Type: SSL',
    'Session Type: AnyC',
    '.anyconnect.devicetype',
    'Invalid password']

logs = []
count = 0
for line in lines_in_file:
    if any(ext in line for ext in filtered_lines):
        try:
            parser = LineParsers.create_parser(line)
            count = count + 1
            logs.append(Log(count, parser))
        except Exception as e:
            print(line)
            raise

logs.sort(key=lambda x: x.action, reverse=False)

output_file = open("/home/mbruncic/PycharmProjects/fister-skripta/resources/output/mbruncic-final.txt", "w+")
for log in logs:
    print('%s %s %s %s %s %s' % (log.get_date(), log.action, log.get_hour(), log.user, log.ip_address, log.get_description_without_spaces()))
    output_file.write('%s %s %s %s %s %s' % (log.get_date(), log.action, log.get_hour(), log.user, log.ip_address, log.get_description_without_spaces()))
    output_file.write("\n")
output_file.close()
