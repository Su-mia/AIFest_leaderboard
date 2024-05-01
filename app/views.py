from django.shortcuts import render
from .leaderboard import calculate_global_rank, get_all_ranks

# Create your views here.


def leaderboard_view(request):
    """
    View function for the leaderboard page.
    """

    teams_first = [
        "kurtosis",
        "Megatron",
        "PentechAI",
        "CrusAIders",
        "Vgaith",
        "K-beans",
        "idk"
    ]  # Replace with actual team names
    competitions_first = [
        "instadeep-challenge-soai",
        "iiot-cyber-security-challenge-haick-2022",
        # "jumia-purchase-prediction",
        # "lcbm-challenge-haick-2022",
    ]  # Replace with actual competition IDs
    weights_first = [30 , 70]  # Replace with actual weights

    # get the global rank of the first set of teams
    global_rank_first = calculate_global_rank(teams_first, competitions_first, weights_first)

    teams_second = [
         "kurtosis",
        "Megatron",
        "PentechAI",
    ]  # Replace with actual team names
    competitions_second = [
        "instadeep-challenge-soai",
    ]  # Replace with actual competition IDs
    weights_second = [100]  # Replace with actual weights

    # get the global rank of the second set of teams
    global_rank_second = calculate_global_rank(teams_second, competitions_second, weights_second)

    # create the context
    context = {
        "global_rank_first": global_rank_first,
        "global_rank_second": global_rank_second,
        "competitions_first": competitions_first,  
        "competitions_second": competitions_second, 
    }
    return render(request, template_name="leaderboard.html", context=context)
