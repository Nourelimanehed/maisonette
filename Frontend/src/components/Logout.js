import { GoogleLogout } from 'react-google-login';


const clientId = "1089944479834-d0lsaghh7lnmqulej1va0lv7c35scrrk.apps.googleusercontent.com";

function Logout () {
    const onSuccess= () => {
        console.log("LOGOUT SUCCESS!");
    }


    return(<div is="signOutButton">
        <GoogleLogout
            clientId={clientId}
            buttonText={"Logout"}
            onLogoutSuccess={onSuccess}
        />
    </div>)
}

export default Logout;