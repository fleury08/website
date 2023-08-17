<script>
    import {Sun, Moon} from 'svelte-bootstrap-icons'
    import {applyTheme, switchTheme, theme} from "./theme-switcher";

    applyTheme()
</script>



<style>
    .theme-switcher{
        color: var(--text-color)
    }
</style>

<div class="d-flex navbar-text cutout-wrapper theme-switcher">
    <Sun width={24} height={24} class="me-2" />
    <div class="form-check form-switch">
      <input type="checkbox" class="form-check-input" id="switchColorMode" on:change={switchTheme} checked={theme() === 'dark'}>
    </div>
    <Moon width={24} height={24} class="icon"/>
</div>