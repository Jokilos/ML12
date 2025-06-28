# Value-based methods



---

## **Relation of Value Function and Policy**

- **Policy (π):**  
  A policy defines the agent’s behavior—how it selects actions in each state.

- **Value Function (V or Q):**  
  A value function measures how good it is to follow a particular policy.  
  - **V<sup>π</sup>(s):** Expected cumulative reward when starting from state s and following policy π.
  - **Q<sup>π</sup>(s, a):** Expected cumulative reward when starting from state s, taking action a, and then following π.

---

### **Key Points of the Relationship**

1. **Value functions are always defined with respect to a specific policy.**
   - The value function tells you the expected return if you act according to that policy.

2. **The value function evaluates a policy.**
   - It quantifies how good it is to be in a state (or to take an action) under the policy.

3. **Improving policies using value functions:**
   - One can improve a policy by selecting actions that maximize the value function.
   - **Policy improvement:** Choose actions that maximize Q<sup>π</sup>(s, a) to get a better policy π'.

4. **Optimal Value Function and Policy:**
   - The optimal value function (V*) gives the best possible return from any state.
   - The optimal policy (π*) always selects actions that maximize the optimal value function.

---

### **Example**

- **Maze Game:**
  - **Policy:** Always move right.
  - **V<sup>π</sup>(s):** Average score if you always move right from state s.
  - If you find a better policy (e.g., move up when near the goal), its value function will be higher.

---

**In summary:**  
A value function tells you how good a policy is; you can use it to compare and improve policies. They are fundamentally linked: value functions evaluate policies, and good value functions guide the search for better policies.


---

## **Value Function vs. Q-Function**

| Aspect                | Value Function (V)                        | Q-Function (Action-Value, Q)                       |
|-----------------------|-------------------------------------------|----------------------------------------------------|
| **Definition**        | Expected cumulative reward from a state, following a policy | Expected cumulative reward from a state **and action**, then following a policy |
| **Notation**          | V<sup>π</sup>(s)                          | Q<sup>π</sup>(s, a)                                |
| **Depends on**        | State (s)                                 | State (s) and Action (a)                           |
| **Usage**             | Evaluates how good it is to be in a state under a policy | Evaluates how good it is to take an action from a state under a policy |
| **Policy Derivation** | Policy selects best action based on value of next state | Policy directly chooses the action with highest Q-value |

---

### **Example (Gridworld):**

- **V<sup>π</sup>(s):**  
  The expected total reward if the agent starts in cell s and follows π.

- **Q<sup>π</sup>(s, a):**  
  The expected total reward if the agent starts in cell s, takes action a, then follows π.

---

**Summary:**  
- **Value function (V):** How good is it to be in state s?
- **Q-function (Q):** How good is it to take action a in state s?

---


---

## **Bellman Equations in Reinforcement Learning**

There are **two main Bellman equations**—one for the value function (V) and one for the action-value function (Q).

---

### **1. Bellman Equation for the Value Function (V)**

For a given policy π:

\[
V^{\pi}(s) = \mathbb{E}_{a \sim \pi(s)} \left[ R(s, a) + \gamma \mathbb{E}_{s' \sim P(s'|s,a)} \left[ V^{\pi}(s') \right] \right]
\]

*In words:*  
The value of state s under policy π equals the expected immediate reward plus the discounted value of the next state, assuming the agent follows π.

---

### **2. Bellman Equation for the Q-Function (Q)**

For a given policy π:

\[
Q^{\pi}(s, a) = \mathbb{E}_{s' \sim P(s'|s,a)} \left[ R(s, a) + \gamma \mathbb{E}_{a' \sim \pi(s')} \left[ Q^{\pi}(s', a') \right] \right]
\]

*In words:*  
The value of taking action a in state s under π is the expected reward plus the discounted expected value of the next state-action pair.

---

### **Bellman Optimality Equations**

For the **optimal policy (π\*)**, the equations become:

- **Value Function:**
  \[
  V^*(s) = \max_{a} \mathbb{E}_{s'} \left[ R(s, a) + \gamma V^*(s') \right]
  \]

- **Q-Function:**
  \[
  Q^*(s, a) = \mathbb{E}_{s'} \left[ R(s, a) + \gamma \max_{a'} Q^*(s', a') \right]
  \]

---

## **Summary Table**

| Name                      | Equation                                                         |
|---------------------------|------------------------------------------------------------------|
| Bellman for V<sup>π</sup> | \( V^{\pi}(s) = \mathbb{E}_{a \sim \pi(s)} [R(s, a) + \gamma \mathbb{E}_{s'} [V^{\pi}(s')]] \) |
| Bellman for Q<sup>π</sup> | \( Q^{\pi}(s, a) = \mathbb{E}_{s'} [R(s, a) + \gamma \mathbb{E}_{a'} [Q^{\pi}(s', a')]] \)     |
| Bellman Optimal V         | \( V^*(s) = \max_{a} \mathbb{E}_{s'} [R(s, a) + \gamma V^*(s')] \)          |
| Bellman Optimal Q         | \( Q^*(s, a) = \mathbb{E}_{s'} [R(s, a) + \gamma \max_{a'} Q^*(s', a')] \)  |

---

**In total, there are two main Bellman equations (one for V, one for Q), each with a version for a general policy and an optimal policy.**Here is the answer:

---

## **Bellman Equation**

The Bellman equation expresses the relationship between the value of a state (or state-action pair) and the values of its successor states.

---

### **1. Bellman Equation for Value Function (V)**

For a policy π:

\[
V^{\pi}(s) = \mathbb{E}_{a \sim \pi(s)} \left[ R(s, a) + \gamma \mathbb{E}_{s' \sim P(s'|s,a)} [V^{\pi}(s')] \right]
\]

---

### **2. Bellman Equation for Q-Function (Q)**

For a policy π:

\[
Q^{\pi}(s, a) = \mathbb{E}_{s' \sim P(s'|s,a)} \left[ R(s, a) + \gamma \mathbb{E}_{a' \sim \pi(s')} [Q^{\pi}(s', a')] \right]
\]

---

### **Optimal Bellman Equations**

- **Optimal Value Function:**
  \[
  V^*(s) = \max_{a} \mathbb{E}_{s'} \left[ R(s, a) + \gamma V^*(s') \right]
  \]

- **Optimal Q-Function:**
  \[
  Q^*(s, a) = \mathbb{E}_{s'} \left[ R(s, a) + \gamma \max_{a'} Q^*(s', a') \right]
  \]

---

**There are two main types of Bellman equations:**
- For the value function (V)
- For the action-value function (Q)  
Each can be written for a specific policy (π) or optimally (∗).

---


---

## **Policy Iteration Algorithm**

**Policy Iteration** is a classic algorithm for finding the optimal policy in a Markov Decision Process (MDP). It alternates between evaluating the current policy and improving it until convergence.

---

### **Stages of Policy Iteration**

1. **Policy Evaluation**
   - Calculate the value function \( V^{\pi} \) for the current policy π.
   - This step estimates how good it is to follow π from every state.

2. **Policy Improvement**
   - Update the policy π by choosing the action that maximizes expected return using the current value function.
   - For each state s:  
     \( \pi_{new}(s) = \arg\max_{a} \mathbb{E}_{s'} [R(s, a) + \gamma V^{\pi}(s')] \)

3. **Repeat**
   - Alternate between policy evaluation and policy improvement until the policy stabilizes (no changes).

---

### **Summary Table**

| Stage              | Description                                             |
|--------------------|--------------------------------------------------------|
| Policy Evaluation  | Compute \( V^{\pi} \) for current π                    |
| Policy Improvement | Update π using the new value function                  |
| Repeat             | Continue until π does not change (converges)           |

---

**Result:**  
The algorithm finds the optimal policy and value function for the MDP.

---


---

## **Model-Free vs. Model-Based Methods**

| Aspect         | Model-Free Methods                            | Model-Based Methods                               |
|----------------|-----------------------------------------------|---------------------------------------------------|
| **Definition** | Learn directly from experience without knowing the environment’s dynamics | Learn or use a model of the environment’s dynamics (transition probabilities & rewards) |
| **Key Idea**   | No explicit model of environment; just learn value/policy | Build/learn a model, then use it for planning or policy learning |
| **Examples**   | Q-learning, SARSA, Policy Gradient            | Dyna-Q, Monte Carlo Tree Search, Value Iteration   |
| **Planning**   | Cannot plan ahead; can only act/react         | Can simulate future steps for planning             |
| **Sample Efficiency** | Often less sample efficient (needs more experience) | More sample efficient (can learn from imagined experiences) |
| **Flexibility**| Simpler, easier for complex/unknown environments | More complex, but can enable planning and faster learning |

---

### **Summary**

- **Model-Free:** No knowledge of how the environment works; learns what to do just by trial and error.
- **Model-Based:** Builds or uses a model of the environment, enabling planning and faster learning.

---


---

## **Prediction vs. Control in Reinforcement Learning**

| Aspect         | Prediction                              | Control                                   |
|----------------|----------------------------------------|-------------------------------------------|
| **Goal**       | Evaluate a given policy                | Find the optimal policy                   |
| **Question**   | “How good is this policy?”             | “What is the best policy?”                |
| **Task**       | Estimate value functions (V<sup>π</sup>, Q<sup>π</sup>) for a fixed π | Improve policy to maximize rewards        |
| **Example**    | Calculate expected rewards if agent always moves right | Learn whether moving right or left is better and choose the best overall strategy |

---

**Summary:**  
- **Prediction:** Value estimation for a specific, fixed policy.
- **Control:** Finding and learning the best (optimal) policy.

---


---

## **Monte Carlo vs. Temporal-Difference (TD) Methods**

| Aspect                | Monte Carlo (MC)                       | Temporal-Difference (TD)                |
|-----------------------|----------------------------------------|-----------------------------------------|
| **Learning Signal**   | Uses complete returns (actual total reward at the end of an episode) | Uses bootstrapping (updates based on current estimate and observed reward) |
| **Update Timing**     | Updates only at the end of an episode  | Updates after every step (can be online)|
| **Need for Episodes** | Requires episodes to terminate         | Works in continuing tasks (does not require episodes to end) |
| **Bias/Variance**     | Unbiased but high variance             | Biased but lower variance               |
| **Examples**          | MC prediction, MC control              | TD(0), SARSA, Q-learning                |

---

### **Summary Table**

| Feature         | Monte Carlo          | Temporal-Difference      |
|-----------------|---------------------|-------------------------|
| Update Target   | Actual return       | \( r + \gamma V(s') \)  |
| When Update     | End of episode      | Each time step          |
| Bootstrapping   | No                  | Yes                     |

---

**Summary:**  
- **Monte Carlo:** Learns from complete episodes using the actual total reward.
- **TD:** Learns step-by-step, updating estimates using other current estimates.

---


---

## **TD(k) and TD(λ)**

### **TD(k)**
- **Definition:**  
  Temporal-Difference learning with a fixed n-step lookahead (often written as TD(n)).
- **How it works:**  
  Updates value estimates using the actual rewards for the next k steps, then bootstraps from the value estimate at step k.
- **Update target:**  
  \[
  G_t^{(k)} = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \dots + \gamma^{k-1} r_{t+k-1} + \gamma^k V(s_{t+k})
  \]
- **Trade-off:**  
  - TD(1) = Monte Carlo (full episode)
  - TD(0) = one-step TD
  - TD(k) interpolates between them

---

### **TD(λ)**
- **Definition:**  
  A generalization of TD(k), called TD-lambda, that combines information from all possible n-step returns using a parameter λ (0 ≤ λ ≤ 1).
- **How it works:**  
  Computes a weighted average of all n-step returns, where λ controls the weight (exponentially decaying for longer n).
- **Eligibility traces:**  
  Used for efficient implementation, allowing the algorithm to assign credit to recently visited states.
- **Special cases:**  
  - TD(0): Pure one-step TD learning (λ = 0)
  - TD(1): Equivalent to Monte Carlo (λ = 1)
- **Advantage:**  
  Balances bias and variance; combines benefits of TD and MC methods.

---

**Summary Table:**

| Method   | Description                                               | Special Cases         |
|----------|----------------------------------------------------------|----------------------|
| TD(k)    | Uses reward over k steps, then bootstraps                | k=1: TD(0), k=episode: MC |
| TD(λ)    | Weighted average of all n-step returns (0 ≤ λ ≤ 1)       | λ=0: TD(0), λ=1: MC  |

---


---

## **SARSA Algorithm**

**SARSA** stands for:  
**State–Action–Reward–State–Action**  
It is an **on-policy** Temporal-Difference (TD) control algorithm.

---

### **How SARSA Works**

1. **Initialize** Q-values \( Q(s, a) \) arbitrarily for all states and actions.
2. For each episode:
   - Initialize state \( s \)
   - Choose action \( a \) using the current policy (e.g., ε-greedy from Q)
   - Repeat for each step of the episode:
     1. Take action \( a \), observe reward \( r \) and next state \( s' \)
     2. Choose next action \( a' \) using the current policy (from \( Q \))
     3. Update Q-value:
        \[
        Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma Q(s', a') - Q(s, a) \right]
        \]
     4. Set \( s = s' \), \( a = a' \)
   - Until \( s' \) is terminal

---

### **Key Points**

- **On-policy:** Updates Q-values based on the action actually taken by the current policy.
- **Exploration:** Typically uses ε-greedy policy for exploration.
- **Updates:** Uses the next action chosen by the same policy for bootstrapping.

---

### **Summary Table**

| Step        | Description                                     |
|-------------|------------------------------------------------|
| S           | Current state                                  |
| A           | Current action                                 |
| R           | Reward received                                |
| S’          | Next state                                     |
| A’          | Next action (chosen by current policy)         |

---

**In short:**  
SARSA learns the action-value function for the policy it is actually following, updating based on the sequence (State, Action, Reward, State, Action).

---


---

## **Q-Learning Algorithm**

**Q-learning** is an **off-policy** Temporal-Difference (TD) control algorithm that learns the optimal action-value function, regardless of the policy being followed.

---

### **How Q-learning Works**

1. **Initialize** Q-values \( Q(s, a) \) arbitrarily for all states and actions.
2. For each episode:
   - Initialize state \( s \)
   - Repeat for each step of the episode:
     1. Choose action \( a \) (e.g., ε-greedy from Q)
     2. Take action \( a \), observe reward \( r \) and next state \( s' \)
     3. Update Q-value:
        \[
        Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
        \]
     4. Set \( s = s' \)
   - Until \( s' \) is terminal

---

### **Key Points**

- **Off-policy:** Updates Q-values using the maximum estimated value for the next state, independent of the agent’s actual actions.
- **Exploration:** Typically uses ε-greedy for action selection.
- **Goal:** Learns the optimal action-value function \( Q^*(s, a) \).

---

### **Summary Table**

| Step        | Description                                     |
|-------------|------------------------------------------------|
| S           | Current state                                  |
| A           | Current action                                 |
| R           | Reward received                                |
| S’          | Next state                                     |
| max \( Q(s', a') \) | Maximum Q-value for next state         |

---

**In short:**  
Q-learning learns the optimal policy by updating Q-values towards the best possible future values, regardless of the policy currently being executed.

---


---

## **On-Policy vs. Off-Policy Algorithms**

| Aspect        | On-Policy                                 | Off-Policy                              |
|---------------|-------------------------------------------|-----------------------------------------|
| **Definition**| Learns the value of the policy being actually followed | Learns the value of an optimal or different policy, regardless of the agent's actions |
| **Learning**  | Uses the same policy for action selection and learning updates | Can use one policy to generate behavior (behavior policy), and another to update (target policy) |
| **Examples**  | SARSA, On-policy Monte Carlo              | Q-learning, Off-policy Monte Carlo      |
| **Exploration**| Must explore with the same policy it's learning about | Can explore with any policy, learns about the optimal one |
| **Practicality** | Often safer, but may converge slower   | Often more efficient, but can be less stable |

---

**Summary:**  
- **On-policy:** Learns about the policy it is actually following.
- **Off-policy:** Learns about a different (often optimal) policy, while possibly following another for exploration.

---