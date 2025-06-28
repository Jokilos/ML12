# Advanced topics in RL


# Reinforcement Learning for Improving Agent Design

---

## 1. Overview

- **Reinforcement Learning (RL) for Improving Agent Design** refers to the use of RL techniques to **automate and optimize the design process** of agents, which could be robots, software agents, or other autonomous systems.
- Instead of manually engineering agent components (e.g., morphology, controllers, sensor placement), RL is used to **learn or evolve designs** that maximize performance on given tasks.

---

## 2. Key Concepts

| Concept               | Description                                                      |
|-----------------------|------------------------------------------------------------------|
| **Agent Design**      | Physical or virtual attributes of the agent (e.g., robot shape, joints, sensors). |
| **Design Optimization** | Process of finding the best agent design to improve task performance. |
| **RL Role**            | Use RL to search over design and control policies jointly or sequentially. |

---

## 3. Approaches

### a) **Joint Design and Control Learning**

- RL simultaneously learns:
  - The **agent’s control policy** (how to act).
  - The **agent’s design parameters** (e.g., limb lengths, actuator strengths).
- Objective: Maximize cumulative reward by optimizing both design and policy.

### b) **Design as a Parameterized Search**

- Represent designs as parameters.
- Use RL or policy gradient methods to optimize these parameters.
- Treat design parameters as part of the environment or policy input.

### c) **Evolutionary RL**

- Combine evolutionary algorithms with RL:
  - Evolution optimizes design parameters.
  - RL optimizes control policies for each design.
- Iteratively improve designs based on RL-evaluated fitness.

---

## 4. Benefits of Using RL for Agent Design

| Benefit                          | Explanation                                      |
|---------------------------------|-------------------------------------------------|
| **Automated Discovery**          | Reduces manual engineering effort and biases.   |
| **Task-Specific Optimization**  | Designs are optimized for specific tasks/environments. |
| **Joint Optimization**           | Finds synergistic combinations of design and control. |
| **Adaptability**                 | Can adapt designs to changing objectives or constraints. |

---

## 5. Challenges

| Challenge                         | Explanation                                      |
|----------------------------------|-------------------------------------------------|
| **High Dimensionality**            | Large search space combining design and control parameters. |
| **Sample Complexity**              | Training both design and control requires many environment interactions. |
| **Physical Realism and Constraints** | Ensuring designs are physically feasible and manufacturable. |
| **Transfer to Real World**          | Bridging the gap between simulated optimized designs and real-world implementation. |

---

## 6. Applications

- **Robotics:** Learning robot morphologies and controllers simultaneously.
- **Autonomous Vehicles:** Optimizing sensor placements and control policies.
- **Game AI:** Designing agent architectures and behaviors.
- **Industrial Automation:** Optimizing machinery and control strategies jointly.

---

## 7. Example Methods and Studies

- **Co-Optimization of Morphology and Control:** Using RL to jointly optimize robot shape and walking policy (e.g., OpenAI’s learned locomotion).
- **Neural Architecture Search (NAS):** RL-based search for optimal neural network designs.
- **Design Embedding in Policy Inputs:** Policies conditioned on design parameters for adaptable control.

---

## 8. Summary

| Aspect               | Description                                   |
|----------------------|-----------------------------------------------|
| Goal                 | Automate and optimize agent design using RL  |
| Methods              | Joint design-control RL, evolutionary RL, NAS |
| Benefits             | Tailored, high-performance, and adaptive agents |
| Challenges           | Complexity, sample efficiency, physical constraints |

---

## 9. References

- Ha, D., & Schmidhuber, J. (2018). *World Models*.  
- OpenAI et al. (2018). *Learning Agile Robotic Locomotion Skills by Imitating Animals*.  
- Elsken, T., Metzen, J. H., & Hutter, F. (2019). *Neural Architecture Search: A Survey*.

---

Reinforcement Learning for improving agent design represents a promising direction toward creating highly capable, task-optimized agents with minimal human intervention.

# Open-Endedness in Reinforcement Learning: The Example of POET

---

## 1. What is Open-Endedness?

- **Open-endedness** refers to the property of systems that continually generate **novel, diverse, and increasingly complex behaviors or artifacts** without a predefined endpoint.
- In reinforcement learning and AI, open-ended systems strive for **unbounded learning and creativity**, exploring a wide range of challenges and solutions autonomously.

---

## 2. What is POET?

- **POET** stands for **Paired Open-Ended Trailblazer**, an algorithm designed to promote open-ended learning in RL.
- It simultaneously **generates diverse environments** and trains agents to solve them.
- The environments and agents **coevolve**, driving continual innovation and complexity growth.

---

## 3. How POET Works

- **Environment Generation:**  
  POET maintains a population of environments with varying difficulty and features, generated automatically (e.g., obstacle courses).

- **Agent Training:**  
  Each environment has an associated agent trained to solve that environment.

- **Mutual Improvement:**  
  - New environments are created by mutating existing ones.
  - Agents are evolved by learning on their own or transferred to other environments.
  - Environments that are too hard or too easy are discarded, focusing on challenging but solvable tasks.

- This process leads to a **progressive curriculum of environments and agents** without external supervision.

---

## 4. Open-Endedness in POET

- POET demonstrates open-endedness by:

  - **Automatically creating novel, diverse, and increasingly complex tasks**.
  - **Driving agents to develop increasingly sophisticated behaviors**.
  - **Avoiding fixed goals or end states**, instead fostering continuous innovation.
  - **Leveraging transfer learning** where agents trained in one environment help solve others.

---

## 5. Strengths of POET

| Strength                                   | Explanation                                     |
|--------------------------------------------|------------------------------------------------|
| **Autonomous Curriculum Generation**       | Eliminates need for handcrafted training curricula. |
| **Diversity and Novelty**                    | Encourages a wide range of skills and environments. |
| **Continuous Learning and Improvement**     | Agents and environments co-evolve indefinitely. |
| **Transfer and Generalization**              | Agents can transfer knowledge across tasks.     |

---

## 6. Limitations and Challenges

| Limitation                                | Explanation                                      |
|-------------------------------------------|-------------------------------------------------|
| **Computationally Intensive**               | Requires substantial resources to maintain populations of agents and environments. |
| **Evaluation Complexity**                    | Measuring progress and diversity is non-trivial. |
| **Scalability to Real-World Tasks**           | Mostly demonstrated in simulated environments; real-world adoption remains challenging. |

---

## 7. Summary Table

| Aspect                 | POET                                         |
|------------------------|----------------------------------------------|
| Algorithm Type         | Coevolution of agents and environments       |
| Goal                   | Open-ended generation of challenges and solutions |
| Key Mechanism          | Environment mutation, agent training, transfer |
| Open-Endedness         | Continuous novelty and complexity growth     |
| Applications           | Robotics, game AI, procedural content generation |

---

## 8. References

- Wang, J., et al. (2019). *Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions*.  
  [https://arxiv.org/abs/1901.01753](https://arxiv.org/abs/1901.01753)

---

POET exemplifies open-endedness in reinforcement learning by fostering a self-sustaining cycle of environment creation and agent learning, enabling continuous discovery and skill acquisition without explicit external goals.

# Morphological Approach: Learning to Control Self-Assembling Morphologies

---

## 1. Overview

- The **morphological approach** in reinforcement learning involves **learning both the physical structure (morphology)** and the **control policy** of an agent simultaneously.
- **Self-assembling morphologies** refer to agents that can dynamically build or modify their own body structures during learning or deployment.
- This approach aims to discover **optimal body designs and control strategies** jointly to maximize task performance.

---

## 2. Key Concepts

| Concept               | Description                                      |
|-----------------------|-------------------------------------------------|
| **Morphology**        | The agent's physical structure (e.g., number, shape, and arrangement of limbs or modules). |
| **Self-Assembly**      | The process by which individual parts autonomously connect to form a complete agent. |
| **Joint Optimization** | Simultaneous learning of morphology and control policy. |
| **Reinforcement Learning** | The framework used to optimize control and sometimes morphology based on task rewards. |

---

## 3. Learning Framework

- **Design Space:** Morphologies are parameterized (e.g., via modular components, graph structures).
- **Control Policy:** Parameterized controllers (e.g., neural networks) that generate actions based on sensory inputs.
- **Objective:** Maximize cumulative reward through both morphological adaptation and control optimization.
- **Approaches:**
  - **Evolutionary Methods:** Evolve morphologies and controllers.
  - **Gradient-Based Methods:** When differentiable parameterizations are available.
  - **RL with Morphology Parameters:** Treat morphology parameters as part of the policy or environment and optimize via RL.

---

## 4. Advantages of Morphological Learning

| Advantage                                | Explanation                                      |
|-----------------------------------------|-------------------------------------------------|
| **Task-Specific Body Design**            | Morphologies optimized for the task can outperform fixed designs. |
| **Increased Adaptability**                | Agents can adjust their bodies to new environments or tasks. |
| **Improved Efficiency**                   | Optimal morphology can reduce control effort or energy consumption. |
| **Emergent Behaviors**                    | Novel and sophisticated behaviors can arise from co-optimization. |

---

## 5. Challenges

| Challenge                               | Explanation                                      |
|----------------------------------------|-------------------------------------------------|
| **High-Dimensional Search Space**       | Joint space of morphologies and controls is large and complex. |
| **Physical Constraints**                 | Ensuring physically realizable and stable morphologies. |
| **Sample Efficiency**                    | Learning both morphology and control can require extensive interaction. |
| **Transfer to Real-World Robots**        | Sim-to-real gap and hardware constraints complicate deployment. |

---

## 6. Example Studies

- **Self-Assembling Modular Robots:** Agents learn to connect modules to form functional bodies for locomotion.
- **Morphology-Policy Co-Optimization:** Differentiable simulators enable gradient-based joint learning.
- **Evolutionary Approaches:** Use genetic algorithms to evolve morphology and control in simulation.

---

## 7. Summary Table

| Aspect               | Description                                  |
|----------------------|----------------------------------------------|
| Focus                | Joint learning of body morphology and control |
| Methods              | Evolutionary algorithms, RL, differentiable simulation |
| Benefits             | Task-adapted morphology, emergent behaviors |
| Challenges           | Complexity, physical constraints, sample efficiency |

---

## 8. References

- Clune, J. et al. (2014). *Evolving modular neural networks with a novel coevolutionary approach*.  
- Wang, J., et al. (2021). *Learning to Control Self-Assembling Morphologies*.  
- Cheney, N., Bongard, J., & Lipson, H. (2013). *Unshackling evolution: evolving soft robots with multiple materials and a powerful generative encoding*.

---

The morphological approach to learning control enables agents to discover both **how to build** and **how to act**, unlocking new possibilities in adaptive and efficient robotic systems.

# Inductive Biases in Machine Learning and Reinforcement Learning

---

## 1. Definition of Inductive Bias

- **Inductive bias** refers to the set of assumptions a learning algorithm uses to predict outputs for inputs it has never seen before.
- It guides the learning process by restricting the hypothesis space or influencing the preference among hypotheses.
- Without inductive biases, learning from limited data is impossible because infinitely many explanations fit the data.

---

## 2. Why Inductive Biases are Important?

- They enable **generalization** from finite training data.
- Help algorithms **learn efficiently** by focusing on plausible solutions.
- Affect the **performance, sample efficiency, and robustness** of learning systems.

---

## 3. Examples of Inductive Biases

| Example                         | Description                                  | Context/Use Case                        |
|--------------------------------|----------------------------------------------|---------------------------------------|
| **Smoothness Assumption**        | Nearby inputs have similar outputs            | Kernel methods, Gaussian processes    |
| **Sparsity**                    | Only a few features are relevant               | Lasso regression, feature selection   |
| **Temporal Structure**          | Data points close in time are correlated       | Recurrent neural networks (RNNs)      |
| **Spatial Invariance**          | Patterns are invariant to translation          | Convolutional neural networks (CNNs) |
| **Hierarchical Compositionality** | Complex concepts composed of simpler parts   | Hierarchical RL, modular networks     |
| **Markov Property**             | Future depends only on current state            | Markov Decision Processes (MDPs)      |
| **Symmetry and Equivariance**   | Outputs invariant/equivariant to certain transformations | Graph neural networks, physics-informed models |

---

## 4. Inductive Biases in Reinforcement Learning

- **Policy Parameterization Bias:** Choice of policy class (e.g., linear, neural networks) imposes assumptions on policy complexity.
- **Value Function Approximation Bias:** Selecting function approximators (e.g., tabular, linear, deep nets) introduces bias on value estimation.
- **Exploration Strategy:** Assumptions about how to explore (e.g., \(\epsilon\)-greedy, UCB) affect learning dynamics.
- **Model Assumptions:** Model-based methods assume the environment dynamics can be approximated or learned effectively.

---

## 5. Summary Table

| Aspect                 | Inductive Bias Example                       | Effect on Learning                       |
|------------------------|---------------------------------------------|-----------------------------------------|
| Input Structure        | CNNs exploit spatial locality                 | Efficient vision learning                |
| Temporal Data          | RNNs assume sequential dependencies           | Effective sequence modeling              |
| Environment Dynamics   | Markov assumption                              | Simplifies decision process              |
| Policy Class           | Parametric form (e.g., neural nets)           | Limits policy complexity                 |
| Exploration            | \(\epsilon\)-greedy exploration               | Balances exploration/exploitation       |

---

## 6. Conclusion

Inductive biases are essential assumptions embedded within learning algorithms that enable them to generalize and learn efficiently. Thoughtful incorporation of inductive biases tailored to the problem domain significantly improves the success of reinforcement learning and other machine learning methods.


# Relational Inductive Bias in Reinforcement Learning: Example of Relational Deep Reinforcement Learning

---

## 1. What is Relational Inductive Bias?

- **Relational inductive bias** is an assumption embedded in learning algorithms that the data or environment consists of **entities (objects) and their relationships**, and that reasoning about these relations is crucial for understanding and decision-making.
- It encourages models to **explicitly represent and manipulate structured information** about interactions between components.

---

## 2. Relational Inductive Bias in Deep RL

- Traditional deep RL methods often treat input as unstructured data (e.g., images, flat feature vectors).
- Relational inductive bias enables the agent to:
  - Recognize objects as discrete entities.
  - Model interactions and dependencies between objects.
  - Generalize better across environments with varying numbers and configurations of objects.

---

## 3. Relational Deep Reinforcement Learning

- Combines **graph neural networks (GNNs)** or **relation networks** with RL algorithms.
- Inputs are represented as **graphs** where:
  - Nodes correspond to entities or objects.
  - Edges represent relationships or interactions.
- The agent uses relational reasoning to process these graphs and make decisions.

---

## 4. Example: Relational Deep RL Architecture

| Component             | Description                                           |
|-----------------------|-------------------------------------------------------|
| **Object Encoder**    | Encodes each object’s features into node embeddings.   |
| **Relational Module** | Processes nodes and edges using message passing or attention to capture interactions. |
| **Policy Network**    | Uses relational embeddings to output actions or value estimates. |

---

## 5. Benefits of Relational Inductive Bias

| Benefit                                  | Explanation                                      |
|------------------------------------------|-------------------------------------------------|
| **Improved Generalization**               | Can handle variable numbers of objects and novel configurations. |
| **Sample Efficiency**                     | Leverages structured representations to learn faster. |
| **Compositional Reasoning**               | Better captures complex dependencies between entities. |
| **Transferability**                       | Policies learned on one arrangement can transfer to others. |

---

## 6. Example Applications

- **Multi-object manipulation:** Robots interacting with multiple objects.
- **Multi-agent systems:** Reasoning about other agents’ states and actions.
- **Relational reasoning tasks:** Games or environments where object interactions determine outcomes.

---

## 7. Summary Table

| Aspect                | Relational Deep RL                             |
|-----------------------|-----------------------------------------------|
| Inductive Bias        | Objects and their relations                    |
| Representation        | Graph-based (nodes and edges)                  |
| Model Architecture    | Graph Neural Networks, Relation Networks       |
| Advantages            | Generalization, compositionality, transferability |
| Suitable Domains      | Complex, structured environments with many entities |

---

## 8. References

- Zambaldi, V., et al. (2018). *Relational Deep Reinforcement Learning*.  
  [https://arxiv.org/abs/1806.01830](https://arxiv.org/abs/1806.01830)  
- Battaglia, P. W., et al. (2018). *Relational inductive biases, deep learning, and graph networks*.  
  [https://arxiv.org/abs/1806.01261](https://arxiv.org/abs/1806.01261)

---

Relational inductive bias enables deep RL agents to reason about structured environments more effectively, leading to more robust, adaptable, and generalizable policies.

# Including Biases as Losses: The Example of Policy Value Embedding (PVE)

---

## 1. Overview

- In reinforcement learning, **inductive biases** can be incorporated not only through architectural choices but also via **additional loss functions** during training.
- These auxiliary losses encourage the learned representations or policies to possess desired properties, guiding learning toward more effective or interpretable solutions.
- **Policy Value Embedding (PVE)** exemplifies this approach by integrating relational inductive biases as losses to improve state representation learning.

---

## 2. What is Policy Value Embedding (PVE)?

- PVE is a representation learning method that embeds states into a latent space respecting **policy and value function structures**.
- It encourages the embedding space to reflect **similarities in policy behavior and value estimates**.
- This is achieved by adding **bias-inducing loss terms** that regularize the latent representations accordingly.

---

## 3. Including Biases as Losses in PVE

- The key idea is to design **auxiliary loss functions** that encode relational or structural biases:

  - **Policy Similarity Loss:**  
    Encourages states with similar optimal policies to have similar embeddings.

  - **Value Consistency Loss:**  
    Encourages embeddings to capture value function smoothness or ordering.

- These losses are minimized jointly with the standard RL objective, shaping the latent space to reflect meaningful task-related relationships.

---

## 4. Example Loss Formulations in PVE

| Loss Type               | Description                                    | Purpose                                     |
|------------------------|------------------------------------------------|---------------------------------------------|
| **Policy Embedding Loss** | Minimize distance between embeddings of states with similar policies:  

\[
\mathcal{L}_{policy} = \sum_{(s_i, s_j)} w_{ij} \| \phi(s_i) - \phi(s_j) \|^2
\]

where \(w_{ij}\) encodes similarity of policies at \(s_i, s_j\). | Captures policy-driven state similarity          |
| **Value Embedding Loss**   | Enforce embedding distances to reflect value differences:

\[
\mathcal{L}_{value} = \sum_{(s_i, s_j)} \left| \| \phi(s_i) - \phi(s_j) \| - |V(s_i) - V(s_j)| \right|
\]

| Aligns latent geometry with value function structure |

---

## 5. Benefits of Incorporating Biases as Losses

| Benefit                                  | Explanation                                      |
|------------------------------------------|-------------------------------------------------|
| **Improved Representation Quality**      | Embeddings capture meaningful task-relevant relations. |
| **Better Generalization**                 | Structured latent space aids transfer and robustness. |
| **Sample Efficiency**                     | Auxiliary losses provide additional learning signals. |
| **Interpretability**                      | Learned embeddings reflect policy and value relationships. |

---

## 6. Challenges

| Challenge                                | Explanation                                      |
|------------------------------------------|-------------------------------------------------|
| **Designing Effective Losses**            | Requires insight into which biases to encode and how. |
| **Balancing Loss Terms**                   | Auxiliary losses must be weighted properly to avoid overpowering primary objectives. |
| **Computational Overhead**                 | Additional losses increase training complexity. |

---

## 7. Summary

| Aspect              | Description                                     |
|---------------------|------------------------------------------------|
| Approach           | Encode inductive biases as auxiliary loss terms |
| Example            | PVE uses policy and value similarity losses      |
| Goal               | Shape learned latent representations             |
| Advantages         | Enhances learning efficiency and representation quality |
| Limitations        | Requires careful loss design and tuning          |

---

## 8. References

- Agarwal, R., et al. (2020). *Learning Latent Representations for Policy Evaluation*.  
- PVE: Policy Value Embedding, incorporating policy and value structure into latent representations.

---

Including inductive biases as losses, as exemplified by PVE, is a powerful technique to guide representation learning and improve reinforcement learning outcomes.

# Causality and Adversarial Examples in Reinforcement Learning (RL)

---

## 1. Causality in Reinforcement Learning

### What is Causality?

- **Causality** refers to understanding the cause-effect relationships between variables, beyond mere correlations.
- In RL, causal reasoning helps agents **understand how actions influence future states and rewards** in a principled way.

### Importance in RL

- Enables better **generalization and robustness** by distinguishing true causal effects from spurious correlations.
- Helps agents **transfer knowledge across environments** with different confounding factors.
- Facilitates **interpretability** and **explainability** of agent decisions.

### Challenges

- Learning causal structure from interaction data is difficult due to **confounding variables**, **partial observability**, and **non-stationarity**.
- Most RL algorithms implicitly rely on correlational patterns rather than explicit causal models.

### Approaches to Incorporate Causality

- **Causal Models & Structural Causal Models (SCMs):** Integrating SCMs into RL frameworks.
- **Counterfactual Reasoning:** Estimating what would happen under different actions.
- **Causal Discovery:** Learning causal graphs from data to improve policy learning.

---

## 2. Adversarial Examples in Reinforcement Learning

### What are Adversarial Examples?

- Inputs intentionally designed to **mislead or confuse** a learning algorithm, causing it to make incorrect decisions.
- Commonly studied in supervised learning (e.g., image classification), but also relevant in RL.

### Adversarial Examples in RL

- Adversaries can **perturb observations**, **manipulate rewards**, or **modify environment dynamics**.
- Can lead to **suboptimal or unsafe policies**, performance degradation, or failure to learn.

### Examples

- Slightly altered observations causing wrong action selection.
- Manipulated reward signals that misguide learning.
- Environment changes that exploit learned policy weaknesses.

### Defense and Robustness

- **Adversarial Training:** Training with adversarially perturbed data.
- **Robust Policies:** Learning policies that perform well under a range of perturbations.
- **Detection Mechanisms:** Identifying when inputs have been adversarially altered.
- **Causality-Based Defenses:** Using causal reasoning to detect and ignore spurious or manipulated signals.

---

## 3. Relationship Between Causality and Adversarial Robustness

- Causal models can **improve robustness** by focusing on invariant causal relationships rather than brittle correlations.
- Causal reasoning can help **identify adversarial manipulations** that exploit non-causal features.
- Incorporating causality into RL may lead to agents that are **less susceptible to adversarial attacks**.

---

## 4. Summary Table

| Topic                 | Description                                   | Challenges                              | Potential Solutions                     |
|-----------------------|-----------------------------------------------|---------------------------------------|---------------------------------------|
| **Causality in RL**   | Understanding cause-effect in environment transitions and rewards | Confounding, partial observability    | SCMs, counterfactuals, causal discovery |
| **Adversarial Examples** | Malicious perturbations to inputs or environment to mislead agent | Detection, robustness, safe learning | Adversarial training, robust policies, causal defenses |

---

## 5. References

- Pearl, J. (2009). *Causality: Models, Reasoning and Inference*.  
- Zhang, C., et al. (2020). *Robust Reinforcement Learning via Causal Models*.  
- Huang, S., et al. (2017). *Adversarial Attacks on Deep Reinforcement Learning*.  
- Pinto, L., et al. (2017). *Robust Adversarial Reinforcement Learning*.

---

Causality and adversarial examples are critical considerations for building **robust, generalizable, and trustworthy reinforcement learning agents** in real-world applications.

# Causal Calculus: A Brief Description

---

## 1. What is Causal Calculus?

- **Causal calculus** is a formal framework developed by Judea Pearl for reasoning about cause-and-effect relationships using graphical models (causal diagrams).
- It provides a set of rules to **manipulate and compute causal effects** from observational and interventional data.

---

## 2. Purpose of Causal Calculus

- To answer **causal queries**, such as:
  - What is the effect of intervening (doing) on a variable?
  - How to estimate causal effects from non-experimental (observational) data?
  - How to identify confounding factors and control for them?

---

## 3. Core Concepts

| Concept              | Description                                       |
|----------------------|---------------------------------------------------|
| **Causal Graph (DAG)** | Directed acyclic graph representing causal relationships among variables. |
| **Intervention (do-operator)** | Notation \(do(X=x)\) represents setting variable \(X\) to value \(x\) externally. |
| **Back-Door Criterion** | A graphical condition to identify confounders to adjust for unbiased causal effect estimation. |
| **Front-Door Criterion** | An alternative adjustment method when back-door adjustment is not possible. |

---

## 4. Main Rules of Causal Calculus (Pearl's Do-Calculus)

Pearl's do-calculus includes three rules that allow transforming expressions involving the do-operator:

1. **Insertion/Deletion of Observations:**

\[
P(y | do(x), z, w) = P(y | do(x), w) \quad \text{if } (Y \perp Z | X,W)_{G_{\overline{X}}}
\]

2. **Action/Observation Exchange:**

\[
P(y | do(x), do(z), w) = P(y | do(x), z, w) \quad \text{if } (Y \perp Z | X,W)_{G_{\overline{X}, \underline{Z}}}
\]

3. **Insertion/Deletion of Actions:**

\[
P(y | do(x), do(z), w) = P(y | do(x), w) \quad \text{if } (Y \perp Z | X,W)_{G_{\overline{X}, \overline{Z(W)}}}
\]

where conditional independencies are checked on modified graphs.

---

## 5. Applications

- Estimating causal effects from observational data.
- Designing experiments and interventions.
- Understanding confounding and mediation in complex systems.
- Informing causal inference in machine learning and AI.

---

## 6. Summary

| Aspect               | Description                                      |
|----------------------|--------------------------------------------------|
| Framework            | Graphical causal models and do-operator notation |
| Purpose              | Reason about and compute causal effects          |
| Key Tool             | Pearl's do-calculus rules                          |
| Outcome              | Enables identification and estimation of causal quantities from data |

---

## 7. References

- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*.  
- Pearl, J. (1995). *Causal Diagrams for Empirical Research*.  
- Spirtes, P., Glymour, C., & Scheines, R. (2000). *Causation, Prediction, and Search*.

---

Causal calculus provides a rigorous mathematical foundation for reasoning about causality, essential for causal inference and decision-making in AI and beyond.

# Causal Confusion in Imitation Learning

---

## 1. What is Causal Confusion?

- **Causal confusion** occurs when a learning agent mistakenly learns to rely on features or correlations that are **predictive but not causally relevant** for the task.
- The agent's policy may perform well on training data but fails to generalize or succeed when the spurious correlations change or disappear.

---

## 2. Causal Confusion in Imitation Learning

- In **imitation learning (IL)**, agents learn policies by mimicking expert demonstrations.
- If the expert’s behavior correlates with irrelevant environmental features (confounders), the agent may learn to condition its actions on these features instead of true causal factors.
- This leads to **suboptimal or brittle policies** that fail under distribution shifts or interventions.

---

## 3. Illustrative Example

- Consider an expert driving a car where the **presence of a pedestrian** and **a particular background object** are correlated.
- The expert slows down due to the pedestrian (causal).
- However, the background object consistently appears with pedestrians.
- A naive imitation learner might learn to slow down when it sees the background object, mistaking correlation for causation.
- When the background object appears without a pedestrian, the agent incorrectly slows down (failure).

---

## 4. Consequences of Causal Confusion

| Consequence                     | Explanation                                      |
|--------------------------------|-------------------------------------------------|
| **Poor Generalization**          | Policies fail when spurious correlations change. |
| **Unreliable Decision Making**   | Agent acts on irrelevant cues, potentially causing errors. |
| **Difficulty in Transfer Learning** | Learned policies do not adapt well to new environments. |

---

## 5. Addressing Causal Confusion

| Approach                      | Description                                      |
|-------------------------------|-------------------------------------------------|
| **Causal Imitation Learning** | Incorporate causal reasoning to disentangle causal factors from confounders. |
| **Interventional Data**        | Use data collected under interventions to identify causal relationships. |
| **Invariant Risk Minimization** | Learn representations invariant to spurious correlations. |
| **Feature Selection**          | Identify and use only causally relevant features. |

---

## 6. Summary

| Aspect               | Description                                   |
|----------------------|-----------------------------------------------|
| Problem              | Learning policies based on spurious correlations rather than causal factors |
| Context              | Imitation learning from expert demonstrations |
| Impact               | Poor generalization and failure in new or shifted environments |
| Solutions            | Causal inference, intervention, invariant learning |

---

## 7. References

- de Haan, P., et al. (2019). *Causal Confusion in Imitation Learning*.  
- Zhang, J., et al. (2020). *Invariant Causal Prediction for Block MDPs*.  
- Pearl, J. (2009). *Causality: Models, Reasoning and Inference*.

---

Understanding and mitigating causal confusion is essential to develop robust and reliable imitation learning agents that generalize beyond their training data.

# End-to-End Learning for Self-Driving Cars

---

## 1. Overview

- **End-to-end learning** for self-driving cars refers to training a single model (often a deep neural network) that directly maps raw sensory input (e.g., camera images) to driving commands (steering, acceleration, braking).
- This contrasts with traditional modular pipelines where perception, localization, planning, and control are handled separately.
- The approach aims to simplify system design and leverage large datasets to learn complex driving behaviors.

---

## 2. Typical Architecture

- Input: Raw images, sensor data (LiDAR, radar, GPS).
- Model: Convolutional Neural Networks (CNNs) or other architectures.
- Output: Control commands or waypoints.
- Training: Supervised learning from **human driving demonstrations** (imitation learning) or reinforcement learning.

---

## 3. Benefits of End-to-End Learning

| Benefit                           | Explanation                                      |
|----------------------------------|-------------------------------------------------|
| **Simplified Pipeline**            | Avoids complex hand-engineered components.       |
| **Feature Learning**               | Automatically learns relevant features from raw data. |
| **Adaptability**                  | Can learn complex behaviors and adapt to diverse scenarios. |
| **Potential for Improvement**     | Continuous improvement with more data and better architectures. |

---

## 4. Problems with Imitation Learning in End-to-End Driving

### a) **Covariate Shift / Distribution Mismatch**

- Training data consists of expert demonstrations, but at test time, the agent's actions can lead to states not seen during training.
- This mismatch causes **compounding errors** and poor recovery from mistakes.

### b) **Limited Exploration**

- IL relies on supervised data and does not explore alternative actions.
- The model cannot learn how to recover from novel or unexpected situations.

### c) **Causal Confusion**

- The model may learn spurious correlations in the data (e.g., background features) that do not causally influence driving decisions, leading to poor generalization.

### d) **Data Requirements**

- Requires large amounts of high-quality labeled driving data covering diverse scenarios.

### e) **Lack of Interpretability**

- End-to-end models are often black boxes, making debugging and safety validation challenging.

---

## 5. Mitigating Imitation Learning Problems

| Approach                        | Description                                      |
|---------------------------------|-------------------------------------------------|
| **Data Augmentation**            | Increase diversity of training data to reduce covariate shift. |
| **DAgger (Dataset Aggregation)** | Iteratively collect data from the learner’s policy to reduce distribution mismatch. |
| **Hybrid Methods**               | Combine IL with reinforcement learning for exploration and recovery. |
| **Causal Inference Techniques** | Reduce causal confusion by focusing on causal features. |
| **Modular Architectures**        | Blend end-to-end learning with interpretable submodules. |

---

## 6. Summary Table

| Aspect                      | End-to-End Learning Approach                     |
|-----------------------------|--------------------------------------------------|
| Input                      | Raw sensor data (images, LiDAR, etc.)             |
| Output                     | Direct control commands                            |
| Training                   | Supervised imitation learning (mostly)            |
| Advantages                 | Simplification, automatic feature learning         |
| Challenges                 | Covariate shift, limited exploration, causal confusion, data demands |

---

## 7. References

- Bojarski, M., et al. (2016). *End to End Learning for Self-Driving Cars*.  
- Ross, S., et al. (2011). *A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning* (DAgger).  
- Codevilla, F., et al. (2018). *End-to-End Driving via Conditional Imitation Learning*.

---

End-to-end learning offers a promising but challenging avenue for autonomous driving, requiring careful consideration of imitation learning pitfalls and strategies to enhance robustness and safety.

# Random Exploration: Example of *Learning to Fly by Crashing*

---

## 1. Overview of Random Exploration

- **Random exploration** involves the agent taking actions in a largely random or uninformed manner to gather diverse experience about the environment.
- It is a fundamental strategy to discover new states and learn effective policies, especially when prior knowledge is limited.
- Though simple, random exploration can be effective in some settings but may be inefficient or unsafe in complex environments.

---

## 2. *Learning to Fly by Crashing* – The Approach

- Presented by *Mahjourian et al.* (2018), this approach uses **random exploration** to train a drone to **learn how to fly indoors** by crashing repeatedly.
- The drone performs **random flights** in an environment, collecting data about states leading to crashes and safe navigation.
- This data is then used to train a **collision prediction model** and a **policy to avoid obstacles**.

---

## 3. Key Elements of the Approach

| Aspect                   | Description                                    |
|--------------------------|------------------------------------------------|
| **Exploration Method**    | Purely random actions during initial data collection phase. |
| **Data Collection**       | Thousands of crashes provide diverse failure/success examples. |
| **Learning Objective**    | Train a model to predict collisions and learn safe flight policies. |
| **Policy Improvement**    | Use learned collision model to avoid unsafe actions. |

---

## 4. Why Use Random Exploration Here?

- **No prior model:** The drone starts with no knowledge of the environment or dynamics.
- **Data diversity:** Random crashes generate a wide range of experiences, including failure modes.
- **Simplicity:** Easy to implement without complex exploration strategies.
- **Real-world feasibility:** Enables data collection in real environments without pre-programmed behaviors.

---

## 5. Strengths of Random Exploration in This Context

| Strength                                  | Explanation                                      |
|-------------------------------------------|-------------------------------------------------|
| **Simplicity and Scalability**             | No need for handcrafted exploration policies.   |
| **Comprehensive Failure Data**              | Captures rich information on unsafe states.      |
| **Effective for Unknown Environments**      | Useful when no prior knowledge exists.            |
| **Enables Self-Supervised Learning**         | Labels generated automatically from crashes.     |

---

## 6. Limitations and Challenges

| Limitation                                | Explanation                                      |
|-------------------------------------------|-------------------------------------------------|
| **Inefficiency**                           | Random actions can be wasteful, requiring many crashes/data. |
| **Safety Concerns**                        | Crashing can damage hardware or be hazardous in some settings. |
| **Slow Convergence**                       | Random exploration may take long to discover effective policies. |
| **Not Suitable for All Domains**           | In some environments, random exploration is impractical or impossible. |

---

## 7. Summary Table

| Aspect                 | Description                                    |
|------------------------|------------------------------------------------|
| Exploration Strategy  | Random action sampling                          |
| Environment           | Real-world indoor drone flight                  |
| Data                  | Large-scale crash data for learning             |
| Benefits              | Simplicity, diverse experience collection       |
| Drawbacks             | Inefficiency, safety risks                        |

---

## 8. References

- Mahjourian, R., Xu, D., & Fei-Fei, L. (2018). *Learning to Fly by Crashing*.  
  [https://arxiv.org/abs/1805.12114](https://arxiv.org/abs/1805.12114)

---

Random exploration, despite its simplicity, can be a powerful tool for data collection and learning in unknown, real-world settings, exemplified by the *Learning to Fly by Crashing* approach.

# Domain Randomization: Example from OpenAI Rubik’s Cube Project

---

## 1. What is Domain Randomization?

- **Domain randomization** is a technique used in sim-to-real transfer to improve the generalization of models trained in simulation.
- It involves **randomly varying simulation parameters** (e.g., textures, lighting, object properties) during training so the learned policy becomes robust to discrepancies between simulation and the real world.
- The goal is to enable policies trained in simulation to **transfer effectively to real-world environments** without additional fine-tuning.

---

## 2. OpenAI Rubik’s Cube Project Overview

- OpenAI trained a robotic system to **solve a Rubik’s Cube using a Shadow Dexterous Hand**.
- The system was trained **entirely in simulation**, using reinforcement learning.
- Transitioning to the real robot required overcoming the **sim-to-real gap**.

---

## 3. Use of Domain Randomization in the Project

- OpenAI applied extensive **domain randomization** during training, randomizing:

  - **Physics parameters:** friction coefficients, object mass, joint damping.
  - **Visual appearance:** lighting conditions, textures, colors.
  - **Sensor noise:** camera noise, latency, and inaccuracies.
  - **Robot dynamics:** actuator delays, motor strengths.

- This forced the policy to learn **robust control strategies** invariant to these variations.

---

## 4. Benefits Demonstrated

| Benefit                               | Explanation                                       |
|-------------------------------------|--------------------------------------------------|
| **Improved Transferability**          | Policy trained on randomized simulation performed well on the real robot. |
| **Robustness to Real-World Variability** | Policy handled uncertainties and noise in actual hardware. |
| **Reduced Need for Real-World Data**  | Minimized costly real-world training or fine-tuning. |

---

## 5. Challenges and Considerations

| Challenge                           | Explanation                                      |
|-----------------------------------|-------------------------------------------------|
| **Choosing Randomization Range**    | Too narrow may not cover real-world variability; too broad can slow learning. |
| **Computational Cost**               | Increased training time due to diverse simulation settings. |
| **Residual Reality Gap**             | Some discrepancies may still require real-world fine-tuning. |

---

## 6. Summary Table

| Aspect               | OpenAI Rubik’s Cube Project                    |
|----------------------|------------------------------------------------|
| Task                 | Dexterous robotic manipulation of Rubik’s Cube |
| Training             | Reinforcement learning in simulation with domain randomization |
| Randomized Domains   | Physics, visuals, sensors, robot dynamics       |
| Outcome              | Successful zero-shot transfer to real robot     |
| Key Technique        | Domain randomization to bridge sim-to-real gap |

---

## 7. References

- OpenAI et al. (2019). *Solving Rubik’s Cube with a Robot Hand*.  
  [https://arxiv.org/abs/1910.07113](https://arxiv.org/abs/1910.07113)  
- Tobin, J., et al. (2017). *Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World*.  

---

Domain randomization proved critical in enabling the OpenAI robotic hand to perform complex manipulation tasks in the real world after training purely in simulation, highlighting its power in sim-to-real transfer.

# General/Universal Random Functions and Hindsight Replay Buffer Technique

---

## 1. General/Universal Random Functions

### Definition

- **General/Universal Random Functions** refer to randomized components or functions used in reinforcement learning to introduce stochasticity or variability in policies, environments, or algorithms.
- These functions can be used to generate **diverse behaviors, explore effectively, or regularize learning**.

### Examples and Uses

- **Randomized Policies:** Policies that select actions based on probability distributions (e.g., \(\epsilon\)-greedy, softmax).
- **Parameter Noise:** Adding noise to policy parameters to induce consistent exploratory behavior.
- **Random Network Distillation:** Using random projections to estimate novelty for exploration bonuses.
- **Random Initialization:** Initializing neural networks or models randomly to encourage diverse learning trajectories.

### Benefits

- Promote **exploration** in unknown environments.
- Help avoid **local optima** by injecting variability.
- Can improve **robustness and generalization**.

---

## 2. Hindsight Replay Buffer Technique

### What is Hindsight Experience Replay (HER)?

- HER is a replay buffer technique designed to improve learning in environments with **sparse and binary rewards**.
- Introduced by Andrychowicz et al. (2017), HER allows the agent to learn from **failed attempts** by **relabeling goals** post hoc.

### How HER Works

- During training, the agent stores transitions \((s_t, a_t, r_t, s_{t+1}, g)\) where \(g\) is the original goal.
- When sampling from the replay buffer, HER **relabels the goal** \(g\) to a different goal \(g'\) that was actually achieved later in the episode.
- The reward is recomputed with respect to the new goal \(g'\), turning unsuccessful trajectories into successful ones for alternative goals.

### Benefits of HER

- **Improves sample efficiency** by extracting more learning signal from sparse rewards.
- Enables learning **multi-goal policies** that generalize to various objectives.
- Facilitates learning **in challenging environments** where the original goal is rarely reached.

---

## 3. Summary Table

| Technique                      | Purpose                                    | Key Idea                                            | Benefits                                  |
|-------------------------------|--------------------------------------------|-----------------------------------------------------|-------------------------------------------|
| General/Universal Random Functions | Introduce stochasticity for exploration or regularization | Use randomized policies, noise, or functions         | Enhanced exploration, robustness, generalization |
| Hindsight Experience Replay (HER) | Improve learning with sparse rewards     | Relabel goals in replay buffer to learn from failures | Sample efficiency, multi-goal learning            |

---

## 4. References

- Andrychowicz, M., et al. (2017). *Hindsight Experience Replay*.  
- Plappert, M., et al. (2017). *Parameter Space Noise for Exploration*.  
- Burda, Y., et al. (2018). *Exploration by Random Network Distillation*.

---

General/random functions and hindsight replay buffers are powerful tools to enhance exploration and learning efficiency, especially in complex or sparse-reward reinforcement learning tasks.