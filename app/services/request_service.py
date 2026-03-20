

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
                    <Session.getDocumentRq />
                    <Session.closeRq />
                </requests>
            </server>
        """
        },
    "manuscript_get_value": {
        "name": "Manuscript Get Value",
        "template": 
        """
            <server>
                <requests>
                    <Session.loginRq userName="admin" password="admin" />
                    <OnlineData.loadPolicyRq policyID="2" />
                    <OnlineData.loadHistoryRq historyID="2" var.manuScriptID = "@manuScriptID" />
                    <ManuScript.getValueRq field="data.TotalResult" manuscript="~manuScriptID~" />
                    <Session.closeRq />
                </requests>
            </server>
        """
        },
    "get_session": {
        "name": "Get Session",
        "template": 
        """
            <server>
                <requests>
                    <Session.resumeRq sessionID="7977960C:76B74042:ADC860EB:32FD8D0D:7A35FE0D:48E90C4C" />
                    <Session.getDocumentRq />
                </requests>
            </server>
        """
        },
    "rollback/abort": {
        "name": "Rollback/Abort",
        "template": 
        """
            <server>
                <requests>
                    <Session.loginRq userName="admin" password="admin" />
                    <OnlineData.loadPolicyRq policyID="865010" />
                    <Session.getElementRq path="//policyAdmin/transactions/transaction[last()]/HistoryID" var.lastHistoryID="@value"/>
                    <TransACT.rollbackTransactionRq historyID="~lastHistoryID~" />
                    <TransACT.abortTransactionRq historyID="~lastHistoryID~" allowCheckoutOverride="1" />
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
        
    