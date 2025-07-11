from game.nim_env import Nim
from agent.q_learning_agent import QLearningAgent

def human_turn(env):
    valid = env.get_valid_actions()
    print("Sua vez!")
    print(f"Movimentos válidos: {valid}")
    while True:
        try:
            heap = int(input("Escolhe o index de um Monte: "))
            amount = int(input("Escolha quantas pedras remover: "))
            if (heap, amount) in valid:
                return (heap, amount)
            else:
                print("Movimento inválido, tente novamente")
        except ValueError:
            print("Por favor insira numeros válidos")

def main():
    env = Nim()
    actions = [(i, j) for i in range(len(env.heaps)) for j in range(1, max(env.heaps)+1)]
    agent = QLearningAgent(actions)
    
    state = env.reset()
    done = False
    human_turn_flag = True

    while not done:
        env.render()
        if human_turn_flag:
            action = human_turn(env)
        else:
            valid_actions = env.get_valid_actions()
            action = agent.choose_action(state, valid_actions)
            print(f"Ação IA: {action}")
        
        state, reward, done = env.step(action)
        human_turn_flag = not human_turn_flag
    
    env.render()
    if human_turn_flag:
        print("I.A Venceu!")
    else:
        print("Você Venceu!")

if __name__ == "__main__":
    main()
