from flask import jsonify
from api.helper.db import db
from api.model.Campaign import CampaignModel


class CampaignService:

    def getCampaigns(self):
        campaigns = CampaignModel.query.all()
        results = [
            {
                "name": campaign.name,
                "active": campaign.active,
            } for campaign in campaigns]

        return {"status": "success", "data": results}


    def createCampaigns(self, data):
        new_campaign = CampaignModel(name=data['name'], active=True)
        db.session.add(new_campaign)
        db.session.commit()
        result = {"status": "success", "message": f"Campaign {new_campaign.name} has been created successfully."}
        return jsonify(result)