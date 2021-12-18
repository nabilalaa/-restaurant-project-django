// remove items

let items = document.querySelectorAll(".delete");

items.forEach((el) => {
	el.onclick = function () {
		el.parentElement.remove();
	};
});
