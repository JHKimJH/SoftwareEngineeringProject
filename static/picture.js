// var submit = document.getElementById('submitButton');
// submit.onclick = showImage;     //Submit 버튼 클릭시 이미지 보여주기

// function showImage() {
//     var newImage = document.getElementById('image-show').lastElementChild;
//     newImage.style.visibility = "visible";
    
// }


function loadFile(input) {
    if (document.getElementsByClassName('img').length > 0){
        while(document.getElementsByClassName('img').length>0){
            var oldImage = document.getElementById('image-show').lastElementChild;
            //oldImage.style.visibility = "hidden";
            //document.getElementById('image-show').removeChild(oldImage);
            oldImage.remove();
            var name = document.getElementById('demo');
            name.value = "";
        }
    }


    if(input.files.length == 1){
        var file = input.files[0];	//선택된 파일 가져오기
    
        var name = document.getElementById('demo');
        name.value = file.name;
    
        
        var newImage = document.createElement("img");
        newImage.setAttribute("class", 'img');
    
    
        //이미지 source 가져오기
        newImage.src = URL.createObjectURL(file);   
    
        
        newImage.style.width = "100%";
        newImage.style.height = "40%";
        newImage.style.display = "block";
        //newImage.style.visibility = "hidden";   //버튼을 누르기 전까지는 이미지 숨기기
        newImage.style.marginLeft = "auto";
        newImage.style.marginRight = "auto";
        newImage.style.objectFit = "contain";
    
        var container = document.getElementById('image-show');
        container.appendChild(newImage);
    }
    else{

        for (var i = 0; i < input.files.length; i ++){
            var file = input.files[i];	//선택된 파일 가져오기
    
            var name = document.getElementById('demo');
            name.value = name.value + "," + file.name;
        
                
            var newImage = document.createElement("img");
            newImage.setAttribute("class", 'img');
        
        
            //이미지 source 가져오기
            newImage.src = URL.createObjectURL(file);   

            newImage.style.width = "100%";
            newImage.style.height = "40%";
            newImage.style.display = "block";
            //newImage.style.visibility = "hidden";   //버튼을 누르기 전까지는 이미지 숨기기
            newImage.style.marginLeft = "auto";
            newImage.style.marginRight = "auto";
            newImage.style.objectFit = "contain";
        
        
            var container = document.getElementById('image-show');
            container.appendChild(newImage);
        }
    }
 

};

