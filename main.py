import TradingGameEnv
import baseline_agents
from stable_baselines.common.env_checker import check_env

# Validate the environment

# add 1 baseline agent
agents = [baseline_agents.BaselineAgent1()]
env = TradingGameEnv.TradingGameEnv(other_agent_list = agents) # 2 agents, 1 suit, 4 sub-piles (3days)

# If the environment don't follow the interface, an error will be thrown
check_env(env, warn=True)
print("The environment is valid.")

# Playing test rounds
print("Playing test rounds:")
obs = env.reset()
print("obs space", env.observation_space)
print("action space", env.action_space)
print("sample action", env.action_space.sample())
print("public pile", env.public_pile)
print("hands", env.hands)

env.render()
print('obs=', obs)

while(True):
	obs, reward, done, info = env.step([1,1,40,45]) # buy at 40; sell at 45
	env.render()
	print('obs=', obs, 'reward=', reward, 'done=', done)
	if done:
		break
