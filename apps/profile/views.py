from django.shortcuts import render

from apps.profile.forms import ProfileForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def profile_view(request):
    profile = request.user
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            profile = form.save(commit=False)

            profile.save()

            msg = "Profile Updated successfully."

        else:
            msg = 'Error validating the form'

    return render(request, "home/settings.html", {"form": form, "msg": msg})
