### Reinforcement Learning Formalism: Markov Decision Process (MDP)

**MDP** is a mathematical framework to describe RL problems. It is defined by:

- **States (S):** All possible situations the agent can be in.
- **Actions (A):** All possible actions the agent can take.
- **Transition Function (P):** Probability of moving to a new state after taking an action.
- **Reward Function (R):** The immediate reward received after transitioning from one state to another due to an action.
- **Discount Factor (γ):** Determines the importance of future rewards.

#### Example:
- **Game:** Gridworld
  - **States:** Positions on the grid.
  - **Actions:** {Up, Down, Left, Right}
  - **Transition:** Moving to a new cell based on action.
  - **Reward:** +1 for reaching the goal, 0 otherwise.

---

### Policy (π)

A **policy** is the agent’s strategy for deciding actions. It maps states to actions (can be deterministic or stochastic).

#### Example:
- **Policy:** In Gridworld, always move right if possible.

---

### Value Function

**Value functions** estimate how good it is to be in a state (or to take an action in a state), based on expected cumulative reward.

- **State Value Function (Vπ(s)):** Expected reward starting from state s and following policy π.
- **Action Value Function (Qπ(s, a)):** Expected reward starting from state s, taking action a, and following policy π.

#### Example:
- **Vπ(s):** Expected total reward if the agent is at cell (2,3) and follows policy π until the goal.

---

### Rewards

**Rewards** are scalar feedback signals from the environment that indicate the immediate benefit of an action.

#### Example:
- **Positive Reward:** +10 for reaching the exit.
- **Negative Reward:** -1 for hitting a wall.
- **Neutral Reward:** 0 for regular moves.

---

**Summary Table:**

| Concept          | Definition                                      | Example (Gridworld)                        |
|------------------|-------------------------------------------------|--------------------------------------------|
| MDP              | RL problem formalism                            | Grid, movement, state transitions          |
| Policy (π)       | Agent’s strategy (state → action)               | Always move right                          |
| Value Function   | Expected cumulative reward (state/action value) | Value of being at (2,3)                    |
| Reward           | Immediate feedback signal                       | +1 for goal, -1 for wall, 0 otherwise      |
