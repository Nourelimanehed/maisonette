import { TextField } from "@mui/material";
import React from "react";

 function SecondStep({ formData, setFormData }){
 
    return(
        <div className="Step-Container">
          <br/>
          <div className="form-2-field">
            <div className="form-1-field">
            <select className="form-select-field" value={formData.Type}onChange={(event) => setFormData({ ...formData, Type: event.target.value })}>
                <option value='0'>Type</option>
                <option value='1'>Terrain</option>
                <option value='2'>Terrain Agricole</option>
                <option value='3'>Appartement</option>
                <option value='4'>Maison</option>
                <option value='5'>Bangalow</option> 
              </select>  
            </div>
            <div className="form-1-field">
            <select className="form-select-field" value={formData.Categorie}onChange={(event) => setFormData({ ...formData, Categorie: event.target.value })}>
                <option value='0'>Catégorie</option>
                <option value='1'>Vente</option>
                <option value='2'>Echange</option>
                <option value='3'>Location</option>
                <option value='4'>Location pour vacances</option>
              </select>  
            </div>
          </div>
          <br/>
          <div className="form-2-field" style={{gap:'225px'}}>
            <div>
              <TextField className="form-1-field" label="Surface M^2" margin ="normal" variant="outlined" color="secondary" value={formData.Surface}onChange={(event) => setFormData({ ...formData, Surface: event.target.value })}/>
            </div>
            <div>
              <TextField className="form-1-field" label="Prix DA" margin ="normal" variant="outlined" color="secondary" value={formData.Prix}onChange={(event) => setFormData({ ...formData, Prix: event.target.value })}/>
            </div>
          </div>
          <br/>
        </div>
    )
}
export default SecondStep;