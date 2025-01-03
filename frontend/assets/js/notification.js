socket.on('new_notification', function(notification) {
    const notificationsDiv = document.getElementById('notifications');
    notificationsDiv.innerHTML += `<p>${notification.message}</p>`;
});
