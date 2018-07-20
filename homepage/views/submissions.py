from django.conf import settings
from homepage.models import *
from django_mako_plus import view_function
@view_function
def process_request(request):

    submissions = Submission.objects.all()
    return request.dmp.render('submissions.html', {'submissions': submissions})
