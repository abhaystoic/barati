//Thanks to : https://www.fir3net.com/Web-Development/Django/how-do-i-use-ajax-along-side-django.html
$(document).ready(function() {
    $('#add_to_cart').submit(function() { // catch the form's submit event
        $.ajax({
            url : this.action, 
            type : "POST",
            dataType: "json", 
            data: $(this).serialize(), // get the form data
            context : this,
            success : function(json) {
              alert(json);
              if (json == "successfully added in cart")
              {
                  //code for badging cart icon
              }
              },
            error : function(xhr,errmsg,err) {
              alert(xhr.status + ": " + xhr.responseText);
              }
        });
        return false;
    });
    });

