import React, { Component } from 'react';
import ListPoke from '../components/ListPoke';
import ListPokeType from '../components/ListPokeType';
import TrackPoke from '../components/TrackPoke';

import { BrowserRouter as Router, Route } from "react-router-dom";

class App extends Component {
  render() {
    return (
      <div className="App">
        <header >
          <h1>
            Gotta catch 'em all!
          </h1>
        </header>
        <Router>
          <Route exact path="/" component={ListPoke} />
          <Route path="/type/:type_name" component={ListPokeType} />
          <Route path="/track-poke" component={TrackPoke} />
        </Router>
      </div>
    );
  }
}

export default App;
