#!/usr/bin/env python3
"""
Test script to verify installation of Intelligent Video Editor
"""

import sys
import importlib

def test_import(module_name, package_name=None):
    """Test if a module can be imported"""
    try:
        if package_name:
            importlib.import_module(package_name)
        else:
            importlib.import_module(module_name)
        print(f"✅ {module_name}")
        return True
    except ImportError as e:
        print(f"❌ {module_name}: {e}")
        return False
    except Exception as e:
        print(f"⚠️ {module_name}: {e}")
        return False

def main():
    """Test all required dependencies"""
    print("🔍 Testing Intelligent Video Editor Installation")
    print("=" * 50)
    
    # Core dependencies
    dependencies = [
        ("opencv-python", "cv2"),
        ("numpy", "numpy"),
        ("moviepy", "moviepy"),
        ("librosa", "librosa"),
        ("pydub", "pydub"),
        ("scenedetect", "scenedetect"),
        ("streamlit", "streamlit"),
        ("pillow", "PIL"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("scikit-learn", "sklearn"),
        ("tqdm", "tqdm"),
    ]
    
    print("\n📦 Testing Core Dependencies:")
    failed_imports = []
    
    for package, module in dependencies:
        if not test_import(module, package):
            failed_imports.append(package)
    
    # Test our custom modules
    print("\n🔧 Testing Custom Modules:")
    custom_modules = [
        "core.scene_detector",
        "core.audio_processor", 
        "core.music_sync",
        "core.color_grading",
        "core.video_exporter",
        "utils.file_utils",
        "utils.video_utils"
    ]
    
    for module in custom_modules:
        if not test_import(module):
            failed_imports.append(module)
    
    # Summary
    print("\n" + "=" * 50)
    if failed_imports:
        print(f"❌ Installation incomplete. Failed imports: {len(failed_imports)}")
        print("Missing packages:")
        for package in failed_imports:
            print(f"  - {package}")
        print("\n💡 To install missing packages, run:")
        print("   pip install -r requirements.txt")
        return False
    else:
        print("✅ All dependencies installed successfully!")
        print("\n🚀 You can now run the application with:")
        print("   streamlit run app.py")
        return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 