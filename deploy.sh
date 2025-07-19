#!/bin/bash

# Python Projects Portfolio - Deployment Script
# This script helps prepare and deploy the portfolio to various platforms

echo "🚀 Python Projects Portfolio - Deployment Helper"
echo "================================================="

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "✅ Checking prerequisites..."

if ! command_exists python; then
    echo "❌ Python is not installed. Please install Python 3.9+ first."
    exit 1
fi

if ! command_exists git; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

echo "✅ All prerequisites met!"

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run tests
echo "🧪 Testing application..."
python -c "
import app
print('✅ App imports successfully')
"

# Check file structure
echo "📁 Verifying file structure..."
required_files=(
    "app.py"
    "requirements.txt" 
    "vercel.json"
    "templates/base.html"
    "templates/index.html"
    "templates/project.html"
    "static/css/style.css"
    "static/js/main.js"
)

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ Missing: $file"
    fi
done

echo ""
echo "🎯 Deployment Options:"
echo "======================"
echo ""
echo "1. 🟢 Vercel (Recommended - Free)"
echo "   - Visit: https://vercel.com"
echo "   - Connect GitHub repository"
echo "   - Auto-deploy on push"
echo ""
echo "2. 🔵 Heroku"
echo "   - Install Heroku CLI"
echo "   - heroku create your-app-name"
echo "   - git push heroku main"
echo ""
echo "3. 🟡 Railway"
echo "   - Visit: https://railway.app"
echo "   - Connect GitHub repository"
echo "   - One-click deployment"
echo ""
echo "4. 🟠 PythonAnywhere"
echo "   - Upload files via web interface"
echo "   - Configure WSGI app"
echo ""

echo "📋 Pre-deployment Checklist:"
echo "============================"
echo "□ All Python files in my-python-codes/ directory"
echo "□ All demo templates created and working"
echo "□ Static files (CSS, JS) optimized"
echo "□ Requirements.txt updated"
echo "□ vercel.json configured"
echo "□ README.md complete"
echo "□ .gitignore file present"
echo "□ Local testing successful"
echo ""

echo "🔗 Next Steps:"
echo "==============="
echo "1. Push code to GitHub repository"
echo "2. Connect to Vercel for automatic deployment"
echo "3. Update README.md with live URL"
echo "4. Share your amazing portfolio!"
echo ""

echo "✨ Happy Deploying! ✨"
