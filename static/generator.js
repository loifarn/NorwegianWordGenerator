// Takes button click event, runs generator from flask app and gives value back to data.result
$(function() {
  $('.generate').bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/_lag_ord', {
      a: $('input[name="generate"]').val()
    }, function(data) {
      $("#result").text(data.result);
    });
    return false;
  });
});