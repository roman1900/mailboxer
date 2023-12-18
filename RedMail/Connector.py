from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient

class Connector:
    def __init__(self,client_id,tenant_id,client_secret):
        credential = ClientSecretCredential(client_id,
                                            tenant_id,
                                            client_secret)
        scopes = ["https://graph.microsoft.com/.default"]
        self.client = GraphServiceClient(credentials=credential, scopes=scopes)