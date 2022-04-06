from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

