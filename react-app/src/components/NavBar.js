import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';

import "./NavBar.css";

const NavBar = ({ setAuthenticated }) => {
  return (
    <div className="navbar_container">
      <nav>
        <ul>
          <li className="link">
            <NavLink to="/" exact={true} activeClassName="active">
              Home
            </NavLink>
          </li>
          {/* <li>
            <NavLink to="/gyms" exact={true} activeClassName="active">
              Gyms
            </NavLink>
          </li> */}
          <li className="link">
            <NavLink to="/raids" exact={true} activeClassName="active">
              Raids
            </NavLink>
          </li>
          {/* <li>
            <LogoutButton setAuthenticated={setAuthenticated} />
          </li> */}
        </ul>
      </nav>
    </div>
  );
};

export default NavBar;