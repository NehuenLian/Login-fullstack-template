<script>
import { enhance } from '$app/forms';
import { validateEmail, validatePasswordLength, validatePasswordCase, validatePasswordSymbols, 
  validateConfirmPassword } from '$lib/utils/validations.js';

import eyeOpen from '$lib/assets/eye-open.svg';
import eyeClosed from '$lib/assets/eye-closed.svg';

let errors = [];

let email = "";
let password = "";
let confirmPassword = "";

let showPassword = false;
let passwordInput;

function togglePassword() {
  showPassword = !showPassword;
  passwordInput.type = showPassword ? 'text' : 'password';
}

// show errors
$: {
  errors = [];
  if (email && !validateEmail(email)) {
    errors.push('• Please enter a valid email address.');
  }

  if (password && !validatePasswordLength(password)) {
    errors.push('• The password must be at least 8 characters long.');
  } else if (password && !validatePasswordCase(password)) {
    errors.push('• Password must have at least one uppercase and lowercase letter.');
  } else if (password && !validatePasswordSymbols(password)) {
    errors.push('• Password must have at least one symbol.')
  }

  if (confirmPassword && !validateConfirmPassword(password, confirmPassword)) {
    errors.push('• Passwords must be identical.');
  }
}

// data returned from server
export let data;
$: if (data?.error) {
  email = "";
  password = "";
  confirmPassword = "";
}

</script>

<main class="register-container">
  <form class="register-form" method="POST" use:enhance>
    <h1>Sign Up</h1>

    <input type="text" placeholder="Email" bind:value={email} name="email" required />
    
    <div class="password-wrapper">
      <input bind:this={passwordInput} type="password" placeholder="Password" bind:value={password} name="password" required />
      <button type="button" class="showPassword" on:click={togglePassword}>
        <img src={showPassword ? eyeClosed : eyeOpen} alt="Show Password" />
      </button>
    </div>

    <input type="password" placeholder="Confirm Password" bind:value={confirmPassword} name="confirmPassword" required />

    <!--Fields validations-->
    {#each errors as error}
      <p class="register-error">{error}</p>
    {/each}

    <button type="submit" disabled={errors.length > 0 || !email && !password && !confirmPassword}>Sign Up</button>
    
    {#if data?.error}
      <p class="register-error">{data.error}</p>
    {/if}

    <p class="login-text">
      Already have an account?
      <a href="/login">Log In</a>
    </p>
  </form>

</main>

<style>
  :global(html, body) {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: #121212;
    font-family: 'Segoe UI', sans-serif;
  }

  .register-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #121212;
  }

  .register-form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 350px;
    padding: 2rem;
    border-radius: 12px;
    background-color: #1e1e1e;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
    color: #fff;
    width: 90%;
  }

  h1 {
    text-align: center;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #ffffff;
  }

  input {
    padding: 0.75rem;
    border-radius: 8px;
    border: 1px solid #2c2c2c;
    background-color: #2c2c2c;
    color: #fff;
    font-size: 1rem;
    transition: border-color 0.2s, background-color 0.2s;
  }

  input::placeholder {
    color: #b0b0b0;
  }

  input:focus {
    outline: none;
    border-color: #5865f2;
    background-color: #3a3a3a;
  }

  .password-wrapper {
    position: relative;
    width: 100%;
  }

  .password-wrapper input {
    width: 100%;
    padding-right: 2.5em; /* espacio para el botón */
    box-sizing: border-box;
  }

  .showPassword {
    position: absolute;
    right: 0.5em;
    top: 50%;
    transform: translateY(-50%);
    border: none;
    background: transparent;
    cursor: pointer;
    font-size: 1.2em;
    line-height: 1;
    padding: 0;
  }

  .showPassword:hover {
    background-color: #cfcfcf;
  }

  button {
    padding: 0.75rem;
    border: none;
    border-radius: 8px;
    background-color: #5865f2;
    color: #fff;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  button:hover {
    background-color: #4752c4;
  }

  button:disabled {
    background-color: #8f97f2;
    cursor: not-allowed;
    opacity: 0.6;
  }

  .register-error {
    color: #FF5C5C;
    font-weight: bold;
    font-size: 14px;
    text-align: left;
    margin-top: 0px;
    margin-bottom: 0px;
    padding-bottom: 0px;
    padding-top: 0px;
  }

  .login-text {
    text-align: center;
    font-size: 0.9rem;
    margin-top: 0.5rem;
    color: #b0b0b0;
  }

  .login-text a {
    color: #fff;
    text-decoration: none;
    font-weight: 500;
    margin-left: 0.25rem;
  }

  .login-text a:hover {
    text-decoration: underline;
  }
</style>
