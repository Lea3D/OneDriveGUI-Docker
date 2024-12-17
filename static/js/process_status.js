document.addEventListener("DOMContentLoaded", () => {
    const statusList = document.getElementById("status-list");
    const refreshButton = document.getElementById("refreshStatus");
    const clearButton = document.getElementById("clearStatus");

    // Function to fetch and populate the status list
    function fetchStatusList() {
        fetch("/api/process/status")
            .then(response => response.json())
            .then(data => {
                statusList.innerHTML = ""; // Clear current content
                data.forEach(status => {
                    const statusItem = document.createElement("div");
                    statusItem.textContent = `${status.timestamp}: ${status.message}`;
                    statusList.appendChild(statusItem);
                });
            })
            .catch(error => {
                console.error("Error fetching status list:", error);
            });
    }

    // Function to clear the status list on the server
    function clearStatusList() {
        fetch("/api/process/status", {
            method: "DELETE",
        })
            .then(response => {
                if (response.ok) {
                    statusList.innerHTML = "";
                    alert("Status list cleared successfully.");
                } else {
                    alert("Failed to clear status list.");
                }
            })
            .catch(error => {
                console.error("Error clearing status list:", error);
            });
    }

    // Event listeners
    refreshButton.addEventListener("click", fetchStatusList);
    clearButton.addEventListener("click", clearStatusList);

    // Initialize the page with current status
    fetchStatusList();
});
