<script>

let username = "";
let password = "";

function handleLogin() {
  console.log('login');
  username = "";
  password = "";
}
</script>

<main class="login-container">
  <form class="login-form" on:submit={handleLogin}>
    <h1>Log In</h1>

    <input type="text" placeholder="Username or Email" bind:value={username} required />
    <input type="password" placeholder="Password" bind:value={password} required />

    <button type="submit">Log In</button>

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
