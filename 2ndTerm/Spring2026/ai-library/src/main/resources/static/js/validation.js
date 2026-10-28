document.addEventListener("DOMContentLoaded", function() {
	
	const form = document.querySelector("form[data-validate]");
	if(form === null) return;
	
	form.addEventListener("submit", function (e) {
		const inputs = form.querySelectorAll("input[data-label]");
		for (const input of inputs) {
			if(input.value.trim() === ""){
				e.preventDefault();
				alert(input.dataset.label + "을(를) 입력하세요.");
				input.focus()
				return;
			}
		}
	});
});