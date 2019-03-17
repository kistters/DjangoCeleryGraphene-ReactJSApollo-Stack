import React, { Component } from 'react';
import Poke from './Poke';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header >
          <h1>
            Gotta catch 'em all!
          </h1>
        </header>
        <Poke name='bulbasaur' types="grass" />
        <Poke name='blastoise' types="water">My favorite Poke</Poke>
      </div>
    );
  }
}

export default App;
