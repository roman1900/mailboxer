from RedMail.M365.Parser import M365Parser
from RedMail.M365.Connector import M365Connector
from RedMail.M365.Collector import M365Collector
from sanic import Sanic, Request, json
from sanic.response import HTTPResponse, text
import yaml

app = Sanic(__name__)

with open('config.yml','r') as file:
    config = yaml.safe_load(file)
    mailConnector = M365Connector(config)
mailCollector = M365Collector(mailConnector)

@app.get("/ping")
def ping(request: Request) -> HTTPResponse:
    return text("pong!")

@app.get("/get")
async def get(request: Request) -> HTTPResponse:
    address = request.args.get("address")
    if address is None:
        return HTTPResponse(body = "address must be provided", status=500)
    mailCollection = await mailCollector.get_inbox_changes(address)
    parser = M365Parser(mailCollection)
    return json(parser.mail_subject_list())

