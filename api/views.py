from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from api.models import VersionDescriptionHtml, VersionMinecraft, VersionDescription


@api_view(['GET'])
def getDescription(request, type, version):
    version = VersionMinecraft.objects.filter(version=version)
    if version:
        data_model = VersionDescription.objects.filter(types=type, version=version[0])
        if data_model:
            description = data_model[0].description.__dict__
            description.pop('_state')
            description.pop('id')
            description['b_text'] = [text.strip() for text in description['b_text'].split('\n')]
            return Response(description)

    return Response({"error": "not founded!"}, status=status.HTTP_404_NOT_FOUND)