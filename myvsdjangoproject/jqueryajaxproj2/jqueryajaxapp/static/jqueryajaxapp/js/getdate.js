function showDate() {
  $("#currentdate").load("getdate", processResponse);
}

// first content is added in the html element then callback is run
function processResponse(responseText, textStatus, xhr) {
  //  alert($('#currentdate').text());
  if (textStatus === "error") {
    $("#currentdate").text(
      "An error occured during your request:" + xhr.status
    );
  }
  //  else {
  //      $('#currentdate').html("done!");
  //  }
}
