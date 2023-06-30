function validateform1() {
    let id = document.forms["myform"]["id"].value;
    let depart = document.forms["myform"]["depart"].value;
    if (id.length != 8) {
        alert("your id must be at least 8 characters long.");
    }
    if (depart == "select depart") {
        alert("please select your department");
    } else {
        window.location = "home.html";

    }
}