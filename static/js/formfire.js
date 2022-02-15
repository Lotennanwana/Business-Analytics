var config = {
    apiKey: "AIzaSyDtbIrjdIuyRtFSr0Hyynxo2_lYMH-js8o",
    authDomain: "dsc-covenant-university.firebaseapp.com",
    databaseURL: "https://dsc-covenant-university.firebaseio.com",
    projectId: "dsc-covenant-university",
    storageBucket: "dsc-covenant-university.appspot.com",
    messagingSenderId: "939153188275"
};
firebase.initializeApp(config);

let messagesRef = firebase.database().ref('messages');

document.getElementById('mailform').addEventListener('submit', submitForm);

function submitForm(e) {
    e.preventDefault();
    let email = getInputVal('email');
    saveMessage(email);
    document.querySelector('.alert').style.display = 'block';
    setTimeout(function () {
        document.querySelector('.alert').style.display = 'none';
    }, 5000);
    document.getElementById('mailform').reset();

}

function getInputVal(id) {
    return document.getElementById(id).value;
}

function saveMessage(email) {
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
        email: email
    });
}
