import React from 'react';
import { NavLink } from 'react-router-dom';
import Typography from '@material-ui/core/Typography';

import "./NavBar.css";
import LogoutButton from './auth/LogoutButton';
import Logo from "../assets/logo.png";

const NavBar = ({ setAuthenticated }) => {
  return (
    <div className="navbar_container">
      <div className="empty_div" />
      <div className="logo_container">
        <img src={Logo} alt="logo" className="logo" />
      </div>
      <nav>
        <ul>
          <li className="link">
            <NavLink to="/" exact={true} activeClassName="active">
              <Typography>
                Home
              </Typography>
            </NavLink>
          </li>
          {/* <li>
            <NavLink to="/gyms" exact={true} activeClassName="active">
              Gyms
            </NavLink>
          </li> */}
          <li className="link">
            <NavLink to="/raids" exact={true} activeClassName="active">
              <Typography> 
                Raids
              </Typography>
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