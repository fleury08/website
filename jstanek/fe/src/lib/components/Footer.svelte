<script lang="ts">
  const year = new Date().getFullYear();
  const copyright = `Copyright © ${year} Jaroslav Staněk`;
  const links = [
    { name: "Python", url: "https://www.python.org/" },
    {name: "FastAPI", url: "https://fastapi.tiangolo.com/"},
    { name: "SvelteKit", url: "https://kit.svelte.dev/" },
    { name: "Shadcn", url: "https://shadcn.com" },
    { name: "Tailwindcss", url: "https://tailwindcss.com" }
  ]
</script>

<div class="footer">
  <div>{copyright}</div>
  <div>
    Created with:
  {#each links as link}
    <a href={link.url} target="_blank" rel="noreferrer">{link.name}</a>
  {/each}
  </div>
</div>