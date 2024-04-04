import json
from datetime import datetime
import sys

try:
    file = sys.argv[1]
    if file:
        data = json.load(open(file))
        dt_obj = datetime.fromtimestamp(1545730073)

        message = ''
        for message_object in data['messages']:
            dt_obj = datetime.fromtimestamp(int(message_object['timestamp_ms'])/1000)
            date = str(dt_obj).split(" ")[0]
            time = str(str(dt_obj).split(" ")[1]).split(".")[0]
            date_safe = '{0}, {1}'.format(date,time)
            if 'content' in message_object:
                if 'share' in message_object and 'link' in message_object['share']:
                    formatter_message = '[{0}] {1}: {2} ({3})\n'.format(date_safe, message_object['sender_name'], message_object['content'], message_object['share']['link'])
                else:
                    formatter_message = '[{0}] {1}: {2}\n'.format(date_safe, message_object['sender_name'], message_object['content'])
                message += formatter_message

        with open("Generated.txt", "w", encoding="utf-8") as text_file:
            text_file.write(message)
            print('[*] File Generated Successfully!!')
except:
    print('[-] Provide json Filename/filepath! eg. python script.py <filename>')



