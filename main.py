# नेत्र-कवच मुख्य इंजन - जादुई डायरी लॉजिक
import re

def netra_analyzer(message):
    scam_patterns = {
        "डर (Fear)": [r"बिजली काट", r"अकाउंट बंद", r"पुलिस", r"कोर्ट", r"जेल"],
        "लालच (Greed)": [r"लॉटरी", r"जीता है", r"इनाम", r"मुफ्त", r"कैशबैक"],
        "जल्दबाजी (Urgency)": [r"अभी करें", r"तुरंत", r"आज रात", r"अंतिम चेतावनी"]
    }
    
    risk_score = 0
    found = []
    for emotion, keywords in scam_patterns.items():
        for pattern in keywords:
            if re.search(pattern, message):
                found.append(emotion)
                risk_score += 33

    print(f"नेत्र-कवच रिपोर्ट: {found} पहचानें गए। रिस्क स्कोर: {risk_score}%")
    return risk_score

# टेस्ट रन
netra_analyzer("बधाई हो! आपने लॉटरी जीती है, तुरंत संपर्क करें।")
