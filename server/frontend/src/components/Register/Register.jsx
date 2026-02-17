import React, { useState } from "react";
import "./Register.css";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");

  const goLogin = () => {
    window.location.href = "/login";
  };

  const register = async (e) => {
    e.preventDefault();
    let register_url = window.location.origin + "/djangoapp/register";
    
    const res = await fetch(register_url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "userName": userName,
            "password": password,
            "firstName": firstName,
            "lastName": lastName,
            "email": email
        }),
    });
    
    const json = await res.json();
    if (json.status) {
        sessionStorage.setItem('username', json.userName);
        window.location.href = window.location.origin;
    } else if (json.error === "Already Registered") {
        alert("The user with same username is already registered");
        window.location.href = window.location.origin;
    }
  };

  return (
    <div className="register_container" style={{ width: "50%", margin: "auto", padding: "20px" }}>
      <div className="header" style={{ textAlign: "center", marginBottom: "20px" }}>
        <h1>Sign Up</h1>
      </div>
      
      <form onSubmit={register}>
        <div className="form-group mb-3">
          <label>Username</label>
          <input type="text" name="username" placeholder="Enter Username" className="form-control" onChange={(e) => setUserName(e.target.value)} required />
        </div>
        
        <div className="form-group mb-3">
          <label>First Name</label>
          <input type="text" name="firstName" placeholder="Enter First Name" className="form-control" onChange={(e) => setFirstName(e.target.value)} required />
        </div>
        
        <div className="form-group mb-3">
          <label>Last Name</label>
          <input type="text" name="lastName" placeholder="Enter Last Name" className="form-control" onChange={(e) => setLastName(e.target.value)} required />
        </div>
        
        <div className="form-group mb-3">
          <label>Email</label>
          <input type="email" name="email" placeholder="Enter Email" className="form-control" onChange={(e) => setEmail(e.target.value)} required />
        </div>
        
        <div className="form-group mb-3">
          <label>Password</label>
          <input type="password" name="password" placeholder="Enter Password" className="form-control" onChange={(e) => setPassword(e.target.value)} required />
        </div>
        
        <div className="submit_panel" style={{ textAlign: "center", marginTop: "20px" }}>
          <button className="btn btn-primary" type="submit">Register</button>
          <button className="btn btn-secondary ms-2" onClick={goLogin} type="button">Login</button>
        </div>
      </form>
    </div>
  );
};

export default Register;
