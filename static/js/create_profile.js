document.addEventListener("DOMContentLoaded", () => {
    const createProfileForm = document.getElementById("createProfileForm");
    const cancelBtn = document.getElementById("cancelBtn");

    createProfileForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const formData = new FormData(createProfileForm);
        const profileData = Object.fromEntries(formData.entries());
        profileData.autoSync = formData.has("autoSync");

        fetch("/api/profile/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(profileData),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to create profile");
                }
                return response.json();
            })
            .then(data => {
                alert("Profile created successfully!");
                window.location.href = `/profile/${data.profileId}`;
            })
            .catch(error => {
                console.error("Error creating profile:", error);
                alert("Unable to create profile. Please try again later.");
            });
    });

    cancelBtn.addEventListener("click", () => {
        window.location.href = "/"; // Redirect to main page
    });
});
