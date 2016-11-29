from Sender import Main
import sys

main = Main.Main()

# set verifying key, json data, template parameter
# edit the parameters (smtp login)

main.setSMTP(sys.argv[1],sys.argv[2])

# edit the parameters (verifying key, json data, html template) - string

# main.setInfor(yourVarifingKey,'{"sender":yourEMAIL, "receiver":othersEMAIL, "subject":SUBJECT}',HTMLparams)
main.setInfor(sys.argv[3],sys.argv[4],sys.argv[5])

main.run()