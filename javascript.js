function randomArticle(){
	var elements = document.getElementsByClassName('story');
	var randomElement = Math.round(Math.random()*elements.length);
	var innerHTMLStringHref = elements[randomElement].innerHTML.toString();
	innerHTMLtitle = innerHTMLStringHref.substring(innerHTMLStringHref.indexOf("\">"),innerHTMLStringHref.indexOf("</a>"));
	innerHTMLtitle = innerHTMLtitle.substring(2);
	innerHTMLSlink = innerHTMLStringHref.substring(10,innerHTMLStringHref.indexOf('\">'));
	//document.getElementById("randomLink").innerHTML = innerHTMLSlink;
	//document.getElementById("randomLinkTitle").innerHTML = innerHTMLtitle;
	var link = document.createElement("a");
	link.setAttribute("href",innerHTMLSlink);
	var contentOfA = document.createTextNode(innerHTMLtitle);
	link.appendChild(contentOfA);

	if (document.querySelector("#randomLinkTitle").hasChildNodes()) {
		document.querySelector("#randomLinkTitle").innerHTML = '';
		document.querySelector("#randomLinkTitle").appendChild(link);
	}else{
		window.alert("There was an error, This is the catch.")
		document.querySelector("#randomLinkTitle").appendChild(link);
	}
}