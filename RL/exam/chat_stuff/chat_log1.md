## Reinforcement-learning basics:

1. What is RL formalism (MDP), policy, value function, rewards? Give examples.


## RL Formalism: Markov Decision Process (MDP)

**MDP** is the mathematical framework for modeling RL problems. An MDP is defined by:

- **States (S):** All possible situations the agent can be in.
- **Actions (A):** All possible actions the agent can take.
- **Transition function (P):** Probability of moving from one state to another given an action, \( P(s'|s, a) \).
- **Reward function (R):** Immediate reward received after transitioning from state \( s \) to state \( s' \) via action \( a \).
- **Discount factor (γ):** How much future rewards are valued compared to immediate rewards (0 ≤ γ < 1).

**Example:**  
In a grid world, each cell is a state, the agent can move (actions: up, down, left, right), and the reward is +1 for reaching the goal, 0 otherwise.

---

## Policy (π)

A **policy** defines the agent’s way of behaving at a given time. It maps states to actions:  
π(a|s) = probability of taking action a in state s.

**Example:**  
In the grid world, a policy could be: "Always move right unless at the rightmost edge, then move down."

---

## Value Function

A **value function** estimates the expected cumulative reward from a state (or state-action pair), following a policy.

- **State value function (Vπ(s)):** Expected reward starting from state s and following policy π.
- **Action value function (Qπ(s, a)):** Expected reward starting from state s, taking action a, and following π thereafter.

**Example:**  
In the grid world, Vπ(s) could be higher for states closer to the goal.

---

## Rewards

A **reward** is a scalar feedback signal from the environment indicating the immediate benefit of an action.

**Example:**  
- +10 for reaching the goal
- -1 for hitting a wall
- 0 for normal moves

---

**Summary Table:**

| Concept         | Definition                                                     | Example (Grid World)              |
|-----------------|----------------------------------------------------------------|-----------------------------------|
| MDP             | States, actions, transitions, rewards, discount                | Grid cells, moves, rules, scores  |
| Policy (π)      | State-to-action mapping                                        | Always move right                 |
| Value Function  | Expected cumulative reward (Vπ(s), Qπ(s, a))                   | Higher near goal                  |
| Reward          | Immediate feedback                                             | +1 at goal, 0 elsewhere           |
2. What are the basic components of a reinforcement learning algorithm?


## Basic Components of a Reinforcement Learning Algorithm

1. **Agent**
   - The learner or decision-maker.
   
2. **Environment**
   - The external system with which the agent interacts.

3. **State (s)**
   - A representation of the current situation of the environment.

4. **Action (a)**
   - Choices available to the agent at each state.

5. **Policy (π)**
   - The strategy used by the agent to select actions based on states.

6. **Reward Signal (r)**
   - Immediate feedback received after taking an action.

7. **Value Function (V or Q)**
   - Estimates the expected cumulative reward from a state (V) or from a state-action pair (Q).

8. **Model of the Environment** *(optional)*
   - Predicts the next state and reward, used in model-based approaches.

---

**Summary Table:**

| Component           | Description                                    |
|---------------------|------------------------------------------------|
| Agent               | Learner/decision maker                        |
| Environment         | System interacted with                         |
| State (s)           | Current situation                              |
| Action (a)          | Choices for the agent                          |
| Policy (π)          | Action-selection strategy                      |
| Reward (r)          | Immediate feedback                             |
| Value function      | Expected long-term reward                      |
| Model *(optional)*  | Predicts state transitions and rewards         |
## Value-based methods

1. What is the relation of value function and a policy?


## Relation of Value Function and a Policy

- **Value function** measures how good it is for an agent to be in a state (or to take an action in a state), assuming the agent follows a particular **policy**.
- The value function is always defined **with respect to a policy**.

### Formal Definitions

- **Policy (π):** A mapping from states to actions.
- **State value function (V<sub>π</sub>(s)):** Expected cumulative reward starting from state \(s\) and following policy π.
- **Action value function (Q<sub>π</sub>(s, a)):** Expected cumulative reward starting from state \(s\), taking action \(a\), then following policy π.

\[
V_{\pi}(s) = \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t r_{t+1} \mid s_0 = s \right]
\]

\[
Q_{\pi}(s, a) = \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t r_{t+1} \mid s_0 = s, a_0 = a \right]
\]

### Key Points

- **Given a policy, you can compute its value function.**
- **Given a value function, you can derive a better policy** (e.g., by acting greedily with respect to the value function).

### Example

If the policy is “always move right,” the value function tells you the expected reward you’ll get from each state if you always move right.

---

**Summary:**  
The value function evaluates how good a policy is, and policies can be improved using value functions. They are tightly coupled in RL.
