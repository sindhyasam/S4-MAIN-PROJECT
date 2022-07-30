function showPasswordRegister() {
  var pass_1 = document.getElementById("pass-field_r1");
  var pass_2 = document.getElementById("pass-field_r2");
  if (pass_1.type === "password") {
    pass_1.type = "text";
  } else {
    pass_1.type = "password";
  }
  if (pass_2.type === "password") {
    pass_2.type = "text";
  } else {
    pass_2.type = "password";
  }
}

/********* Additional profile update ********************/

function showPopUp(){
  document.getElementById('updateImagePopUp').style.display = "block";
}

function hidePopUp(){
  document.getElementById('updateImagePopUp').style.display = "none";
}

$("#PopUpCancel").click(function (e) {
  hidePopUp();
});

$("#PopUpSave").click(function (e) {
  hidePopUp();
});

$("#profileImageFirst").click(function (e) {
  showPopUp();
});

$("#profileImage").click(function (e) {
  $("#imageUpload").click();
});

function fasterPreview(uploader) {
  if (uploader.files && uploader.files[0]) {
    $('#profileImage').attr('src',
      window.URL.createObjectURL(uploader.files[0]));
  }
}

$("#imageUpload").change(function () {
  fasterPreview(this);
});

/************* additional about update******************/ 
function showPopUpDesc(){
  document.getElementById('updateDescPopUp').style.display = "block";
}

function hidePopUpDesc(){
  document.getElementById('updateDescPopUp').style.display = "none";
}

$("#profileAbout").click(function (e) {
  showPopUpDesc();
});

$("#PopUpDescCancel").click(function (e) {
  hidePopUpDesc();
});