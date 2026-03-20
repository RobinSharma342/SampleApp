

requests = {
    "load_policy": {
        "name": "Load Policy",
        "template": 
        """
            <server>
                <requests>
                    <Session.loginRq userName="admin" password="admin" />
                    <OnlineData.loadPolicyRq policyID="2" />
                    <OnlineData.loadHistoryRq historyID="2" />
                    <Session.closeRq />
                </requests>
            </server>
        """
        },
    "load_config": {
        "name": "Load Config",
        "template": 
        """
            <server>
                <requests>
                    <Session.loginRq userName="admin" password="admin" />
                    <Settings.getServerRootPathRq var.rootPath="@path" />
                    <ScriptLibrary.loadDocumentRq xmlFileName="~rootPath~\Shared\Server.config" />
                    <ScriptLibrary.loadDocumentRq xmlFileName="~rootPath~\Web\Web.config" />
                    <Session.closeRq />
                </requests>
                </server>
        """
        }
}

def get_service_request(request_type):
    request_template = requests.get(request_type).get("template")
    print(f"Request Type: {request_type}, Template: {request_template}")
    return request_template 
        
    