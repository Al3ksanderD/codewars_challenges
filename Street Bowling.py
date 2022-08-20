def ball_test(s, r):
    """
    Imagine you are trying to roll a ball a certain distance down a road.
    The ball will have a starting speed that slowly degrades due to friction and cracks in the road.
    Every time the ball rolls a distance equal to its speed or rolls over a crack,
    its speed decreases by 1. Given a speed of s which the ball starts rolling,
    and a roadmap r of the street represented by a string,
    return whether or not the ball will be able to make it to its destination (True or False).
    """
    counter = 0
    temp_counter = 0
    distance = 0
    for x in range(len(r)):
        if r[x] == "_":
            distance += 1
            if distance == s:
                distance = 0
                temp_counter += 1
                s -= temp_counter
                temp_counter = 0

        elif r[x] == "x":
            distance += 1
            if distance == s:
                distance = 0
                temp_counter += 1
                s -= temp_counter
                temp_counter = 0
            temp_counter += 1
    if s >= 0:
        return True
    else:
        return False

list = "xxxxxxxxxx_____x___xx__xx____________x__________x_"
print(ball_test(24, list))
