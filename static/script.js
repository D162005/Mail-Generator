// script.js

function toggleGenerateFrom() {
    var toggleButton = document.getElementById("toggleButton");
    var toggleText = document.getElementById("toggleText");

    if (toggleButton.checked) {
        toggleText.textContent = "Generate from Database";
    } else {
        toggleText.textContent = "Generate from main.py";
    }
}

document.getElementById("toggleButton").addEventListener("change", toggleGenerateFrom);

function generateEmail() {
    var topic = document.getElementById("topic").value;
    var useDatabase = document.getElementById("toggleButton").checked;

    // Show loading message
    document.getElementById("emailContent").value = "Generating mail template...";

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic: topic, use_database: useDatabase }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            document.getElementById("emailContent").value = data.error;
        } else {
            // Set the mail content to the textarea
            document.getElementById("emailContent").value = data.mail_content;
            alert("Mail template generated and stored in database!");
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById("emailContent").value = "Error generating mail template. Please try again.";
    });
}


function copyToClipboard() {
    var emailContent = document.getElementById("emailContent");
    emailContent.select();
    document.execCommand("copy");
    alert("Email content copied to clipboard!");
}

function clearAll() {
    document.getElementById("topic").value = "";
    document.getElementById("emailContent").value = "";
    document.getElementById("notification").innerText = "";
}

function showNotification(message) {
    var notification = document.getElementById("notification");
    notification.innerText = message;
    notification.style.display = "block";

    // Hide notification after 3 seconds
    setTimeout(function() {
        notification.style.display = "none";
    }, 3000);
}

document.getElementById("generateButton").addEventListener("click", generateEmail);
document.getElementById("copyButton").addEventListener("click", copyToClipboard);
document.getElementById("clearButton").addEventListener("click", clearAll); 