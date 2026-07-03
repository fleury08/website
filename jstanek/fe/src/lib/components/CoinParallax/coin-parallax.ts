const THRESHOLD = 10

export function handleHover(ev: MouseEvent) {
	const {clientX, clientY, currentTarget} = ev
	const {clientWidth, clientHeight, offsetLeft, offsetTop, style } = currentTarget as HTMLElement

	const horizontal = (clientX - offsetLeft) / clientWidth
	const vertical = (clientY - offsetTop) / clientHeight
	const rotateX = (THRESHOLD / 2 - horizontal * THRESHOLD)
	const rotateY = (vertical * THRESHOLD - THRESHOLD / 2)
	style.transform = `perspective(${clientWidth}px) rotateX(${rotateY}deg) rotateY(${rotateX}deg) scale3d(1, 1, 1)`
	style.setProperty("--opacity-before-content", `${(Math.abs(rotateX)/THRESHOLD)+.5}`)

}

export function resetStyles(ev: MouseEvent) {
	setTimeout(() => {
		const el: HTMLElement = ev.target as HTMLElement
		el.style.transform = `perspective(${el.clientWidth}px) rotateX(0deg) rotateY(0deg) rotateZ(0deg) scale3d(1, 1, 1)`
		el.style.transitionDuration = "0"
		el.style.setProperty("--opacity-before-content", "0")
	}, 200)
}

export function spinCoin(ev: MouseEvent) {
	const el: HTMLElement = ev.target as HTMLElement
	el.classList.add("coin-rotate")
}
