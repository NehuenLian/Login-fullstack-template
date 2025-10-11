<script>
import { enhance } from '$app/forms';

let username = "";
let password = "";
let confirmPassword = "";

export let data;
$: if (data?.error) {
  username = "";
  password = "";
  confirmPassword = "";
}

</script>

<main class="register-container">
  <form class="register-form" method="POST" use:enhance>
    <h1>Sign Up</h1>

    <input type="text" placeholder="Username or Email" bind:value={username} name="username" required />
    <input type="password" placeholder="Password" bind:value={password} name="password" required />
    <input type="password" placeholder="Confirm Password" bind:value={confirmPassword} name="confirmPassword" required />

    <button type="submit">Sign Up</button>

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
    width: 350px;
    padding: 2rem;
    border-radius: 12px;
    background-color: #1e1e1e;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
    color: #fff;
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

  .register-error {
    color: #ff0000;
    font-weight: bold;
    text-align: center;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
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
