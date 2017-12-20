let x = new XMLHttpRequest();
let Events = {};
let Body = document.getElementsByTagName('body')[0];
x.open("GET", "https://www.eventbriteapi.com/v3/events/search/?sort_by=date&location.address=Boston&subcategories=2005%2C2007%2C2999&token=WKFJTUI4NXRQBOLGHL4C", true);
x.onload = function () {
	MegaObject = JSON.parse(x.response);
	Events = MegaObject.events;
	Events.forEach((event) => {
		Body.innerText = Body.innerText + event.start.local + ' ' + event.name.text + '\n' + event.description.text + '\n\n';
	})
};
x.send();