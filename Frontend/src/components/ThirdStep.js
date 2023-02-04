import AddPhotoAlternateIcon from '@mui/icons-material/AddPhotoAlternate';

/*<TextField className="form-field" label="Img" margin ="normal" variant="outlined" color="secondary"/> */

import React, { useState } from "react";
const ThirdStep = () => {
  const [selectedImages, setSelectedImages] = useState([]);

  const onSelectFile = (event) => {
    const selectedFiles = event.target.files;
    const selectedFilesArray = Array.from(selectedFiles);

    const imagesArray = selectedFilesArray.map((file) => {
      return URL.createObjectURL(file);
    });

    setSelectedImages((previousImages) => previousImages.concat(imagesArray));

    // FOR BUG IN CHROME
    event.target.value = "";
  };

  function deleteHandler(image) {
    setSelectedImages(selectedImages.filter((e) => e !== image));
    URL.revokeObjectURL(image);
  }

  return (
    <section className="Step-Container" >
      <div className="form-image-container">
            <input type="file" id="file" accept="image/*"  onChange={onSelectFile}/>
            <label for="file" className="add-image-label">
              <i className="material-icons">
              <AddPhotoAlternateIcon/>  
              </i> &nbsp;
              Uploader une photo
            </label>
          </div>
      <br />

      <input type="file" multiple />

      {selectedImages.length > 0 &&
        (selectedImages.length > 10 ? (
          
          <h2>
            Vous pouvez ajouter que 10 images. S'il Vous plait suprimer <b style={{color:'red'}}> {selectedImages.length - 10} </b> images {" "}
          </h2>
          
        ) : (
        
          <div style={{display:'flex', justifyContent:'center'}}>
            <button
            className="light-btn"
            onClick={() => {
              console.log(selectedImages);
            }}
          >
            Ajouter {selectedImages.length} photo
            {selectedImages.length === 1 ? "" : "s"}
          </button>
          </div>
          
          
        ))}
      <br/> 
      <br/>
      <div className="images" style={{display:'flex',flexWrap:'wrap', gap:'40px'}}>
        {selectedImages &&
          selectedImages.map((image, index) => {
            return (
              <div key={image}  style={{display:'flex', flexDirection:'column'}}>
                <img src={image} height="200"  alt="upload" />
                <button className="light-btn" onClick={() => deleteHandler(image)}>
                  supprimer image
                </button>
              </div>
            );
          })}
      </div>
    </section>
  );
};

export default ThirdStep;

/*import AddPhotoAlternateIcon from '@mui/icons-material/AddPhotoAlternate';
import React from "react";

function ThirdStep({ formData, setFormData }){
  
    return(
        <div className="Step-Container">
          <div className="form-image-container">
            <input type="file" id="file" accept="image/*"  onChange={(event) => setFormData({ ...formData, Img: event.target.files })}/>
            <label for="file" className="add-image-label">
              <i className="material-icons">
              <AddPhotoAlternateIcon/>  
              </i> &nbsp;
              Ajouter une photo
            </label>
          </div>
        </div>
    )
}
export default ThirdStep;*/