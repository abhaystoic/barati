/*	
	var focusCookies = getCookie("focus");
	if (focusCookie == "location")
	{
		$( "#main_preference_location" ).focus();
	}*/

	function createFocusCookie(name, value)
	{
	   var date = new Date();
	   date.setTime(date.getTime() + (10*60*1000));/* Keep focus cookie for 10 minutes*/
	   var expires = "; expires=" + date.toGMTString();
	   document.cookie = name + "=" + value + expires + "; path=/";
	   alert(document.cookie);
	}
	
	function destroyCookie(name)
	{
		document.cookie = name + "= ;expires=Thu, 01 Jan 1970 00:00:00 UTC";
	}
	
	function getCookie(name)
	{
		var focusCookie = name + "=";
    	var ca = document.cookie.split(";");
    	for(var i=0; i<ca.length; i++) 
    	{
	        var c = ca[i];
	        while (c.charAt(0)==' ') c = c.substring(1);
	        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    	}
    	return "";
	}
