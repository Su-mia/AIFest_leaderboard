from django.shortcuts import render
from .leaderboard import calculate_global_rank, get_all_ranks

# Create your views here.


def leaderboard_view(request):
    """
    View function for the leaderboard page.
    """

    teams_first = [
          "Myss AI",
          "ML Builders",
          "zero"

    ]  # Replace with actual team names
    competitions_first = [
        "image-classification-aifest24",
        "multi-label-classification-aifest24",
        "cars-price-prediction"
    ]  # Replace with actual competition IDs
    weights_first = [6 , 6 , 5]  # Replace with actual weights

    additionalList = {
    'kurtosis': { 'not-in-kaggle' : {'rank': 2, 'inCompetition': True}}, 
    'Megatron': { 'not-in-kaggle' : {'rank': 1, 'inCompetition': True}}, 
    }

    # get the global rank of the first set of teams
    global_rank_first = calculate_global_rank(teams_first, competitions_first, weights_first , False , {})

    teams_second = [
         "ABCode",
         "LuminAi",
         "HyperML",
         "0v3r_fl0w",
         "BONSWAYNAGUI",
         "Data Seekers",
         "TeamOne",
         "the brainiacs",
    ]  # Replace with actual team names
    competitions_second = [
       "help-djelloul-to-grow-his-business-classification",
       "ai-fest-smurfs-challenge",
       "risky-patterns-in-io-t-device-interactions",
       "space-aifest24",
       "the-boss",
    ]  # Replace with actual competition IDs
    weights_second = [4 , 6 , 6, 5, 5]  # Replace with actual weights

    # get the global rank of the second set of teams
    global_rank_second = calculate_global_rank(teams_second, competitions_second, weights_second , False , {})

    # create the context
    context = {
        "global_rank_first": global_rank_first,
        "global_rank_second": global_rank_second,
        "competitions_first": competitions_first,  
        "competitions_second": competitions_second, 
    }
    return render(request, template_name="leaderboard.html", context=context)
