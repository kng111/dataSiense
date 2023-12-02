def make_decision_tree():
    # Создаем простое дерево решений для игры в "20 вопросов"
    
    decision_tree = {
        'question': 'Is it a living thing?',
        'yes': {
            'question': 'Does it have fur?',
            'yes': 'It could be a mammal.',
            'no': 'It could be something else.'
        },
        'no': 'It might be a non-living thing.'
    }
    
    return decision_tree

def play_game(tree):
    # Играем в "20 вопросов" на основе дерева решений
    
    current_node = tree
    
    while isinstance(current_node, dict):
        print(current_node['question'])
        answer = input("Enter 'yes' or 'no': ").lower()
        
        if answer == 'yes':
            current_node = current_node['yes']
        elif answer == 'no':
            current_node = current_node['no']
        else:
            print("Invalid answer. Please enter 'yes' or 'no'.")
    
    print("Result: " + current_node)

# Создаем дерево решений
decision_tree = make_decision_tree()

# Играем в "20 вопросов"
play_game(decision_tree)
