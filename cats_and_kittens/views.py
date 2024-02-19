import random
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import MomCat, Kitten

from django.core.serializers import serialize

from django.shortcuts import render, redirect
from .forms import MomCatForm, KittenForm

import logging

def generate_random_name(prefix):
    return f'{prefix}_{random.randint(1, 100000)}'

class CatsAndKittensView(View):
    def get(self, request):
        # Retrieve all MomCat instances along with associated Kitten instances
        cats = MomCat.objects.prefetch_related('kittens').all()

        # Serialize the queryset to JSON
        data = []
        for momcat in cats:
            momcat_name = momcat.name
            momcat_age = momcat.age
            momcat_owner = momcat.owners_name
            momcat_kittens = momcat.kittens.all()
            kittens = []
            for kitten in momcat_kittens:
                kittens.append([kitten.name, kitten.age_in_months]) 
            data.append([momcat_name, momcat_age, momcat_owner, kittens])

        return JsonResponse(data, safe=False)

    def post(self, request, num = 0):
        for _ in range(num):
            momcat_form = MomCatForm({
                'name': generate_random_name('MomCat'),
                'age': random.randint(1, 15),
                'owners_name': generate_random_name('Owner'),
            })

            logger = logging.getLogger('django')


            momcat = momcat_form.save()
            logger.debug(f"num = {num}")
            logger.debug(f"momcat_id = {momcat.id}")

            num_kittens = random.randint(0, 10)
            for _ in range(num_kittens):
                kitten_form = KittenForm({
                    'name': generate_random_name('Kitten'),
                    'age_in_months': random.randint(1, 12),
                    'momcat': momcat,
                })

                if kitten_form.is_valid():
                    kitten = kitten_form.save(commit=False)
                    kitten.momcat = momcat  # Set the momcat field
                    kitten.save()

        momcat_form = MomCatForm(prefix='momcat')
        kitten_form = KittenForm(prefix='kitten')   
        return render(request, 'create_cats_and_kittens.html', {'momcat_form': momcat_form, 'kitten_form': kitten_form})
