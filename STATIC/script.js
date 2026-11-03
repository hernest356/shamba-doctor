function sendMessage() {
    const input = document.getElementById("message");
    const message = input.value.trim();

    if (message === "") {
        return;
    }

    const chatBox = document.getElementById("chat-box");

    // Display farmer's message
    const userMessage = document.createElement("div");
    userMessage.className = "message user";

    userMessage.innerHTML = `
        <strong>👨‍🌾 You:</strong>
        <p>${message}</p>
    `;

    chatBox.appendChild(userMessage);

    // Send message to Python
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {

        // Display Shamba Doctor's response
        const botMessage = document.createElement("div");
        botMessage.className = "message bot";

        botMessage.innerHTML = `
            <strong>🤖 Shamba Doctor:</strong>
            <p>${data.response}</p>
        `;

        chatBox.appendChild(botMessage);

        // Scroll to latest message
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    // Clear input
    input.value = "";
}