var draggedIndex = "0";
var droppedItem = false;
var dragging = false;
var imageXOffset = 0;
var imageYOffset = 0;
var dragStartX = 0;
var dragStartY = 0;
var currentX = imageXOffset;
var currentY = imageYOffset;
var scale = 1;

window.onload = function()
{
	var can = document.getElementById("canvas");
	can.addEventListener("dragstart", dragStart, false);
	can.addEventListener("dragover", allowDrop, false);
	can.addEventListener("drop", drop, false)
	can.addEventListener("drag", dragMain, false);
	can.addEventListener("dragend", dragEnd, false);	
}

setInterval(function()
{
	var can = document.getElementById("canvas");
	var con = can.getContext("2d");
	con.clearRect(0,0, can.width, can.height);
	var imgFace = document.getElementById("face");
	
	con.drawImage(imgFace, imageXOffset, imageYOffset, can.width * scale, can.height * scale);

	if(draggedIndex != "0" && droppedItem)
	{
		var imgHair = document.getElementById(draggedIndex);
		con.drawImage(imgHair, 0, 0, can.width, can.height);
	}

}, 1);

function dragStart(event)
{
	dragging = true;
	dragStartX = event.pageX;
	dragStartY = event.pageY;
}

function dragMain(event)
{
	if(dragging)
	{
		imageXOffset = event.pageX - dragStartX;
		imageYOffset = event.pageY - dragStartY;
	}
}

function dragEnd(event)
{
	dragging = false;
}

function allowDrop(ev)
{
	ev.preventDefault();
}

function drag(ev)
{
	draggedIndex = ev.target.id;
	imageXOffset = 0;
	imageYOffset = 0;
	droppedItem = false;
}

function drop(ev)
{
	ev.preventDefault();
	droppedItem = true;
	
}

function readURL(input) 
{
	if (input.files && input.files[0]) 
	{
		var reader = new FileReader();

		reader.onload = function (e)
		{
			$('#face').attr('src', e.target.result);
		}

		reader.readAsDataURL(input.files[0]);
	}
}		

function postCreation(path, params, method)
{
	var canvas = document.getElementById("canvas");	
	var context = canvas.getContext('2d');

	params['imageData'] = context.getImageData(0, 0, canvas.width, canvas.height);

    var method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);
    
    for(var key in params) {
        if(params.hasOwnProperty(key)) {
        	
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
         }
    }

    document.body.appendChild(form);
    form.submit();
}

$("#userFile").change(function(){
	readURL(this);
});
$("#downloadImgLink").click(function(){
	$('#downloadImgLink').attr('href', canvas.toDataURL());
});
$("#refreshButton").click(function(){
	imageXOffset = 0;
	imageYOffset = 0;
});
$("#zoomin").click(function(){
	scale += 0.1;
	if(scale > 2) scale = 2;
});
$("#zoomout").click(function(){
	scale -= 0.1;
	if(scale < 0.1) scale = 0.1;
});