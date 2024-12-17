document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const statusMessage = document.getElementById('status-message');

    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const responseUrl = document.getElementById('response-url').value;

        if (!responseUrl.includes('nativeclient?code=')) {
            statusMessage.textContent = 'Invalid response URL. Please try again.';
            statusMessage.style.color = 'red';
            return;
        }

        try {
            statusMessage.textContent = 'Logging in...';
            statusMessage.style.color = 'blue';

            const response = await fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ response_url: responseUrl }),
            });

            const result = await response.json();

            if (response.ok) {
                statusMessage.textContent = 'Login successful!';
                statusMessage.style.color = 'green';
            } else {
                statusMessage.textContent = `Login failed: ${result.error}`;
                statusMessage.style.color = 'red';
            }
        } catch (error) {
            statusMessage.textContent = 'An error occurred. Please try again later.';
            statusMessage.style.color = 'red';
            console.error(error);
        }
    });
});
