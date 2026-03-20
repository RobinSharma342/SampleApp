
function copyCode(sectionID) {
    // Get the code block
    const codeBlock = document.getElementById(sectionID);
    
    // Create a temporary text area to hold the code
    const textArea = document.createElement("textarea");
    textArea.value = codeBlock.textContent;
    document.body.appendChild(textArea);
    
    // Select and copy the text
    textArea.select();
    document.execCommand("copy");
    
    // Remove the temporary text area
    document.body.removeChild(textArea);
    
    // Provide feedback to the user
    showNotification("Copied to clipboard!");
}

function showNotification(message) {
    const notification = document.getElementById('notification');
    notification.textContent = message; // Set the message
    notification.style.display = 'block'; // Show the notification

    // Hide the notification after 3 seconds
    setTimeout(() => {
        notification.style.display = 'none';
    }, 900);
}