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
    address = request.args.get("address")
    if address is None:
        return HTTPResponse(body = "address must be provided", status=500)
    mailCollection = await mailCollector.get_delta_by_id(address)
    reader = Reader.Reader(mailCollection)
    return json(reader.mail_subject_list())

