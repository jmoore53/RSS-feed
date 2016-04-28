function randomArticle(){
	var elements = document.getElementsByClassName('story');
	var randomElement = Math.round(Math.random()*elements.length);
	var innerHTMLStringHref = elements[randomElement].innerHTML.toString();
	innerHTMLtitle = innerHTMLStringHref.substring(innerHTMLStringHref.indexOf("\">"),innerHTMLStringHref.indexOf("</a>"));
	innerHTMLtitle = innerHTMLtitle.substring(2);
	innerHTMLSlink = innerHTMLStringHref.substring(10,innerHTMLStringHref.indexOf('\">'));
	document.getElementById("randomLinkTitle").innerHTML = innerHTMLtitle;
	document.getElementById("randomLink").innerHTML = innerHTMLSlink;
}