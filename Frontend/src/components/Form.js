import { Step, StepButton, StepLabel, Stepper } from "@mui/material";
import FirstStep from "./FirstStep";
import SecondStep from "./SecondStep";
import ThirdStep from "./ThirdStep";
import { useContext } from "react";
import { useState } from "react";
import { Link } from "react-router-dom";


function Form(){
    const [page, setPage] = useState(0);
    const [formData, setFormData] = useState({
        Titre: "",
        Déscription: "",
        Adresse: "",
        Wilaya: "",
        Commune: "",
        Type: "",
        Categorie: "",
        Surface: "",
        Prix: "",
        Img:"",
      });

  const FormTitles = ["Informations", "Ajoutez des spécifications", "Veulliez séléctionner des images"];
  
  const PageDisplay = () => {
    if (page === 0) {
      return < FirstStep formData={formData} setFormData={setFormData} />;
    } else if (page === 1) {
      return <SecondStep formData={formData} setFormData={setFormData} />;
    } else {
      return <ThirdStep formData={formData} setFormData={setFormData}/>;
    }
  };
    
  return (
    <div className="form-father">
      <div className="form-container" >
        
          <div style={{display:'flex', justifyContent:'center'}}>
            <div className="progressbar" >
              <br/> <br/>
              <div style={{ width: page === 0 ? "33.3%" : page == 1 ? "66.6%" : "100%" }}></div>
            </div>
          </div>
          

          <div className="form" >
            <div className="form-title" >
              {FormTitles[page]}
            </div>
            <div  className="form-content">{PageDisplay()}</div>
            <div className="form-btns" >
              <button   className="form-btn" disabled={page == 0} onClick={() => {setPage((currPage) => currPage - 1);}}>
                Précédent
              </button>  
              
              <button className="form-btn"   onClick={() => {if (page === FormTitles.length - 1) {alert("Annonce enregistrée avec succés");console.log(formData);} else {setPage((currPage) => currPage + 1);} }}>
              
                
                   {page === FormTitles.length - 1 ? <Link to="/"> Valider </Link> : "Suivant"}
                
              
              </button>  
            
            </div>
            <br/>
          </div>
        
      </div>
    </div>
       
    );
  };
  
  export default Form;