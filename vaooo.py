from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        lover_name = request.form.get("lover_name", "").strip()
        
        if name.lower() == "vaooo" and lover_name.lower() == "nike":
            return render_template("countdown.html")
        else:
            return render_template("index.html", error=True)
    
    return render_template("index.html", error=False)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)