from RedMail.Base.Parser import Parser
from RedMail.Base.Email import Email

class M365Parser(Parser):
    def __init__(self,emailBundle):
        self.emailBundle = emailBundle
    def print_mail_subject(self):
        for email in self.emailBundle.value:
            print(email.subject)
    def mail_subject_list(self):
        slist = []
        for email in self.emailBundle.value:
            slist.append(email.subject)
        return slist
    def print_mail_full(self):
        for email in self.emailBundle.value:
            print(email)

    def parse_subject_list(self)-> list:
        return []
    
    def parse_email(self,email: object)-> Email:
        return Email()
    
    def parse_all_email(self)-> list[Email]:
        result = []
        for email in self.emailBundle:
            result.append(self.parse_email(email))
        return result

