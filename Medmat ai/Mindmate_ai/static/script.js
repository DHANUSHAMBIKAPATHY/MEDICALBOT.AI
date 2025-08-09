const micBtn = document.getElementById("mic-btn");
const chatBox = document.getElementById("chat-box");

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US';

micBtn.addEventListener("click", () => {
    recognition.start();
});

recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    addMessage("user", transcript);
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: transcript })
    })
    .then(res => res.json())
    .then(data => {
        addMessage("bot", data.reply);
        speak(data.reply);
    });
};

function addMessage(role, text) {
    const div = document.createElement("div");
    div.className = role;
    div.textContent = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.voice = window.speechSynthesis.getVoices().find(v => v.lang === 'en-US');
    window.speechSynthesis.speak(utterance);
}
