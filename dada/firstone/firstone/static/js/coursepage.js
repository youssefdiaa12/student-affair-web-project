function validateform1() {
    let id = document.forms["myform"]["id"].value;
    let credithours = document.forms["myform"]["creditnumber"].value;
    let hallnumber = document.forms["myform"]["hall"].value;
    let coursename = document.forms["myform"]["name"].value;
    if (credithours < 10) {
        alert("your credit hours is not enough to choose a department");
    } else if (id.length != 8) {
        alert("your id must be at least 8 characters long.");
    } else if (hallnumber < 0 || hallnumber.length == 0) {
        alert("please enter a correct hall number");
    } else if (coursename == null || coursename == "") {
        alert("please enter a course name you want to register");
    } else {
        window.location = "home.html";

    }
}