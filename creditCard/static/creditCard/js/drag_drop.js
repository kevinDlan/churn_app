//selecting all required elements
const dropArea = document.querySelector(".drag-area");
dragText = dropArea.querySelector("p");
button = document.querySelector("#chooseFile");
input = document.querySelector("#input");
submit = document.querySelector("#submit_btn");
choose = document.querySelector('#chooseFile');
let file; //this is a global variable and we'll use it inside multiple functions

button.onclick = () => {
  input.click(); //if user click on the button then the input also clicked
};

input.addEventListener("change", function () {
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  file = this.files[0];
  dropArea.classList.add("active");
  // showFile(); //calling function
  submit.removeAttribute('hidden')
  choose.remove()
});

//If user Drag File Over DropArea
dropArea.addEventListener("dragover", (event) => {
  event.preventDefault(); //preventing from default behaviour
  dropArea.classList.add("active");
  dragText.textContent = "Relâchez pour télécharger le fichier";
});

//If user leave dragged File from DropArea
dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Glissez-déposez pour télécharger le fichier";
});

//If user drop File on DropArea
dropArea.addEventListener("drop", (event) => {
  event.preventDefault(); //preventing from default behaviour
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  file = event.dataTransfer.files[0];
  // showFile(); //calling function
  submit.removeAttribute("hidden");
  choose.remove();
});

function showFile() {
  let fileType = file.type; //getting selected file type
//   let validExtensions = ["image/jpeg", "image/jpg", "image/png"]; //adding some valid image extensions in array
  let validExtensions = ["application/vnd.ms-excel","text/plain","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"];
  if (validExtensions.includes(fileType)) {
    //if user selected file is an image file
    let fileReader = new FileReader(); //creating new FileReader object
    fileReader.onload = () => {
      let fileURL = fileReader.result; //passing user file source in fileURL variable
      let imgTag = `<img src="${fileURL}" alt="">`; //creating an img tag and passing user selected file source inside src attribute
      dropArea.innerHTML = imgTag; //adding that created img tag inside dropArea container
    };
    fileReader.readAsDataURL(file);
  } else {
    alert("Le fichier entré n'est pas requis");
    dropArea.classList.remove("active");
    dragText.textContent = "Glissez-déposez pour télécharger le fichier";
  }
}
