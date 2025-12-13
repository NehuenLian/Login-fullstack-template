<script>
import Navbar from '$lib/components/Navbar.svelte';
import { PUBLIC_API_URL } from '$env/static/public';
import { fetchWithApi } from '$lib/helpers/fetchWithToken';

const API_URL = PUBLIC_API_URL;

let result = '';

async function testRefresh() {
  try {
    const accessToken = sessionStorage.getItem('access_token');

    const res = await fetchWithApi(`${API_URL}/api/auth/protected-test`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${accessToken}`
      },
      credentials: 'include'
    });

    if (!res.ok) {
      throw new Error(`Status ${res.status}`);
    }

    const data = await res.json();
    result = JSON.stringify(data, null, 2);
  } 
  catch (err) {
    result = 'Error: ' + err.message;
  }
}

</script>

<Navbar />

<div class="welcome">
  <h1>Test Page</h1>
  <p>This page can only be accessed if you are logged in.</p>

  <button class="test-token-button" on:click={testRefresh}>
    Test refresh token
  </button>

  {#if result}
    <pre>{result}</pre>
  {/if}

  <form method="POST" action="/logout">
    <button class="logout-button" type="submit">Logout</button>
  </form>
</div>


<style>
  :global(html, body) {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: #121212;
    font-family: 'Segoe UI', sans-serif;
    color: #fff;
  }

  .welcome {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center; 
    gap: 0.5rem; 
  }

  h1 {
    margin: 0;
    font-size: 2rem;
    color: #fff;
  }

  p {
    margin: 0;
    font-size: 1rem;
    color: #fff;
  }

  .logout-button {
    padding: 0.75rem;
    border: none;
    border-radius: 8px;
    background-color: #5865f2;
    color: #fff;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .test-token-button {
    padding: 0.75rem;
    border: none;
    border-radius: 8px;
    background-color: #5865f2;
    color: #fff;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .logout-button:hover {
    background-color: #4752c4;
  }
  

</style>