import React, { Component } from 'react';
import ListPoke from '../components/ListPoke';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header >
          <h1>
            Gotta catch 'em all!
          </h1>
        </header>
        <ListPoke />
      </div>
    );
  }
}

export default App;
