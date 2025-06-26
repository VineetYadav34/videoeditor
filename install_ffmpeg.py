#!/usr/bin/env python3
"""
FFmpeg installer for Windows
"""

import os
import sys
import urllib.request
import zipfile
import subprocess
from pathlib import Path

def download_ffmpeg():
    """Download FFmpeg for Windows"""
    print("🎬 Installing FFmpeg for Windows...")
    
    # FFmpeg download URL (static build)
    ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    
    # Create temp directory
    temp_dir = Path("temp_ffmpeg")
    temp_dir.mkdir(exist_ok=True)
    
    zip_path = temp_dir / "ffmpeg.zip"
    
    try:
        print("📥 Downloading FFmpeg...")
        urllib.request.urlretrieve(ffmpeg_url, zip_path)
        
        print("📦 Extracting FFmpeg...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        # Find the extracted folder
        extracted_folders = [f for f in temp_dir.iterdir() if f.is_dir() and f.name.startswith("ffmpeg")]
        if not extracted_folders:
            print("❌ Could not find extracted FFmpeg folder")
            return False
        
        ffmpeg_folder = extracted_folders[0]
        bin_folder = ffmpeg_folder / "bin"
        
        if not bin_folder.exists():
            print("❌ Could not find FFmpeg bin folder")
            return False
        
        # Copy to a permanent location
        install_dir = Path("C:/ffmpeg")
        if install_dir.exists():
            print("⚠️  FFmpeg already exists at C:/ffmpeg")
        else:
            print(f"📁 Installing to {install_dir}")
            import shutil
            shutil.copytree(ffmpeg_folder, install_dir)
        
        # Test FFmpeg
        ffmpeg_exe = install_dir / "bin" / "ffmpeg.exe"
        if ffmpeg_exe.exists():
            print("✅ FFmpeg installed successfully!")
            print(f"📍 Location: {install_dir}")
            print(f"🔧 Executable: {ffmpeg_exe}")
            print("\n📋 Next steps:")
            print("1. Add C:\\ffmpeg\\bin to your PATH environment variable")
            print("2. Restart your terminal")
            print("3. Test with: ffmpeg -version")
            return True
        else:
            print("❌ FFmpeg executable not found")
            return False
            
    except Exception as e:
        print(f"❌ Error installing FFmpeg: {e}")
        return False
    finally:
        # Cleanup
        if temp_dir.exists():
            import shutil
            shutil.rmtree(temp_dir)

def add_to_path():
    """Add FFmpeg to PATH (requires admin privileges)"""
    print("\n🔧 Adding FFmpeg to PATH...")
    print("⚠️  This requires administrator privileges")
    
    try:
        # Use PowerShell to add to PATH
        cmd = [
            "powershell", "-Command",
            "[Environment]::SetEnvironmentVariable('Path', $env:Path + ';C:\\ffmpeg\\bin', 'User')"
        ]
        subprocess.run(cmd, check=True)
        print("✅ Added FFmpeg to PATH")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to add to PATH (try running as administrator)")
        return False

def main():
    """Main installation function"""
    print("🎬 FFmpeg Installer for Intelligent Video Editor")
    print("=" * 50)
    
    # Check if FFmpeg is already installed
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ FFmpeg is already installed and working!")
            return True
    except FileNotFoundError:
        pass
    
    # Install FFmpeg
    if download_ffmpeg():
        # Try to add to PATH
        if add_to_path():
            print("\n🎉 FFmpeg installation complete!")
            print("🔄 Please restart your terminal and test with: ffmpeg -version")
        else:
            print("\n⚠️  Please manually add C:\\ffmpeg\\bin to your PATH")
    else:
        print("\n❌ FFmpeg installation failed")
        print("💡 Manual installation:")
        print("1. Download from: https://ffmpeg.org/download.html")
        print("2. Extract to C:\\ffmpeg")
        print("3. Add C:\\ffmpeg\\bin to PATH")

if __name__ == "__main__":
    main() 