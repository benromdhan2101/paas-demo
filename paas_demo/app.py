from flask import Flask
app = Flask(__name__)

# ❌ Fake secret hardcoded (bad practice)
SECRET_KEY = "12345-FAKE-SECRET-LEAKED"

@app.route("/")
def home():
    print("Current secret:", SECRET_KEY)
    return "Hello from the PaaS Security Demo!"

if __name__ == "__main__":
    app.run()

