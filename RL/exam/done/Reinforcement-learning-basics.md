# Reinforcement-learning basics:


# Reinforcement Learning Basics

## 1. RL Formalism (MDP), Policy, Value Function, Rewards

### Markov Decision Process (MDP)
A **Markov Decision Process (MDP)** is a mathematical framework used to model decision-making problems in Reinforcement Learning (RL). It provides the formalism for the environment in which the agent interacts.

An MDP is defined by the tuple \( (S, A, P, R, \gamma) \):

- **S**: A finite set of states the agent can be in.
- **A**: A finite set of actions available to the agent.
- **P**: Transition probability function \( P(s' | s, a) \) — the probability of moving to state \( s' \) from state \( s \) after taking action \( a \).
- **R**: Reward function \( R(s, a, s') \) — the immediate reward received after transitioning from state \( s \) to \( s' \) due to action \( a \).
- **\(\gamma\)**: Discount factor (\(0 \leq \gamma \leq 1\)) — determines the importance of future rewards.

The goal of the agent is to find a policy that maximizes cumulative (discounted) rewards over time.

---

### Policy (\(\pi\))
A **policy** defines the agent’s behavior at each state, specifying what action to take.

- **Deterministic policy**: \(\pi(s) = a\), a fixed action for each state.
- **Stochastic policy**: \(\pi(a|s) = P(a | s)\), a probability distribution over actions given the state.

Example:
- In a grid-world game, a policy might be "always move right when possible."

---

### Value Function
The **value function** estimates the expected cumulative reward starting from a state (or state-action pair), following a particular policy.

- **State-value function \(V^\pi(s)\)**:
  \[
  V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^{t} R_{t+1} \mid S_0 = s \right]
  \]
  Expected return starting from state \(s\) and following policy \(\pi\).

- **Action-value function \(Q^\pi(s,a)\)**:
  \[
  Q^\pi(s,a) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^{t} R_{t+1} \mid S_0 = s, A_0 = a \right]
  \]
  Expected return starting from state \(s\), taking action \(a\), then following policy \(\pi\).

Example:
- In chess, the value function estimates the likelihood of winning starting from a particular board configuration.

---

### Rewards
**Rewards** are scalar feedback signals received after taking an action in a state, guiding the learning process.

- Immediate rewards: \(R_t\) is received at time step \(t\).
- Goal: maximize cumulative discounted reward \( G_t = \sum_{k=0}^\infty \gamma^k R_{t+k+1} \).

Example:
- In a video game, the agent receives +10 points for collecting a coin and -5 for hitting an obstacle.

---

## Example: Simple Grid World

- **States (S)**: Positions on a 4x4 grid.
- **Actions (A)**: {Up, Down, Left, Right}.
- **Transition (P)**: Moving in the chosen direction unless blocked by a wall.
- **Reward (R)**: +1 for reaching the goal state, 0 otherwise.
- **Policy (\(\pi\))**: Move right until the goal is reached.
- **Value function \(V^\pi(s)\)**: Expected number of steps (or rewards) to reach the goal from state \(s\).

---

This formalism allows an RL agent to learn optimal behaviors via interaction with the environment by maximizing expected rewards over time.

# Basic Components of a Reinforcement Learning Algorithm

A reinforcement learning (RL) algorithm typically consists of the following core components:

---

## 1. Agent
- The learner or decision-maker.
- Interacts with the environment by selecting actions based on a policy.
- Learns from feedback (rewards) to improve its behavior over time.

---

## 2. Environment
- The external system with which the agent interacts.
- Defines the states, dynamics (state transitions), and rewards.
- Responds to the agent’s actions by moving to new states and providing rewards.

---

## 3. State (\(S\))
- A representation of the current situation or configuration of the environment.
- The agent observes the state to decide what action to take next.

---

## 4. Action (\(A\))
- The choices available to the agent at each state.
- The agent selects an action based on the current policy.

---

## 5. Policy (\(\pi\))
- A mapping from states to actions (can be deterministic or stochastic).
- Governs the agent's behavior.
- The goal is to learn or improve the policy to maximize cumulative rewards.

---

## 6. Reward Signal (\(R\))
- Numerical feedback received after taking an action in a state.
- Indicates how good or bad the action was in that context.
- Drives the learning process.

---

## 7. Value Function
- Estimates how good it is to be in a given state (or state-action pair), in terms of expected cumulative rewards.
- Helps the agent evaluate and improve its policy.

---

## 8. Model of the Environment (optional)
- Some algorithms use a model to simulate environment dynamics (transition probabilities and rewards).
- Enables planning by predicting future states and rewards.
- Not always available or necessary (model-free RL).

---

## Summary Diagram

Agent <----> Environment
   |              |
 Policy          States
   |              |
 Actions <---- Rewards
```

---

## Example Flow of an RL Algorithm

1. **Observe** current state \(s_t\).
2. **Select** action \(a_t\) based on policy \(\pi(s_t)\).
3. **Execute** action \(a_t\), environment moves to next state \(s_{t+1}\).
4. **Receive** reward \(r_{t+1}\).
5. **Update** policy or value function based on experience \((s_t, a_t, r_{t+1}, s_{t+1})\).
6. Repeat until task completion or convergence.

---

These components together form the backbone of any reinforcement learning algorithm.
```