from flask import Blueprint, request

from api.service.CampaignService import CampaignService


campaign_route = Blueprint("campaign_route", __name__)

campaign_service = CampaignService()

@campaign_route.route("/", methods = ['POST', 'GET'])
def get_campaign():

    if request.method == 'GET':
        campaigns = campaign_service.getCampaigns()
        return campaigns

    if request.method == 'POST':
        data = request.json
        return campaign_service.createCampaigns(data)


