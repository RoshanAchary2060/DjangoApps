function showDate() {
    $('#currentdate').load('getdate #time',processResponse)
}
function processResponse(responseText, textStatus, xhr) {
    if (textStatus == 'error') {
        $('currentdate').text('An error occured during your request:' + xhr.textStatus + " " + xhr.text)
    }
}