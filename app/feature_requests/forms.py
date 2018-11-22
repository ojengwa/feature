from wtforms_alchemy import ModelForm
from app.models import FeatureRequest


class FeatureRequestForm(ModelForm):
    
    class Meta:
        model = FeatureRequest