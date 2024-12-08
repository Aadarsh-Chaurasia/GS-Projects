    const form = document.getElementById("contactForm");
    const nameInput = document.getElementById("name");
    const emailInput = document.getElementById("email");
    const messageInput = document.getElementById("message-box");
    const submitButton = document.getElementById("submit");
    const successMessage = document.getElementById("successMessage");

    // Functions for Validation.
    const isAlphabetic = (text) => /^[a-zA-Z\s]+$/.test(text);
    const isValidEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

    const validateForm = () => {
        const isNameValid = isAlphabetic(nameInput.value.trim());
        const isEmailValid = isValidEmail(emailInput.value.trim());
        const isMessageValid = messageInput.value.trim().length >= 10;

        // Enable disable submit button if response is valid.
        submitButton.disabled = !(isNameValid && isEmailValid && isMessageValid);

        return isNameValid && isEmailValid && isMessageValid;
    };

    const resetForm = () => {
        form.reset();
        submitButton.disabled = true;
    };

    // Event Listeners
    [nameInput, emailInput, messageInput].forEach((input) => {
        input.addEventListener("input", validateForm);
    });

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        if (validateForm()) {
            successMessage.textContent = "Form submitted successfully!";
            successMessage.style.color = "green";
            resetForm();
        } else {
            // Incase user forcefull enables submit button.
            successMessage.textContent = "Please correct the errors before submitting.";
            successMessage.style.color = "red";
        }
    });

    // Initial state
    submitButton.disabled = true;