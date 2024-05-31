# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_play, opponent_history=[], guess="R", play_order={}):

    if prev_play == "":
        opponent_history.append("S")
    else:
        opponent_history.append(prev_play)

    if len(opponent_history) >= 5:

        possibleMoves = []
        possible_order = {}

        prevSequence = "".join(opponent_history[-5:])
        play_order[prevSequence] = play_order.get(prevSequence, 0) + 1
        for n in ["R", "P", "S"]:
            potential_play = "".join(opponent_history[-4:]) + n
            possibleMoves.append(potential_play)

        for n in possibleMoves:
            if n in play_order:
                possible_order[n] = play_order[n]

        if possible_order:
            commonSequence = None
            currMax = 0

            for sequence, frequency in possible_order.items():
                if frequency > currMax:
                    commonSequence = sequence
                    currMax = frequency
            guess = commonSequence[-1]

    Counter = {"R": "P", "P": "S", "S": "R"}
    myMove = Counter[guess]

    return myMove
