import React from 'react';
import ReactDOM from 'react-dom';
//import './styles/index.css';

import * as serviceWorker from './serviceWorker';

import { ApolloClient } from 'apollo-client'
import { ApolloProvider } from "react-apollo";
import { HttpLink, InMemoryCache } from 'apollo-boost'


import App from './components/App';


const httpLink = new HttpLink({ uri: 'http://127.0.0.1:8000/graphql/' })

const client = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
})


ReactDOM.render(
    <ApolloProvider client={client}>
        <App />
    </ApolloProvider>
, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
