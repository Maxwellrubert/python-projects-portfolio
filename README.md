# Maxwell's Python Projects Portfolio

A modern, interactive web portfolio showcasing Python programming projects with live demos, source code viewing, and responsive design.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-black.svg)

## Live Demo

� **[View Live Portfolio](https://your-portfolio-url.vercel.app)**

## Features

- **Interactive Demos**: Try each project directly in your browser
- **Responsive Design**: Works perfectly on desktop and mobile
- **Modern UI**: Clean, professional design with dark/light mode
- **Live Code Execution**: Real-time interaction with Python logic
- **Project Filtering**: Search and filter projects by difficulty and technology
- **Source Code Viewer**: View the original Python code for each project

## Project Structure

```
MyWorksApp/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── main.js       # JavaScript functionality
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Landing page
│   ├── project.html      # Project detail page
│   └── demos/            # Individual project demos
│       ├── calculator.html
│       ├── password_generator.html
│       ├── number_guessing.html
│       └── rock_paper_scissors.html
└── my-python-codes/      # Original Python projects
    ├── 10-calculator.py
    ├── 11-blackjack21.py
    ├── 12-guessnum.py
    └── ... (other projects)
```

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd "C:\Users\maxwe\Documents\VS Code\MyWorksApp"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and visit:
   ```
   http://localhost:5000
   ```

## Available Projects

1. **Calculator** - Basic arithmetic operations with a modern interface
2. **Password Generator** - Secure password creation with customizable options
3. **Number Guessing Game** - Guess the number with difficulty levels
4. **Rock Paper Scissors** - Classic game with bot opponent
5. **Blackjack 21** - Card game with dealer AI
6. **Hangman** - Word guessing game
7. **Caesar Cipher** - Text encryption/decryption
8. **Higher Lower Game** - Comparison guessing game
9. **Coffee Machine** - Virtual coffee ordering system
10. **Secret Auction** - Blind bidding system

## Deployment Options

This Flask application can be deployed to various platforms:

### Recommended: **Vercel** (Free tier available)
1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the project directory
3. Follow the prompts

### Alternative Options:
- **Render**: Free tier with easy Python deployment
- **Netlify**: For static deployment (requires conversion)
- **Heroku**: Classic platform (paid plans)
- **Railway**: Modern deployment platform

## Customization

### Colors and Themes
Edit CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #3b82f6;    /* Main blue */
    --accent-color: #10b981;     /* Green accent */
    --bg-primary: #ffffff;       /* Background */
    /* ... other variables */
}
```

### Adding New Projects
1. Add project data to `projects_data` in `app.py`
2. Create API endpoint for interactive functionality
3. Create demo template in `templates/demos/`
4. Add corresponding Python file to `my-python-codes/`

## 🔧 Development

### Running in Development Mode
```bash
# Enable debug mode
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows

python app.py
```

### File Structure
- **Backend**: Flask handles API endpoints and renders templates
- **Frontend**: Vanilla JavaScript with modern CSS
- **Styling**: CSS Grid/Flexbox for responsive layout
- **Interactivity**: Fetch API for seamless demo experience

## Mobile Support

The website is fully responsive and works great on:
- Desktop computers
- Tablets
- Mobile phones
- Various screen sizes

## Contributing

This is a personal portfolio project, but suggestions and improvements are welcome!

## License

This project is for educational purposes. Feel free to use as inspiration for your own portfolio!

## About

Created by **Maxwell Rubert** as a showcase of beginner Python programming skills.

**Technologies Used:**
- Python & Flask
- HTML5 & CSS3
- Vanilla JavaScript
- Font Awesome Icons
- Google Fonts (Poppins)

---

*Happy coding! 🐍✨*
