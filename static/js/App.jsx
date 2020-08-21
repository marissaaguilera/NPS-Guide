// import {Register} from "./RegisterComponent.jsx"



const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
// const useLocation = ReactRouterDOM.useLocation;
// const useHistory = ReactRouterDOM.useHistory;


//Hooks to user useState and useEffect

//in the parenthesis we have empty quotes for a string 
//useEffect runs something for me everytime the component renders

function Homepage() {
    return ( 
        <div>Welcome to your NPS Guide!</div>
    );
}


function Login() {
    return (
        <div>
            Email: 
            <input type="text" name="email"></input><br />
            Password: 
            <input type="text" name="password"></input><br />
            <button type="submit">Login</button>
        </div>
    );
}
// submit button - watch video, creating a post, input as they change, 
//create post = do for login and register  

// 
//not connected to my route unless i send it to my login route 
// need fetch request everytime that i want to send info to my server 

//usestate assigns items to the value and connected function, create the state
//useeffect want to change something, effecting the state with a change 

//react redux is like an umbrella, 
//component does and action, goes from one place to another

function Register() {
    
    const [first_name, set_first_name] = React.useState('')
    const [last_name, set_last_name] = React.useState('')
    const [email, set_email] = React.useState('')
    const [password, set_password] = React.useState('')


    console.log(first_name)
    console.log(last_name)
    console.log(email)
    console.log(password)

    return (
        <div id="register">
            First Name:  
            <input onChange={event => set_first_name(event.target.value)} type="text" name="first_name" required></input><br />
            Last Name: 
            <input onChange={event => set_last_name(event.target.value)} type="text" name="last_name" required></input><br />
            Email: 
            <input onChange={event => set_email(event.target.value)} type="text" name="email" required></input><br />
            Password:  
            <input onChange={event => set_password(event.target.value)} type="text" name="password" required></input><br />

            <button type="submit">Register</button>
        </div>

    );
}
//submit onclick 
//send to the backend 


//when input value changes set first name to first name, onchange is liek onclick 

// function Logout() {
//     return (
//         <div>
            
//         </div>
//     )
// }

function SearchPark() {
    return (
        <div>
            Search
            <input type="text"></input>
            <button>Search</button>
        </div>
    );
}
//render this in the choose parks page

// function Activities() {
//     return (
//         <div>
            
//         </div>
//     )
// }
// function Bucketlist() {
//     return (
//         <div>
            
//         </div>
//     )
// }
// function BucketlistItem() {
//     return (
//         <div>
            
//         </div>
//     )
// }

function App() {
    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/login">Login</Link>
                        </li>
                        <li>
                            <Link to="/register">Register</Link>
                        </li>
                        <li>
                            <Link to="/search-park">Search Park</Link>
                        </li>
                    </ul>
                </nav>
                <Switch>
                    <Route path="/login">
                        <Login />
                    </Route>
                    <Route path="/register">
                        <Register />
                    </Route>
                    <Route path="/">
                        <Homepage />
                    </Route>
                </Switch>
            </div>
        </Router>
    );
}


//NOTES: 
//order matters in the switch, homepage goes last 
//pass props in switch on line 79 for example 
// #hit routes with fetch request and return a json 



// function SeacrhPark() {
//     return <div>Welcome to my site</div>
// }


// function SearchBox() {
//     return <div>Welcome to my site</div>
// }



ReactDOM.render(<App />, document.getElementById('root'))
//only need to list this once. all other components will be rendered by other components