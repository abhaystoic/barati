//Used for suggesting locality based on sublocation search string
//Refer to : http://blog.appliedinformaticsinc.com/autocomplete-quick-intro-django-haystack-solr-jquery/
//Refer to : https://jqueryui.com/autocomplete/
(function($){
$('#search_everything').autocomplete({
    source: function (request, response) {
        $.getJSON("/search_everything/?search_everything=" + request.term + "&product_type=" + $( "#product_type_main_filter" ).val(), function (data) { 
              var results = data.results || [];
              var resultEverythingJsonArr = [];
              if(results.length > 0) {
                 var res_length = (results.length);
                 for(i=0;i<res_length;i++)
                 {
                     if (results[i] != null)
                     {
                       resultEverythingJsonArr.push(results[i]);
                     }
                 }
              }
              response(resultEverythingJsonArr);
        });
    },
    select: function( event, ui ) {
         window.location.href = "/"+ ui.item.type + "_details/" + ui.item.id;
    }
});
})(jQuery);
