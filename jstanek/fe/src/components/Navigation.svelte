<script>
    import ThemeSwitcher from "./ThemeSwitcher/ThemeSwitcher.svelte"
</script>

<nav class="navbar navbar-expand-lg" id="navbar">
        <div class="container">
            <ThemeSwitcher></ThemeSwitcher>
            <div class="d-flex navbar-text cutout-wrapper">
                <div class="d-flex">
                    <a href="/" class="align-top"><div class="website-logo"></div></a>
                </div>
            </div>
        </div>
    </nav>
    <div class="w-100 fixed-top">
        <div class="progress" style="height: 2px;">
          <div id="scroll-percentage" class="progress-bar" role="progressbar"></div>
        </div>
    </div>