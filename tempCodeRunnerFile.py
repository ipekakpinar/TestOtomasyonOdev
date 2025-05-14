from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_invalid_login():
    print("Tarayıcı başlatılıyor...")
    driver = webdriver.Chrome()

    print("Login sayfasına gidiliyor...")
    driver.get("https://the-internet.herokuapp.com/login")

    print("Kullanıcı adı ve şifre giriliyor...")
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    print("Hata mesajı kontrol ediliyor...")
    error_message = driver.find_element(By.ID, "flash").text
    if "Your username is invalid!" in error_message:
        print("✅ Test Başarılı: Hata mesajı göründü.")
    else:
        print("❌ Test Başarısız: Hata mesajı bulunamadı.")

    print("Ekran görüntüsü alınıyor...")
    driver.save_screenshot("test-sonucu.png")

    print("Tarayıcı kapatılıyor...")
    driver.quit()

test_invalid_login()
