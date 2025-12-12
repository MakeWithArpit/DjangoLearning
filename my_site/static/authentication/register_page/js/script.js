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
    }, 5000);
}

function showSuccess(message) {
    const successDiv = document.getElementById('successMessage');
    successDiv.textContent = message;
    successDiv.style.display = 'block';
}

document.getElementById('password').addEventListener('input', function(e) {
    const password = e.target.value;
    let strength = 0;

    const requirements = {
        length: password.length >= 8,
        uppercase: /[A-Z]/.test(password),
        lowercase: /[a-z]/.test(password),
        number: /[0-9]/.test(password),
        special: /[!@#$%^&*]/.test(password)
    };

    Object.keys(requirements).forEach(key => {
        const element = document.getElementById(`req-${key}`);
        if (requirements[key]) {
            element.classList.add('requirement-met');
            strength += 20;
        } else {
            element.classList.remove('requirement-met');
        }
    });

    const meter = document.getElementById('strengthMeter');
    meter.style.width = strength + '%';

    if (strength < 40) meter.style.background = '#ff3333';
    else if (strength < 80) meter.style.background = '#ffaa00';
    else meter.style.background = '#33ff33';
});

document.getElementById('email').addEventListener('blur', function(e) {
    const email = e.target.value;
    if (email && !email.toLowerCase().endsWith('@gmail.com')) {
        showError('Please use a Gmail address');
        e.target.value = '';
    }
});

document.getElementById('registerForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
        fullName: document.getElementById('fullName').value,
        email: document.getElementById('email').value,
        whatsapp: document.getElementById('whatsapp').value,
        userId: document.getElementById('userId').value,
        password: document.getElementById('password').value,
        confirmPassword: document.getElementById('confirmPassword').value,
        securityQuestion: document.getElementById('securityQuestion').value,
        securityAnswer: document.getElementById('securityAnswer').value
    };

    if (formData.password !== formData.confirmPassword) {
        showError('Passwords do not match!');
        return;
    }

    const users = JSON.parse(localStorage.getItem('gpsUsers') || '[]');

    if (users.some(u => u.userId === formData.userId)) {
        showError('User ID already exists.');
        return;
    }

    users.push({
        fullName: formData.fullName,
        email: formData.email,
        whatsapp: formData.whatsapp,
        userId: formData.userId,
        password: formData.password,
        securityQuestion: formData.securityQuestion,
        securityAnswer: formData.securityAnswer,
        registeredAt: new Date().toISOString()
    });

    localStorage.setItem('gpsUsers', JSON.stringify(users));

    showSuccess('Account created successfully! Redirecting...');
    setTimeout(() => {
        window.location.href = 'login.html';
    }, 2000);
});
