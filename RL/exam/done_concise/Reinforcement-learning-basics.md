# Reinforcement-learning basics:



---

## 1. **RL Formalism: Markov Decision Process (MDP)**

- **Definition:**  
  An MDP provides a mathematical framework for modeling decision making.  
- **Components:**  
    - **States (S):** All possible situations (e.g., positions in a grid).
    - **Actions (A):** Choices at each state (e.g., move up, down).
    - **Transition Probability (P):** Probability of moving to a state given current state and action.
    - **Reward (R):** Immediate gain from taking an action.
    - **Discount Factor (γ):** Weighs importance of future rewards (0 ≤ γ < 1).

**Example:**  
A robot navigating a maze:  
- **States:** Each cell in the maze.  
- **Actions:** Move north, south, east, west.  
- **Rewards:** +10 for reaching the goal, -1 for hitting a wall.

---

## 2. **Policy (π)**

- **Definition:**  
  A policy is a strategy or rule the agent uses to choose actions at each state.

- **Types:**  
    - **Deterministic:** Always choose the same action for a state.
    - **Stochastic:** Assign probabilities to possible actions.

**Example:**  
- In the maze, the policy could be: "If at a junction, always move towards the goal."

---

## 3. **Value Function**

- **Definition:**  
  The value function estimates how good it is to be in a certain state (or perform an action), in terms of expected future rewards.

    - **State Value (V(s)):** Expected total reward from state s, following policy π.
    - **Action Value (Q(s, a)):** Expected total reward from state s, taking action a, then following policy π.

**Example:**  
- V(s): Expected score when starting from cell s, if following the best route.
- Q(s, a): Expected score if you move north from cell s, then follow the best route.

---

## 4. **Rewards**

- **Definition:**  
  Scalar feedback signal received after taking an action in a state.

**Example:**  
- +1 for reaching the goal.
- -1 for each step taken.
- -10 for falling into a trap.

---

**Summary Table:**

| Concept        | Definition                              | Example (Maze)                   |
|----------------|-----------------------------------------|----------------------------------|
| MDP            | Environment model                       | The maze and rules               |
| Policy (π)     | Agent’s strategy                        | Always move towards the exit     |
| Value Function | Expected cumulative reward              | V(state: near exit) = high value |
| Reward         | Immediate feedback after action         | +10 for exit, -1 per step        |

---



---

## 1. **Agent**
- The learner or decision-maker that interacts with the environment.

## 2. **Environment**
- The external system with which the agent interacts, receives states, and gets rewards.

## 3. **State (s)**
- The current situation or observation received from the environment.

## 4. **Action (a)**
- The set of all possible moves or decisions the agent can make.

## 5. **Policy (π)**
- The agent’s strategy to choose actions from states, possibly probabilistic.

## 6. **Reward Signal (r)**
- The immediate feedback received after taking an action, guiding learning.

## 7. **Value Function (V or Q)**
- Estimates of cumulative future rewards, used to evaluate the desirability of states or actions.

## 8. **Model of the Environment** (optional)
- A representation of how the environment works, predicting next states and rewards (used in model-based RL).

---

**Summary Table:**

| Component    | Description                                 |
|--------------|---------------------------------------------|
| Agent        | Learner/decision-maker                      |
| Environment  | External system interacted with             |
| State        | Current situation                           |
| Action       | Possible choices                            |
| Policy       | Decision-making strategy                    |
| Reward       | Immediate feedback                          |
| Value Func.  | Expected cumulative reward                  |
| Model        | (Optional) Environment simulator/predictor  |

---
