from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    #context = {'my_list' : [{'restaurant_name': ['Pizza Hut', 'Dunkin Donuts', 'KFC']},
    #                        {'food_type': ['Pizza', 'Donuts', 'Fried Chicken'}]]}


    context = {'my_list':
                        [{'restaurant_name': 'kfc',
                         'food_type': 'chicken'},

                         {'restaurant_name': 'pizza hut',
                         'food_type': 'pizza'},

                         {'restaurant_name': 'dunkin donuts',
                          'food_type': 'donuts'}
                                            ]}
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {'my_object':
                            {'restaurant_name': 'pizza hut',
                             'food_type': 'pizza'}

    }
    return render(request, 'detail.html', context)
