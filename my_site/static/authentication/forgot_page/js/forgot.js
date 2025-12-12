let currentUser = null;
let currentStep = 1;

function togglePassword(fieldId) {
    const passwordInput = document.getElementById(fieldId);
    const toggleBtn = event.target;
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.textContent = 'HIDE';
    } else {
        passwordInput.type = 'password';
        toggleBtn.textContent = 'SHOW';
    }
}

function showError(message) {
    const errorDiv = document.getElementById('errorMessage');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 4000);
}

function showSuccess(message) {
    const successDiv = document.getElementById('successMessage');
    successDiv.textContent = message;
    successDiv.style.display = 'block';
}

function goToStep(step) {
    document.querySelectorAll('.form-step').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.step').forEach(s => {
        s.classList.remove('active');
        s.classList.remove('completed');
    });

    document.getElementById(`step${step}`).classList.add('active');
    
    for (let i = 1; i <= 3; i++) {
        const indicator = document.getElementById(`step${i}Indicator`);
        if (i < step) {
            indicator.classList.add('completed');
        } else if (i === step) {
            indicator.classList.add('active');
        }
    }

    currentStep = step;
}

// Password strength meter
document.addEventListener('DOMContentLoaded', function() {
    const newPasswordInput = document.getElementById('newPassword');
    
    if (newPasswordInput) {
        newPasswordInput.addEventListener('input', function(e) {
            const password = e.target.value;
            let strength = 0;

            if (password.length >= 8) strength += 20;
            if (/[A-Z]/.test(password)) strength += 20;
            if (/[a-z]/.test(password)) strength += 20;
            if (/[0-9]/.test(password)) strength += 20;
            if (/[!@#$%^&*]/.test(password)) strength += 20;

            const meter = document.getElementById('strengthMeter');
            meter.style.width = strength + '%';
            
            if (strength < 40) {
                meter.style.background = '#ff3333';
            } else if (strength < 80) {
                meter.style.background = '#ffaa00';
            } else {
                meter.style.background = '#33ff33';
            }
        });
    }
});

// Step 1: Verify User ID
document.getElementById('step1Form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const userId = document.getElementById('userId').value;
    const users = JSON.parse(localStorage.getItem('gpsUsers') || '[]');
    const user = users.find(u => u.userId === userId);

    if (!user) {
        showError('User ID not found. Please check and try again.');
        return;
    }

    currentUser = user;

    const questionSelect = document.getElementById('securityQuestion');
    const questions = {
        'pet': "What is your pet's name?",
        'city': "In what city were you born?",
        'school': "What is your school's name?",
        'mother': "What is your mother's maiden name?",
        'color': "What is your favorite color?"
    };

    questionSelect.innerHTML = `<option value="${user.securityQuestion}">${questions[user.securityQuestion]}</option>`;
    
    goToStep(2);
});

// Step 2: Verify Security Question
document.getElementById('step2Form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const answer = document.getElementById('securityAnswer').value;

    if (answer.toLowerCase() !== currentUser.securityAnswer.toLowerCase()) {
        showError('Incorrect answer. Please try again.');
        return;
    }

    goToStep(3);
});

// Step 3: Set New Password
document.getElementById('step3Form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (newPassword !== confirmPassword) {
        showError('Passwords do not match!');
        return;
    }

    if (newPassword.length < 8 || 
        !/[A-Z]/.test(newPassword) || 
        !/[a-z]/.test(newPassword) || 
        !/[0-9]/.test(newPassword) || 
        !/[!@#$%^&*]/.test(newPassword)) {
        showError('Password must contain at least 8 characters, including uppercase, lowercase, number, and special character.');
        return;
    }

    const users = JSON.parse(localStorage.getItem('gpsUsers') || '[]');
    const userIndex = users.findIndex(u => u.userId === currentUser.userId);
    
    if (userIndex !== -1) {
        users[userIndex].password = newPassword;
        localStorage.setItem('gpsUsers', JSON.stringify(users));
        
        showSuccess('✅ Password reset successful! Redirecting to login...');
        
        setTimeout(() => {
            window.location.href = 'login.html';
        }, 2000);
    } else {
        showError('An error occurred. Please try again.');
    }
});