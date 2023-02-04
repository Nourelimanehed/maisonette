
import image from "./../graphics/Back-ground-image.png" 
import SearchBar from "./SearchBar";
import NewAdds from "./NewAdds";
import FilterBar from "./FilterBar";

const Home = () => {
    return (
      <div id="home-back-ground-container">
      <img src={image} id="back-ground-image" alt="not found"/>
      <FilterBar/>
      <div id="home-back-ground-element-text"> Découvrez votre location idéale</div>
      <SearchBar/>
      <NewAdds/>
      </div>
    );
  };
  
  export default Home;