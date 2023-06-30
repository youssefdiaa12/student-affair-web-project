function validateform1() {
    let id = document.forms["myform"]["id"].value;
    let password = document.forms["myform"]["password"].value;
    let gpa = document.forms["myform"]["gpa"].value;
    let num = document.forms["myform"]["no"].value;
    let gender = document.forms["myform"]["gender"].value;
    let email = document.forms["myform"]["mail"].value;
    if (password == null || password == "") {
        alert("please enter a valid password");
    } else if (id.length != 8) {
        alert("your id must be at least 8 characters long.");
    } else if (gpa <= 0 || gpa > 4) {
        alert("please enter a correct gpa");
    } else if (num.length != 11) {
        alert("your telephone number must be 11");
    } else if (gender != "male" || gender != "female" || gender == null) {
        alert("please enter your gender");
    } else if (email == null) {
        alert("please enter your email");
    } else {
        window.location = "home.html";

    }
}