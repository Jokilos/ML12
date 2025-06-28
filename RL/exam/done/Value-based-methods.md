# Value-based methods


# Relation Between Value Function and Policy in Reinforcement Learning

---

## 1. Definitions Recap

- **Policy (\(\pi\))**: A mapping from states to actions, defining the agent's behavior.
  - \(\pi(a|s)\): Probability of taking action \(a\) in state \(s\).
- **Value Function**: Measures the expected cumulative reward when following a policy from a given state (or state-action pair).
  - **State-value function \(V^\pi(s)\)**:
    \[
    V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t R_{t+1} \mid S_0 = s \right]
    \]
  - **Action-value function \(Q^\pi(s,a)\)**:
    \[
    Q^\pi(s,a) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t R_{t+1} \mid S_0 = s, A_0 = a \right]
    \]

---

## 2. Relationship

- The **value function depends on the policy** \(\pi\) because it calculates expected returns **assuming** the agent behaves according to \(\pi\).
- The value function evaluates **how good it is to follow policy \(\pi\)** starting from a state (or state-action pair).
- Conversely, the **policy can be improved using the value function** by choosing actions that maximize expected returns.

---

## 3. Policy Evaluation and Improvement

- **Policy Evaluation**: Computing the value function \(V^\pi\) or \(Q^\pi\) for a given policy \(\pi\).
- **Policy Improvement**: Using the value function to define a better policy \(\pi'\):
  \[
  \pi'(s) = \arg\max_a Q^\pi(s,a)
  \]
- This iterative process (Policy Iteration) converges to the optimal policy \(\pi^*\).

---

## 4. Intuition

- **Value function** answers: *"If I start here and follow policy \(\pi\), how much reward can I expect?"*
- **Policy** answers: *"Given the current situation, what action should I take?"*

They are tightly coupled:
- The policy determines the value function.
- The value function guides the improvement of the policy.

---

## 5. Summary

| Concept          | Role                                    | Dependency                  |
|------------------|----------------------------------------|-----------------------------|
| Policy \(\pi\)   | Defines agent's behavior (action choice) | Independent (starting point) |
| Value function \(V^\pi, Q^\pi\) | Expected returns following \(\pi\)  | Depends on \(\pi\)           |
| Optimal policy \(\pi^*\) | Maximizes value function               | Derived from value function  |

---

Understanding this relationship is fundamental for designing and analyzing reinforcement learning algorithms.

# Difference Between Value Function and Q-Function

---

## 1. Definitions

- **Value Function \(V^\pi(s)\)**:  
  The expected cumulative reward starting from state \(s\) and following policy \(\pi\):
  \[
  V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t R_{t+1} \mid S_0 = s \right]
  \]
  It answers: *"How good is it to be in state \(s\) under policy \(\pi\)?"*

- **Action-Value Function (Q-Function) \(Q^\pi(s,a)\)**:  
  The expected cumulative reward starting from state \(s\), taking action \(a\), and thereafter following policy \(\pi\):
  \[
  Q^\pi(s,a) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t R_{t+1} \mid S_0 = s, A_0 = a \right]
  \]
  It answers: *"How good is it to take action \(a\) in state \(s\) under policy \(\pi\)?"*

---

## 2. Key Differences

| Aspect                     | Value Function \(V^\pi(s)\)                         | Q-Function \(Q^\pi(s,a)\)                                 |
|----------------------------|----------------------------------------------------|----------------------------------------------------------|
| Input                      | State \(s\)                                        | State-action pair \((s,a)\)                              |
| Output                     | Expected return starting from state \(s\)         | Expected return starting from state \(s\), taking action \(a\) |
| Dependency                 | Depends on the policy \(\pi\)                      | Depends on the policy \(\pi\)                            |
| Use in Policy              | Indirect (needs policy to choose action)           | Direct (can select action by maximizing \(Q\))          |
| Role in Control            | Evaluates states                                   | Evaluates state-action pairs                             |
| Example                    | "How good is this position?"                       | "How good is making this move in this position?"        |

---

## 3. Relationship Between \(V\) and \(Q\)

The value function can be derived from the Q-function given a policy \(\pi\):
\[
V^\pi(s) = \sum_{a} \pi(a|s) Q^\pi(s,a)
\]
- For deterministic policies: \(V^\pi(s) = Q^\pi(s, \pi(s))\).

---

## 4. Intuition

- **Value function \(V^\pi(s)\)** summarizes the expected return from state \(s\), averaging over actions taken by policy \(\pi\).
- **Q-function \(Q^\pi(s,a)\)** provides a more detailed estimate including the immediate choice of action, useful for action selection and policy improvement.

---

## 5. Summary

| Function       | Purpose                         | Input                      | Use Case                       |
|----------------|---------------------------------|----------------------------|--------------------------------|
| Value Function | Evaluate state under policy      | State \(s\)                | Policy evaluation              |
| Q-Function     | Evaluate state-action pair       | State \(s\), Action \(a\)  | Action selection and control  |

---

Understanding both value functions is critical for designing RL algorithms that learn optimal policies effectively.

# Bellman Equations in Reinforcement Learning

---

## 1. What is the Bellman Equation?

The **Bellman equation** expresses a recursive relationship that relates the value of a state (or state-action pair) to the values of its successor states. It forms the foundation for many RL algorithms by breaking down the value function into immediate reward plus discounted value of next states.

---

## 2. Types of Bellman Equations

There are two main Bellman equations corresponding to the two types of value functions:

### a) Bellman Expectation Equation for the State-Value Function \(V^\pi(s)\)

For a given policy \(\pi\), the value of a state is:

\[
V^\pi(s) = \mathbb{E}_\pi \left[ R_{t+1} + \gamma V^\pi(S_{t+1}) \mid S_t = s \right]
\]

Expanded form:

\[
V^\pi(s) = \sum_{a} \pi(a|s) \sum_{s', r} P(s', r | s, a) \big[ r + \gamma V^\pi(s') \big]
\]

- \(P(s', r | s, a)\): Probability of transitioning to state \(s'\) and receiving reward \(r\) after action \(a\) in state \(s\).
- \(\gamma\): Discount factor.

---

### b) Bellman Expectation Equation for the Action-Value Function \(Q^\pi(s,a)\)

\[
Q^\pi(s,a) = \mathbb{E} \left[ R_{t+1} + \gamma \sum_{a'} \pi(a'|S_{t+1}) Q^\pi(S_{t+1}, a') \mid S_t = s, A_t = a \right]
\]

Expanded form:

\[
Q^\pi(s,a) = \sum_{s', r} P(s', r | s, a) \left[ r + \gamma \sum_{a'} \pi(a'|s') Q^\pi(s', a') \right]
\]

---

### c) Bellman Optimality Equation for the State-Value Function \(V^*(s)\)

For the **optimal value function** \(V^*(s)\), the maximum expected return achievable from state \(s\):

\[
V^*(s) = \max_a \sum_{s', r} P(s', r | s, a) \left[ r + \gamma V^*(s') \right]
\]

---

### d) Bellman Optimality Equation for the Action-Value Function \(Q^*(s,a)\)

For the **optimal action-value function** \(Q^*(s,a)\):

\[
Q^*(s,a) = \sum_{s', r} P(s', r | s, a) \left[ r + \gamma \max_{a'} Q^*(s', a') \right]
\]

---

## 3. Summary: Number of Bellman Equations

There are **four** main Bellman equations:

| Bellman Equation Type               | Value Function | Description                     |
|-----------------------------------|----------------|---------------------------------|
| 1. Bellman Expectation (State)    | \(V^\pi(s)\)   | Value under a fixed policy \(\pi\) |
| 2. Bellman Expectation (Action)   | \(Q^\pi(s,a)\) | Action-value under policy \(\pi\)  |
| 3. Bellman Optimality (State)     | \(V^*(s)\)     | Optimal value function             |
| 4. Bellman Optimality (Action)    | \(Q^*(s,a)\)   | Optimal action-value function      |

---

## 4. Intuition

- **Expectation equations** describe the value following a *specific* policy.
- **Optimality equations** describe the value assuming *optimal* action choices at every step.

---

## 5. Importance

- Bellman equations provide a foundation for dynamic programming, temporal-difference learning, and Q-learning.
- Solving Bellman equations yields the value functions which guide the agent’s decisions.

---

# Policy Iteration Algorithm in Reinforcement Learning

---

## 1. What is Policy Iteration?

**Policy Iteration** is a classic algorithm used to find the optimal policy in a Markov Decision Process (MDP). It iteratively improves a policy by alternating between evaluating the current policy and improving it based on the evaluation until convergence.

---

## 2. Overview

- Policy Iteration involves two main steps:
  1. **Policy Evaluation**: Calculate the value function \(V^\pi\) for the current policy \(\pi\).
  2. **Policy Improvement**: Update the policy by acting greedily with respect to the current value function.

- The algorithm converges to the **optimal policy** \(\pi^*\) and its corresponding value function \(V^*\).

---

## 3. Stages of Policy Iteration

### Stage 1: Policy Evaluation

- Given a policy \(\pi\), compute the state-value function \(V^\pi(s)\) by solving the Bellman expectation equation:
  \[
  V^\pi(s) = \sum_a \pi(a|s) \sum_{s', r} P(s', r | s, a) \left[ r + \gamma V^\pi(s') \right]
  \]
- This can be done either:
  - **Exactly:** Solve the system of linear equations.
  - **Iteratively:** Using iterative methods until \(V^\pi\) converges.

---

### Stage 2: Policy Improvement

- Use the computed \(V^\pi\) to improve the policy by choosing actions that maximize expected return:
  \[
  \pi'(s) = \arg\max_a \sum_{s', r} P(s', r | s, a) \left[ r + \gamma V^\pi(s') \right]
  \]
- Replace the old policy \(\pi\) with the new policy \(\pi'\).

---

## 4. Algorithm Summary

1. **Initialize** an arbitrary policy \(\pi\).
2. **Repeat** until policy converges:
   - **Policy Evaluation**: Compute \(V^\pi\) for current \(\pi\).
   - **Policy Improvement**: Update \(\pi\) greedily using \(V^\pi\).
3. **Output** the optimal policy \(\pi^*\) and value function \(V^*\).

---

## 5. Key Properties

- **Guaranteed convergence** to the optimal policy in a finite number of iterations for finite MDPs.
- Each iteration improves the policy or confirms optimality.
- Often faster than value iteration in practice because policy evaluation uses the current policy directly.

---

## 6. Intuition

- Start with a random policy.
- Evaluate how good it is.
- Improve it by choosing better actions.
- Repeat until no further improvements are possible.

---

## 7. Example (Pseudo-code)

```python
Initialize policy π arbitrarily
Repeat:
    # Policy Evaluation
    Compute V^π(s) for all s under π
    policy_stable = True

    # Policy Improvement
    For each state s:
        old_action = π(s)
        π(s) = argmax_a Σ_{s',r} P(s',r|s,a) [r + γ V^π(s')]
        if old_action != π(s):
            policy_stable = False
Until policy_stable == True

---

Policy Iteration is a fundamental algorithm illustrating the interaction between value functions and policies in Reinforcement Learning.
```

# Differences Between Model-Free and Model-Based Reinforcement Learning Methods

---

## 1. Definitions

- **Model-Based Methods**  
  Methods that learn or use a model of the environment’s dynamics (transition probabilities and reward function) to plan and make decisions.

- **Model-Free Methods**  
  Methods that learn policies or value functions directly from experience without explicitly modeling the environment’s dynamics.

---

## 2. Key Differences

| Aspect                  | Model-Based Methods                                  | Model-Free Methods                                |
|-------------------------|----------------------------------------------------|--------------------------------------------------|
| **Environment Model**   | Use or learn a model \(P(s', r | s, a)\)            | Do not require or learn environment model       |
| **Planning**            | Perform planning by simulating future states using the model | Learn from direct interaction without planning  |
| **Sample Efficiency**   | Generally more sample-efficient due to planning     | Often less sample-efficient; require more data   |
| **Computational Cost**  | Higher computation due to planning and model updates | Lower computation per step but may require more steps |
| **Policy Learning**     | Policy derived from planning with the model         | Policy/value updated directly from experience    |
| **Examples**            | Dynamic Programming, Monte Carlo Tree Search, Dyna  | Q-Learning, SARSA, Policy Gradient methods       |
| **Adaptability**        | Can adapt quickly if model is accurate              | Slower adaptation, relies on observed transitions|

---

## 3. Intuition

- **Model-Based**: "Think before acting" — use knowledge about how the world works to plan the best action.
- **Model-Free**: "Learn by trial and error" — improve actions purely from observed rewards without understanding the environment explicitly.

---

## 4. Advantages and Disadvantages

| Model-Based                                  | Model-Free                                 |
|---------------------------------------------|--------------------------------------------|
| + Can plan ahead and foresee consequences   | + Simpler to implement                      |
| + Better sample efficiency                   | + Robust to model inaccuracies             |
| - Requires accurate model or model learning | - Often slower learning                     |
| - Computationally expensive                  | - May require many interactions             |

---

## 5. Example Scenario: Robot Navigation

- **Model-Based:** The robot learns or is given a map (model) of the environment and plans paths to the goal.
- **Model-Free:** The robot learns which actions lead to the goal by trial and error, without explicit knowledge of the map.

---

## 6. Summary

| Feature               | Model-Based                  | Model-Free                  |
|-----------------------|-----------------------------|-----------------------------|
| Requires Environment Model? | Yes                         | No                          |
| Planning Capability       | Yes                         | No                          |
| Learning Approach         | Indirect (via model)         | Direct (from experience)    |
| Sample Efficiency         | High                        | Lower                      |
| Computational Cost        | Higher                      | Lower                      |

---

Understanding these differences helps in choosing the right RL approach depending on task complexity, available information, and computational resources.

# Difference Between Prediction and Control in Reinforcement Learning

---

## 1. Definitions

- **Prediction**  
  The task of estimating the value function \(V^\pi(s)\) or \(Q^\pi(s,a)\) for a **given fixed policy** \(\pi\).  
  It answers: *"How good is this policy?"*

- **Control**  
  The task of finding the **optimal policy** \(\pi^*\) that maximizes the expected cumulative reward.  
  It answers: *"What is the best policy to follow?"*

---

## 2. Key Differences

| Aspect                | Prediction                             | Control                                  |
|-----------------------|-------------------------------------|------------------------------------------|
| Objective             | Evaluate the value of a fixed policy \(\pi\) | Find the optimal policy \(\pi^*\)          |
| Outputs               | Value function \(V^\pi\) or \(Q^\pi\) | Optimal policy \(\pi^*\) and its value function \(V^*, Q^*\) |
| Policy                | Fixed and known                      | Unknown and to be improved                |
| Complexity            | Simpler problem                     | More complex; involves exploration and improvement |
| Examples of Algorithms | Monte Carlo policy evaluation, TD prediction | Q-learning, SARSA, Policy Iteration       |

---

## 3. Intuition

- **Prediction:**  
  "Given that I behave like this policy, what reward can I expect?"

- **Control:**  
  "What should I do to get the maximum reward?"

---

## 4. Relationship

- Prediction is often a **sub-problem** within control algorithms.
- Control methods typically alternate between:
  - Estimating value functions for a current policy (**prediction**).
  - Improving the policy based on those estimates (**control**).

---

## 5. Summary Table

| Aspect           | Prediction                       | Control                            |
|------------------|---------------------------------|----------------------------------|
| Goal             | Evaluate policy                  | Find optimal policy              |
| Known Policy     | Yes                             | No                              |
| Output           | \(V^\pi\), \(Q^\pi\)            | \(\pi^*\), \(V^*\), \(Q^*\)      |
| Problem Type     | Policy evaluation               | Policy optimization              |

---

Understanding the distinction helps clarify different objectives and methods in reinforcement learning.

# Differences Between Monte Carlo (MC) and Temporal-Difference (TD) Methods

---

## 1. Overview

Both Monte Carlo and Temporal-Difference are fundamental methods for **prediction** in reinforcement learning, i.e., estimating value functions from experience. They differ in how they estimate returns and update value estimates.

---

## 2. Key Differences

| Aspect                     | Monte Carlo (MC)                                     | Temporal-Difference (TD)                          |
|----------------------------|-----------------------------------------------------|--------------------------------------------------|
| **Update Timing**           | Updates only at the end of an episode (after episode termination) | Updates after every step (online, incremental)   |
| **Return Estimation**       | Uses **actual returns** (sum of discounted rewards to episode end) | Uses **bootstrapping**: one-step reward + estimated value of next state |
| **Requirement on Episodes** | Requires episodes to terminate (episodic tasks)    | Can be used in both episodic and continuing tasks |
| **Bias and Variance**       | Unbiased but high variance                           | Biased but lower variance                         |
| **Sample Efficiency**       | Less sample efficient due to waiting for episode end | More sample efficient due to incremental updates |
| **Convergence**             | Converges to true value as number of episodes → ∞ | Converges under certain conditions; faster learning in practice |
| **Example Algorithms**      | Monte Carlo policy evaluation                        | TD(0), SARSA, Q-learning                          |

---

## 3. Update Equations

- **Monte Carlo Update** (for state \(s_t\)):

\[
V(s_t) \leftarrow V(s_t) + \alpha \left[ G_t - V(s_t) \right]
\]

Where \(G_t\) is the **actual return** from time \(t\) to episode end:

\[
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots
\]

- **Temporal-Difference Update** (TD(0)):

\[
V(s_t) \leftarrow V(s_t) + \alpha \left[ R_{t+1} + \gamma V(s_{t+1}) - V(s_t) \right]
\]

---

## 4. Intuition

- **Monte Carlo**: Wait until the end of an episode to see the full outcome, then update estimates.
- **Temporal-Difference**: Update estimates step-by-step using current estimates to bootstrap future rewards.

---

## 5. When to Use Which?

| Scenario                         | Preferred Method          |
|---------------------------------|--------------------------|
| Episodic tasks with clear episode ends | Monte Carlo              |
| Continuing tasks or when early updates needed | Temporal-Difference       |
| When lower variance desired but willing to wait | Monte Carlo              |
| When faster, incremental learning is required    | Temporal-Difference       |

---

## 6. Summary Table

| Feature                 | Monte Carlo (MC)                          | Temporal-Difference (TD)               |
|-------------------------|------------------------------------------|---------------------------------------|
| Update Frequency        | End of episode                          | Every time step                       |
| Use of Bootstrapping    | No                                       | Yes                                   |
| Requires Episode End    | Yes                                      | No                                    |
| Variance of Estimate    | High                                     | Lower                                 |
| Bias                   | No (unbiased)                            | Yes (biased)                          |
| Sample Efficiency      | Lower                                   | Higher                               |

---

Both methods are foundational and often combined in algorithms like TD(\(\lambda\)) to balance their strengths.

# TD(k) and TD(λ) in Reinforcement Learning

---

## 1. Temporal-Difference (TD) Learning Recap

- TD methods update value estimates based on bootstrapping: combining observed rewards and current value estimates.
- Standard TD(0) updates values using the **one-step return**.

---

## 2. TD(k): k-Step Temporal-Difference Learning

### Definition
- TD(k) generalizes TD(0) by using **k-step returns** to update value estimates.
- Instead of updating after one step, it looks ahead \(k\) steps before updating.

### k-Step Return
\[
G_t^{(k)} = R_{t+1} + \gamma R_{t+2} + \dots + \gamma^{k-1} R_{t+k} + \gamma^k V(S_{t+k})
\]

### Update Rule
\[
V(S_t) \leftarrow V(S_t) + \alpha \left[ G_t^{(k)} - V(S_t) \right]
\]

### Intuition
- Balances between:
  - **TD(0):** bootstrap after 1 step (low variance, high bias).
  - **Monte Carlo:** bootstrap after episode ends (high variance, low bias).
- Larger \(k\) means using longer returns, less bootstrapping, closer to Monte Carlo.

---

## 3. TD(λ): Lambda Return and Eligibility Traces

### Definition
- TD(λ) combines returns from **all possible k-step returns** (for \(k=1,2,\dots\)) using a weighting parameter \(\lambda \in [0,1]\).
- It blends between TD(0) and Monte Carlo methods smoothly.

### λ-Return
\[
G_t^\lambda = (1-\lambda) \sum_{k=1}^\infty \lambda^{k-1} G_t^{(k)}
\]

Where \(G_t^{(k)}\) is the k-step return as defined above.

### Update Rule
\[
V(S_t) \leftarrow V(S_t) + \alpha \left[ G_t^\lambda - V(S_t) \right]
\]

### Eligibility Traces (Efficient Implementation)
- Instead of explicitly computing all returns, TD(λ) uses **eligibility traces** to assign credit to recently visited states.
- Eligibility traces decay over time, controlled by \(\lambda\).

---

## 4. Intuition Behind \(\lambda\)

| \(\lambda\) Value | Behavior                                      |
|------------------|-----------------------------------------------|
| 0                | Becomes TD(0) — only one-step return used    |
| Close to 1       | Approaches Monte Carlo — full return used     |
| Between 0 and 1  | Trade-off between bias and variance            |

---

## 5. Summary

| Method       | Description                              | Update Target                          | Notes                             |
|--------------|----------------------------------------|--------------------------------------|----------------------------------|
| **TD(k)**   | Uses fixed \(k\)-step returns           | \(G_t^{(k)}\)                        | Generalizes TD(0) and MC          |
| **TD(λ)**   | Weighted average of all k-step returns | \(G_t^\lambda = (1-\lambda) \sum \lambda^{k-1} G_t^{(k)}\) | Uses eligibility traces for efficiency |

---

## 6. Practical Importance

- TD(λ) often achieves better learning performance by balancing bias and variance.
- Eligibility traces enable online and incremental updates.
- Widely used in many RL algorithms (e.g., SARSA(λ)).

---

## References

- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*. (Chapter on TD Methods)

# SARSA Algorithm in Reinforcement Learning

---

## 1. What is SARSA?

- **SARSA** stands for **State-Action-Reward-State-Action**.
- It is an **on-policy** Temporal-Difference (TD) control algorithm used to learn the optimal action-value function \(Q^*(s,a)\) and the corresponding policy.
- Unlike off-policy methods like Q-learning, SARSA updates its Q-values based on the action actually taken by the current policy.

---

## 2. Key Idea

SARSA updates the Q-value \(Q(s,a)\) using the current state-action pair \((s,a)\), the reward \(r\), the next state \(s'\), and the next action \(a'\) chosen by the policy:

\[
Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma Q(s', a') - Q(s,a) \right]
\]

- \(\alpha\): learning rate  
- \(\gamma\): discount factor

---

## 3. Algorithm Steps

1. **Initialize** the Q-values \(Q(s,a)\) arbitrarily (e.g., zero).
2. **Observe** the initial state \(s\).
3. **Choose** an action \(a\) from \(s\) using the current policy (e.g., \(\epsilon\)-greedy based on \(Q\)).
4. **Repeat** for each step of the episode:
   - Take action \(a\), observe reward \(r\) and next state \(s'\).
   - Choose next action \(a'\) from \(s'\) using the policy (e.g., \(\epsilon\)-greedy).
   - Update Q-value:
     \[
     Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma Q(s', a') - Q(s,a) \right]
     \]
   - Update state-action pair: \(s \leftarrow s', a \leftarrow a'\).
5. **Repeat** until episode ends or convergence.

---

## 4. Characteristics

| Feature               | Description                                     |
|-----------------------|------------------------------------------------|
| **On-policy**          | Learns value of the policy it is actually following |
| **Bootstrapping**      | Updates Q-values using existing estimates       |
| **Exploration**        | Typically uses \(\epsilon\)-greedy policy       |
| **Convergence**        | Converges to optimal policy under suitable conditions (e.g., decaying \(\epsilon\), learning rate) |

---

## 5. Intuition

- SARSA learns the value of the policy it follows, including the exploratory actions.
- Because it updates based on the actual next action \(a'\), it naturally accounts for the current exploration strategy.
- This can lead to more conservative learning compared to off-policy methods (like Q-learning) which assume greedy next actions.

---

## 6. Pseudocode

```python
Initialize Q(s,a) arbitrarily
For each episode:
    Initialize state s
    Choose action a from s using policy derived from Q (e.g., ε-greedy)
    Repeat for each step of episode:
        Take action a, observe reward r and next state s'
        Choose next action a' from s' using policy derived from Q (ε-greedy)
        Q[s,a] = Q[s,a] + α * (r + γ * Q[s',a'] - Q[s,a])
        s = s'; a = a'
    until s is terminal

---

## 7. Summary

| Aspect            | SARSA                                   |
|-------------------|-----------------------------------------|
| Type              | On-policy TD control algorithm          |
| Updates           | Uses \((s,a,r,s',a')\) tuple            |
| Policy            | Learns value of behavior policy         |
| Exploration       | Naturally incorporates exploration policy|
| Use Cases         | Tasks where following the current policy matters, safe learning |

---

SARSA is a foundational RL algorithm balancing learning and exploration by updating based on the actual behavior policy.
```

# Q-Learning Algorithm in Reinforcement Learning

---

## 1. What is Q-Learning?

- **Q-Learning** is a popular **off-policy** Temporal-Difference (TD) control algorithm.
- It learns the **optimal action-value function** \(Q^*(s,a)\) directly, regardless of the policy being followed.
- The learned \(Q^*\) can be used to derive the optimal policy by choosing actions that maximize \(Q^*(s,a)\).

---

## 2. Key Idea

Q-Learning updates the Q-value \(Q(s,a)\) using the current state-action pair \((s,a)\), the reward \(r\), the next state \(s'\), and the maximum Q-value over all possible actions in \(s'\):

\[
Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s,a) \right]
\]

- \(\alpha\): learning rate  
- \(\gamma\): discount factor

This update uses the **greedy action** at the next state, regardless of the action actually taken.

---

## 3. Algorithm Steps

1. **Initialize** Q-values \(Q(s,a)\) arbitrarily (e.g., zero).
2. **Observe** the initial state \(s\).
3. **Repeat** for each step of the episode:
   - Select an action \(a\) from \(s\) using an exploration policy (e.g., \(\epsilon\)-greedy).
   - Execute action \(a\), observe reward \(r\) and next state \(s'\).
   - Update Q-value:
     \[
     Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s,a) \right]
     \]
   - Update state: \(s \leftarrow s'\).
4. **Repeat** until episode ends or convergence.

---

## 4. Characteristics

| Feature               | Description                                     |
|-----------------------|------------------------------------------------|
| **Off-policy**         | Learns optimal policy independent of actual policy followed |
| **Bootstrapping**      | Updates based on estimated optimal future value |
| **Exploration**        | Uses separate exploration policy (e.g., \(\epsilon\)-greedy) |
| **Convergence**        | Proven to converge to optimal \(Q^*\) under suitable conditions |

---

## 5. Intuition

- Q-Learning estimates the best possible future reward assuming **greedy action selection** from the next state onward.
- It can learn optimal behavior while following an exploratory (non-greedy) policy.
- This separation makes it more flexible and widely used.

---

## 6. Pseudocode

```python
Initialize Q(s,a) arbitrarily
For each episode:
    Initialize state s
    Repeat for each step of episode:
        Choose action a from s using exploration policy (e.g., ε-greedy)
        Take action a, observe reward r and next state s'
        Q[s,a] = Q[s,a] + α * (r + γ * max_{a'} Q[s',a'] - Q[s,a])
        s = s'
    until s is terminal

---

## 7. Summary

| Aspect            | Q-Learning                              |
|-------------------|----------------------------------------|
| Type              | Off-policy TD control algorithm        |
| Updates           | Uses \((s,a,r,s')\) tuple and max over next actions |
| Policy            | Learns optimal policy regardless of behavior policy |
| Exploration       | Separate from learning policy (e.g., \(\epsilon\)-greedy) |
| Use Cases         | Wide application; effective in many environments |

---

Q-Learning is a foundational RL algorithm that enables learning optimal policies through direct estimation of action values.
```

# Difference Between On-Policy and Off-Policy Algorithms in Reinforcement Learning

---

## 1. Definitions

- **On-Policy Algorithms**  
  Learn the value of the **policy being actually followed** by the agent, including its exploration behavior. The policy used to generate behavior (behavior policy) and the policy being evaluated or improved (target policy) are the **same**.

- **Off-Policy Algorithms**  
  Learn the value of an **optimal or target policy** different from the policy used to generate behavior (behavior policy). The behavior policy and target policy are **different**.

---

## 2. Key Differences

| Aspect                   | On-Policy                         | Off-Policy                             |
|--------------------------|----------------------------------|--------------------------------------|
| **Policy Evaluated**     | The same policy used to select actions (behavior policy = target policy) | A different policy from the behavior policy (target policy ≠ behavior policy) |
| **Exploration**          | Exploration is integrated into the policy being learned (e.g., \(\epsilon\)-greedy) | Can learn optimal policy while following exploratory behavior policy |
| **Examples of Algorithms** | SARSA, Monte Carlo control (on-policy) | Q-Learning, Expected SARSA, Deep Q-Network (DQN) |
| **Learning Stability**   | Typically more stable, since learning matches behavior | Can be less stable due to discrepancy between behavior and target policies |
| **Use Cases**            | When it is important to evaluate or improve the current behavior policy | When the goal is to learn an optimal policy irrespective of current behavior |

---

## 3. Intuition

- **On-Policy:** Learn about and improve the policy you are currently using, including its exploration steps.  
  *“Learn while acting.”*

- **Off-Policy:** Learn about the best possible policy even if you are currently exploring or acting differently.  
  *“Learn from others’ experience.”*

---

## 4. Summary Table

| Feature               | On-Policy                   | Off-Policy                    |
|-----------------------|-----------------------------|-------------------------------|
| Behavior Policy       | Same as target policy       | Different from target policy  |
| Policy Improvement    | Improves the policy used to generate data | Improves a different (often optimal) policy |
| Exploration Handling  | Exploration is part of the policy | Exploration can be separate from learning |
| Example Update Rule   | Uses action actually taken next (e.g., SARSA) | Uses greedy max action next (e.g., Q-Learning) |

---

## 5. Practical Considerations

- **On-Policy** methods are simpler and safer when the current policy must be evaluated accurately.
- **Off-Policy** methods are more flexible and powerful, capable of learning optimal policies while following exploratory or random policies.

---

Understanding these differences is crucial for selecting appropriate RL algorithms based on task requirements and constraints.