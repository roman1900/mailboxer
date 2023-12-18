from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from RedMail.Base.Connector import Connector

class M365Connector(Connector):
    def __init__(self,config):
        self.client = self.connect(config)

    def connect(self,config):
        credential = ClientSecretCredential(config["client_id"],
                                            config["tenant_id"],
                                            config["client_secret"])
        scopes = ["https://graph.microsoft.com/.default"]
        return GraphServiceClient(credentials=credential, scopes=scopes)

