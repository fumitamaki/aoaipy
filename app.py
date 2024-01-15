from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    data = request.json
    user_prompt = data['prompt']

    # Azure OpenAI Serviceとの通信
    response = requests.post(
        "https://aoaiedus.openai.azure.com/openai/deployments/gpt35edu/chat/completions?api-version=2023-03-15-preview",
        headers={
            "Content-Type": "application/json",
            "api-key": "2936c47122a34396b2d4559c2a94e4e9"
        },
        json={
            "messages": [
                {"role": "system", "content": "You are a helpful assistant, teaching people about AI."},
                {"role": "user", "content": user_prompt}
            ]
        }
    )

    ai_response = response.json()
    return jsonify({"response": ai_response['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run()
