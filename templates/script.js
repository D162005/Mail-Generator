function generateEmail() {
    var topic = document.getElementById("topic").value;
    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic: topic }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            document.getElementById("emailContent").innerText = data.error;
        } else {
            document.getElementById("emailContent").innerText = data.mail_content;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function copyToClipboard() {
    var emailContent = document.getElementById("emailContent");
    emailContent.select();
    document.execCommand("copy");
    alert("Email content copied to clipboard!");
}

document.getElementById("generateButton").addEventListener("click", generateEmail);
document.getElementById("copyButton").addEventListener("click", copyToClipboard);
