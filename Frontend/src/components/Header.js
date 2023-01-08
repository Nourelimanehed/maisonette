import React from 'react'
import { Outlet, Link } from "react-router-dom";


const Header = () => {
    return(
    <>
      <nav>
        <div className="flex-container">
            <ul id="nav-part1">
                <li>
                    <Link to="/ ">
                        <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <g clip-path="url(#clip0_202_3570)">
                                <path d="M25 24.5H3V26.5H25V24.5Z" fill="#5D70D5"/>
                                <path d="M28 26.5H0V27.5H28V26.5Z" fill="#5D70D5"/>
                                <path opacity="0.6" d="M4 14.328V24.5H7V14.5H13V24.5H24V14.328L14 4.328L4 14.328ZM16 17.5V16.5V14.5H18H19H21V16.5V17.5V19.5H19H18H16V17.5Z" fill="#5D70D5"/>
                                <path d="M22 8V1.414H19V5L14 0L0.292969 13.707L1.70697 15.121L14 2.828L26.293 15.121L27.707 13.707L22 8Z" fill="#5D70D5"/>
                                <path d="M9 18.5H8V20.5H9V18.5Z" fill="#5D70D5"/>
                                <path opacity="0.6" d="M18 19.5H19V17.5H21V16.5H19V14.5H18V16.5H16V17.5H18V19.5Z" fill="#5D70D5"/>
                            </g>
                            <defs>
                                <clipPath id="clip0_202_3570">
                                    <rect width="28" height="27.5" fill="white"/>
                                </clipPath>
                            </defs>
                        </svg>
                    </Link>
                </li>
                <li>
                    <Link id="site-name" to="/">MaiSonaite</Link> 
                </li>
                <li>
                    <button className="light-btn">Déposer annonce</button>
                </li>
            </ul>
            
            <ul id="nav-part2">
                <li>
                    <Link className="nav-item" to="/aide">Aide</Link>
                </li>
                <li>
                    <Link className="nav-item"  to="/annonces">Annonces</Link>
                </li>
                <li>
                    <Link className="nav-item"  to="/mesOffres">Mes Offres</Link>
                </li>
                <li>
                    <Link className="nav-item"  to="/mesAnnonces">Mes Annonces</Link>
                </li>
                <li>
                    <button className="dark-btn" id="cnx-btn">Connexion</button>
                </li>
            </ul>
        </div>
      </nav>
      <Outlet />
    </> 
    );
}

export default Header;