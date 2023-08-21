from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import paginator
from django.template.loader import render_to_string

from apps.logus.models import BookedRoomModel

NEWS_COUNT_PER_PAGE = 5


def pagination(request):
    global patient
    page = int(request.GET.get('page', 1))
    posts = BookedRoomModel.objects.all().order_by('id')
    p = paginator.Paginator(posts,
                            NEWS_COUNT_PER_PAGE)
    try:
        post_page = p.page(page)
    except paginator.EmptyPage:
        post_page = paginator.Page([], page, p)

    if not request.is_ajax():
        return render(request,
                      'Hospital/patients-my-patients.html', {'patients': post_page})
    else:
        content = ''
        for patient in post_page:
            content += render_to_string('Hospital/patients-my-patients.html',
                                        {'patients': patient},
                                        request=request)
        print(patient)
        print(">>>>>>>>>>>>>>>>")
        # print(content)
        return render(request, 'Hospital/patients-my-patients.html', {
            'room': patient,
            "content": content,
            "end_pagination": True if page >= p.num_pages else False,
        })

