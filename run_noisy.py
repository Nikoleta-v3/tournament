import axelrod as axl

turns = 200
repetitions = 100
noise = 0.05
processes = 0
filename = "noisy_interactions.csv"

players = [s() for s in axl.ordinary_strategies]
tournament = axl.Tournament(players, turns=turns, repetitions=repetitions, noise=noise, processes=processes)
tournament.play(filename)