import React from "react";

const CommuneFilter = () => {
    return (
      <div className="filter" >
      <div className="filter-title" >COMMUNE</div>
      <hr/>
      <select size={6}>
       <option value="0">-Sélectioner une commune-</option>
       <option value="1">Adrar 01</option>
       <option value="2">Chlef 02</option>
       <option value="3">Laghouat 03</option>
       <option value="4">Oum El Bouaghi 04</option>
       <option value="5">Batna 05</option>
       <option value="6">Bejaia 06</option>
       <option value="7">Biskra 07</option>
       <option value="8">Bechar 08</option>
       <option value="9">Blida 09</option>
       <option value="10">Bouira 10</option>
       <option value="11">Tamanrasset 11</option>
       <option value="12">Tebessa 12</option>
       <option value="13">Tlemcen 13</option>
       <option value="14">Tiaret 14</option>
       <option value="15">Tizi Ouzou 15</option>
       <option value="16">Alger 16</option>
       <option value="17">Djelfa 17</option>
       <option value="18">Jijel 18</option>
       <option value="19">Setif 19</option>
       <option value="20">Saida 20</option>
       <option value="21">Skikda 21</option>
       <option value="22">Sidi Bel Abbes 22</option>
       <option value="23">Annaba 23</option>
       <option value="24">Guelma 24</option>
       <option value="25">Constantine 25</option>
       <option value="26">Medea 26</option>
       <option value="27">Mostaganem 27</option>
       <option value="28">M'sila 28</option>
       <option value="29">Mascara 29</option>
       <option value="30">Ouargla 30</option>
       <option value="31">Oran 31</option>
       <option value="32">El Baydah 32</option>
       <option value="33">Illizi 32</option>
       <option value="34">Bordj Bou Arreridj 34</option>
       <option value="35">Boumerdes 35</option>
       <option value="36">El Taref 36</option>
       <option value="37">Tindouf 37</option>
       <option value="38">Tissemslit 38</option>
       <option value="39">El Oued 39</option>
       <option value="40">Khenchela 40</option>
       <option value="41">Souk Ahras 41</option>
       <option value="42">Tipaza 42</option>
       <option value="43">Mila 43</option>
       <option value="44">Ain Defla 44</option>
       <option value="45">Naama 45</option>
       <option value="46">Ain Temouchent 46</option>
       <option value="47">Ghardaia 47</option>
       <option value="48">Relizane 48</option>
       <option value="49">Timimoun 49</option>
       <option value="50">Bordj Baji Mokhtar 50</option>
       <option value="51">Ouled Djellal 51</option>
       <option value="52">Beni Abbes 52</option>
       <option value="53">In Salah 53</option>
       <option value="54">In Guezzam 54</option>
       <option value="55">Touggourt 55</option>
       <option value="56">Djanet 56</option>
       <option value="57">El M'Ghair 57</option>
       <option value="58">El Meniaa 58</option>
      </select>
      <div className="filter-btn">
        <br/>
        <button className="light-btn" >Valider</button>
      </div>
    </div>
    );
  };
  
export default CommuneFilter;