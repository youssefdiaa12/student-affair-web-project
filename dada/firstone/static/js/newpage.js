var el_up = document.getElementById("GFG_UP");
var el_down = document.getElementById("GFG_DOWN");

el_up.innerHTML = "Click on the button to generate " +
    "a link using JavaScript.";

function GFG_Fun() {
    // Create anchor element.
    var a = document.createElement('a');

    // Create the text node for anchor element.
    var link = document.createTextNode("Student Affairs");

    // Append the text node to anchor element.
    a.appendChild(link);

    // Set the title.
    a.title = "Student affair page";

    // Set the href property.
    a.href = "home.html";

    // Append the anchor element to the body.
    document.body.appendChild(a);
}

function ay() {

    // Create anchor element.
    var a = document.createElement('a');

    // Create the text node for anchor element.
    //  var link = document.createTextNode("Student Affairs");

    // Append the text node to anchor element.
    a.appendChild(link);
    // Set the href property.
    location.href = "#";

    // Append the anchor element to the body.
    document.body.appendChild(a);
    location.href = "home.html";
}

function validateform() {
    let id = document.forms["myform"]["id"].value;
    let password = document.forms["myform"]["password"].value;
    let gpa = document.forms["myform"]["gpa"].value;
    let num = document.forms["myform"]["number"].value;
    if (password == null || password == "") {
        alert("please enter a valid password");
    } else if (id.length != 8 || isNaN(id.value)) {
        alert("your id must be at least 8 characters long.");
    } else if (gpa < 0 || gpa > 4) {
        alert("please enter a correct gpa");
    } else if (num.length != 11 || isNaN(num.value)) {
        alert("your telephone number must be 11");
    } else {
        window.location = "home.html";

    }
}

function validation() {
    let password = document.forms["myform"]["password"].value;
    if (password == null || password == "") {
        alert("please enter a valid password");
    } else {
        window.location = "home.html";
    }
}