function show(i)
{
	var x = document.getElementById("myModal");
	
	im = document.getElementById("modalImage");
	caption = document.getElementById("id");
	im.src = i.src;
	caption.innerHTML = i.alt;
	x.style.display ="block";
	//alert("Hello");
}

function hide()
{
	var x = document.getElementById("myModal");
	
	x.style.display ="none";
	
}