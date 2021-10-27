import React from 'react';
import { Link } from 'react-router-dom';

export const Navbar = ()=> {
  return (
    <div>
      <Link to="/" className="btn btn-success " tabIndex={-1} role="button" aria-disabled="true">USERS</Link>
      <Link to="/about" className="btn btn-danger" tabIndex={-1} role="button" aria-disabled="true">ABOUT</Link>
    </div>
  );
}
