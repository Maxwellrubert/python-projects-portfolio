from flask import Flask, render_template, request, jsonify, abort
import random
import json
import os
import logging

app = Flask(__name__)

# Production configuration
if os.environ.get('VERCEL'):
    app.config['ENV'] = 'production'
    app.config['DEBUG'] = False
else:
    app.config['DEBUG'] = True

# Set up logging for production
if not app.debug:
    logging.basicConfig(level=logging.INFO)

# Project metadata
projects_data = {
    "calculator": {
        "title": "Calculator",
        "description": "A simple calculator with basic arithmetic operations",
        "difficulty": "Easy",
        "technologies": ["Python", "Functions"],
        "icon": "🧮",
        "order": 1
    },
    "password-generator": {
        "title": "Password Generator",
        "description": "Generate secure passwords with customizable length and character types",
        "difficulty": "Easy",
        "technologies": ["Python", "Random", "Lists"],
        "icon": "🔐",
        "order": 2
    },
    "number-guessing": {
        "title": "Number Guessing Game",
        "description": "Guess the random number with difficulty levels",
        "difficulty": "Easy",
        "technologies": ["Python", "Random", "Loops"],
        "icon": "🎯",
        "order": 3
    },
    "rock-paper-scissors": {
        "title": "Rock Paper Scissors",
        "description": "Classic game with ASCII art and bot opponent",
        "difficulty": "Easy",
        "technologies": ["Python", "Random", "ASCII Art"],
        "icon": "✂️",
        "order": 4
    },
    "blackjack": {
        "title": "Blackjack 21",
        "description": "Card game with dealer AI and smart ace handling",
        "difficulty": "Medium",
        "technologies": ["Python", "Game Logic", "Lists"],
        "icon": "🃏",
        "order": 5
    },
    "hangman": {
        "title": "Hangman Game",
        "description": "Word guessing game with lives system",
        "difficulty": "Medium",
        "technologies": ["Python", "String Manipulation", "Loops"],
        "icon": "🎪",
        "order": 6
    },
    "caesar-cipher": {
        "title": "Caesar Cipher",
        "description": "Encrypt and decrypt messages using Caesar cipher",
        "difficulty": "Medium",
        "technologies": ["Python", "Encryption", "Strings"],
        "icon": "🔒",
        "order": 7
    },
    "higher-lower": {
        "title": "Higher Lower Game",
        "description": "Guess which option has more followers/popularity",
        "difficulty": "Medium",
        "technologies": ["Python", "Data Comparison", "Game Logic"],
        "icon": "📊",
        "order": 8
    },
    "coffee-machine": {
        "title": "Coffee Machine",
        "description": "Simulate a coffee vending machine with resources management",
        "difficulty": "Hard",
        "technologies": ["Python", "OOP", "State Management"],
        "icon": "☕",
        "order": 9
    },
    "secret-auction": {
        "title": "Secret Auction",
        "description": "Blind auction system with multiple bidders",
        "difficulty": "Medium",
        "technologies": ["Python", "Dictionaries", "User Input"],
        "icon": "🔨",
        "order": 10
    }
}

@app.route('/')
def home():
    # Sort projects by order
    sorted_projects = sorted(projects_data.items(), key=lambda x: x[1]['order'])
    return render_template('index.html', projects=sorted_projects)

@app.route('/project/<project_id>')
def project_detail(project_id):
    if project_id not in projects_data:
        return "Project not found", 404
    
    project = projects_data[project_id]
    
    # Load the source code
    source_code = get_source_code(project_id)
    
    return render_template('project.html', project=project, project_id=project_id, source_code=source_code)

def get_source_code(project_id):
    """Load the actual Python source code for a project"""
    
    # Map project IDs to actual Python files
    file_mapping = {
        'calculator': '10-calculator.py',
        'password-generator': '5-passwordgen.py', 
        'number-guessing': '12-guessnum.py',
        'rock-paper-scissors': '4-rockpaperscissors.py',
        'blackjack': '11-blackjack21.py',
        'hangman': '7-hangman.py',
        'caesar-cipher': '8-caesercipher.py',
        'higher-lower': '14-higherlowergame.py',
        'coffee-machine': '15-coffeemachine.py',
        'secret-auction': '9-secretbidmod.py'
    }
    
    if project_id not in file_mapping:
        return "# Source code not available for this project yet."
    
    file_path = os.path.join('my-python-codes', file_mapping[project_id])
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"# Source code file not found: {file_path}"
    except Exception as e:
        return f"# Error loading source code: {str(e)}"

@app.route('/api/calculator', methods=['POST'])
def calculator_api():
    data = request.json
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    
    return jsonify({'result': result})

@app.route('/api/password-generator', methods=['POST'])
def password_generator_api():
    data = request.json
    length = int(data.get('length', 12))
    include_letters = data.get('letters', True)
    include_numbers = data.get('numbers', True)
    include_symbols = data.get('symbols', True)
    
    alphabets = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '#', '$', '%', '^', '&', '*', '=', '/', '<', '>', '|']
    
    char_pool = []
    if include_letters:
        char_pool.extend(alphabets)
    if include_numbers:
        char_pool.extend(numbers)
    if include_symbols:
        char_pool.extend(symbols)
    
    if not char_pool:
        return jsonify({'error': 'Must include at least one character type'}), 400
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return jsonify({'password': password})

@app.route('/api/number-guessing', methods=['POST'])
def number_guessing_api():
    data = request.json
    action = data.get('action')
    
    if action == 'start':
        difficulty = data.get('difficulty', 'easy')
        target_number = random.randint(1, 100)
        chances = 10 if difficulty == 'easy' else 5
        
        return jsonify({
            'target_number': target_number,
            'chances': chances,
            'max_chances': chances,
            'message': f'I\'m thinking of a number between 1 and 100. You have {chances} chances!'
        })
    
    elif action == 'guess':
        guess = int(data['guess'])
        target = int(data['target_number'])
        remaining_chances = int(data['remaining_chances'])
        
        if guess == target:
            return jsonify({
                'correct': True,
                'message': f'🎉 Congratulations! You guessed it! The number was {target}.',
                'game_over': True
            })
        elif remaining_chances <= 1:
            return jsonify({
                'correct': False,
                'message': f'💀 Game over! The number was {target}.',
                'game_over': True
            })
        else:
            if guess > target:
                hint = '📉 Too high!'
            else:
                hint = '📈 Too low!'
            
            remaining = remaining_chances - 1
            return jsonify({
                'correct': False,
                'message': f'{hint} You have {remaining} chances left.',
                'remaining_chances': remaining,
                'game_over': False
            })

@app.route('/api/rock-paper-scissors', methods=['POST'])
def rock_paper_scissors_api():
    data = request.json
    player_choice = data['choice'].lower()
    
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    
    # Determine winner
    if player_choice == bot_choice:
        result = 'draw'
        message = "It's a tie!"
    elif (player_choice == 'rock' and bot_choice == 'scissors') or \
         (player_choice == 'paper' and bot_choice == 'rock') or \
         (player_choice == 'scissors' and bot_choice == 'paper'):
        result = 'win'
        message = "You win!"
    else:
        result = 'lose'
        message = "Bot wins!"
    
    return jsonify({
        'player_choice': player_choice,
        'bot_choice': bot_choice,
        'result': result,
        'message': message
    })

# Error handlers for production
@app.errorhandler(404)
def not_found_error(error):
    return render_template('base.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('base.html'), 500

@app.errorhandler(Exception)
def handle_exception(e):
    if app.debug:
        raise e
    app.logger.error(f'Unhandled exception: {e}')
    return render_template('base.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
