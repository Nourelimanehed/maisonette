import React from 'react'
import AddRectangle from "./AddRectangle"
import AddChat from "./AddChat"
import AddContentTable from './AddContentTable'
import AddMap from "./AddMap"

const AddDetails = ({title,price,area}) => {
  return (
    <div className="add-details-container">
        
        <div className="add-details-top-part">
            <h1>{title}</h1>
            <hr/>
            <div className="add-view">
                <AddRectangle/>
                <AddChat/>
            </div>
        </div>
        
        <div className="add-details-middle-part">
          <p>Le text descriptif</p>
          <AddContentTable/>
        </div>
        
        <div className="add-details-bottom-part">
          <AddMap/>
        </div>
    
    </div>
  )
}

export default AddDetails;