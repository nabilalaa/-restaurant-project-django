// remove items

let items = document.querySelectorAll(".delete");


items.forEach((el) => {
	el.onclick = setTimeout(function () {
		el.parentElement.remove();
	},1000)
});
