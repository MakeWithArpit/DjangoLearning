// script.js

// 1. Simple Form Validation & Alert
document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");
    
    forms.forEach(form => {
        form.addEventListener("submit", (e) => {
            e.preventDefault(); // Stop actual submission for demo
            
            // Basic validation check
            const inputs = form.querySelectorAll("input");
            let valid = true;
            
            inputs.forEach(input => {
                if(!input.value) {
                    valid = false;
                    input.style.borderColor = "red";
                } else {
                    input.style.borderColor = "#ccc";
                }
            });

            if(valid) {
                alert("Success! Form submitted (Demo Only).");
                form.reset();
            } else {
                alert("Please fill in all fields.");
            }
        });
    });
});