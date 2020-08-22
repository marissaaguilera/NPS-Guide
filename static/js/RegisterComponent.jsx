
import React from 'react'


//Hooks to user useState and useEffect
const [first_name, set_first_name] = React.useState('')
//in the parenthesis we have empty quotes for a string 
//useEffect runs something for me everytime the component renders

function Register() {
    return (
        <div id="register">
            First Name:  
            <input type="text" name="fname" required></input><br />
            Last Name: 
            <input type="text" name="lname" required></input><br />
            Email: 
            <input type="text" name="email" required></input><br />
            Password:  
            <input type="text" name="password" required></input><br />
            <button type="submit">Register</button>
        </div>

    );
}

export default Register;
//like calling it, if someone tries to import 
//something from this file give them register 