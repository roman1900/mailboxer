class Reader:
    def __init__(self,mailCollection):
        self.mailCollection = mailCollection
    def print_mail_subject(self):
        for email in self.mailCollection.value:
            print(email.subject)
    def mail_subject_list(self):
        slist = []
        for email in self.mailCollection.value:
            slist.append(email.subject)
        return slist
    def print_mail_full(self):
        for email in self.mailCollection.value:
            print(email)