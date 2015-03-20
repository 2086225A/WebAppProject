function changeImage(imageid) {
    var image = document.getElementById(imageid);
    if (image.src.match("/static/images/notliked.png")) {
        image.src = "/static/images/liked.png";

    } else {
        image.src = "/static/images/notliked.png";

    }
}