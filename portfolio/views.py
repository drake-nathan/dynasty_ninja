from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .make_graph import make_graph
import json
import requests


def home(request):
    return render(request, 'portfolio/home.html')

@login_required
def portfolio(request):
    # call main function via graph function
    context_graph, pretty_string, total_num_of_players = make_graph(request.user.username)
    # pass context to django template
    context = {
        'graph': context_graph,
        'league_string': pretty_string,
        'total_num_of_players': total_num_of_players
    }
    return render(request, 'portfolio/portfolio.html', context)

# frontend lib: recharts
def get_graph(request):
    context_graph, pretty_string, total_num_of_players = make_graph(request.user.username)
    data = json.dumps(context_graph)  # this may not be necessary, I think there is a JsonResponse type that accepts a dict
    return requests.Response(data=data)


def showcase(request):

    context_graph, pretty_string, total_num_of_players = make_graph('nastynateff')
    
    context = {
        'graph': context_graph,
        'league_string': pretty_string,
        'total_num_of_players': total_num_of_players
    }
    return render(request, 'portfolio/showcase.html', context)