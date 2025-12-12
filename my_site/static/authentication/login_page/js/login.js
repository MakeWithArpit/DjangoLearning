// Toggle password visibility
function togglePassword() {
    const passwordInput = document.getElementById('password');
    const toggleBtn = document.getElementById('togglePassword');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.textContent = 'HIDE';
    } else {
        passwordInput.type = 'password';
        toggleBtn.textContent = 'SHOW';
    }
}

// Show error message
function showError(message) {
    const errorDiv = document.getElementById('errorMessage');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 4000);
}

// Show success message
function showSuccess(message) {
    const successDiv = document.getElementById('successMessage');
    successDiv.textContent = message;
    successDiv.style.display = 'block';
    setTimeout(() => {
        successDiv.style.display = 'none';
    }, 4000);
}

// Handle login form submission
function handleLogin(e) {
    e.preventDefault();
    
    const userId = document.getElementById('userId').value;
    const password = document.getElementById('password').value;
    const securityQuestion = document.getElementById('securityQuestion').value;
    const securityAnswer = document.getElementById('securityAnswer').value;

    // Validate all fields are filled
    if (!userId || !password || !securityQuestion || !securityAnswer) {
        showError('Please fill in all fields');
        return;
    }

    // Get users from localStorage
    const users = JSON.parse(localStorage.getItem('gpsUsers') || '[]');
    const user = users.find(u => u.userId === userId);

    // Check if user exists
    if (!user) {
        showError('User ID not found. Please register first.');
        return;
    }

    // Verify password
    if (user.password !== password) {
        showError('Incorrect password.');
        return;
    }

    // Verify security question and answer
    if (user.securityQuestion !== securityQuestion || 
        user.securityAnswer.toLowerCase() !== securityAnswer.toLowerCase()) {
        showError('Security question or answer is incorrect.');
        return;
    }

    // Login successful
    showSuccess('Login successful! Redirecting...');
    
    // Store current user in sessionStorage
    sessionStorage.setItem('currentUser', JSON.stringify(user));
    
    // Redirect after delay
    setTimeout(() => {
        alert('Login successful! Dashboard page coming soon.');
        // window.location.href = 'dashboard.html'; // Uncomment when dashboard is ready
    }, 1500);
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Toggle password button
    const toggleBtn = document.getElementById('togglePassword');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', togglePassword);
    }

    // Login form submission
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }
});