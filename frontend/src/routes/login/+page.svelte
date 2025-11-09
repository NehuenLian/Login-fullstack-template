<script>
import { enhance } from '$app/forms';
import eyeOpen from '$lib/assets/eye-open.svg';
import eyeClosed from '$lib/assets/eye-closed.svg';

import { goto } from '$app/navigation';
import { browser } from '$app/environment';

let email = "";
let password = "";
let rememberMe = false;
let showPassword = false;
let passwordInput;

export let form;

function togglePassword() {
  showPassword = !showPassword;
  passwordInput.type = showPassword ? 'text' : 'password';
}

// get data from server
async function handleSubmit() {
  return async ({ result }) => {
    if (result.type === 'success') {
      
      if (browser && result.data?.access_token) {

        sessionStorage.setItem('access_token', result.data.access_token);
      }
      goto('/dashboard');
    }
    else if (result.type === 'failure') {
      password = "";
    }
  };
}

</script>

<main class="login-container">
  <form class="login-form" method="POST" use:enhance={handleSubmit}>
    <h1>Login</h1>
    <input type="text" placeholder="Email" bind:value={email} name="email" required />
    
    <div class="password-wrapper">
      <input bind:this={passwordInput} type="password" placeholder="Password" bind:value={password} name="password" required />
      <button type="button" class="showPassword" on:click={togglePassword}>
        <img src={showPassword ? eyeClosed : eyeOpen} alt="Show Password" />
      </button>
    </div>

    <label class="remember-me">
      <input type="checkbox" bind:checked={rememberMe} name="rememberMe">
      Remember me
    </label>

    <button type="submit" disabled={!email || !password} >Log In</button>

    {#if form?.error}
      <p class="login-error">{form.error}</p>
    {/if}

    <p class="register-text">
      Don't have an account?
      <a href="/register">Sign Up</a>
    </p>
  </form>

</main>

<style>
    :global(html, body) {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: #121212;
    }

  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #121212;
    font-family: 'Segoe UI', sans-serif;
  }

  .login-form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 350px;
    padding: 2rem;
    border-radius: 12px;
    background-color: #1e1e1e;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
    color: #fff;
  }

  .login-error {
    color: #FF5C5C;
    font-weight: bold;
    text-align: center;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
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

  .register-text {
    text-align: center;
    font-size: 0.9rem;
    margin-top: 0.5rem;
    color: #b0b0b0;
  }

  .register-text a {
    color: #fff;
    text-decoration: none;
    font-weight: 500;
    margin-left: 0.25rem;
  }

  .register-text a:hover {
    text-decoration: underline;
  }
</style>