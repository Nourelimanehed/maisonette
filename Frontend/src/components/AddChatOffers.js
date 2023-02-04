import { MesOffresInfo } from "./MesOffresInfo";


const AddChatOffers = () => {
    
    return (
      <div className="add-chat-container">
        <div className="add-chat-top">Mes Offres</div>
        <hr/>
        <div className="add-chat-middle">
          {MesOffresInfo.map((MonOffre)=>(
            <button className="offer-btn" >{MonOffre.name}</button> 
          ))}
        </div>
        <hr/>
      </div>
    );
  };
  
  export default AddChatOffers;