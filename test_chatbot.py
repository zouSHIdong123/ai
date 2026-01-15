#!/usr/bin/env python3
"""
Test script to demonstrate the chatbot functionality
"""

from chatbot import MoonshotChatbot
import os

def test_without_api():
    """Test the chatbot structure without making actual API calls"""
    print("Testing chatbot structure...")
    
    # Temporarily set a fake API key for initialization
    original_key = os.environ.get('MOONSHOT_API_KEY')
    os.environ['MOONSHOT_API_KEY'] = 'fake_key_for_test'
    
    try:
        bot = MoonshotChatbot()
        print("✓ Chatbot initialized successfully")
        
        # Show initial history
        print(f"✓ Initial history length: {len(bot.get_history())}")
        
        # Test reset functionality
        bot.reset_conversation()
        print(f"✓ After reset history length: {len(bot.get_history())}")
        
        print("\nAll tests passed! The chatbot structure is working correctly.")
        
    except Exception as e:
        print(f"✗ Error during testing: {e}")
    
    finally:
        # Restore original environment
        if original_key is not None:
            os.environ['MOONSHOT_API_KEY'] = original_key
        else:
            del os.environ['MOONSHOT_API_KEY']

def demo_usage():
    """Demonstrate how to use the chatbot"""
    print("\n" + "="*50)
    print("DEMONSTRATION OF CHATBOT USAGE")
    print("="*50)
    print("""
1. Basic usage:
   ```python
   from chatbot import MoonshotChatbot
   
   bot = MoonshotChatbot()  # Uses MOONSHOT_API_KEY env var
   response = bot.chat("Hello!")
   print(response)
   ```

2. With explicit API key:
   ```python
   bot = MoonshotChatbot(api_key="your-api-key-here")
   ```

3. Reset conversation:
   ```python
   bot.reset_conversation()
   ```

4. Run interactive mode:
   ```bash
   python chatbot.py
   ```
    """)

if __name__ == "__main__":
    test_without_api()
    demo_usage()