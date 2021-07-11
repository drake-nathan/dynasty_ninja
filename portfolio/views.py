from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .make_graph import make_graph


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

def showcase(request):

    context_graph, pretty_string, total_num_of_players = make_graph('nastynateff')
    
    context = {
        'graph': context_graph,
        'league_string': pretty_string,
        'total_num_of_players': total_num_of_players
    }
    return render(request, 'portfolio/showcase.html', context)