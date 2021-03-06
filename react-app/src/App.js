import React, { useState, useEffect } from "react";
import { BrowserRouter, Route } from "react-router-dom";
import { Provider } from "react-redux";

import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import { authenticate } from "./services/auth";
import MapSimple from "./components/Map";
import Raid from "./components/Raid";

function App({ store }) {
  const [authenticated, setAuthenticated] = useState(true);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async() => {
      const user = await authenticate();
      if (!user.errors) {
        setAuthenticated(true);
      }
      setLoaded(true);
    })();
  }, []);

  if (!loaded) {
    return null;
  }

  return (
    <Provider store={store}>
      <BrowserRouter>
        <Route path="/" exact={true} authenticated={authenticated}>
          <NavBar setAuthenticated={setAuthenticated} />
          <MapSimple />
        </Route>
        <Route path="/raids" exact={true}>
          <NavBar />
          <Raid />
        </Route>  
        <Route path="/login" exact={true}>
          <LoginForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm authenticated={authenticated} setAuthenticated={setAuthenticated} />
        </Route>
        <ProtectedRoute path="/users" exact={true} authenticated={authenticated}>
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true} authenticated={authenticated}>
          <User />
        </ProtectedRoute>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
