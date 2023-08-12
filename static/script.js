let images = document.querySelectorAll('.image-container');
clicked = false;
images.forEach(image =>{
    image.addEventListener("click", function(){
        if (clicked) {
            image.lastElementChild.style.transform = "scale(1,1)";
            images.forEach(otherImage => {
                otherImage.style.display = "block";
        });
        clicked = false;
        }else{
        images.forEach(otherImage => {
            if (otherImage !== image) {
                otherImage.style.display = "none";
            }
        });
        image.lastElementChild.style.transform = "scale(3,3)";
        clicked = true;
    }
    });
       
});