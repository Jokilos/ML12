# Policy gradient-methods


# When to Use Policy Methods vs. Value Methods in Reinforcement Learning

---

## 1. Overview

Both **policy-based methods** and **value-based methods** are fundamental approaches in reinforcement learning (RL) with different strengths and weaknesses. Choosing between them depends on the problem characteristics and practical considerations.

---

## 2. Value-Based Methods

### What They Do
- Learn a value function (e.g., \(Q(s,a)\) or \(V(s)\)) and derive a policy by selecting actions that maximize the value.
- Examples: Q-learning, SARSA, Deep Q-Networks (DQN).

### When to Use Value-Based Methods

| Scenario/Condition                       | Reason                                      |
|----------------------------------------|---------------------------------------------|
| **Discrete and low-dimensional action spaces** | Easy to represent and maximize over actions explicitly. |
| **Environments where optimal policy is deterministic** | Value-based methods naturally find greedy optimal policies. |
| **Sample efficiency is important** | Value methods often require fewer samples in simple domains. |
| **You want to reuse old experience efficiently** | Many value methods use replay buffers effectively. |

### Limitations

- Difficult to scale to **continuous or high-dimensional action spaces**.
- May struggle with stochastic policies or partial observability.

---

## 3. Policy-Based Methods

### What They Do
- Directly parameterize and optimize the policy \(\pi_\theta(a|s)\) without requiring a value function (though often combined with one).
- Examples: REINFORCE, Actor-Critic methods, Proximal Policy Optimization (PPO).

### When to Use Policy-Based Methods

| Scenario/Condition                       | Reason                                      |
|----------------------------------------|---------------------------------------------|
| **Continuous or high-dimensional action spaces** | Directly parameterizing policies is easier than value maximization. |
| **Stochastic policies needed (e.g., for exploration or partial observability)** | Policy methods naturally represent stochastic policies. |
| **Smooth policy updates desired** | Policy gradients provide stable, incremental improvements. |
| **When modeling complex policies with neural networks** | Policy methods handle complex policy parameterizations well. |
| **Partially Observable Markov Decision Processes (POMDPs)** | Stochastic policies can better handle uncertainty. |

### Limitations

- Typically have **higher variance** in gradient estimates.
- Often require more samples for convergence.
- May be less sample efficient in some settings.

---

## 4. Summary Comparison

| Feature                     | Value-Based Methods                    | Policy-Based Methods                     |
|-----------------------------|-------------------------------------|-----------------------------------------|
| Policy Representation       | Implicit (greedy w.r.t value)        | Explicit (parameterized policy)          |
| Action Space                | Discrete, low-dimensional             | Continuous or discrete                    |
| Policy Type                | Usually deterministic                 | Can be stochastic or deterministic       |
| Sample Efficiency           | Generally higher in simple tasks      | Often lower, but improving with actor-critic |
| Exploration Handling        | Via value estimates                   | Intrinsic via stochastic policies         |
| Stability                  | Can be unstable with function approximation | Typically more stable with proper baselines |
| Computational Complexity    | Usually simpler                       | Can be more computationally intensive     |

---

## 5. Practical Advice

- Use **value-based methods** when:
  - Action space is discrete and manageable.
  - You want a simpler, sample-efficient solution.
- Use **policy-based methods** when:
  - Action space is continuous or very large.
  - You require stochastic policies or smooth policy improvements.
  - The task involves partial observability or complex policies.

---

## 6. Hybrid Approaches

- **Actor-Critic methods** combine value and policy methods to leverage their strengths:
  - Critic estimates value functions to reduce variance.
  - Actor updates policy parameters directly.

---

Choosing between policy and value methods depends on task requirements, action space characteristics, and computational constraints.

# Two Gradient-Free Policy Algorithms in Reinforcement Learning

---

## 1. Evolution Strategies (ES)

- A class of black-box optimization algorithms inspired by natural evolution.
- Optimize policy parameters by evaluating performance of perturbed parameter vectors.
- Does **not** require gradient information; uses fitness measurements to guide updates.
- Suitable for high-dimensional, continuous control problems.

---

## 2. Cross-Entropy Method (CEM)

- A population-based optimization technique.
- Iteratively samples policy parameters from a distribution, evaluates them, and updates the distribution to focus on the best-performing samples.
- Does not rely on gradients; uses sampling and selection to improve policies.

---

Both ES and CEM are examples of **gradient-free** policy optimization methods that explore policy space via black-box optimization rather than differentiable updates.

# Evolutionary Strategies (ES): Strengths and Weaknesses

---

## 1. What are Evolutionary Strategies?

- Evolutionary Strategies are gradient-free, black-box optimization algorithms inspired by biological evolution.
- They optimize policy parameters by iteratively sampling, evaluating, and updating a population of candidate solutions based on their performance.

---

## 2. Strengths of Evolutionary Strategies

| Strength                            | Explanation                                      |
|-----------------------------------|-------------------------------------------------|
| **Gradient-Free Optimization**    | Can optimize non-differentiable, noisy, or complex objectives where gradients are unavailable or unreliable. |
| **Scalability and Parallelism**   | Highly parallelizable since evaluations of candidate solutions are independent; well-suited for distributed computing. |
| **Robustness to Local Optima**    | Population-based search helps avoid getting stuck in local minima compared to gradient-based methods. |
| **Simplicity**                    | Conceptually simple and easy to implement without requiring gradient computations or backpropagation. |
| **Works with Black-Box Policies** | Can optimize any policy parameterization, including non-differentiable or simulator-based policies. |

---

## 3. Weaknesses of Evolutionary Strategies

| Weakness                          | Explanation                                      |
|----------------------------------|-------------------------------------------------|
| **Sample Inefficiency**           | Requires a large number of environment interactions (samples) to evaluate many candidate solutions. |
| **Slow Convergence**              | Typically slower than gradient-based methods, especially in high-dimensional parameter spaces. |
| **Lack of Fine-Grained Updates** | Updates are based on population statistics, which may be less precise than gradient-based updates. |
| **No Exploitation of Problem Structure** | Does not leverage gradient information or domain knowledge, potentially missing faster optimization paths. |
| **Scaling to Very High Dimensions** | Performance can degrade as the number of parameters grows, requiring more samples to explore effectively. |

---

## 4. Summary Table

| Aspect                 | Strengths                                | Weaknesses                          |
|------------------------|-----------------------------------------|-----------------------------------|
| Gradient Requirement    | Not required                            | N/A                               |
| Parallelism            | Excellent (evaluations are independent) | N/A                               |
| Sample Efficiency       | Low (requires many samples)              | Inefficient for complex tasks     |
| Convergence Speed       | Relatively slow                         | Can be slow compared to gradient methods |
| Applicability           | Black-box, non-differentiable policies  | May struggle with very large parameter spaces |

---

## 5. Conclusion

Evolutionary Strategies are powerful for problems where gradients are unavailable or unreliable and when parallel computation resources are abundant. However, they tend to be less sample efficient and slower to converge compared to gradient-based reinforcement learning methods.

---

# Comparison of On-Policy and Off-Policy Methods in Reinforcement Learning

---

## 1. Definitions

- **On-Policy Methods:**  
  Learn the value of and improve the **same policy** that is used to make decisions and generate data (behavior policy = target policy).

- **Off-Policy Methods:**  
  Learn the value of an **optimal or target policy** different from the policy used to generate behavior (behavior policy ≠ target policy).

---

## 2. Comparison Table

| Aspect                      | On-Policy Methods                                | Off-Policy Methods                               |
|-----------------------------|-------------------------------------------------|-------------------------------------------------|
| **Behavior vs Target Policy** | Behavior policy = Target policy                   | Behavior policy ≠ Target policy                   |
| **Data Usage**               | Learns from actions taken by current policy      | Learns from actions that may be exploratory or different |
| **Exploration Handling**     | Exploration is part of the policy being evaluated | Exploration can be separate from the policy being learned |
| **Stability**               | Generally more stable                             | Can be less stable due to distribution mismatch  |
| **Sample Efficiency**        | Often less sample efficient                       | Often more sample efficient                        |
| **Policy Type**              | Typically stochastic policies                      | Can learn deterministic or stochastic policies    |
| **Learning Target**          | Evaluates/improves current policy                 | Evaluates/improves an optimal or different policy |
| **Examples of Algorithms**   | SARSA, REINFORCE, Actor-Critic                    | Q-Learning, Deep Q-Network (DQN), Expected SARSA |

---

## 3. Examples of Algorithms

| On-Policy Algorithms         | Off-Policy Algorithms          |
|------------------------------|-------------------------------|
| - SARSA                      | - Q-Learning                  |
| - REINFORCE (Monte Carlo)    | - Deep Q-Network (DQN)        |
| - Actor-Critic Methods (A2C, A3C) | - Expected SARSA             |
| - Proximal Policy Optimization (PPO) | - Deep Deterministic Policy Gradient (DDPG) |

---

## 4. When to Use Which?

| Scenario                         | Preferred Method                 |
|---------------------------------|--------------------------------|
| Need stable learning with policy matching behavior | On-policy methods               |
| Want to learn optimal policy independent of behavior | Off-policy methods              |
| Continuous action spaces with deterministic policies | Off-policy (e.g., DDPG)         |
| Problems with limited data and stable updates      | On-policy                      |

---

## 5. Summary

| Aspect             | On-Policy                         | Off-Policy                        |
|--------------------|----------------------------------|---------------------------------|
| Policy evaluated   | Current behavior policy           | Optimal or different policy       |
| Learning stability | Higher                          | Potentially lower                  |
| Exploration        | Incorporated in policy            | Separate from policy              |
| Sample efficiency  | Lower                           | Higher                           |
| Examples           | SARSA, REINFORCE, PPO             | Q-learning, DQN, DDPG             |

---

Understanding these differences assists in selecting the appropriate RL algorithm based on task requirements and data availability.

# Policy Gradient Theorem

---

## 1. Statement of the Policy Gradient Theorem

Given a parameterized stochastic policy \(\pi_\theta(a|s)\) and the objective function:

\[
J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_{t=0}^{\infty} \gamma^t r_{t+1} \right]
\]

the **policy gradient theorem** states that the gradient of \(J(\theta)\) with respect to \(\theta\) can be expressed as:

\[
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a|s) Q^{\pi_\theta}(s,a) \right]
\]

where \(Q^{\pi_\theta}(s,a)\) is the action-value function under policy \(\pi_\theta\).

---

## 2. Intuition

- The theorem expresses the gradient of expected return as an expectation over the gradient of the log-policy weighted by the action-value function.
- This allows estimating the gradient from sampled trajectories without needing the environment model.

---

## 3. Proof of the Policy Gradient Theorem

### Setup

- Define \(d^{\pi_\theta}(s)\) as the discounted state distribution under policy \(\pi_\theta\):

\[
d^{\pi_\theta}(s) = \sum_{t=0}^\infty \gamma^t P(S_t = s | \pi_\theta)
\]

- Objective function:

\[
J(\theta) = \sum_s d^{\pi_\theta}(s) \sum_a \pi_\theta(a|s) r(s,a)
\]

More generally, the expected return is:

\[
J(\theta) = \mathbb{E}_{s \sim d^{\pi_\theta}, a \sim \pi_\theta} \left[ Q^{\pi_\theta}(s,a) \right]
\]

---

### Step 1: Express the gradient of \(J(\theta)\)

\[
\nabla_\theta J(\theta) = \nabla_\theta \sum_s d^{\pi_\theta}(s) \sum_a \pi_\theta(a|s) r(s,a)
\]

More generally, for the expected return:

\[
\nabla_\theta J(\theta) = \nabla_\theta \sum_s d^{\pi_\theta}(s) \sum_a \pi_\theta(a|s) Q^{\pi_\theta}(s,a)
\]

---

### Step 2: Use the log-derivative trick on \(\pi_\theta(a|s)\)

\[
\nabla_\theta \pi_\theta(a|s) = \pi_\theta(a|s) \nabla_\theta \log \pi_\theta(a|s)
\]

Thus,

\[
\nabla_\theta J(\theta) = \sum_s d^{\pi_\theta}(s) \sum_a \nabla_\theta \pi_\theta(a|s) Q^{\pi_\theta}(s,a) + \sum_s \nabla_\theta d^{\pi_\theta}(s) \sum_a \pi_\theta(a|s) Q^{\pi_\theta}(s,a)
\]

---

### Step 3: Handle the gradient of the state distribution \(\nabla_\theta d^{\pi_\theta}(s)\)

- The term \(\nabla_\theta d^{\pi_\theta}(s)\) is complicated because the state distribution depends on the policy over multiple time steps.
- Using **Markov property** and the **policy gradient theorem**, this term can be shown to be accounted for implicitly when taking expectations over trajectories.

- **Key insight** (from Sutton et al., 2000): The second term can be rewritten so that only the first term remains in expectation form with respect to the discounted state visitation distribution.

---

### Step 4: Final form of the gradient

Putting it all together, the policy gradient reduces to:

\[
\nabla_\theta J(\theta) = \sum_s d^{\pi_\theta}(s) \sum_a \pi_\theta(a|s) \nabla_\theta \log \pi_\theta(a|s) Q^{\pi_\theta}(s,a)
\]

Or equivalently,

\[
\nabla_\theta J(\theta) = \mathbb{E}_{s \sim d^{\pi_\theta}, a \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a|s) Q^{\pi_\theta}(s,a) \right]
\]

---

## 4. Summary

- The policy gradient theorem provides a **tractable way to compute gradients** for policy optimization.
- It avoids differentiating the state distribution explicitly.
- Forms the basis for many policy gradient algorithms like REINFORCE and Actor-Critic methods.

---

## 5. References for Deeper Study

- Sutton, R. S., et al. (2000). *Policy Gradient Methods for Reinforcement Learning with Function Approximation*.  
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (Chapter 13).

---

# REINFORCE Algorithm

---

## 1. What is REINFORCE?

- REINFORCE is a **Monte Carlo policy gradient** algorithm introduced by Ronald Williams (1992).
- It directly optimizes a parameterized stochastic policy \(\pi_\theta(a|s)\) by using sampled trajectories to estimate the gradient of the expected return.
- It is one of the simplest policy gradient methods and serves as a foundation for many advanced algorithms.

---

## 2. Key Idea

- The algorithm updates policy parameters \(\theta\) in the direction that **increases the log-probability** of actions that lead to higher returns.
- Uses the **likelihood ratio trick** (log-derivative trick) to estimate the gradient.

---

## 3. Objective Function

The objective is to maximize the expected return:

\[
J(\theta) = \mathbb{E}_{\pi_\theta} \left[ G_t \right] = \mathbb{E}_{\pi_\theta} \left[ \sum_{k=t}^\infty \gamma^{k-t} r_{k+1} \right]
\]

where \(G_t\) is the return following time \(t\).

---

## 4. Update Rule

For each time step \(t\) in a sampled episode:

\[
\theta \leftarrow \theta + \alpha \gamma^t G_t \nabla_\theta \log \pi_\theta(a_t | s_t)
\]

- \(\alpha\): learning rate  
- \(\gamma^t\): discount factor weighting  
- \(G_t\): total discounted return from time \(t\)  
- \(\nabla_\theta \log \pi_\theta(a_t | s_t)\): gradient of log-probability of the action taken

---

## 5. Algorithm Steps

1. **Initialize** policy parameters \(\theta\).
2. **Repeat** for each episode:
   - Generate an episode by following policy \(\pi_\theta\):  
     \((s_0, a_0, r_1, s_1, a_1, r_2, \dots, s_{T})\).
   - For each time step \(t\) in the episode:
     - Compute return \(G_t = \sum_{k=t}^T \gamma^{k-t} r_{k+1}\).
     - Update policy parameters:
       \[
       \theta \leftarrow \theta + \alpha \gamma^t G_t \nabla_\theta \log \pi_\theta(a_t | s_t)
       \]
3. **Repeat** until convergence.

---

## 6. Characteristics

| Feature                   | Description                                      |
|---------------------------|-------------------------------------------------|
| **Type**                  | Monte Carlo, on-policy policy gradient           |
| **Update Frequency**      | At the end of each episode (using full returns)  |
| **Variance**              | High variance in gradient estimates               |
| **Bias**                  | Unbiased gradient estimates                        |
| **Use of Baselines**      | Can reduce variance by subtracting a baseline (e.g., value function) |

---

## 7. Strengths and Limitations

| Strengths                              | Limitations                            |
|---------------------------------------|--------------------------------------|
| Simple to implement                    | High variance in updates              |
| Does not require a value function     | Requires complete episodes (episodic)|
| Can optimize stochastic policies      | Slow convergence due to variance     |

---

## 8. Summary

| Notation                   | Description                            |
|----------------------------|--------------------------------------|
| \(\pi_\theta(a|s)\)        | Parameterized stochastic policy       |
| \(G_t\)                    | Return (sum of discounted future rewards) |
| \(\nabla_\theta \log \pi_\theta(a|s)\) | Gradient of log-policy                 |
| \(\alpha\)                 | Learning rate                        |

---

REINFORCE is a foundational policy gradient algorithm that enables direct policy optimization using sampled returns without requiring a value function or environment model.

---

# Asynchronous Advantage Actor-Critic (A3C) Algorithm

---

## 1. What is A3C?

- **A3C** is a popular **policy gradient** method that combines actor-critic architecture with asynchronous parallel training.
- Introduced by Mnih et al. (2016), it uses multiple parallel agents (workers) interacting with independent copies of the environment to stabilize and speed up training.
- Each worker maintains its own copy of the policy (actor) and value function (critic) networks and updates a shared global network asynchronously.

---

## 2. Key Components

- **Actor**: Learns the policy \(\pi_\theta(a|s)\), responsible for selecting actions.
- **Critic**: Learns the value function \(V_w(s)\), used as a baseline to reduce variance in policy gradient updates.
- **Advantage function**:  
  \[
  A(s_t, a_t) = R_t - V_w(s_t)
  \]
  where \(R_t\) is the n-step return, helps improve stability.

---

## 3. Algorithm Overview

- Multiple agents run in parallel, each interacting with its own environment instance.
- Each agent collects experience for a number of steps (or until terminal state).
- Computes gradients of policy and value networks using the collected experience.
- Asynchronously applies gradients to update the global shared parameters.
- Workers periodically sync their local parameters from the global network.

---

## 4. Pseudocode for A3C

```python
# Global shared parameters: theta (policy), w (value)
# Initialize global network parameters theta, w
# Initialize global counter T = 0
# Max global steps T_max

def worker():
    t = 1
    # Initialize thread-specific parameters theta', w' from global theta, w
    while T < T_max:
        t_start = t
        # Get initial state s_t
        states, actions, rewards = [], [], []
        done = False
        while not done and t - t_start < t_max:
            a_t = sample_action(pi_theta_prime(s_t))
            s_t1, r_t1, done = env.step(a_t)
            states.append(s_t)
            actions.append(a_t)
            rewards.append(r_t1)
            s_t = s_t1
            t += 1
            T += 1

        R = 0 if done else V_w_prime(s_t)
        # Compute n-step returns backward
        for i in reversed(range(len(states))):
            R = rewards[i] + gamma * R
            # Accumulate gradients wrt theta' and w' using advantage (R - V_w_prime(states[i]))
            # Policy gradient: grad_theta' += ∇_theta' log pi_theta'(actions[i]|states[i]) * (R - V_w_prime(states[i]))
            # Value function gradient: grad_w' += ∇_w' (R - V_w_prime(states[i]))^2

        # Update global parameters using accumulated gradients
        apply_gradients_to_global(grad_theta', grad_w')

        # Synchronize thread-specific parameters from global
        theta' = theta
        w' = w

# Launch multiple workers asynchronously

---

## 5. Strengths of A3C

| Strength                                    | Explanation                                            |
|---------------------------------------------|--------------------------------------------------------|
| **Asynchronous Parallelism**                 | Multiple workers stabilize and speed up training by decorrelating experiences. |
| **On-policy Learning with Low Variance**    | Uses advantage estimates to reduce variance of policy gradients. |
| **No Experience Replay Needed**               | Removes the need for replay buffers, reducing memory usage. |
| **Handles Continuous and Discrete Actions** | Flexible policy representation (stochastic policies). |
| **Faster Training**                           | Parallelism and asynchronous updates improve wall-clock efficiency. |

---

## 6. Weaknesses of A3C

| Weakness                                   | Explanation                                            |
|--------------------------------------------|--------------------------------------------------------|
| **Implementation Complexity**                | Requires multi-threading or multi-processing setup.     |
| **Non-Determinism**                          | Asynchronous updates can lead to non-reproducible results. |
| **Potential Instability**                     | Despite improvements, training can still be unstable without careful tuning. |
| **Resource Intensive**                        | Needs multiple environment instances and CPUs/cores.  |

---

## 7. Summary Table

| Aspect               | Description                                   |
|----------------------|-----------------------------------------------|
| Algorithm Type       | Asynchronous, on-policy actor-critic          |
| Learning Components  | Policy (actor), Value function (critic)       |
| Parallelism          | Multiple asynchronous workers                  |
| Advantage Estimation | n-step returns used to compute advantage      |
| Memory               | No replay buffer needed                         |
| Suitable for        | Complex, high-dimensional, continuous/discrete action spaces |

---

A3C is a powerful, scalable RL algorithm that leverages asynchronous parallelism and advantage actor-critic methods to achieve strong performance on a variety of challenging tasks.

---
```

# IMPALA (Importance Weighted Actor-Learner Architectures)

---

## 1. What is IMPALA?

- **IMPALA** is a scalable distributed reinforcement learning architecture introduced by DeepMind (Espeholt et al., 2018).
- It decouples acting and learning by separating **many actors** (which interact with environments) from a centralized **learner** (which updates the policy).
- Designed to efficiently scale RL training across many machines and cores.

---

## 2. Key Features

### a) Actor-Learner Architecture

- **Actors** run in parallel, each interacting with its own environment instance and generating experience.
- **Learner** receives experience trajectories from actors and updates the policy network.
- Actors periodically sync updated policy parameters from the learner.

### b) Off-Policy Correction via V-Trace

- Because actors act on slightly stale policies (due to asynchronous updates), IMPALA uses the **V-trace** algorithm to correct for off-policy data.
- V-trace applies importance sampling weights to adjust the learner’s value and policy gradient estimates, enabling stable learning.

---

## 3. How IMPALA Works

1. **Actors** generate trajectories using their local (possibly outdated) policy parameters.
2. Trajectories are sent asynchronously to the **learner**.
3. The learner uses V-trace to compute corrected targets and policy gradients.
4. Learner updates policy and value network parameters.
5. Updated parameters are sent back to actors.

---

## 4. Advantages of IMPALA

| Strength                                  | Explanation                                      |
|-------------------------------------------|-------------------------------------------------|
| **High scalability**                       | Can scale to thousands of actors and GPUs.      |
| **Efficient resource utilization**        | Decouples acting from learning to maximize throughput. |
| **Handles off-policy data**                 | V-trace corrects for policy lag between actors and learner. |
| **Supports complex environments**          | Suitable for large-scale, high-dimensional tasks. |

---

## 5. Summary Table

| Component          | Description                                   |
|--------------------|-----------------------------------------------|
| Architecture       | Distributed actor-learner framework             |
| Off-policy Correction | Uses V-trace importance weighting               |
| Actors             | Generate experience asynchronously               |
| Learner            | Centralized network updates                       |
| Scalability        | Designed for large-scale parallelism             |

---

## 6. References

- Espeholt, L., Soyer, H., Munos, R., et al. (2018). *IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures*.  
  [https://arxiv.org/abs/1802.01561](https://arxiv.org/abs/1802.01561)

---

IMPALA is a state-of-the-art distributed RL system enabling efficient large-scale training with stable off-policy corrections.

# Trust Region Policy Optimization (TRPO)

---

## 1. Overview

- **TRPO** is a policy gradient method designed to improve policy updates' stability and reliability.
- Introduced by Schulman et al. (2015), TRPO constrains policy updates to stay within a **trust region**, limiting the size of policy changes per iteration.
- This prevents destructive large updates that degrade performance.

---

## 2. Objective and Motivation

- Standard policy gradient updates can make large parameter changes, leading to performance collapse.
- TRPO formulates policy optimization as a constrained optimization problem:

\[
\max_{\theta} \quad \mathbb{E}_{s \sim \rho_{\theta_{\text{old}}}, a \sim \pi_{\theta_{\text{old}}}} \left[ \frac{\pi_\theta(a|s)}{\pi_{\theta_{\text{old}}}(a|s)} A_{\theta_{\text{old}}}(s,a) \right]
\]

subject to:

\[
\mathbb{E}_{s \sim \rho_{\theta_{\text{old}}}} \left[ D_{\mathrm{KL}}\left( \pi_{\theta_{\text{old}}}(\cdot|s) \| \pi_{\theta}(\cdot|s) \right) \right] \leq \delta
\]

where:

- \(\pi_\theta\) is the new policy,
- \(\pi_{\theta_{\text{old}}}\) is the old policy,
- \(A_{\theta_{\text{old}}}(s,a)\) is the advantage function,
- \(D_{\mathrm{KL}}\) is the KL-divergence,
- \(\delta\) is a small positive constant controlling the trust region size,
- \(\rho_{\theta_{\text{old}}}\) is the discounted state visitation distribution under the old policy.

---

## 3. Derivation Sketch

### Step 1: Surrogate Objective

Define the **surrogate loss** as:

\[
L_\theta(\theta) = \mathbb{E}_{s,a \sim \pi_{\theta_{\text{old}}}} \left[ \frac{\pi_\theta(a|s)}{\pi_{\theta_{\text{old}}}(a|s)} A_{\theta_{\text{old}}}(s,a) \right]
\]

This objective approximates the expected improvement from the old policy to the new policy.

---

### Step 2: Constrained Optimization Problem

We want to solve:

\[
\max_\theta L_\theta(\theta) \quad \text{s.t.} \quad \bar{D}_{\mathrm{KL}}(\theta_{\text{old}}, \theta) \leq \delta
\]

where \(\bar{D}_{\mathrm{KL}}\) is the average KL divergence over states:

\[
\bar{D}_{\mathrm{KL}}(\theta_{\text{old}}, \theta) = \mathbb{E}_{s \sim \rho_{\theta_{\text{old}}}} \left[ D_{\mathrm{KL}} \left( \pi_{\theta_{\text{old}}}(\cdot|s) \| \pi_\theta(\cdot|s) \right) \right]
\]

---

### Step 3: Linearize the Objective and Quadratic Approximate the Constraint

- Approximate the surrogate loss by first-order Taylor expansion around \(\theta_{\text{old}}\):

\[
L_\theta(\theta) \approx L_\theta(\theta_{\text{old}}) + g^T (\theta - \theta_{\text{old}})
\]

where \(g = \nabla_\theta L_\theta(\theta) |_{\theta_{\text{old}}}\) is the policy gradient.

- Approximate the KL divergence constraint via second-order Taylor expansion:

\[
\bar{D}_{\mathrm{KL}}(\theta_{\text{old}}, \theta) \approx \frac{1}{2} (\theta - \theta_{\text{old}})^T H (\theta - \theta_{\text{old}})
\]

where \(H\) is the Fisher Information Matrix of the policy.

---

### Step 4: Solve the Constrained Quadratic Problem

\[
\max_{\delta \theta} \quad g^T \delta \theta \quad \text{s.t.} \quad \frac{1}{2} \delta \theta^T H \delta \theta \leq \delta
\]

- Solution is given by:

\[
\delta \theta = \sqrt{\frac{2 \delta}{g^T H^{-1} g}} H^{-1} g
\]

- This is a **natural gradient step** scaled to satisfy the KL constraint.

---

### Step 5: Practical Implementation

- Use **conjugate gradient** method to compute \(H^{-1} g\) efficiently.
- Use **line search** to ensure the KL constraint is satisfied after the update.

---

## 4. Pseudocode for TRPO

```python
Initialize policy parameters θ

for iteration = 1, 2, ... do
    Collect trajectories by running policy π_θ
    Estimate advantages Â(s, a)
    Compute policy gradient g = ∇_θ L_θ(θ) at current θ
    Compute Fisher Information Matrix H (or its approximation)
    Solve H δθ = g using conjugate gradient to get step direction
    Compute step size scaling to satisfy KL constraint δ
    Perform line search to find acceptable θ_new:
        θ_new = θ + step_size * δθ
    Update policy parameters θ ← θ_new
end for

---

## 5. Strengths of TRPO

| Strength                                      | Explanation                                        |
|-----------------------------------------------|--------------------------------------------------|
| **Monotonic improvement guarantees**          | Constrains updates to avoid large destructive policy changes. |
| **Stable and reliable training**                | Reduces policy collapse common in naive policy gradients. |
| **Sample efficiency**                          | More efficient than vanilla policy gradients in many tasks. |
| **Theoretically grounded**                      | Derived with strong theoretical motivation and guarantees. |

---

## 6. Weaknesses of TRPO

| Weakness                                    | Explanation                                        |
|---------------------------------------------|--------------------------------------------------|
| **Complex implementation**                    | Requires computing Fisher Information Matrix and conjugate gradient. |
| **Computationally expensive**                 | More costly per update compared to simpler methods like vanilla policy gradients or PPO. |
| **Difficult hyperparameter tuning**          | Trust region size \(\delta\) and line search parameters require careful tuning. |
| **Less scalable to very large networks**     | Computing and storing approximations for large neural networks can be challenging. |

---

## 7. Summary

| Aspect                    | Description                                   |
|---------------------------|-----------------------------------------------|
| Algorithm Type           | Trust-region constrained policy gradient    |
| Key Idea                 | Constrain KL divergence between old and new policies to ensure stable updates |
| Optimization Technique   | Natural gradient with conjugate gradient and line search |
| Strengths                | Stability, monotonic improvement, theoretical guarantees |
| Weaknesses               | Complexity, computational cost, tuning difficulty |

---

## 8. References

- Schulman, J., Levine, S., Moritz, P., Jordan, M., & Abbeel, P. (2015). *Trust Region Policy Optimization*.  
  [https://arxiv.org/abs/1502.05477](https://arxiv.org/abs/1502.05477)

---
```

# Proximal Policy Optimization (PPO) Algorithm

---

## 1. Overview

- **PPO** is a policy gradient method designed to achieve reliable and stable policy updates with simpler implementation and better sample efficiency than TRPO.
- Introduced by Schulman et al. (2017), PPO uses a **surrogate objective** with a clipped probability ratio to prevent large destructive policy updates.
- It balances between **exploration and exploitation** by restricting how much the policy can change during each update.

---

## 2. Motivation

- TRPO enforces a hard constraint on KL divergence between old and new policies but requires complex second-order optimization.
- PPO simplifies this by using a **surrogate clipped objective** to approximate trust regions with first-order optimization methods.

---

## 3. Derivation of PPO Objective

### Step 1: Define the Probability Ratio

\[
r_t(\theta) = \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_{\text{old}}}(a_t | s_t)}
\]

This ratio measures how much the new policy differs from the old policy for the action taken.

---

### Step 2: Surrogate Objective (Unclipped)

\[
L^{\text{CPI}}(\theta) = \mathbb{E}_t \left[ r_t(\theta) \hat{A}_t \right]
\]

where \(\hat{A}_t\) is an estimator of the advantage function at time \(t\).

---

### Step 3: Clipped Surrogate Objective

To prevent large updates, PPO clips the ratio to stay within \([1-\epsilon, 1+\epsilon]\):

\[
L^{\text{CLIP}}(\theta) = \mathbb{E}_t \left[ \min \left( r_t(\theta) \hat{A}_t, \ \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right) \right]
\]

- The \(\min\) operator ensures the objective never improves if the change in policy is too large.
- \(\epsilon\) is a hyperparameter (e.g., 0.1 or 0.2) controlling the clipping range.

---

### Step 4: Final Objective with Value Function and Entropy Bonus (Optional)

The full PPO objective often includes:

- **Value function loss** to fit \(V(s)\).
- **Entropy bonus** to encourage exploration.

\[
L(\theta) = \mathbb{E}_t \left[ L^{\text{CLIP}}(\theta) - c_1 L^{\text{VF}}(\theta) + c_2 S[\pi_\theta](s_t) \right]
\]

where:

- \(L^{\text{VF}}(\theta) = (V_\theta(s_t) - V^{\text{target}}_t)^2\) is value loss,
- \(S[\pi_\theta](s_t)\) is the entropy of the policy,
- \(c_1, c_2\) are coefficients balancing the terms.

---

## 4. PPO Algorithm Pseudocode

```python
initialize policy parameters θ
initialize value function parameters φ

for iteration in range(1, N):
    # Collect trajectories using current policy π_θ
    trajectories = collect_trajectories(π_θ)
    
    # Compute advantage estimates Â_t using value function V_φ
    advantages = compute_advantages(trajectories, V_φ)
    
    for epoch in range(K):  # multiple epochs of minibatch updates
        for minibatch in sample_minibatches(trajectories):
            # Compute ratio
            r_t = π_θ(a_t|s_t) / π_{θ_old}(a_t|s_t)
            
            # Compute clipped surrogate objective
            L_clip = mean( min(r_t * Â_t, clip(r_t, 1-ε, 1+ε) * Â_t) )
            
            # Compute value loss
            L_vf = mean( (V_φ(s_t) - V_target_t)^2 )
            
            # Compute entropy bonus
            S = mean( entropy(π_θ(s_t)) )
            
            # Total loss (to maximize)
            loss = -L_clip + c1 * L_vf - c2 * S
            
            # Perform gradient descent step on loss
            optimizer.step(loss)
    
    # Update old policy parameters θ_old ← θ

---

## 5. Strengths of PPO

| Strength                                         | Explanation                                    |
|-------------------------------------------------|------------------------------------------------|
| **Simplicity and Ease of Implementation**        | Uses first-order optimization and simple clipping instead of complex second-order methods. |
| **Stable and Reliable Updates**                   | Clipped objective prevents large destructive policy changes. |
| **Good Sample Efficiency**                        | Efficient use of collected trajectories via multiple epochs of minibatch updates. |
| **Supports Large-Scale and Complex Tasks**       | Works well with deep neural networks and high-dimensional action spaces. |
| **Widely Adopted**                                | Serves as a strong baseline in modern RL research and applications. |

---

## 6. Weaknesses of PPO

| Weakness                                        | Explanation                                    |
|------------------------------------------------|------------------------------------------------|
| **Hyperparameter Sensitivity**                   | Performance depends on clipping parameter \(\epsilon\), learning rates, and other coefficients. |
| **No Theoretical Guarantees for Monotonic Improvement** | Unlike TRPO, PPO lacks strict theoretical guarantees. |
| **Possible Overfitting to Trajectories**         | Multiple epochs on same data may lead to overfitting if not regularized. |
| **Still Requires Careful Tuning**                 | Requires tuning of batch sizes, number of epochs, and advantage estimation. |

---

## 7. Summary Table

| Aspect                 | Description                           |
|------------------------|-------------------------------------|
| Algorithm Type         | First-order policy gradient with clipped surrogate objective |
| Key Idea               | Clip probability ratio to limit policy update size |
| Optimization           | Stochastic gradient descent with minibatches and multiple epochs |
| Strengths              | Simplicity, stability, sample efficiency |
| Weaknesses             | Hyperparameter tuning, lacks strict monotonic improvement guarantees |

---

## 8. References

- Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). *Proximal Policy Optimization Algorithms*.  
  [https://arxiv.org/abs/1707.06347](https://arxiv.org/abs/1707.06347)

---

PPO strikes a practical balance between ease of implementation, performance, and stability, making it one of the most popular policy gradient methods in modern reinforcement learning.
```

# Deep Deterministic Policy Gradient (DDPG) and Twin Delayed DDPG (TD3) Algorithms

---

## 1. Overview

- **DDPG** and **TD3** are off-policy, actor-critic algorithms designed for **continuous action spaces**.
- They combine ideas from DQN and policy gradients to learn deterministic policies.
- TD3 is an improved version of DDPG that addresses some of its key limitations.

---

## 2. DDPG Algorithm Derivation

### a) Problem Setup

- Policy is deterministic: \( \mu_\theta(s) \), parameterized by \(\theta\).
- Critic \(Q_w(s,a)\) estimates action-value function, parameterized by \(w\).

### b) Critic Update (Bellman Equation)

Critic is trained to minimize the Bellman error:

\[
L(w) = \mathbb{E}_{(s,a,r,s')} \left[ \left( Q_w(s,a) - y \right)^2 \right]
\]

where the target \(y\) is:

\[
y = r + \gamma Q_{w'}(s', \mu_{\theta'}(s'))
\]

- \(w', \theta'\) are parameters of **target networks** (delayed copies of \(w, \theta\)) used for stability.

### c) Actor Update

Update actor policy by maximizing expected Q-values:

\[
\nabla_\theta J \approx \mathbb{E}_s \left[ \nabla_a Q_w(s,a) |_{a=\mu_\theta(s)} \nabla_\theta \mu_\theta(s) \right]
\]

This is the deterministic policy gradient.

### d) Algorithm Highlights

- Uses replay buffer for off-policy learning.
- Employs target networks for stability.
- Adds noise to actions during training for exploration.

---

## 3. TD3 Algorithm Improvements Over DDPG

TD3 addresses overestimation bias and instability in DDPG by introducing:

| Improvement              | Description                                      |
|--------------------------|-------------------------------------------------|
| **Clipped Double Q-Learning** | Uses two critic networks \(Q_{w_1}, Q_{w_2}\), and takes the minimum of their estimates to form target \(y\), reducing overestimation bias. |
| **Delayed Policy Updates**       | Updates the actor and target networks less frequently than critics to stabilize learning. |
| **Target Policy Smoothing**      | Adds clipped noise to target action \( \mu_{\theta'}(s') \) during critic target computation to smooth Q-values and reduce variance. |

### TD3 Target Computation

\[
\tilde{a} = \text{clip}\left( \mu_{\theta'}(s') + \epsilon, -c, c \right), \quad \epsilon \sim \text{clip}(\mathcal{N}(0, \sigma), -c, c)
\]

\[
y = r + \gamma \min_{i=1,2} Q_{w_i'}(s', \tilde{a})
\]

---

## 4. Pseudocode for TD3

```python
Initialize actor μ_θ and critics Q_{w1}, Q_{w2} with weights θ, w1, w2
Initialize target networks θ', w1', w2' ← θ, w1, w2
Initialize replay buffer

for episode = 1, M:
    Initialize state s
    for t = 1, T:
        # Select action with exploration noise
        a = μ_θ(s) + noise
        Execute action a, observe r, s'
        Store (s, a, r, s') in replay buffer
        s = s'
        
        # Sample minibatch from replay buffer
        (s_i, a_i, r_i, s_i') ~ replay buffer
        
        # Compute target action with smoothing noise
        a_i' = clip(μ_{θ'}(s_i') + clip(N(0, σ), -c, c), action_low, action_high)
        
        # Compute target Q-value
        y_i = r_i + γ * min(Q_{w1'}(s_i', a_i'), Q_{w2'}(s_i', a_i'))
        
        # Update critics by minimizing MSE loss
        L(w_j) = (Q_{w_j}(s_i, a_i) - y_i)^2,  j=1,2
        
        # Update critics w1, w2 by gradient descent
        
        # Delayed policy update
        if t % policy_delay == 0:
            # Update actor using deterministic policy gradient
            ∇_θ J ≈ ∇_a Q_{w1}(s, a)|_{a=μ_θ(s)} ∇_θ μ_θ(s)
            Update actor θ by gradient ascent
            
            # Update target networks
            θ' ← τ θ + (1 - τ) θ'
            w_j' ← τ w_j + (1 - τ) w_j',  j=1,2

---

## 5. Strengths of DDPG/TD3

| Strength                                   | Explanation                                      |
|--------------------------------------------|-------------------------------------------------|
| **Handles continuous action spaces**        | Works well where value-based methods struggle.  |
| **Off-policy learning**                      | Efficient use of replay buffer improves sample efficiency. |
| **TD3 reduces overestimation bias**          | Clipped double Q-learning improves stability and performance over DDPG. |
| **Policy smoothing and delayed updates**     | Enhance robustness and prevent divergence.      |
| **Scalable to high-dimensional action spaces** | Suitable for complex control tasks (e.g., robotics). |

---

## 6. Weaknesses of DDPG/TD3

| Weakness                                    | Explanation                                      |
|---------------------------------------------|-------------------------------------------------|
| **Exploration challenges**                    | Deterministic policies rely on added noise for exploration, which can be inefficient. |
| **Sensitive to hyperparameters**              | Performance depends heavily on noise scale, learning rates, etc. |
| **Function approximation errors**             | Still susceptible to instability with complex function approximators. |
| **Sample efficiency**                         | Off-policy, but requires many environment interactions. |

---

## 7. Summary Table

| Aspect                 | DDPG                                     | TD3                                      |
|------------------------|------------------------------------------|------------------------------------------|
| Policy Type            | Deterministic policy                      | Deterministic policy                      |
| Critic Networks        | Single critic                             | Two critics (clipped double Q-learning)  |
| Policy Update Frequency| Every step                               | Delayed updates (less frequent)          |
| Exploration Noise      | Added to actions                         | Added to target action (policy smoothing)|
| Stability             | Prone to overestimation and instability | More stable and robust                    |
| Sample Efficiency      | Moderate                                | Improved over DDPG                        |

---

## 8. References

- Lillicrap, T. P., et al. (2015). *Continuous control with deep reinforcement learning*.  
- Fujimoto, S., Hoof, H., & Meger, D. (2018). *Addressing Function Approximation Error in Actor-Critic Methods*. (TD3)  
  [https://arxiv.org/abs/1802.09477](https://arxiv.org/abs/1802.09477)

---
```

# Polyak Averaging

---

## 1. What is Polyak Averaging?

- **Polyak averaging** is a technique used to improve the stability and convergence of iterative optimization algorithms.
- It computes a moving average of the parameter vectors during training rather than using the latest parameters alone.
- Given parameter vectors \(\{\theta_k\}\) at iterations \(k=1,2,\dots\), the Polyak averaged parameters \(\bar{\theta}_k\) are computed as:

\[
\bar{\theta}_k = \frac{1}{k} \sum_{i=1}^k \theta_i
\]

- Alternatively, it can be implemented as an **exponentially weighted moving average**:

\[
\bar{\theta}_k = \tau \bar{\theta}_{k-1} + (1 - \tau) \theta_k
\]

where \(\tau \in [0,1]\) is a smoothing factor.

---

## 2. Where is Polyak Averaging Used?

- **Reinforcement Learning:**

  - Used in **target networks** for algorithms like DDPG, TD3, and DQN to stabilize learning by slowly updating target network parameters:

    \[
    \theta_{\text{target}} \leftarrow \tau \theta_{\text{target}} + (1-\tau) \theta_{\text{online}}
    \]
  
  - Helps reduce oscillations and divergence by smoothing updates.

- **Stochastic Optimization:**

  - Polyak averaging is used in stochastic gradient descent (SGD) to improve convergence rates and reduce variance in parameter estimates.

- **Deep Learning:**

  - Averaging weights over training iterations can improve generalization and robustness.

---

## 3. Advantages of Polyak Averaging

- **Stabilizes training** by smoothing parameter updates.
- **Improves convergence** and can reduce variance/noise in parameters.
- **Simple to implement** and computationally cheap.

---

## 4. Alternatives to Polyak Averaging

| Alternative                     | Description                                    |
|--------------------------------|------------------------------------------------|
| **Hard Target Network Updates** | Replace target network parameters with online network parameters periodically (e.g., every fixed number of steps) instead of gradual updates. |
| **Exponential Moving Average (EMA)** | Similar to Polyak averaging but uses a fixed smoothing coefficient \(\tau\) for continuous updates. |
| **No Target Networks**          | Some algorithms avoid target networks but may suffer from instability. |
| **Weight Averaging Techniques** | Such as Stochastic Weight Averaging (SWA) used in supervised learning to improve generalization. |

---

## 5. Summary

| Aspect                 | Polyak Averaging                         |
|------------------------|-----------------------------------------|
| Purpose                | Smooth and stabilize parameter updates  |
| Common Usage           | Target network updates in RL algorithms |
| Formula                | \(\bar{\theta} \leftarrow \tau \bar{\theta} + (1-\tau) \theta\) |
| Benefits               | Improves stability, reduces variance     |
| Alternatives           | Hard updates, EMA, SWA                    |

---

Polyak averaging is a key technique in modern RL to ensure stable and reliable training of deep neural networks.

# Replay Buffer Technique in Reinforcement Learning

---

## 1. What is a Replay Buffer?

- A **replay buffer** (or experience replay) is a memory data structure that stores past experiences (transitions) collected by the agent during interaction with the environment.
- Each experience typically consists of a tuple:
  
  \[
  (s_t, a_t, r_{t+1}, s_{t+1}, \text{done})
  \]

  where:
  - \(s_t\): current state,
  - \(a_t\): action taken,
  - \(r_{t+1}\): reward received,
  - \(s_{t+1}\): next state,
  - \(\text{done}\): episode termination flag.

- The stored experiences are **sampled randomly** to train the agent.

---

## 2. Purpose of Replay Buffer

- **Breaks correlations** between consecutive samples by randomizing experience replay.
- **Improves sample efficiency** by reusing past experiences multiple times.
- **Stabilizes training** by smoothing the data distribution.
- Allows off-policy learning algorithms to update from past experiences.

---

## 3. How Replay Buffer Works

1. **Storage:** Continuously store experiences as the agent interacts with the environment.
2. **Sampling:** Randomly sample mini-batches of experiences uniformly (or prioritized) from the buffer.
3. **Learning:** Use sampled batches to perform gradient updates on neural networks (e.g., Q-networks, policy networks).
4. **Capacity:** Typically has a fixed maximum size; old experiences are discarded when full (FIFO).

---

## 4. Where is Replay Buffer Used?

- **Value-based Methods:**
  - Deep Q-Networks (DQN)
  - Double DQN
  - Dueling DQN

- **Actor-Critic Methods:**
  - Deep Deterministic Policy Gradient (DDPG)
  - Twin Delayed DDPG (TD3)
  - Soft Actor-Critic (SAC)

- **Off-policy Algorithms:**
  - Any off-policy method that learns from past data rather than current policy rollout.

---

## 5. Variants of Replay Buffer

| Variant                   | Description                                      |
|---------------------------|-------------------------------------------------|
| **Uniform Replay Buffer** | Samples experiences uniformly at random.        |
| **Prioritized Experience Replay (PER)** | Samples experiences based on importance (e.g., TD error), improving learning efficiency. |

---

## 6. Benefits of Replay Buffer

- Breaks temporal correlations in training data.
- Enables efficient reuse of experiences.
- Improves convergence stability and speed.
- Makes off-policy learning possible.

---

## 7. Summary Table

| Aspect                | Description                             |
|-----------------------|-----------------------------------------|
| Purpose              | Store and reuse past experiences          |
| Functionality        | Random sampling to reduce correlation    |
| Used In             | Off-policy RL algorithms (DQN, DDPG, TD3) |
| Variants            | Uniform sampling, prioritized replay     |

---

Replay buffers are a fundamental component in modern deep RL, crucial for stabilizing and improving learning performance.

# Double Q-Learning

---

## 1. What is Double Q-Learning?

- **Double Q-Learning** is an extension of the standard Q-Learning algorithm designed to **reduce overestimation bias** in action-value estimates.
- It maintains **two separate Q-value estimates**, \(Q_1\) and \(Q_2\), which are updated independently.
- During learning, one Q-function is used to select the best action, while the other is used to evaluate that action, mitigating the maximization bias.

---

## 2. Why is Double Q-Learning Needed?

- **Overestimation Bias in Q-Learning:**

  - Standard Q-Learning uses the **max operator** over estimated Q-values to select the best next action:

    \[
    \max_a Q(s', a)
    \]

  - If the Q-values have noise or estimation errors, the max operator tends to select overestimated values, leading to systematic positive bias.

- This bias can cause suboptimal policies, slower learning, or divergence.

---

## 3. How Double Q-Learning Works

- Maintain two Q-functions \(Q_1\) and \(Q_2\) with parameters \(\theta_1\) and \(\theta_2\).
- At each update step, randomly choose which Q-function to update.
- For updating \(Q_1\), use \(Q_2\) to evaluate the next action selected by \(Q_1\):

\[
y = r + \gamma Q_2 \left( s', \arg\max_a Q_1(s', a) \right)
\]

- Similarly for updating \(Q_2\):

\[
y = r + \gamma Q_1 \left( s', \arg\max_a Q_2(s', a) \right)
\]

- This decouples action selection and evaluation, reducing overestimation.

---

## 4. When is Double Q-Learning Used?

- When **overestimation bias** negatively impacts learning performance.
- In environments where Q-value estimates are noisy or function approximation errors are significant.
- Widely used in **Deep RL**, e.g., **Double DQN**, where two neural networks approximate \(Q_1\) and \(Q_2\).

---

## 5. Benefits of Double Q-Learning

| Benefit                           | Explanation                                      |
|----------------------------------|-------------------------------------------------|
| Reduces overestimation bias       | Leads to more accurate Q-value estimates        |
| Improves learning stability       | Avoids overly optimistic value estimates        |
| Often leads to better policies    | More reliable policy improvement                 |
| Simple to implement               | Minimal overhead compared to standard Q-learning|

---

## 6. Summary Table

| Aspect                 | Standard Q-Learning          | Double Q-Learning                         |
|------------------------|-----------------------------|------------------------------------------|
| Number of Q-functions   | 1                           | 2                                        |
| Update Target          | \(r + \gamma \max_a Q(s',a)\) | \(r + \gamma Q_{\text{other}}(s', \arg\max_a Q_{\text{current}}(s', a))\) |
| Bias                   | Positive (overestimation)    | Reduced bias                             |
| Stability              | Potentially unstable         | More stable                             |
| Usage                  | Basic Q-learning             | Improved Q-learning, Deep RL algorithms |

---

## 7. References

- Hasselt, H. V. (2010). *Double Q-learning*. Advances in Neural Information Processing Systems (NIPS).  
- Van Hasselt, H., Guez, A., & Silver, D. (2016). *Deep Reinforcement Learning with Double Q-learning*.  
  [https://arxiv.org/abs/1509.06461](https://arxiv.org/abs/1509.06461)

---

Double Q-Learning is a simple yet powerful modification to standard Q-Learning that significantly improves policy learning by mitigating overestimation bias.

# Methods of Ensuring Exploration in Policy Algorithms

---

Exploration is crucial in reinforcement learning (RL) to discover rewarding actions and avoid premature convergence to suboptimal policies. Policy algorithms employ various methods to encourage exploration during training.

---

## 1. Stochastic Policies

- **Using stochastic (probabilistic) policies** inherently encourages exploration by sampling different actions according to a probability distribution.

- Examples:
  - Parameterize policies as probability distributions (e.g., Gaussian policy in continuous action spaces).
  - Softmax policies in discrete action spaces.

---

## 2. Entropy Regularization

- Add an **entropy bonus** term to the policy objective to encourage **higher entropy** (more randomness) in the action distribution.

- Objective modification:

  \[
  J(\theta) = \mathbb{E}[\text{Return}] + \beta \mathbb{E}_{s} [ \mathcal{H}(\pi_\theta(\cdot|s)) ]
  \]

  where \(\mathcal{H}\) is the entropy and \(\beta\) controls exploration strength.

- Higher entropy prevents the policy from collapsing too quickly to deterministic behavior.

---

## 3. Parameter Noise

- Add noise directly to the **policy parameters** rather than action outputs.

- This leads to more consistent exploration patterns across time steps, as the entire policy is perturbed.

- Used in methods like **NoisyNet** and some actor-critic algorithms.

---

## 4. Action Noise

- Add noise to the **actions** selected by the policy (especially in deterministic policy algorithms).

- Examples:

  - **Gaussian noise** added to continuous actions (e.g., DDPG).
  - **Ornstein-Uhlenbeck process** for temporally correlated noise.

---

## 5. Exploration Schedules

- **Decaying exploration parameters** (e.g., \(\epsilon\)-greedy schedule):

  - Start with high exploration (large \(\epsilon\)) and gradually reduce it over time.

- Balances exploration and exploitation during training.

---

## 6. Intrinsic Motivation / Curiosity

- Add an **intrinsic reward** based on novelty or prediction error to encourage exploration of unfamiliar states.

- Examples include:

  - Prediction error of learned models.
  - State visitation counts or pseudo-counts.

---

## 7. Bootstrapped Policies

- Maintain multiple policy “heads” or ensembles, each trained on different data subsets.

- Randomly select one policy at the start of each episode to encourage diverse exploration.

---

## 8. Summary Table

| Method                  | Description                                 | Typical Use Cases                  |
|-------------------------|---------------------------------------------|----------------------------------|
| Stochastic Policies     | Sample actions probabilistically             | Policy gradient methods           |
| Entropy Regularization  | Add entropy bonus to objective                | PPO, A3C, SAC                    |
| Parameter Noise         | Add noise to policy parameters                | NoisyNet, parameter perturbations |
| Action Noise            | Add noise to actions                           | DDPG, TD3                        |
| Exploration Schedules   | Decaying \(\epsilon\)-greedy or noise scale  | Discrete and continuous actions  |
| Intrinsic Motivation    | Reward novelty or surprise                     | Curiosity-driven RL              |
| Bootstrapped Policies   | Multiple policy heads for diverse exploration| Ensemble or Bayesian RL          |

---

Effective exploration methods depend on the problem, policy type, and action space. Combining these techniques often yields better performance in complex environments.


# Soft Actor-Critic (SAC) Algorithm

---

## 1. Overview

- **Soft Actor-Critic (SAC)** is an off-policy actor-critic algorithm designed for continuous action spaces.
- It optimizes a **maximum entropy objective**, encouraging policies that maximize expected reward while also maximizing entropy (randomness) for better exploration.
- Developed by Haarnoja et al. (2018), SAC achieves state-of-the-art performance with stable and sample-efficient learning.

---

## 2. Maximum Entropy RL Objective

SAC maximizes the expected return **and** the expected entropy of the policy:

\[
J(\pi) = \sum_{t=0}^\infty \mathbb{E}_{(s_t,a_t) \sim \rho_\pi} \left[ r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot|s_t)) \right]
\]

where:

- \(\mathcal{H}(\pi(\cdot|s_t)) = -\mathbb{E}_{a_t \sim \pi} [\log \pi(a_t|s_t)]\) is the entropy,
- \(\alpha > 0\) is the temperature parameter balancing reward and entropy.

---

## 3. Key Components and Derivation

### a) Soft Q-Function

The soft Q-function satisfies the **soft Bellman equation**:

\[
Q^\pi(s,a) = r(s,a) + \gamma \mathbb{E}_{s' \sim p} \left[ V^\pi(s') \right]
\]

where the value function is:

\[
V^\pi(s) = \mathbb{E}_{a \sim \pi} \left[ Q^\pi(s,a) - \alpha \log \pi(a|s) \right]
\]

---

### b) Soft Policy Improvement

The policy aims to minimize the KL divergence between itself and the Boltzmann distribution induced by \(Q\):

\[
\pi^* = \arg\min_\pi D_{KL} \left( \pi(\cdot|s) \bigg\| \frac{\exp\left(\frac{1}{\alpha} Q^\pi(s, \cdot)\right)}{Z^\pi(s)} \right)
\]

which leads to the policy update:

\[
\pi(a|s) \propto \exp\left(\frac{1}{\alpha} Q^\pi(s,a)\right)
\]

---

### c) Parameterized Components

- **Q-functions:** Two soft Q-functions \(Q_{\theta_1}, Q_{\theta_2}\) to mitigate positive bias (similar to TD3).
- **Policy:** Parameterized stochastic policy \(\pi_\phi(a|s)\).
- **Value function:** Often implicit through Q-functions and policy.

---

### d) Loss Functions

- **Q-function Loss:**

\[
J_Q(\theta_i) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}} \left[ \frac{1}{2} \left( Q_{\theta_i}(s,a) - y \right)^2 \right]
\]

where the target is:

\[
y = r + \gamma \mathbb{E}_{a' \sim \pi_\phi} \left[ \min_{j=1,2} Q_{\bar{\theta}_j}(s', a') - \alpha \log \pi_\phi(a'|s') \right]
\]

- **Policy Loss:**

\[
J_\pi(\phi) = \mathbb{E}_{s \sim \mathcal{D}, a \sim \pi_\phi} \left[ \alpha \log \pi_\phi(a|s) - \min_{j=1,2} Q_{\theta_j}(s,a) \right]
\]

- **Temperature \(\alpha\) Loss (optional):** Automatically tune \(\alpha\) by minimizing:

\[
J(\alpha) = \mathbb{E}_{a \sim \pi_\phi} \left[ -\alpha \log \pi_\phi(a|s) - \alpha \bar{\mathcal{H}} \right]
\]

where \(\bar{\mathcal{H}}\) is a target entropy.

---

## 4. SAC Algorithm Pseudocode

```python
Initialize Q-functions Q_{θ1}, Q_{θ2} and policy π_φ with parameters θ1, θ2, φ
Initialize target Q-networks Q_{θ1'}, Q_{θ2'} with parameters θ1' ← θ1, θ2' ← θ2
Initialize temperature parameter α (optional)

for each iteration:
    for each environment step:
        Select action a_t ~ π_φ(·|s_t) with added exploration noise
        Execute a_t, observe reward r_t and next state s_{t+1}
        Store (s_t, a_t, r_t, s_{t+1}) in replay buffer

    for each gradient step:
        Sample minibatch (s_i, a_i, r_i, s_i') from replay buffer

        # Compute target Q-value
        a_i' ~ π_φ(·|s_i')
        target_Q = r_i + γ * (min(Q_{θ1'}(s_i', a_i'), Q_{θ2'}(s_i', a_i')) - α * log π_φ(a_i'|s_i'))

        # Update Q-functions by minimizing loss
        Update θ1, θ2 to minimize:
          J_Q(θ_i) = (Q_{θ_i}(s_i, a_i) - target_Q)^2

        # Update policy by minimizing:
        J_π(φ) = E_{s_i} [ α log π_φ(a_i|s_i) - min(Q_{θ1}(s_i, a_i), Q_{θ2}(s_i, a_i)) ]

        # (Optional) Update temperature α by minimizing:
        J(α) = E_{a_i} [ -α log π_φ(a_i|s_i) - α * target_entropy ]

        # Soft update target networks
        θ_i' ← τ θ_i + (1 - τ) θ_i',  for i=1,2

---

## 5. Strengths of SAC

| Strength                                   | Explanation                                      |
|--------------------------------------------|-------------------------------------------------|
| **Stable and sample-efficient**             | Off-policy learning and entropy regularization improve stability and exploration. |
| **Automatic exploration-exploitation tradeoff** | Entropy maximization encourages diverse behaviors. |
| **Robust to hyperparameters**                | Temperature \(\alpha\) can be automatically tuned. |
| **Reduced overestimation bias**              | Uses clipped double Q-learning with two critics. |
| **Effective in continuous action spaces**   | Handles high-dimensional, continuous control tasks well. |

---

## 6. Weaknesses of SAC

| Weakness                                    | Explanation                                      |
|---------------------------------------------|-------------------------------------------------|
| **Computationally expensive**                 | Maintains multiple networks and requires multiple gradient steps per environment step. |
| **Complex implementation**                     | More components and hyperparameters than simpler algorithms. |
| **Sample complexity**                          | Although improved, still requires significant samples for complex tasks. |

---

## 7. Summary Table

| Aspect                 | Description                                |
|------------------------|--------------------------------------------|
| Algorithm Type         | Off-policy maximum entropy actor-critic   |
| Policy                 | Stochastic, entropy-regularized            |
| Value Functions        | Two Q-functions with target networks       |
| Exploration            | Encouraged via entropy maximization        |
| Strengths              | Stability, robustness, exploration         |
| Weaknesses             | Computational cost, complexity              |

---

## 8. References

- Haarnoja, T., Zhou, A., Abbeel, P., & Levine, S. (2018). *Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor*.  
  [https://arxiv.org/abs/1801.01290](https://arxiv.org/abs/1801.01290)

---
```

# Maximum Entropy Reinforcement Learning (MaxEnt RL) Formalism

---

## 1. Standard RL Objective

- The goal in **standard reinforcement learning** is to find a policy \(\pi\) that **maximizes the expected cumulative discounted reward**:

\[
J(\pi) = \mathbb{E}_{\pi} \left[ \sum_{t=0}^\infty \gamma^t r(s_t, a_t) \right]
\]

- Here, \(\gamma \in [0,1)\) is the discount factor.

- The policy typically converges to a **deterministic** or **greedy** policy maximizing expected returns.

---

## 2. Maximum Entropy RL Objective

- **Maximum entropy RL** augments the standard objective by adding an **entropy term** to encourage stochasticity (exploration):

\[
J(\pi) = \mathbb{E}_{\pi} \left[ \sum_{t=0}^\infty \gamma^t \left( r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot|s_t)) \right) \right]
\]

where:

- \(\mathcal{H}(\pi(\cdot|s_t)) = - \mathbb{E}_{a_t \sim \pi} [\log \pi(a_t|s_t)]\) is the entropy of the policy at state \(s_t\).
- \(\alpha > 0\) is the **temperature parameter** balancing reward and entropy.

---

## 3. Key Differences

| Aspect                   | Standard RL                            | Maximum Entropy RL                        |
|--------------------------|-------------------------------------|------------------------------------------|
| Objective                | Maximize expected cumulative reward | Maximize reward + expected policy entropy |
| Policy Behavior          | Often deterministic (greedy)          | Stochastic with higher entropy (more exploration) |
| Exploration              | Implicit (via stochasticity or added noise) | Explicitly encouraged via entropy term   |
| Solution Characteristics| Single optimal policy maximizing reward | Set of near-optimal stochastic policies  |
| Robustness               | May overfit to deterministic solutions | More robust and resilient to uncertainty |

---

## 4. Advantages of Maximum Entropy RL

- **Improved exploration** by encouraging diverse behaviors.
- **Robustness to model inaccuracies and noise** due to stochastic policies.
- Can represent **multi-modal policies**, capturing multiple good strategies.
- Leads to **smoother optimization landscapes**.

---

## 5. Summary

| Feature                | Standard RL                      | Maximum Entropy RL                 |
|------------------------|---------------------------------|----------------------------------|
| Objective              | \(\max_\pi \mathbb{E}[\sum \gamma^t r_t]\) | \(\max_\pi \mathbb{E}[\sum \gamma^t (r_t + \alpha \mathcal{H}(\pi))]\) |
| Policy                 | Often deterministic             | Stochastic and entropy-regularized |
| Exploration Mechanism  | External or implicit            | Built-in via entropy maximization |
| Typical Algorithms     | Q-Learning, SARSA, DQN          | Soft Actor-Critic (SAC), Maximum Entropy RL |

---

Maximum entropy reinforcement learning extends the standard RL framework by explicitly encouraging stochastic policies, resulting in better exploration and robustness, which is especially valuable in complex or uncertain environments.