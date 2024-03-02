import numpy as np

from wfcrl.rewards import StepPercentage

from wfcrl.environments import make


env = make("Dec_Ablaincourt_Floris", max_num_steps=30, reward_shaper=StepPercentage())


def dummy_policy(agent, i):
    if (agent == "turbine_1") and (i == 20):
        return {
            "yaw": np.array([15.0]),
        }
    return {"yaw": np.array([0])}


env.reset()
r = {agent: 0 for agent in env.possible_agents}
done = {agent: False for agent in env.possible_agents}
num_steps = {agent: 0 for agent in env.possible_agents}
for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()
    done[agent] = done[agent] or termination or truncation
    r[agent] += reward
    action = dummy_policy(agent, num_steps[agent])
    num_steps[agent] += 1
    env.step(action)

print(f"Total reward = {r}")
