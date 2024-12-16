document.addEventListener("DOMContentLoaded", () => {
    const profileSelect = document.getElementById("profileSelect");
    const createProfileBtn = document.getElementById("createProfileBtn");

    // Fetch profiles dynamically from the API and populate the dropdown
    fetch("/api/profile/list")
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to fetch profiles");
            }
            return response.json();
        })
        .then(data => {
            profileSelect.innerHTML = ""; // Clear existing options
            data.profiles.forEach(profile => {
                const option = document.createElement("option");
                option.value = profile.id;
                option.textContent = profile.name;
                profileSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error("Error fetching profiles:", error);
            alert("Unable to fetch profiles. Please try again later.");
        });

    // Add event listener to the Create/Import button
    createProfileBtn.addEventListener("click", () => {
        window.location.href = "/create-profile"; // Redirect to profile creation page
    });

    // Add event listener to profile selection change
    profileSelect.addEventListener("change", () => {
        const selectedProfile = profileSelect.value;
        console.log(`Selected profile ID: ${selectedProfile}`);

        // Perform an action based on the selected profile
        // For example, navigate to the profile details page
        window.location.href = `/profile/${selectedProfile}`;
    });
});
