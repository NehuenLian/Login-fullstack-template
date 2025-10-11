<script>
</script>

<div class="welcome">
    <h1>Test Page</h1>
    <p>This page can only be accessed if you are logged in.</p>
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

</style>