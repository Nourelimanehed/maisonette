import Header from "./components/Header";
import Home from "./components/Home";
import Help from "./components/Help";
import Adds from "./components/Adds";
import MyOffers from "./components/MyOffers";
import MyAdds from "./components/MyAdds";
import NoPage from "./components/NoPage"
import AddDetails from "./components/AddDetails";

import './App.css'

import { BrowserRouter, Routes, Route } from "react-router-dom";


function App() {
    return (
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Header/>}>
          <Route index element={<Home/>} />
          <Route path="aide" element={<Help/>} />
          <Route path="annonces" element={<Adds/>} />
          <Route path="mesOffres" element={<MyOffers/>} />
          <Route path="mesAnnonces" element={<MyAdds/>} />
          <Route path="detailesAnnonce" element={<AddDetails/>}/>
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
    );
  }

  export default App;