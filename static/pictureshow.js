function showFile() {
    //var file = input.files[0];	//선택된 파일 가져오기
    var filepath = document.getElementById('demo').value;
    if(filepath != "/"){

        if(filepath.includes(",")){
            var strarray = filepath.split(",");
            for (var i = 1; i < strarray.length; i++){
                //새로운 이미지 div 추가
                var newImage = document.createElement("img");
                newImage.setAttribute("class", 'img');

                //var = "C:\Users\janek\Videos\Captures\" + input;
                //이미지 source 가져오기
                newImage.src = "/static/pictures/" + strarray[i];   

                newImage.style.width = "100%";
                newImage.style.height = "40%";
                newImage.style.display = "block";
                newImage.style.marginLeft = "auto";
                newImage.style.marginRight = "auto";
                newImage.style.objectFit = "contain";

                //이미지를 image-show div에 추가
                var container = document.getElementById('image-show');
                container.appendChild(newImage);
            }

        }
        else{
            //새로운 이미지 div 추가
            var newImage = document.createElement("img");
            newImage.setAttribute("class", 'img');

            //var = "C:\Users\janek\Videos\Captures\" + input;
            //이미지 source 가져오기
            newImage.src = "/static/pictures/" + filepath.toString();   

            newImage.style.width = "100%";
            newImage.style.height = "40%";
            newImage.style.display = "block";
            newImage.style.marginLeft = "auto";
            newImage.style.marginRight = "auto";
            newImage.style.objectFit = "contain";

            //이미지를 image-show div에 추가
            var container = document.getElementById('image-show');
            container.appendChild(newImage);
        }
    }
};

showFile();