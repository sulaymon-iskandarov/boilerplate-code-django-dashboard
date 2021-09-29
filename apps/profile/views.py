from django.shortcuts import render, redirect


from apps.profile.forms import ProfileForm
from apps.profile.models import Profile


def profile_view(request):

    profile = request.user

    form = ProfileForm(request.POST or None, instance=profile)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            profile = form.save(commit=False)

            profile.save()

            msg = "Profile Updated successfully."

        else:
            msg = 'Error validating the form'

    return render(request, "home/settings.html", {"form": form, "msg": msg})