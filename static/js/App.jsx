const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
// const useLocation = ReactRouterDOM.useLocation;
// const useHistory = ReactRouterDOM.useHistory;


//Hooks to user useState and useEffect

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


// function Logout() {
//     return (
//         <div>
            
//         </div>
//     )
// }

function SearchPark() {
    return (
        <div>
            
        </div>
    )
}

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
                            <Link to="/register">New User</Link>
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
// 


// function SeacrhPark() {
//     return <div>Welcome to my site</div>
// }


// function SearchBox() {
//     return <div>Welcome to my site</div>
// }



ReactDOM.render(<App />, document.getElementById('root'))
//only need to list this once. all other components will be rendered by other components