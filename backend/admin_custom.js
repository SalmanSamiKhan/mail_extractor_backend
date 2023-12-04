// YourApp/static/admin/YourApp/admin_custom.js

function toggle_user_active(checkbox) {
    const userId = checkbox.getAttribute('data-id');
    const isActive = checkbox.checked;

    fetch(`/admin/backend/customuser/${userId}/change/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ is_active: isActive }),
    })
    .then(response => {
        if (!response.ok) {
            console.error('Error updating user status');
        }
    })
    .catch(error => {
        console.error('Error updating user status:', error);
    });
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
