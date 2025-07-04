#!/usr/bin/env python
"""
Quick test script to verify email generation works without user input
"""
import os
import sys
from datetime import datetime

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from email_ai.main import load_documents
from email_ai.crew import EmailAi

def test_email_generation():
    """Test the email generation functionality"""
    print("🧪 Testing email generation functionality...")
    
    # Load documents
    print("\n📁 Loading documents...")
    document_text = load_documents()
    
    if not document_text:
        print("❌ No documents loaded. Please check the knowledge folder.")
        return False
    
    print(f"✅ Documents loaded successfully")
    
    # Test email generation
    print("\n🤖 Testing email generation...")
    inputs = {
        'topic': 'Send a daily update to my manager',
        'document_text': document_text,
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = EmailAi().crew().kickoff(inputs=inputs)
        print(f"\n✅ Email generation test successful!")
        print(f"📄 Generated email saved to 'generated_email.md'")
        return True
    except Exception as e:
        print(f"\n❌ Email generation test failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_email_generation()
    if success:
        print("\n🎉 All tests passed! The email generation system is working correctly.")
    else:
        print("\n💥 Tests failed. Please check your setup.")
