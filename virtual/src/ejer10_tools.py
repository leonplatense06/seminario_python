def counting_points_mvps(round, points_mvps):
    """This function counts the points of each player in a round, obtains the mvp, 
    upgrades both them in a dictionary and returns the mvp."""
    mvp_points = (-99)
    for p in round:
        round_points = (round[p]['kills'] * 3) + (round[p]['assists']) + ((-1) if (round[p]['deaths']) else 0)
        if (round_points > mvp_points):
            mvp_points = round_points
            mvp = p        
        points_mvps[p]['points'] += round_points
    points_mvps[mvp]['mvps'] += 1
    return mvp