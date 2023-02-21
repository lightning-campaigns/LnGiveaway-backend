from api.helper.db import db


class CampaignModel(db.Model):
    __tablename__ = "campaigns"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, name, active):
        self.name = name
        self.active = active


    def __repr__(self):
        return f"<Campaign {self.name}>"