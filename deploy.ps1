# Python Projects Portfolio - Deployment Script (PowerShell)
# This script helps prepare and deploy the portfolio to various platforms

Write-Host "🚀 Python Projects Portfolio - Deployment Helper" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan

# Function to check if command exists
function Test-CommandExists($command) {
    $null = Get-Command $command -ErrorAction SilentlyContinue
    return $?
}

# Check prerequisites
Write-Host "✅ Checking prerequisites..." -ForegroundColor Green

if (-not (Test-CommandExists "python")) {
    Write-Host "❌ Python is not installed. Please install Python 3.9+ first." -ForegroundColor Red
    exit 1
}

if (-not (Test-CommandExists "git")) {
    Write-Host "❌ Git is not installed. Please install Git first." -ForegroundColor Red
    exit 1
}

Write-Host "✅ All prerequisites met!" -ForegroundColor Green

# Install dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Run tests
Write-Host "🧪 Testing application..." -ForegroundColor Yellow
python -c "import app; print('✅ App imports successfully')"

# Check file structure
Write-Host "📁 Verifying file structure..." -ForegroundColor Yellow
$requiredFiles = @(
    "app.py",
    "requirements.txt", 
    "vercel.json",
    "templates/base.html",
    "templates/index.html", 
    "templates/project.html",
    "static/css/style.css",
    "static/js/main.js"
)

foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "✅ $file" -ForegroundColor Green
    } else {
        Write-Host "❌ Missing: $file" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "🎯 Deployment Options:" -ForegroundColor Cyan
Write-Host "======================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. 🟢 Vercel (Recommended - Free)" -ForegroundColor Green
Write-Host "   - Visit: https://vercel.com"
Write-Host "   - Connect GitHub repository"
Write-Host "   - Auto-deploy on push"
Write-Host ""
Write-Host "2. 🔵 Heroku" -ForegroundColor Blue
Write-Host "   - Install Heroku CLI"
Write-Host "   - heroku create your-app-name"
Write-Host "   - git push heroku main"
Write-Host ""
Write-Host "3. 🟡 Railway" -ForegroundColor Yellow
Write-Host "   - Visit: https://railway.app"
Write-Host "   - Connect GitHub repository" 
Write-Host "   - One-click deployment"
Write-Host ""
Write-Host "4. 🟠 PythonAnywhere" -ForegroundColor DarkYellow
Write-Host "   - Upload files via web interface"
Write-Host "   - Configure WSGI app"
Write-Host ""

Write-Host "📋 Pre-deployment Checklist:" -ForegroundColor Cyan
Write-Host "============================" -ForegroundColor Cyan
Write-Host "□ All Python files in my-python-codes/ directory"
Write-Host "□ All demo templates created and working"
Write-Host "□ Static files (CSS, JS) optimized" 
Write-Host "□ Requirements.txt updated"
Write-Host "□ vercel.json configured"
Write-Host "□ README.md complete"
Write-Host "□ .gitignore file present"
Write-Host "□ Local testing successful"
Write-Host ""

Write-Host "🔗 Next Steps:" -ForegroundColor Cyan
Write-Host "===============" -ForegroundColor Cyan
Write-Host "1. Push code to GitHub repository"
Write-Host "2. Connect to Vercel for automatic deployment"
Write-Host "3. Update README.md with live URL"
Write-Host "4. Share your amazing portfolio!"
Write-Host ""

Write-Host "Happy Deploying!" -ForegroundColor Magenta
