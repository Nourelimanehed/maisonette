import React from 'react'
import TypeFilter from "./TypeFilter";
import PeriodeFilter from "./PeriodeFilter";
import WilayaFilter from "./WilayaFilter";
import CommuneFilter from "./CommuneFilter";
import { useState } from "react";

const FilterBar = ()=> {
  
  const [typeFilter, setTypeFilter] = useState(false);
  const [wilayaFilter, setWilayaFilter] = useState(false);
  const [communeFilter, setCommuneFilter] = useState(false);
  const [periodeFilter, setPeriodeFilter] = useState(false);
  

  const setType = event =>{
      if(!typeFilter){
        setTypeFilter(true);
        setWilayaFilter(false);
        setCommuneFilter(false);
        setPeriodeFilter(false);
      }
      else{setTypeFilter(false);}
  }

  const setWilaya = event =>{
    if(!wilayaFilter){
      setTypeFilter(false);
      setWilayaFilter(true);
      setCommuneFilter(false);
      setPeriodeFilter(false);
    }
    else{setWilayaFilter(false);}
  }
  
  const setCommune = event =>{
    if(!communeFilter){
      setTypeFilter(false);
      setWilayaFilter(false);
      setCommuneFilter(true);
      setPeriodeFilter(false);
    }
    else{setCommuneFilter(false);}
  }
  
  const setPeriode = event =>{
    if(!periodeFilter){
      setTypeFilter(false);
      setWilayaFilter(false);
      setCommuneFilter(false);
      setPeriodeFilter(true);
    }
    else{setPeriodeFilter(false);}
  }

  /*const changeAll = () =>{
  if (typeFilter) {setTypeFilter(false);}
  if (wilayaFilter)  {setWilayaFilter(false);}
  if (communeFilter) {setCommuneFilter(false);}
  if(periodeFilter)  {setPeriodeFilter(false);}
  }onClick={changeAll}*/

  
  return (
    <div className="filter-bar" >
       <button className="filter-bar-btn" onClick={setType} >TYPE</button>
       <button className="filter-bar-btn" onClick={setWilaya}>WILAYA</button>
       <button className="filter-bar-btn" onClick={setCommune}>COMMUNE</button>
       <button className="filter-bar-btn" onClick={setPeriode}>PERIODE</button>
       {typeFilter && ( <div> <TypeFilter/></div>)}
       {wilayaFilter && ( <div> <WilayaFilter/></div>)}
       {communeFilter && ( <div> <CommuneFilter/></div>)}
       {periodeFilter && ( <div> <PeriodeFilter/></div>)}
    </div>
  )
}

export default FilterBar;