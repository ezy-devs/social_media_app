document.getElementById('send-message-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const receiver_id = document.getElementById('receiver-id').value;
    const content = document.getElementById('content').value;

    fetch('/send-message/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify({
            receiver_id: receiver_id,
            content: content
        })

    }).then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Message Sent!');
        }
    });
});

setInterval(() => {
    fetch('/get-messages/')
    .then(data => {
        data.messages.forEach(msg => {
            displayMessage(msg);
        });
    });
}, 3000);

function displayMessage(messages) {
    const chatbox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div')
    messageDiv.textContent = '${message.sender}: ${message.content}';
    chatbox.appendChild(messageDiv);
}