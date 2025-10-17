function validatePasswordLenght(password) {
  return password.length >= 8;
}

function validatePasswordCase(password) {
  const has_upper = /[A-Z]/.test(password);
  const has_lower = /[a-z]/.test(password);

  return has_upper && has_lower
}

function validateConfirmPassword(password, confirmPassword) {
  return password === confirmPassword;
}

function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}