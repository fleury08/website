import {preferences, saveThemePreference} from '$lib/stores/preferences'
import {get} from "svelte/store";
import {browser} from "$app/environment";


//function that changes the theme, and sets a localStorage variable to track the theme between page loads
export function switchTheme(e: Event) {
	const target = e.target as HTMLInputElement
	const theme = target.checked? 'dark' : 'light'
	saveThemePreference(theme)
	applyTheme()
}

export function applyTheme(){
	if(browser) {
		document.documentElement.setAttribute('data-theme', theme());
		document.documentElement.setAttribute('data-bs-theme', theme());
	}
}

export function theme(){
	return get(preferences).theme
}

