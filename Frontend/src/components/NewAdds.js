import React from 'react'
import AddCube from './AddCube';

const NewAdds = ()=> {
  return (
    <div >
      <h1>Nouvelles Annonces</h1>
      <div className="new-adds">
        <AddCube/>
      </div>
    </div>
  )
}

export default NewAdds;