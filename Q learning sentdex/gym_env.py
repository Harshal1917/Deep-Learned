import gym

# Creating an environment with specified render mode
env = gym.make('MountainCar-v0', render_mode="rgb_array")

print("Environment Details:")
print(f"Observation Space: {env.observation_space}")  # The observation space represents the state of the environment, which includes the position and velocity of the car.
print(f"Action Space: {env.action_space}")  # The action space defines the actions the agent can take, which are accelerating left, doing nothing, or accelerating right.
print(f"Action Space Sample: {env.action_space.sample()}")  # This line samples a random action from the action space.
print("Action Space Explanation:")
print("0: Accelerate to the left")  # This action applies a force to the left, moving the car towards the left.
print("1: Do nothing")  # This action does not apply any force, allowing the car to move based on its current velocity.
print("2: Accelerate to the right")  # This action applies a force to the right, moving the car towards the right.
print(f"Reward Range: {env.reward_range}")  # The reward range specifies the minimum and maximum reward the agent can receive in a step.
print(f"Max Episode Steps: {env.spec.max_episode_steps}")  # This specifies the maximum number of steps allowed in an episode.

# Resetting the environment to get the initial observation
observation = env.reset()  # This resets the environment and returns the initial observation.

# Rendering the environment
env.render()  # This renders the environment, allowing us to visualize the state of the environment.

# Taking a random action
action = env.action_space.sample()  # This samples a random action from the action space.
# Correcting the unpacking issue by using the correct number of values
observation, reward, done, truncated, info = env.step(action)  # This takes a step in the environment with the sampled action and returns the new observation, reward, done status, truncated status, and additional information.

# Printing the observation, reward, and done status
print(f"Observation: {observation}")  # This prints the new observation after taking the action.
print(f"Reward: {reward}")  # This prints the reward received after taking the action.
print(f"Done: {done}")  # This prints the done status, indicating if the episode has ended.

# Closing the environment
env.close()  # This closes the environment, freeing up resources.
