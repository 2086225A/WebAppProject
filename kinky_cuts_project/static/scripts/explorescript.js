function changeImage(imageid) {
    var image = document.getElementById(imageid);
    if (image.src.match("/static/images/notliked.png")) {
        image.src = "/static/images/liked.png";
        postLike('/kinkycuts/explore/', {like : 'true', imageID:imageid});
    } else {
        image.src = "/static/images/notliked.png";
        postLike('/kinkycuts/explore/', {like : 'false', imageID:imageid});
    }
}

function postLike(path, params, method)
{
    method = method || "post";

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params)
    {
        if(params.hasOwnProperty(key))
        {
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
