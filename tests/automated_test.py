from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

print("🧪 Starting BASIC Selenium Test...")

try:
    # Simple Chrome setup without extra options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    print("✅ Chrome started successfully!")
    
    # Test with a VERY reliable website
    print("🌐 Navigating to Wikipedia...")
    driver.get("https://www.wikipedia.org/")
    
    # Wait for page to load
    time.sleep(3)
    
    # Verify we're on Wikipedia
    if "Wikipedia" in driver.title:
        print("🎉 SUCCESS: Wikipedia loaded successfully!")
        print(f"📄 Page title: {driver.title}")
    else:
        print("❌ Failed to load Wikipedia")
    
    # Take screenshot as proof
    driver.save_screenshot("wikipedia_test.png")
    print("📸 Screenshot saved: wikipedia_test.png")
    
    # Keep browser open
    print("⏳ Test completed! Browser will close in 5 seconds...")
    time.sleep(5)
    
except Exception as e:
    print(f"❌ Error: {e}")
    
finally:
    driver.quit()
    print("🔚 Browser closed")