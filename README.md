# Mailboxer

Mailboxer intends to be a provider agnostic mailbox management suite. It will initially ship with Microsoft 365 bindings.
Mailboxer will provide interfaces to:
- read new mail
- send mail
- maintain a conversation thread

How to use the Mail Collector:
Firstly you'll need to publish this as an enterprise app in Azure (Entra ID). You need Mail.ReadAll

This will give you a client id, tenant id, and client secret.

create a config.yml file with:
```
client_id: "client_id_from_above"

tenant_id: "tenant_id_from_above"

client_secret: "client_secret_from_above"
```

Next build the docker image:

docker build . -t mailcollector

docker run -p 5000:5000 mailcollector

point your browser at http://localhost:5000/get

Note: This is intended to be run as a service which is only accessible from a secure private network. **Do not place this in an internet facing server, or all your email can be read.**

