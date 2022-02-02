"""Strategies to be included in the tournament"""
import axelrod as axl
import itertools

# Include a list of parametrized strategies
parameterized_players = [
	axl.Random(0.1),
        axl.Random(0.3),
        axl.Random(0.7),
        axl.Random(0.9),
        axl.GTFT(0.1),
        axl.GTFT(0.3),
        axl.GTFT(0.7),
        axl.GTFT(0.9),
        axl.MetaWinner(team=[
        axl.EvolvedHMM5, axl.EvolvedLookerUp2_2_2, axl.EvolvedFSM16,
        axl.EvolvedANN5, axl.PSOGambler2_2_2, axl.FoolMeOnce,
        axl.DoubleCrosser, axl.Gradual
    ]),
]
testing_players = [axl.CURE(Delta) for Delta in range(5)] 

gammas = [0.1, 0.2]

thresholds = [(0, 0),
              (2, 2),
              (3, 3),
              (2, 1), 
              (3, 1), 
              (1, 2), 
              (1, 3),
              (1, 4)]

for gamma in gammas:
    for threshold in thresholds:
        testing_players.append(axl.TEEC(Tthreshold=threshold[1],
                                              Ethreshold=threshold[0],
                                              ExploiRate=gamma))

players = [s() for s in axl.strategies] + parameterized_players + testing_players
players.sort(key=lambda p:p.__repr__())

num_players = len(players)
num_testing = len(testing_players)

source = range(num_players - num_testing)
sink = range(num_players - num_testing, num_players)
edges = list(itertools.product(sink, source))


print(len(players))
