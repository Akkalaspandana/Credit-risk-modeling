# Deployment Guide

## 🚀 Quick Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/credit-risk-modeling.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Set the main file path to: `project-root/main.py`
   - Click "Deploy"

### Option 2: Heroku

1. **Create Procfile**:
   ```
   web: cd project-root && streamlit run main.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Create runtime.txt**:
   ```
   python-3.8.10
   ```

3. **Deploy**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Option 3: Docker

1. **Create Dockerfile**:
   ```dockerfile
   FROM python:3.8-slim
   WORKDIR /app
   COPY project-root/ .
   RUN pip install -r requirements.txt
   EXPOSE 8501
   CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]
   ```

2. **Build and run**:
   ```bash
   docker build -t credit-risk-app .
   docker run -p 8501:8501 credit-risk-app
   ```

## 🔧 Environment Variables

No environment variables are required for basic functionality.

## 📋 Pre-deployment Checklist

- [ ] All dependencies listed in requirements.txt
- [ ] Model files are present in model/ directory
- [ ] Image paths are correct
- [ ] No hardcoded paths
- [ ] Error handling implemented
- [ ] README.md updated
- [ ] .gitignore configured

## 🐛 Troubleshooting

### Common Issues

1. **Module not found errors**:
   - Ensure all dependencies are installed
   - Check Python version compatibility

2. **Model loading errors**:
   - Verify model_data.pkl exists
   - Check file permissions

3. **Image not displaying**:
   - Verify image file exists
   - Check relative path in main.py

### Support

For deployment issues, create an issue in the repository or contact the maintainers.
