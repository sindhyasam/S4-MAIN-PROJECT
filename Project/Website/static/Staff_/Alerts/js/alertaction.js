/************* additional about update******************/ 
function showPopUpDesc(){
    document.getElementById('ReportPopUp').style.display = "block";
  }
  
  function hidePopUpDesc(){
    document.getElementById('ReportPopUp').style.display = "none";
  }
  /*
  $("#report").click(function (e) {
    showPopUpDesc();
  });
  */
  $("#ReportCancel").click(function (e) {
    hidePopUpDesc();
  });

  function genReport(id, deviceID) {
    document.getElementById('reportID').value = id;
    document.getElementById('reportDID').value = deviceID;
    showPopUpDesc();
}
