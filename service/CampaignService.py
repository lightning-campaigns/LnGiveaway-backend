from flask import jsonify


class CampaignService:

    def getCampaigns(self):
        result = {"status": "success"}
        return jsonify(result)

    def createCampaigns(self, data):
        result = {"status": "success"}
        return jsonify(result)