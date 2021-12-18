// choose category
let menu = document.querySelectorAll(".menu");
let list = document.querySelectorAll(".items");

menu.forEach((i) => {
	i.onclick = function () {
		list.forEach((l) => {
			l.style.display = "none";
		});
		document.querySelectorAll(i.dataset.type).forEach((el) => {
			el.style.display = "block";
		});
	};
});

// count
let plus = document.querySelectorAll(".add"),
	mins = document.querySelectorAll(".minus");

plus.forEach((el) => {
	el.onclick = function () {
		num = Number(el.nextElementSibling.value);
		console.log(num);
		el.nextElementSibling.value = num + 1;
	};
});

mins.forEach((el) => {
	el.onclick = function () {
		num = Number(el.previousElementSibling.value);
		if (el.previousElementSibling.value == 1) {
			el.previousElementSibling.value = 1;
		} else {
			el.previousElementSibling.value = num - 1;
		}
	};
});

// mins.forEach((el) => {
// 	el.addEventListener("click", minus);
// });
