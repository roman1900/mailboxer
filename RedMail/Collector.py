class Collector:
    def __init__(self,mailConnector):
        self.mailConnector = mailConnector
        self.deltalink = None
        self.request_configuration = self.mailConnector.client.users.delta.DeltaRequestBuilderGetRequestConfiguration()
        self.request_configuration.headers.add("Prefer", "odata.maxpagesize=2")
        self.request_configuration.headers.add("Prefer", "IdType=\"ImmutableId\"")

    async def get_mail_by_id(self,user_id):
        return await self.mailConnector.client.users.by_user_id(user_id).mail_folders.by_mail_folder_id("Inbox").messages.get(request_configuration = self.request_configuration)
    async def get_delta_by_id(self,user_id):
        if self.deltalink is not None:
            result = await self.mailConnector.client.users.by_user_id(user_id).mail_folders.by_mail_folder_id("Inbox").messages.delta.with_url(self.deltalink).get(request_configuration = self.request_configuration)
        else:
            result = await self.mailConnector.client.users.by_user_id(user_id).mail_folders.by_mail_folder_id("Inbox").messages.delta.get(request_configuration = self.request_configuration)
        self.deltalink = result.odata_delta_link
        return result