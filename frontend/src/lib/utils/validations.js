export function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

export function validatePasswordLenght(password) {
  return password.length >= 8;
}

export function validatePasswordCase(password) {
  const has_upper = /[A-Z]/.test(password);
  const has_lower = /[a-z]/.test(password);

  return has_upper && has_lower
}

export function validatePasswordSymbols(password) {
  const has_symbol = /[^a-zA-Z0-9]/.test(password);
  return has_symbol;
}

export function validateConfirmPassword(password, confirmPassword) {
  return password === confirmPassword;
}