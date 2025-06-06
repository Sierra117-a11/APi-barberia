  const showLoginBtn = document.getElementById('show-login');
  const showRegisterBtn = document.getElementById('show-register');
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');

  showLoginBtn.addEventListener('click', () => {
    loginForm.style.display = 'block';
    registerForm.style.display = 'none';
    showLoginBtn.classList.add('btn-primary');
    showLoginBtn.classList.remove('btn-outline-primary');
    showRegisterBtn.classList.add('btn-outline-secondary');
    showRegisterBtn.classList.remove('btn-secondary');
  });

  showRegisterBtn.addEventListener('click', () => {
    registerForm.style.display = 'block';
    loginForm.style.display = 'none';
    showRegisterBtn.classList.add('btn-secondary');
    showRegisterBtn.classList.remove('btn-outline-secondary');
    showLoginBtn.classList.add('btn-outline-primary');
    showLoginBtn.classList.remove('btn-primary');
  });

  document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Evita que el formulario sea enviado de forma normal

        if (loginForm.checkValidity()) {
            // Si todo está correcto, redirige a agenda.html
            window.location.href = 'agenda.html';
        } else {
            // Si los campos son inválidos, muestra los mensajes de error de validación
            loginForm.reportValidity();
        }
    });
});


