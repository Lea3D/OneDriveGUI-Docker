document.addEventListener("DOMContentLoaded", () => {
    const profileSettingsForm = document.getElementById("profileSettingsForm");
    const profileNameInput = document.getElementById("profileName");
    const syncDirInput = document.getElementById("syncDir");
    const monitorIntervalInput = document.getElementById("monitorInterval");
    const autoSyncCheckbox = document.getElementById("autoSync");
    const saveButton = document.getElementById("saveProfileSettings");
    const discardButton = document.getElementById("discardProfileSettings");
    const browseSyncDirButton = document.getElementById("browseSyncDir");

    // Fetch and populate profile settings
    function fetchProfileSettings() {
        fetch("/api/profile/settings")
            .then(response => response.json())
            .then(data => {
                profileNameInput.value = data.profileName || "";
                syncDirInput.value = data.syncDir || "";
                monitorIntervalInput.value = data.monitorInterval || 1;
                autoSyncCheckbox.checked = data.autoSync || false;
            })
            .catch(error => {
                console.error("Error fetching profile settings:", error);
            });
    }

    // Save profile settings
    saveButton.addEventListener("click", (e) => {
        e.preventDefault();

        const settings = {
            profileName: profileNameInput.value,
            syncDir: syncDirInput.value,
            monitorInterval: monitorIntervalInput.value,
            autoSync: autoSyncCheckbox.checked,
        };

        fetch("/api/profile/settings", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(settings),
        })
            .then(response => {
                if (response.ok) {
                    alert("Settings saved successfully.");
                } else {
                    alert("Failed to save settings.");
                }
            })
            .catch(error => {
                console.error("Error saving profile settings:", error);
            });
    });

    // Discard changes
    discardButton.addEventListener("click", (e) => {
        e.preventDefault();
        fetchProfileSettings();
    });

    // Browse for sync directory
    browseSyncDirButton.addEventListener("click", () => {
        // Implement file dialog integration if backend supports it
        alert("Browse functionality not implemented.");
    });

    // Initialize the form with current settings
    fetchProfileSettings();
});
