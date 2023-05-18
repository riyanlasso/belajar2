const dropArea = document.getElementById("drop-area");
const fileInfo = document.getElementById("file-info");
const displayBtn = document.getElementById("display-info");

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area when item is dragged over it
['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unhighlight, false);
});

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

function highlight(e) {
  dropArea.classList.add('highlight');
}

function unhighlight(e) {
  dropArea.classList.remove('highlight');
}

function handleDrop(e) {
  const dt = e.dataTransfer;
  const files = dt.files;
  
  handleFiles(files);
}

function handleFiles(files) {
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    fileName = file.name;
    fileType = fileName.substring(fileName.lastIndexOf('.') + 1);
    
    if (fileType === 'c3d') {
      fileInfo.innerHTML = `Name: ${fileName}<br>Format: ${fileType}`;
    }
  }
}

displayBtn.addEventListener("click", function() {
  const fileInfoValue = fileName;
  console.log(fileInfoValue);
});
