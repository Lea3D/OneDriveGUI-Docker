document.addEventListener("DOMContentLoaded", () => {
    const loginFrame = document.getElementById("loginFrame");

    // Set the login URL for the iframe
    loginFrame.src = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=d50ca740-c83f-4d1b-b616" +
        "-12c519384f0c&scope=Files.ReadWrite%20Files.ReadWrite.all%20Sites.Read.All%20Sites.ReadWrite.All" +
        "%20offline_access&response_type=code&prompt=login&redirect_uri=https://login.microsoftonline.com" +
        "/common/oauth2/nativeclient";

    // Add event listeners or additional logic if needed for handling iframe interaction
});
