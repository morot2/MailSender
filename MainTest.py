import sys

import Main

main = Main.Main()

# set verifying key, json data, template parameter
# edit the parameters (smtp login)

main.setSMTP(sys.argv[1], sys.argv[2])

# edit the parameters (verifying key, json data, html template) - string

main.run('{"htmlId":"2","verifyingKey":"3333","sender":"analysiser@naver.com", "receiver":"analysiser@naver.com", "subject":"welcome!"}')