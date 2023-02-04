import React from "react";

const TypeFilter = () => {
    return (
      <div className="filter">
        <div className="filter-title">TYPE</div>
        <hr/>
        <div >
          <input type="radio" id="terrain" name="type-choice" />
          <label for="terrain">Terrain</label>
          <br/>
          <input type="radio" id="terrain-Agricole" name="type-choice" />
          <label for="terrain-Agricole">Terrain Agricole</label>
          <br/>
          <input type="radio" id="appartement" name="type-choice" />
          <label for="appartement">Appartement</label>
          <br/>
          <input type="radio" id="maison" name="type-choice" />
          <label for="maison">Maison</label>
          <br/>
          <input type="radio" id="bangalow" name="type-choice"/>
          <label for="bangalow">Bangalow</label>
        </div>
        <div className="filter-btn">
          <button className="light-btn" >Valider</button>
        </div>
      </div>
    );
  };
  
export default TypeFilter;