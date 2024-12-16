document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("setup-wizard-form");
    const statusMessage = document.getElementById("status-message");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const accountEmail = document.getElementById("account-email").value;
        const syncDir = document.getElementById("sync-dir").value;
        const clientId = document.getElementById("client-id").value;
        const clientSecret = document.getElementById("client-secret").value;

        try {
            const response = await fetch("/api/setup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    account_email: accountEmail,
                    sync_dir: syncDir,
                    client_id: clientId,
                    client_secret: clientSecret,
                }),
            });

            if (response.ok) {
                const result = await response.json();
                statusMessage.textContent = result.message;
                statusMessage.style.color = "green";
                form.reset();
            } else {
                const error = await response.json();
                statusMessage.textContent = error.message || "Failed to complete setup.";
                statusMessage.style.color = "red";
            }
        } catch (error) {
            statusMessage.textContent = "An error occurred during the setup process.";
            statusMessage.style.color = "red";
            console.error(error);
        }
    });

    form.addEventListener("reset", () => {
        statusMessage.textContent = "";
    });
});
