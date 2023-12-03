import os
import textworld
import textworld.gym
import gym

os.system('tw-make custom --world-size 2 --quest-length 3 --nb-objects 10 --output tw_games/game.ulx -f -v --seed 123')

env_id = textworld.gym.register_game('tw_games/game.ulx')
print(env_id)
env = gym.make(env_id)
obs, infos = env.reset()
print(obs)
obs, score, done, infos = env.step("go east")
print(obs)
try:
    done = False
    obs, _ = env.reset()
    print(obs)
    nb_moves = 0
    while not done:
        command = input("> ")
        obs, score, done, _ = env.step(command)
        print(obs)
        nb_moves += 1

except KeyboardInterrupt:
    pass  # Press the stop button in the toolbar to quit the game.

print("Played {} steps, scoring {} points.".format(nb_moves, score))

request_infos = textworld.EnvInfos(
    admissible_commands=True,  # All commands relevant to the current state.
    entities=True              # List of all interactable entities found in the game. 
)

# Requesting additional information should be done when registering the game.
env_id = textworld.gym.register_game('tw_games/game.ulx', request_infos)
env = gym.make(env_id)

obs, infos = env.reset()
print("Entities: {}\n".format(infos["entities"]))
print("Admissible commands:\n  {}".format("\n  ".join(infos["admissible_commands"])))

request_infos = textworld.EnvInfos(
    facts=True  # All the facts that are currently true about the world.
)

# Requesting additional information should be done when registering the game.
env_id = textworld.gym.register_game('tw_games/game.ulx', request_infos)
env = gym.make(env_id)

obs, infos = env.reset()

print("-= Facts =-")
print("\n".join(map(str, infos["facts"])))

obs, _, _, infos = env.step("close safe")
print(obs)

print("-= Facts =-")
print("\n".join(map(str, infos["facts"])))

