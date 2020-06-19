import gym
import numpy as np
env=gym.make("MountainCar-v0")
alpha=0.1
gamma=0.1
SHOW_EVERY=2000
EPISODES=25000
Q_space=[20]*len(env.observation_space.high)
interval=(env.observation_space.high-env.observation_space.low)/Q_space
q_table=np.random.uniform(-2,0,Q_space+[env.action_space.n])

#descretize the states function
def desc(state):
    desc_state=(state-env.observation_space.low)/interval
    return tuple(desc_state.astype(np.int))

for episode in range(25000):
    
    initial_state=desc(env.reset()) #initialise the cart    

    done=False
    while not done:
        action=np.argmax(q_table[initial_state])
        new_state,reward,done,_=env.step(action)#optimal action taken
        s_dash=desc(new_state) #s_dash is the new state
        if not done:
        
            Q_s_dash=np.max(q_table[s_dash])
           
            Q_s=q_table[initial_state+(action, )]
            new_q=(1-alpha)*Q_s+ gamma*reward+gamma*Q_s_dash
            q_table[initial_state+(action, )]=new_q
        elif new_state[0]>=env.goal_position:
            q_table[initial_state+(action, )]=0
        initial_state=s_dash
        if episode % SHOW_EVERY == 0:
             env.render()

env.close()
