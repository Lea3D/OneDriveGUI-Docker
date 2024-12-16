document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("import-profile-form");
    const statusMessage = document.getElementById("status-message");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const profileName = document.getElementById("profile-name").value;
        const configPath = document.getElementById("config-path").value;

        try {
            const response = await fetch("/api/profile/import", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    profile_name: profileName,
                    config_path: configPath,
                }),
            });

            if (response.ok) {
                const result = await response.json();
                statusMessage.textContent = result.message;
                statusMessage.style.color = "green";
                form.reset();
            } else {
                const error = await response.json();
                statusMessage.textContent = error.message || "Failed to import profile.";
                statusMessage.style.color = "red";
            }
        } catch (error) {
            statusMessage.textContent = "An error occurred while importing the profile.";
            statusMessage.style.color = "red";
            console.error(error);
        }
    });

    form.addEventListener("reset", () => {
        statusMessage.textContent = "";
    });
});
