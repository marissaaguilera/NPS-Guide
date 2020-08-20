  
'use strict';

const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const useLocation = ReactRouterDOM.useLocation;
const useHistory = ReactRouterDOM.useHistory;



function Homepage() {
    return <div>Welcome to my site</div>
}


function Login() {
    return <div>Welcome to my site</div>
}


function Register() {
    return <div>Welcome to my site</div>
}


function SearchBox() {
    return <div>Welcome to my site</div>
}




// function Homepage() {
//     return <div>Welcome to my site</div>
// }



// function Login(props) { 
//     // a form with no logic yet
//     return (
//         <div id="login">
//             <h1>Login</h1>
//             <form action="/login" method="POST">
//             <p>
//                     Email <input type="text" name="email">
//                 </p>
//                 <p>
//                     Password <input type="text" name="password">
//                 </p>
//                 <p>
//                     <input type="submit">
//                 </p>
//             </form>
//         </div>
//     )
//   }

// function App() {
//     return (
//         <Router>
//             <div>
//                 <nav>
//                     <ul>
//                         <li>
//                             <Link to="/">Home</Link>
//                         </li>
//                         <li>
//                             <Link to="/login">Login</Link>
//                         </li>
//                     </ul>
//                 </nav>
//                 <Switch>
//                     <Route path="/login">
//                         <Login />
//                     </Route>
//                     <Route path="/">
//                         <Homepage />
//                     </Route>
//                 </Switch>
//             </div>
//         </Router>
//     );
// }


ReactDOM.render(<App />, document.getElementById('root'))