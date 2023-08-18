import { persisted } from 'svelte-local-storage-store'
import {get} from "svelte/store";

export const preferences = persisted('preferences', {
        theme: 'light'
})

export function saveThemePreference(theme: string) {
    const prefs = get(preferences)
    prefs.theme = theme
    preferences.set(prefs)
}