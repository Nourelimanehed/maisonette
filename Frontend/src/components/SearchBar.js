import React from 'react'

const SearchBar = ()=> {
  return (
    <div className="search-bar">
        <input className="search-field" type="text" placeholder="Mot clé, Titre, Description . . ."/>
        <button className="search-btn">
            <i>
                <svg  width="29" height="29" viewBox="0 0 29 29" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M28.0046 26.6718L21.7008 20.3681C28.2608 12.7959 22.7451 0.700912 12.636 0.739349C9.47622 0.742737 6.44674 1.99901 4.21185 4.23271C1.97695 6.4664 0.719045 9.49521 0.713959 12.655C0.675521 22.7704 12.7705 28.2862 20.3427 21.7262L26.6721 28.0043C26.8569 28.1275 27.0787 28.1828 27.2997 28.1609C27.5207 28.139 27.7273 28.0412 27.8844 27.8841C28.0414 27.7271 28.1392 27.5205 28.1611 27.2995C28.183 27.0785 28.1277 26.8567 28.0046 26.6718V26.6718ZM2.63583 12.6293C2.63923 9.97877 3.69411 7.43783 5.56895 5.56418C7.44379 3.69054 9.98541 2.63729 12.636 2.6356C25.8905 3.18654 25.8905 22.0786 12.636 22.6295C9.9843 22.6278 7.44171 21.5737 5.56669 19.6987C3.69166 17.8236 2.63753 15.281 2.63583 12.6293V12.6293Z" fill="white"/>
                </svg>
            </i>
        </button>
    </div>
  )
}

export default SearchBar;