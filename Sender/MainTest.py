import sys
from Sender import Main

main = Main.Main()

# set verifying key, json data, template parameter
# edit the parameters (smtp login)

main.setSMTP("id", "pw")

# edit the parameters (verifying key, json data, html template) - string

main.run('{"htmlId":"2","verifyingKey":"3333","sender":"analysiser@naver.com", "receiver":"analysiser@naver.com", "subject":"hello"}')