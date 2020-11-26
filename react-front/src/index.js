import React from 'react';
import ReactDOM from 'react-dom';
//import './styles/index.css';

import * as serviceWorker from './serviceWorker';

import { ApolloClient, ApolloProvider, InMemoryCache, HttpLink } from '@apollo/client';
import { WebSocketLink } from 'apollo-link-ws';
import { split } from 'apollo-link'
import { getMainDefinition } from 'apollo-utilities'

import App from './components/App';

const httpLink = new HttpLink({ uri: 'http://127.0.0.1:8000/graphql/' })

const wsLink = new WebSocketLink({
  uri: `ws://127.0.0.1:8000/ws/graphql/`,
  options: {
    reconnect: true
  }
});

const splitLink = split(
  ({ query }) => {
    const definition = getMainDefinition(query);
    return (
      definition.kind === 'OperationDefinition' &&
      definition.operation === 'subscription'
    );
  },
  wsLink,
  httpLink,
);

const client = new ApolloClient({
  link: splitLink,
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
