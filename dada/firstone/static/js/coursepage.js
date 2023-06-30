function validateform1() {
    let id = document.forms["myform"]["id"].value;
    let credithours = document.forms["myform"]["creditnumber"].value;
    let depart = document.forms["myform"]["sbaey"].value;
    let coursename = document.forms["myform"]["name"].value;
    if (credithours < 40 && depart != "NONE") {
        alert("your credit hours is not enough to choose a department");
    } else if (id.length != 8) {
        alert("your id must be at least 8 characters long.");
    } else if (depart == "select depart") {
        alert("please select department");
    } else if (coursename == null || coursename == "") {
        alert("please enter a course name you want to register");
    } else {
        window.location = "home.html";

    }
}