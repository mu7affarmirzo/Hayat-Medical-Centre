# views.py
from rest_framework import generics

from apps.lis.models.lab_researchs import LabResearchCategoryModel
from ..serializers.labs import LabResearchCategorySerializer


class LabResearchCategoryListAPIView(generics.ListAPIView):
    queryset = LabResearchCategoryModel.objects.all()
    serializer_class = LabResearchCategorySerializer
