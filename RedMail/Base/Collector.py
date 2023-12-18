from RedMail.Base.Connector import Connector
class Collector:
    def __init__(self,connector: Connector):
        self.Connector = connector
    async def get_inbox(self,user_id):
        pass
    async def get_inbox_changes(self,user_id):
        pass