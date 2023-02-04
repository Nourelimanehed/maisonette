import React from "react";
import SearchBar2 from "./SearchBar2"
import FilterBar2 from "./FilterBar2"
import { AddsInfo } from "./AddsInfo";
import AddCube from "./AddCube";

const Help = () => {
    return (
    <div className="adds-container">
      
      <div className="adds-top-part">
        <h1>Annonces</h1>
        <SearchBar2/>
      </div>
      
      <div className = "adds-middle-part">
        <hr/>
        <FilterBar2/>
      </div>
      
      <div className="adds-bottom-part">
        {AddsInfo.map((AddInfo)=>(
          <AddCube title={AddInfo.title} price={AddInfo.prix} area={AddInfo.surface}/>
        ))}        


      </div>
     
      
    </div>
    

    );
  };
  
  export default Help;