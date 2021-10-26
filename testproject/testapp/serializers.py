
from .models import testtable
from rest_framework.serializers import ModelSerializer


class lawSerializers(ModelSerializer):

      class Meta:
          model=testtable
          fields=('id','caseId','caseSection','caseDetails','caseType','userName')