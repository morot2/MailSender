from bs4 import BeautifulSoup
import codecs,pickle

class EditHTML:
    verifyKey=''
    templateId=''

    def setVerifyKey(self,verifyKey):
        self.verifyKey=verifyKey

    def setTemplateId(self, templateId):
        self.templateId=templateId

    def editHTML(self):
        # edit html to insert verifying key
        htmlFile = codecs.open('./template/template'+self.templateId+'.html','r','utf-8')
        html = htmlFile.read()
        soup = BeautifulSoup(html, 'html.parser')
        soup.mark.string = self.verifyKey
        htmlFile.close()

        # write edited html
        editFile = codecs.open('./template/template'+self.templateId+'.html','w','utf-8')
        editFile.write(soup.prettify())
        editFile.close()