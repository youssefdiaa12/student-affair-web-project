function validateform1() {
    let id = document.forms["myform"]["id"].value;
    let password = document.forms["myform"]["id1"].value;
    if (password == null || password == "") {
        alert("please enter a valid password");
    } else if (id.length != 8) {
        alert("your id must be at least 8 characters long.");
    } else {
        window.location = "home.html";

    }
}