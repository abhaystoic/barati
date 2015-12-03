//Thanks to : https://www.fir3net.com/Web-Development/Django/how-do-i-use-ajax-along-side-django.html
/*$(document).ready(function() {
    $('#add_to_cart').submit(function() { // catch the form's submit event
        $.ajax({
            url : this.action, 
            type : "POST",
            dataType: "json", 
            data: $(this).serialize(), // get the form data
            context : this,
            success : function(json) {
              alert(json);
              if (json == "success_add_to_cart")
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
*/
$(document).ready(function() {
    $('form').submit(function() { // catch the form's submit event
        $.ajax({
            url : this.action, 
            type : "POST",
            dataType: "json", 
            data: $(this).serialize(), // get the form data
            context : this,
            success : function(json) {
              if (json == "success_add_to_cart")
              {
                  alert(json);       //code for badging cart icon
              }
              
              if (json == "success_add_to_wishlist")
              {
                 alert(json);  
                 window.location = location.pathname;
              }
              if (json == "success_remove_from_wishlist")
              {
                 alert(json);  
                 window.location = location.pathname;
              }
              },
            error : function(xhr,errmsg,err) {
              alert(xhr.status + ": " + xhr.responseText);
              }
        });
        return false;
    });
    });
/*
$(document).ready(function() {
$('form').submit(function() { // catch the form's submit event
  e.preventDefault();
  alert('hi');
  $.ajax({
      url : this.action, 
      type : "POST",
      dataType: "json", 
      data: $(this).serialize(), // get the form data
      context : this,
      success : function(json) {
        if (json == "success_add_to_wishlist")
        {
           alert(json);  
           window.location = location.pathname;
        }
        },
      error : function(xhr,errmsg,err) {
        alert(xhr.status + ": " + xhr.responseText);
        }
  });
  return false;
});
});*/
