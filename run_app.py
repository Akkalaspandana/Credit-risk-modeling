#!/usr/bin/env python3
"""
Credit Risk Modeling Application Launcher
This script helps you run the Streamlit application from the project root.
"""

import os
import sys
import subprocess

def main():
    """Launch the Streamlit application."""
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(script_dir, "project-root")
    
    # Check if project-root directory exists
    if not os.path.exists(project_root):
        print("❌ Error: project-root directory not found!")
        print("Please ensure you're running this from the correct location.")
        sys.exit(1)
    
    # Check if main.py exists
    main_py = os.path.join(project_root, "main.py")
    if not os.path.exists(main_py):
        print("❌ Error: main.py not found in project-root directory!")
        sys.exit(1)
    
    # Check if requirements.txt exists
    requirements = os.path.join(project_root, "requirements.txt")
    if not os.path.exists(requirements):
        print("❌ Error: requirements.txt not found in project-root directory!")
        sys.exit(1)
    
    print("🚀 Starting Credit Risk Modeling Application...")
    print("📁 Working directory:", project_root)
    print("🌐 The app will open in your default browser")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        # Change to project-root directory and run streamlit
        os.chdir(project_root)
        subprocess.run([sys.executable, "-m", "streamlit", "run", "main.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running application: {e}")
        print("💡 Make sure you have installed all requirements:")
        print("   pip install -r project-root/requirements.txt")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
