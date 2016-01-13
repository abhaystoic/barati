/*Used for the autocomplete feature */
(function($){
  
  var $project = $('#main_preference_location');

  var projects = [
     {
      value: "delhi",
      label: "Delhi",
      desc: "Delhi",
      icon: "delhi.jpg"
     },
  /*{% if query %}
    {% for result in page.object_list %}
       {
         value: "{{ result.object.city}}",
         label: "jQuery",
         desc: "the write less, do more, JavaScript library",
         icon: "jquery_32x32.png"
       },
    {% empty %}
      {
      value: "Noresults",
      label: "Noresults",
      desc: "No results",
      icon: "jquery_32x32.png"
       },
    {% endfor %}
  {% else %}
     {
      value: "Delhi",
      label: "Delhi",
      desc: "Delhi",
      icon: "jquery_32x32.png"
     },
  {% endif %}*/
  ];
  
  $project.autocomplete({
    minLength: 0,
    source: projects,
    focus: function( event, ui ) {
      $project.val( ui.item.label );
      return false;
    }
  });
  
  $project.data( "ui-autocomplete" )._renderItem = function( ul, item ) {
    
    var $li = $('<li>'),
        $img = $('<img>');


    $img.attr({
      src: '../static/images/autocomplete/' + item.icon,
      alt: item.label
    });

    $li.attr('data-value', item.label);
    $li.append('<a href="#">');
    $li.find('a').append($img).append(item.label);    

    return $li.appendTo(ul);
  };
  

})(jQuery);
