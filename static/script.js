
async function sendMessage() {
    const input = document.getElementById("messageInput");
    const messages = document.getElementById("messages");
    const userMessage = input.value;

    if (!userMessage) return;

    // Append user message to the chat
    const userDiv = document.createElement("div");
    userDiv.textContent = `You: ${userMessage}`;
    messages.appendChild(userDiv);

    // Send message to the Flask API
    const response = await fetch("/send_message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage }),
    });

    const data = await response.json();

    // Append AI response to the chat
    const aiDiv = document.createElement("div");
    if (data.response) {
        aiDiv.textContent = `AI: ${data.response}`;
    } else {
        aiDiv.textContent = `Error: ${data.error}`;
    }
    messages.appendChild(aiDiv);

    // Clear the input field
    input.value = "";
    messages.scrollTop = messages.scrollHeight;
}