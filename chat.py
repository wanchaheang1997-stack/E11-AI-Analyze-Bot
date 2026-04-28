import requests

def ask():
    # នេះគឺជា "ខួរក្បាល" AI របស់បង
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyAzLxZohyBsJEORj54Qo8e-ZGsDMjOAbQ4"
    text = input("សួរមកបង: ")
    data = {"contents": [{"parts": [{"text": text}]}]}
    
    try:
        res = requests.post(url, json=data)
        answer = res.json()['candidates'][0]['content']['parts'][0]['text']
        print("\nAI ឆ្លើយថា: " + answer)
    except:
        print("\nមានបញ្ហា! សូមពិនិត្យអ៊ីនធឺណិត ឬ API Key។")

if __name__ == "__main__":
    ask()
