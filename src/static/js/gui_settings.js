document.addEventListener("DOMContentLoaded", () => {
    const settingsForm = document.getElementById("settingsForm");

    // Load settings
    fetch("/api/gui-settings")
        .then(response => response.json())
        .then(data => {
            document.getElementById("startMinimized").checked = data.startMinimized === "True";
            document.getElementById("clientBinPath").value = data.clientBinPath || "";
            document.getElementById("framelessWindow").checked = data.framelessWindow === "True";
            document.getElementById("combinedStartStop").checked = data.combinedStartStop === "True";
            document.getElementById("qWebEngineLogin").checked = data.qWebEngineLogin === "True";
            document.getElementById("debugLevel").value = data.debugLevel || "DEBUG";
            document.getElementById("showDebug").checked = data.showDebug === "True";
            document.getElementById("saveDebug").checked = data.saveDebug === "True";
            document.getElementById("logFile").value = data.logFile || "";
            document.getElementById("logRotationInterval").value = data.logRotationInterval || 24;
            document.getElementById("logBackupCount").value = data.logBackupCount || 3;
        })
        .catch(error => console.error("Error loading settings:", error));

    // Save settings
    settingsForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const settings = {
            startMinimized: document.getElementById("startMinimized").checked ? "True" : "False",
            clientBinPath: document.getElementById("clientBinPath").value,
            framelessWindow: document.getElementById("framelessWindow").checked ? "True" : "False",
            combinedStartStop: document.getElementById("combinedStartStop").checked ? "True" : "False",
            qWebEngineLogin: document.getElementById("qWebEngineLogin").checked ? "True" : "False",
            debugLevel: document.getElementById("debugLevel").value,
            showDebug: document.getElementById("showDebug").checked ? "True" : "False",
            saveDebug: document.getElementById("saveDebug").checked ? "True" : "False",
            logFile: document.getElementById("logFile").value,
            logRotationInterval: document.getElementById("logRotationInterval").value,
            logBackupCount: document.getElementById("logBackupCount").value,
        };

        fetch("/api/gui-settings", {
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
            .catch(error => console.error("Error saving settings:", error));
    });

    // Browse buttons
    document.getElementById("browseClientBinPath").addEventListener("click", () => {
        alert("Browse functionality not implemented.");
    });

    document.getElementById("browseLogFile").addEventListener("click", () => {
        alert("Browse functionality not implemented.");
    });
});
