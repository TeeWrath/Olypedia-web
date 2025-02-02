document.addEventListener("DOMContentLoaded", function () {
    var phoneInput = document.querySelector("#phone");

    if (phoneInput) {
        var iti = window.intlTelInput(phoneInput, {
            initialCountry: "us",  // Set default country to United States
            separateDialCode: true, // Display country code separately
            preferredCountries: ["us", "gb", "in"], // Add commonly used countries at top
            autoPlaceholder: "polite", // Show placeholder based on country selection
            utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js"
        });

        // Ensure the correct number format is sent on form submission
        var form = phoneInput.closest("form");
        if (form) {
            form.addEventListener("submit", function () {
                var hiddenInput = document.createElement("input");
                hiddenInput.type = "hidden";
                hiddenInput.name = "full_phone";
                hiddenInput.value = iti.getNumber(); // Get full phone number with country code
                form.appendChild(hiddenInput);
            });
        }
    }
});
