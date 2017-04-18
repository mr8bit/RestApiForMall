from .models import UserPhoto
from .forms import ImageUploadForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage


@csrf_exempt
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = UserPhoto(photo=form.cleaned_data['image'], email=form.cleaned_data['email'])
            m.save()
            msg = EmailMessage('Фото с норы', 'Фаше фото с терминала',  settings.EMAIL_HOST_USER, [m.email])
            msg.content_subtype = "html"
            msg.attach_file(m.photo.path)
            msg.send()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')
