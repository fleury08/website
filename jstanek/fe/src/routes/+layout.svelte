
<script lang="ts">
  import "../app.pcss";
	import "$lib/assets/css/theme.pcss";
	import { ModeWatcher } from 'mode-watcher';
	import { browser } from '$app/environment';

	// Matomo
	if(browser) {
		let _paq = window._paq = window._paq || [];
		/* tracker methods like "setCustomDimension" should be called before "trackPageView" */
		_paq.push(['trackPageView']);
		_paq.push(['enableLinkTracking']);
		(function() {
			let u = "https://analytics.jstanek.eu/";
			_paq.push(['setTrackerUrl', u + 'matomo.php']);
			_paq.push(['setSiteId', '1']);
			let d = document, g = d.createElement('script'), s = d.getElementsByTagName('script')[0];
			g.async = true;
			g.src = u + 'matomo.js';
			s.parentNode.insertBefore(g, s);
		})();
	}
	// End Matomo Code


</script>
<noscript><p><img src="https://analytics.jstanek.eu/matomo.php?idsite=1&amp;rec=1" style="border:0;" alt="" /></p></noscript>

<ModeWatcher />
<slot></slot>


