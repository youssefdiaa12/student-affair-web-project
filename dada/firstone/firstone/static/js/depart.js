function validateform1() {
    let id = document.forms["myform"]["id"].value;
    let name = document.forms["myform"]["name"].value;
    if (id.length != 8) {
        alert("your id must be at least 8 characters long.");
    } else if (name == null || name == "") {
        alert("please enter a name");
    } else {
        window.location = "home.html";

    }
}