import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';

const NavBar = ({ setAuthenticated }) => {
  return (
    <nav>
      <ul>
        <li>
          <NavLink to="/" exact={true} activeClassName="active">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/gyms" exact={true} activeClassName="active">
            Gyms
          </NavLink>
        </li>
        <li>
          <NavLink to="/raids" exact={true} activeClassName="active">
            Raids
          </NavLink>
        </li>
        {/* <li>
          <LogoutButton setAuthenticated={setAuthenticated} />
        </li> */}
      </ul>
    </nav>
  );
}

export default NavBar;