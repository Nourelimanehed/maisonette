import React, { useState } from "react";
import { Wilayas } from "./Wilayas";


const WilayaFilter = () => {
  
  const [query,setQuery] = useState("");
  const [value,setValue] = useState();
  
  
  return (
  <div className="filter" >
    <div className="filter-title" >WILAYA</div>
    <input className="date-field" type="text" value={value} onClick={(e)=>setValue()} placeholder="Sélectioner une wilaya" onChange={(e) => setQuery(e.target.value.toLowerCase())} />
    <hr/>
    <select className="list" size={6}>
     {Wilayas.filter(wilaya=>wilaya.name.toLowerCase().includes(query)
     ).map((wilaya)=>(
      <option className="list-item" value={wilaya.id} onClick={(e)=>setValue(wilaya.name)}>{wilaya.name}</option>
     ))}
    </select>
    <div className="filter-btn">
      <button className="light-btn" >Valider</button>
    </div>
  </div>);
  };
  
export default WilayaFilter;