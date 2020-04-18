from script import LineParsers
from script.model.Log import Log


input_file = open('/home/mbruncic/PycharmProjects/fister-skripta/resources/input/16-4.txt', 'r')
output_file = open("/home/mbruncic/PycharmProjects/fister-skripta/resources/output/mbruncic-final.txt", "w+")

lines_in_file = input_file.readlines()

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

for log in logs:
    print('%s %s %s %s %s %s' % (log.get_date(), log.action, log.get_hour(), log.user, log.ip_address, log.get_description_without_spaces()))
    output_file.write('%s %s %s %s %s %s' % (log.get_date(), log.action, log.get_hour(), log.user, log.ip_address, log.get_description_without_spaces()))
    output_file.write("\n")
output_file.close()
