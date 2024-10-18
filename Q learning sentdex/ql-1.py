import ale_py

env = ale_py.ALEInterface()
# Assuming the correct path to the ROM file is provided
env.loadROM("E:\\deep learning\\Q learning sentdex\\breakout.bin")
obs = env.reset()
action = env.action_space.sample()
obs, reward, terminated, truncated = env.step(action)
env.close()