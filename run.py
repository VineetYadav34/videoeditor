#!/usr/bin/env python3
"""
Quick start script for Intelligent Video Editor
"""

import os
import sys
import subprocess

def check_ffmpeg():
    """Check if FFmpeg is installed"""
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def main():
    """Main function to start the application"""
    print("🎬 Intelligent Video Editor")
    print("=" * 40)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # Check FFmpeg
    if not check_ffmpeg():
        print("⚠️  FFmpeg not found. Please install FFmpeg:")
        print("   Windows: Download from https://ffmpeg.org/download.html")
        print("   macOS: brew install ffmpeg")
        print("   Linux: sudo apt install ffmpeg")
        print("\nContinuing anyway...")
    else:
        print("✅ FFmpeg found")
    
    # Check if requirements are installed
    try:
        import streamlit
        print("✅ Dependencies found")
    except ImportError:
        print("❌ Dependencies not installed. Installing...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    
    # Start the application
    print("\n🚀 Starting Intelligent Video Editor...")
    print("📱 Open your browser to http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop")
    
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'app.py'])
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

if __name__ == "__main__":
    main() 