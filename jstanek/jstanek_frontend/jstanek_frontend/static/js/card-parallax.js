const card_parallax = document.querySelector(".card-parallax")
const THRESHOLD = 10
const motionMatchMedia = window.matchMedia("(prefers-reduced-motion)")
// const default_left_before = card_parallax.style.getProperty("--left-before-content")
// const default_top_before = card_parallax.style.getProperty("--top-before-content")

function handleHover(e) {
	const {clientX, clientY, currentTarget} = e
	const {clientWidth, clientHeight, offsetLeft, offsetTop} = currentTarget

	const horizontal = (clientX - offsetLeft) / clientWidth
	const vertical = (clientY - offsetTop) / clientHeight
	const rotateX = (THRESHOLD / 2 - horizontal * THRESHOLD).toFixed(2)
	const rotateY = (vertical * THRESHOLD - THRESHOLD / 2).toFixed(2)
	card_parallax.style.transform = `perspective(${clientWidth}px) rotateX(${rotateY}deg) rotateY(${rotateX}deg) scale3d(1, 1, 1)`
	card_parallax.style.setProperty("--opacity-before-content", Math.abs(rotateX)/THRESHOLD)
	// card_parallax.style.setProperty("--top-before-content",default_top_before)
	// card_parallax.style.setProperty("--left-before-content",default_left_before)

}

function resetStyles(e) {
	setTimeout((target) => {
		card_parallax.style.transform = `perspective(${target.clientWidth}px) rotateX(0deg) rotateY(0deg)`
		card_parallax.style.setProperty("--opacity-before-content", 0)
	}, 200, e.currentTarget)

}

card_parallax.style.setProperty("--opacity-before-content", 0)
if (!motionMatchMedia.matches) {
	card_parallax.addEventListener("mousemove", handleHover)
	card_parallax.addEventListener("mouseleave", resetStyles)
}