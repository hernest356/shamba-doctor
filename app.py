from flask import Flask, render_template, request, jsonify
from database import get_crop

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower().strip()

    # Greetings
    if "hello" in message or "hi" in message:
        response = (
            "Hello farmer! 👋 Welcome to Shamba Doctor. "
            "How can I help you today?"
        )

    # Check crops in the database
    elif "maize" in message or "corn" in message:
        crop = get_crop("Maize")

        if crop:
            response = (
                f"🌽 {crop['crop_name']}\n\n"
                f"{crop['description']}\n\n"
                f"🌱 Planting information:\n"
                f"{crop['planting_info']}\n\n"
                f"🌍 Soil requirements:\n"
                f"{crop['soil_requirements']}\n\n"
                f"🐛 Common pests:\n"
                f"{crop['common_pests']}\n\n"
                f"🦠 Common diseases:\n"
                f"{crop['common_diseases']}\n\n"
                f"💡 Management tips:\n"
                f"{crop['management_tips']}"
            )
        else:
            response = "Sorry, I don't have maize information yet."

    elif "tomato" in message:
        crop = get_crop("Tomato")

        if crop:
            response = (
                f"🍅 {crop['crop_name']}\n\n"
                f"{crop['description']}\n\n"
                f"🌱 Planting information:\n"
                f"{crop['planting_info']}\n\n"
                f"🌍 Soil requirements:\n"
                f"{crop['soil_requirements']}\n\n"
                f"🐛 Common pests:\n"
                f"{crop['common_pests']}\n\n"
                f"🦠 Common diseases:\n"
                f"{crop['common_diseases']}\n\n"
                f"💡 Management tips:\n"
                f"{crop['management_tips']}"
            )
        else:
            response = "Sorry, I don't have tomato information yet."

    elif "bean" in message or "beans" in message:
        crop = get_crop("Beans")

        if crop:
            response = (
                f"🫘 {crop['crop_name']}\n\n"
                f"{crop['description']}\n\n"
                f"🌱 Planting information:\n"
                f"{crop['planting_info']}\n\n"
                f"🌍 Soil requirements:\n"
                f"{crop['soil_requirements']}\n\n"
                f"🐛 Common pests:\n"
                f"{crop['common_pests']}\n\n"
                f"🦠 Common diseases:\n"
                f"{crop['common_diseases']}\n\n"
                f"💡 Management tips:\n"
                f"{crop['management_tips']}"
            )
        else:
            response = "Sorry, I don't have beans information yet."

    # Livestock
    elif "cow" in message or "cattle" in message:
        response = (
            "🐄 I can help with cattle problems. "
            "Tell me the symptoms you have noticed, "
            "such as coughing, diarrhea, loss of appetite, "
            "fever, or difficulty walking."
        )

    # Fertilizer and manure
    elif "fertilizer" in message or "manure" in message:
        response = (
            "🌱 I can help with fertilizers and manure. "
            "Tell me which crop you are growing."
        )

    # General response
    else:
        response = (
            "I am Shamba Doctor 🌱. Tell me about your "
            "crop, livestock, pest, soil, fertilizer, "
            "or farming problem."
        )

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)