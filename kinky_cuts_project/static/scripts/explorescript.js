function changeImage() {
    var image = document.getElementById('like');
    if (image.src.match("index1.png")) {
        image.src = "index.png";

    } else {
        image.src = "index1.png";

    }
}