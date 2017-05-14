import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.aggregates.general import ArrayAgg

from .models import Laptime, Car, Track
from .forms import LaptimesForm


def laptimes(request):
    laptimes_with_diffs = []
    sectors = 0
    form = LaptimesForm(request.GET or None)
    if form.is_valid():
        track = get_object_or_404(Track, name=form.cleaned_data['track'],
                                  layout=form.cleaned_data['layout'])
        car = get_object_or_404(Car, brand=form.cleaned_data['brand'],
                                model=form.cleaned_data['model'])
        laptimes = Laptime.objects.filter(track=track, car=car) \
                                  .order_by('user', 'time') \
                                  .distinct('user') \
                                  .values_list('id', flat=True)
        laptimes = Laptime.objects.filter(id__in=laptimes) \
                                  .order_by('time').all()
        for index, laptime in enumerate(laptimes):
            if index > 0:
                diff = laptime.diff_repr_from(laptimes[index-1])
            else:
                diff = 0
            laptimes_with_diffs.append((laptime, diff))
        sectors = track.sectors

        paginator = Paginator(laptimes_with_diffs, 10)
        page = request.GET.get('page')
        try:
            laptimes_with_diffs = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            laptimes_with_diffs = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            laptimes_with_diffs = paginator.page(paginator.num_pages)

    models_per_brand = dict(Car.objects.values('brand')
                            .annotate(models=ArrayAgg('model'))
                            .values_list('brand', 'models'))
    layouts_per_track = dict(
        Track.objects.exclude(layout=None).values('name')
        .annotate(layouts=ArrayAgg('layout'))
        .values_list('name', 'layouts'))

    context = dict(laptimes=laptimes_with_diffs, track_sectors=range(sectors),
                   form=form, models_per_brand=json.dumps(models_per_brand),
                   layouts_per_track=json.dumps(layouts_per_track))
    return render(request, 'laptimes/laptimes.html', context=context)
