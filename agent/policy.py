import random

def epsilon_greedy_policy(q_values, valid_actions, epsilon):
    """
    Escolhe uma ação usando a política epsilon-greedy.

    Args:
        q_values (dict): dicionário ação -> valor Q para o estado atual.
        valid_actions (list): lista das ações válidas no estado atual.
        epsilon (float): probabilidade de explorar (escolher ação aleatória).

    Returns:
        ação escolhida (qualquer tipo que represente a ação)
    """
    if random.random() < epsilon:
        return random.choice(valid_actions)
    else:
        max_q = float('-inf')
        best_actions = []
        for action in valid_actions:
            q = q_values.get(action, 0.0)
            if q > max_q:
                max_q = q
                best_actions = [action]
            elif q == max_q:
                best_actions.append(action)
        return random.choice(best_actions)
