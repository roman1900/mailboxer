from RedMail import Collector,Connector,Reader
from sanic import Sanic, Request, json
from sanic.response import HTTPResponse, text
import yaml

app = Sanic(__name__)

with open('config.yml','r') as file:
    config = yaml.safe_load(file)
    mailConnector = Connector.Connector(config['client_id'],config['tenant_id'],config['client_secret'])
mailCollector = Collector.Collector(mailConnector)

@app.get("/ping")
def ping(request: Request):
    return text("pong!")

@app.get("/get")
async def get(request: Request):
    mailCollection = await mailCollector.get_delta_by_id("mmarschall@105patrickstreet.onmicrosoft.com")
    reader = Reader.Reader(mailCollection)
    return json(reader.mail_subject_list())

