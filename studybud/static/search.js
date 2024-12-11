let rooms = document.getElementsByClassName("card");
console.log(rooms);
let search = document.getElementsByClassName("search").addEventListener("submit", function (e) {
    e.preventDefault();
// console.log(search);

var formData = new FormData(form);
// output as an object
console.log(Object.fromEntries(formData));

// ...or iterate through the name-value pairs
for (var pair of formData.entries()) {
  console.log(pair[0] + ": " + pair[1]);
}
});