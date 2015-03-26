/* Globals */
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

/* Add Event listeners needed to the canvas */
window.onload = function()
{
	var can = document.getElementById("canvas");
	can.addEventListener("dragstart", dragStart, false);
	can.addEventListener("dragover", allowDrop, false);
	can.addEventListener("drop", drop, false)
	can.addEventListener("drag", dragMain, false);
	can.addEventListener("dragend", dragEnd, false);	
}

/* Render the current background image and a hairstyle if present.
   Executed in a set interval */
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

/* Event listeners for canvas */
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

/* Used for the load image button. Transfers the loaded image's data to the canvas (see jQuery below) */
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

/* Generates a form for a POST request, adds a hiddenfield containing
   the canvas data and submits the POST request to be handled in the index view */
function postCreation()
{
	var canvas = document.getElementById("canvas");
	
	var form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", "/kinkycuts/");

    
	var hiddenField = document.createElement("input");
	hiddenField.setAttribute("type", "hidden");
	hiddenField.setAttribute("name", "imagedata");
	hiddenField.setAttribute("value", canvas.toDataURL());
	form.appendChild(hiddenField);

    document.body.appendChild(form);
    form.submit();
}


/* Reads the url from the user's uploaded image */
$("#userFile").change(function(){
	readURL(this);
});

/* Transfers the canvas' data to the href of the download link (button in disguise) */
$("#downloadImgLink").click(function(){
	$('#downloadImgLink').attr('href', canvas.toDataURL());
});

/* Resets the offsets of the rendered background image */
$("#refreshButton").click(function(){
	imageXOffset = 0;
	imageYOffset = 0;
});

/* Increases the scale of the background image */
$("#zoomin").click(function(){
	scale += 0.1;
	if(scale > 2) scale = 2;
});

/* Decreases the scale of the background image */
$("#zoomout").click(function(){
	scale -= 0.1;
	if(scale < 0.1) scale = 0.1;
});