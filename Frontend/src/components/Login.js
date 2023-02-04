import { GoogleLogin } from 'react-google-login';


const clientId = "1089944479834-d0lsaghh7lnmqulej1va0lv7c35scrrk.apps.googleusercontent.com";

function Login () {
    const onSuccess= (res) => {
        console.log("LOGIN SUCCESS! Current user: ",res.profileObj);

    }

    const onFailure= (res) => {
        console.log("LOGIN FAILED! res: ",res);

    }

    return(<div is="signInButton">
        <GoogleLogin
            clientId={clientId}
            buttonText={"Login"}
            onSuccess={onSuccess}
            onFailure={onFailure}
            cookiePolicy={'single_host_origin'}
            isSignedIn={true}
        />
    </div>)
}

export default Login;