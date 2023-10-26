import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS


api = Flask(__name__)
CORS(api)

@api.route('/hello', methods=['GET'])
def hello():
    openai.api_key = ('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')
    user_query = request.args.get('userQuery')
   
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    answer = completion.choices[0].message.content
    return (answer)
if __name__ == '__main__':
    api.run()