# Function approximation 



---

## **Model-Free Prediction with Function Approximation**

**Goal:**  
Estimate the value function \( V^\pi(s) \) for a given policy π in large/continuous state spaces using function approximators.

---

### **1. Function Approximation**

- **Representation:**  
  Use a parameterized function \( \hat{V}(s, w) \) (e.g., linear model, neural network) instead of a table.
- **Update:**  
  Adjust parameters \( w \) based on experience to minimize the prediction error.

---

### **2. Monte-Carlo (MC) Prediction with Function Approximation**

- **Target:**  
  The actual return \( G_t \) (total reward from time t to end of episode).
- **Update Rule:**  
  \[
  w \leftarrow w + \alpha \left[G_t - \hat{V}(s_t, w)\right] \nabla_w \hat{V}(s_t, w)
  \]
- **Characteristics:**  
  - Updates only at the end of episodes.
  - No bootstrapping (uses true returns).
  - Works for episodic tasks.

---

### **3. Temporal-Difference (TD) Prediction with Function Approximation**

- **Target:**  
  The one-step TD target: \( r_{t} + \gamma \hat{V}(s_{t+1}, w) \).
- **Update Rule:**  
  \[
  w \leftarrow w + \alpha \left[r_{t} + \gamma \hat{V}(s_{t+1}, w) - \hat{V}(s_t, w)\right] \nabla_w \hat{V}(s_t, w)
  \]
- **Characteristics:**  
  - Updates after every step (online).
  - Bootstraps using current value estimate.
  - Works for both episodic and continuing tasks.

---

### **Summary Table**

| Aspect          | Monte-Carlo                      | Temporal-Difference         |
|-----------------|----------------------------------|-----------------------------|
| Target          | Full return \( G_t \)            | \( r_{t} + \gamma \hat{V}(s_{t+1}, w) \) |
| Update timing   | End of episode                   | Each time step              |
| Bootstrapping   | No                               | Yes                         |
| Applicability   | Episodic tasks                   | Episodic & continuing tasks |

---

**In short:**  
Model-free prediction with function approximators generalizes value estimates to large spaces, using MC or TD methods to update the parameters based on the observed data.

---


---

## **Potential Problems with Function Approximators in RL**

When using function approximators (like neural networks) in reinforcement learning, several issues can arise:

- **Instability and Divergence:**  
  The learning process may become unstable or even diverge (values grow without bound).
- **Overgeneralization:**  
  Updates to the function approximator in one region can negatively affect value estimates in other regions.
- **Non-stationarity:**  
  The target values change as the policy and value estimates change, making learning more difficult.
- **Bias and Variance:**  
  Approximation may introduce bias (systematic errors) or high variance (noisy estimates).

---

## **The Deadly Triad**

The **deadly triad** refers to a combination of three elements that, when used together, can cause instability and divergence in RL:

1. **Function Approximation:**  
   Using parameterized models (e.g., neural networks) to estimate value functions.

2. **Bootstrapping:**  
   Updating estimates based on other learned estimates (e.g., TD methods using \( r + \gamma V(s') \) as a target).

3. **Off-policy Learning:**  
   Learning the value of one policy (target policy) while following another (behavior policy), as in Q-learning.

**When all three are present, RL algorithms are especially prone to instability and divergence.**

---

### **Summary Table**

| Problematic Element   | Description                              |
|----------------------|-------------------------------------------|
| Function Approximation | Generalizes value estimates              |
| Bootstrapping        | Updates using other estimated values      |
| Off-policy Learning  | Policy being learned ≠ policy generating data |

---

**In summary:**  
Combining function approximation, bootstrapping, and off-policy learning (the deadly triad) can make RL training unstable or divergent.

---


---

## **DQN Algorithm (Deep Q-Network)**

**DQN** is a deep reinforcement learning algorithm that uses a neural network to approximate the Q-function for large/complex state spaces.

---

### **How DQN Works**

1. **Q-Network:**  
   Use a neural network \( Q(s, a; \theta) \) to approximate the action-value function.
2. **Experience Replay:**  
   Store transitions (state, action, reward, next state) in a replay buffer. Sample random minibatches for training to break correlations and improve data efficiency.
3. **Target Network:**  
   Use a separate target network \( Q_{\text{target}}(s, a; \theta^-) \) (a copy of the Q-network) for computing TD targets. Update its parameters less frequently to stabilize targets.

---

### **DQN Update Rule**

For a minibatch of transitions \((s, a, r, s')\):

\[
y = r + \gamma \max_{a'} Q_{\text{target}}(s', a'; \theta^-)
\]

Network parameters are updated by minimizing the loss:

\[
L(\theta) = \mathbb{E} \left[ \left( y - Q(s, a; \theta) \right)^2 \right]
\]

---

### **Problems DQN Aims to Solve**

DQN addresses instability and divergence issues of function approximation in RL, especially with the deadly triad:

1. **Experience Replay:**  
   - Breaks correlations in sequential data.
   - Increases sample efficiency.
2. **Target Network:**  
   - Stabilizes learning targets.
   - Reduces oscillations and divergence due to rapidly shifting targets.
3. **Mini-batch Updates:**  
   - Smoother and more stable gradient updates.

---

### **Summary Table**

| DQN Component     | Purpose                                  |
|-------------------|------------------------------------------|
| Experience Replay | Decorrelate updates, stabilize learning  |
| Target Network    | Fix targets temporarily, reduce feedback loops |
| Deep Network      | Generalize Q-function in large spaces    |

---

**In short:**  
DQN combines neural networks, experience replay, and target networks to enable stable, scalable Q-learning with function approximation, addressing the deadly triad’s instability.

---