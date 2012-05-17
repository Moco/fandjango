import logging

from django.http import HttpResponse
from utils import redirect_to_facebook_authorization, parse_signed_request
from settings import FACEBOOK_APPLICATION_URL, FACEBOOK_APPLICATION_SECRET_KEY
from django.views.decorators.csrf import csrf_exempt

from models import User


def authorize_application(request):
    """
    Redirect to Facebook authorization, then redirect back to the value of the 'redirect_uri' query string
    or default to FACEBOOK_APPLICATION_URL.
    """
    return redirect_to_facebook_authorization(
        redirect_uri=request.GET['redirect_uri'] if 'redirect_uri' in request.GET else FACEBOOK_APPLICATION_URL
    )


@csrf_exempt
def deauthorize_application(request):
    """
    When a user deauthorizes an application, Facebook sends a HTTP POST request to the application's
    "deauthorization callback" URL. This view picks up on requests of this sort and marks the corresponding
    users as unauthorized.
    """
    
    # not sure why, but I didn't get any data in the post request
    if not request.POST.get('signed_request', None):
        logging.error("Facebook deauthorization callback didn't contain a signed_request ?")
        logging.error(request.POST)
        return HttpResponse()

    data = parse_signed_request(request.POST['signed_request'], FACEBOOK_APPLICATION_SECRET_KEY)
    
    user = User.objects.get(facebook_id=data['user_id'])
    user.authorized = False
    user.save()
    
    return HttpResponse()
