<div class="welcome">
    <h1>This is the Template Home/Root.</h1>
    <p>Visit <a href="https://github.com/NehuenLian" target="_blank">github.com/NehuenLian</a> to view the repository.</p>
    <div>
        <a href="/login" target="_blank">View Login</a> | 
        <a href="/register" target="_blank">View Register</a>
    </div>
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

  a {
    color: #505EAF;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

</style>