//Used for suggesting locality based on sublocation search string
//Refer to : http://blog.appliedinformaticsinc.com/autocomplete-quick-intro-django-haystack-solr-jquery/
//Refer to : https://jqueryui.com/autocomplete/
$('#main_preference_sublocation').autocomplete({
    source: function (request, response) {
        $.getJSON("/search/?main_preference_sublocation=" + request.term, function (data) { 
              var results = data.results || [];
              var resultJsonArr = [];
              if(results.length > 0) {
                 var res_length = (results.length);
                 for(i=0;i<res_length;i++)
                 {
                     resultJsonArr.push(results[i]);
                 }
              }
              response(resultJsonArr);
        }); 
    },
    select:function(event, ui){
       $('#go_btn').click();
    }
});

