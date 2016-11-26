from Sender import Main

main= Main.Main()

##set verifying key, json data, template parameter
##edit the parameters
main.setSMTP(yourID,yourPASSWORD)
##edit the parameters
main.setInfor( "2432",'{"sender":yourEMAIL, "receiver":othersEMAIL, "subject":"hello_world!"}',"1")
main.run()