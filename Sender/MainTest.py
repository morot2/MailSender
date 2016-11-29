from Sender import Main

main= Main.Main()

##set verifying key, json data, template parameter
##edit the parameters (smtp login)
main.setSMTP(yourID,youPW)
##edit the parameters (verifying key, json data, html template) - string
main.setInfor(yourVarifyingKey,'{"sender":yourEMAIL, "receiver":othersEMAIL, "subject":yourSUBJECT}',HTMLtemplate)
main.run()