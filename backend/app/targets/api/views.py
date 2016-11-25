from app.api.views import ListCreateView, ReadUpdateDeleteView
from app.targets.api.schemas import TargetSchema
from app.targets.models import Target


class TargetsList(ListCreateView):
    model = Target
    schema = TargetSchema


class TargetSingle(ReadUpdateDeleteView):
    model = Target
    schema = TargetSchema
