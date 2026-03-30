# नेत्र-कवच सुरक्षा लेयर - AES-256 एन्क्रिप्शन
# निर्माता: नीरज जोशी पिथौरागढ़ (NEERAJ_JOSHI_PITHORAGARH_2026)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def protect_data(data, key):
    # की (Key) को 32 बाइट्स का सुनिश्चित करना
    key = key.encode('utf-8')[:32].ljust(32, b'\0')
    cipher = AES.new(key, AES.MODE_CBC)
    # डेटा को एन्क्रिप्ट करना
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return cipher.iv + ct_bytes

print("🛡️ जादुई डायरी: डेटा एन्क्रिप्शन मॉड्यूल सक्रिय।")
