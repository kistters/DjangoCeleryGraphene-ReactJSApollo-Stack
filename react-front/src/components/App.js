import React, {Component} from 'react';
import ListPoke from '../components/ListPoke';
import ListPokeType from '../components/ListPokeType';
import TrackPoke from '../components/TrackPoke';

import {BrowserRouter as Router, Route} from "react-router-dom";


import {Link} from 'react-router-dom';

const Header = () => {
    return (
        <ul>

            <li><Link to="/">Home</Link></li>
            <li><Link to="/type"> Pokemon Types</Link></li>
            <li><Link to="/track-poke">Websocket</Link></li>
        </ul>
    )
}


class App extends Component {
    render() {
        return (
            <div className="App">
                <header>
                    <h1>
                        Gotta catch 'em all!
                    </h1>
                </header>
                <Router>
                    <Header/>
                    <Route exact path="/" component={ListPoke}/>
                    <Route path="/type/:type_name" component={ListPokeType}/>
                    <Route path="/track-poke" component={TrackPoke}/>
                </Router>
            </div>
        );
    }
}

export default App;
