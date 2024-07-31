from django.utils import translation
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models.blocks_and_departments_model import Block, Department
from .serializers.blocks_and_departments_serializer import BlockSerializer, BlockDetailSerializer, DepartmentSerializer
from .models.general_structure_model import GeneralStructure
from .serializers.general_structure_serializer import GeneralSerializer
from rest_framework.views import APIView
from .models.banners_model import Banner
from .serializers.banners_serializer import BannerSerializer
from .models.counters_model import Counter
from .serializers.counters_serializer import CounterSerializer
from ..data.models.news_model import New
from ..data.serializers.news_serializers import NewSerializer
from .models.about_us_models import (AboutUs,
                                     Charter,
                                     Directorate,
                                     History)
from .serializers.about_us_serializers import (CharterSerializer,
                                               DirectorateSerializer,
                                               HistorySerializer,
                                               AboutUsSerializer)
from .models.contacts_model import Contacts
from .serializers.contacts_serializer import ContactSerializer
from .models.scientific_activity_models import ScientificActivity
from .serializers.scientific_activity_serializers import ScientificActSerializer
from apps.main_page.models.resources_model import Journal, Report, Link
from apps.main_page.serializers.resources_serializer import JournalSerializer, ReportSerializer, LinkSerializer



# scientific activity
class ScientificActivityView(APIView):
    def get(self, request, *args, **kwargs):
        data = ScientificActSerializer(ScientificActivity.objects.all(), many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class AboutUsView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class HistoryView(ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class CharterView(ListAPIView):
    queryset = Charter.objects.all()
    serializer_class = CharterSerializer


class DirectorateView(ListAPIView):
    queryset = Directorate.objects.all()
    serializer_class = DirectorateSerializer


# main_page
class BannerView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'banner': BannerSerializer(Banner.objects.all(), many=True).data,
        }
        return Response(data=data, status=status.HTTP_200_OK)


class CounterView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'counter': CounterSerializer(Counter.objects.all(), many=True).data,
        }
        return Response(data=data, status=status.HTTP_200_OK)


class NewsMainPageView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'news': NewSerializer(New.objects.all(), many=True).data[:3],
        }
        return Response(data=data, status=status.HTTP_200_OK)


class ContactsView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'contacts': ContactSerializer(Contacts.objects.all(), many=True).data
        }
        return Response(data=data, status=status.HTTP_200_OK)


# blocks and department
class BlockListAPIView(ListAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

class BlockRetrieveAPIView(RetrieveAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockDetailSerializer 

class DepartmentRetrieveAPIView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer  
    
# generalstructure 
class GeneralAPIView(ListAPIView):
    queryset = GeneralStructure.objects.all()
    serializer_class = GeneralSerializer

class GeneralRetrieveAPIView(RetrieveAPIView):
    queryset = GeneralStructure.objects.all()
    serializer_class = GeneralSerializer 

# resource Journal
class JournalListAPIView(ListAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalRetrieveAPIView(RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer 

# resource Report
class ReportListAPIView(ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportRetrieveAPIView(RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer 

# resource Link

class LinkListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class LinkRetrieveAPIView(RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer 
