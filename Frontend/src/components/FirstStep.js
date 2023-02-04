import { Select, TextField } from "@mui/material";
import React from "react";
import {Wilayas} from './Wilayas'
import {Communes} from './Communes'
 function FirstStep({ formData, setFormData }){

    return(
        <div className="Step-Container">
          
          <div >
            <TextField  className="form-field" label="Titre" margin ="normal" variant="outlined" color="secondary"  
            value={formData.Titre}onChange={(event) =>
            setFormData({ ...formData, Titre: event.target.value })}/>
          </div>
          
          <div>
            <TextField  className="form-field" label="Description" margin ="normal" variant="outlined" color="secondary"
            value={formData.Description}onChange={(event) =>
            setFormData({ ...formData, Description: event.target.value })}/>
          </div>
          <div>
            <TextField className="form-field" label="Adresse" margin ="normal" variant="outlined" color="secondary"
            value={formData.Adresse}onChange={(event) =>
            setFormData({ ...formData, Adresse: event.target.value })}/>
          </div>
          <br/>
          <div className="form-2-field">

            <div className="form-1-field">
              <select className="form-select-field" value={formData.Wilaya}onChange={(event) => setFormData({ ...formData, Wilaya: event.target.value })}>
                <option value='0'>Wilaya</option>
                {Wilayas.map((wilaya)=>(
                <option className="list-item" value={wilaya.id} >{wilaya.name}</option>))}
              </select>  
            </div>

           
            <div className="form-1-field">
              <select className="form-select-field" value={formData.Commune}onChange={(event) => setFormData({ ...formData, Commune: event.target.value })}>
                <option value='0'>Commune</option>
                {Communes.map((Commune)=>(
                <option className="list-item" value={Commune.id} >{Commune.name}</option>))}
              </select>  
            </div>
          </div>
          <br/>
        </div>
        
    )
}
export default FirstStep;