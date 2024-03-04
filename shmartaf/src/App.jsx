import React, { useEffect } from "react";
import { Route, Routes, Navigate, useLocation } from "react-router-dom";

import Layout from "./components/Layout";
import ParentDashboard from "./pages/ParentDashboard";

import Find from "./pages/Find";
import Contacted from "./pages/Contacted";
import Notifications from "./pages/Notifications";
import Favorites from "./pages/Favorites";
import Profile from "./pages/Profile";
import Settings from "./pages/Settings";
import Reviews from "./pages/Reviews";
import Schedule from "./pages/Schedule";
import { BabysitterContext } from "./context/BabysitterContext";
import { useContext } from "react";
import Login from "./pages/Login";
import BabysitterDashboard from "./pages/BabysitterDashboard";
import { useAuth } from "./AuthContext";
import LoginPage from "./pages/LogInPage";
import SignUp from "./pages/SignUp";

function App() {
  const { isAuthenticated, session, user, Login, logout } = useAuth();
  const location = useLocation();
  useEffect(() => {
    // Check if the user is authenticated
    console.log("User:", user);
    console.log("Session:", session);
    // console
    console.log("Is Authenticated:", isAuthenticated);
  }, [isAuthenticated]);

  return (
    //<Favorites/>
    //<Find/>
    //<LoginPage/>
    //isAuthenticated: Favorites
    // <SignUp />
    // <ParentDashboard />
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route
          index
          element={
            isAuthenticated ? (
              user?.roles?.includes("babysitter") ? (
                <BabysitterDashboard />
              ) : (
                <ParentDashboard />
              )
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />
        <Route path="/find" element={<Find />} />
        <Route path="/contacted" element={<Contacted />} />
        <Route path="/notifications" element={<Notifications />} />
        <Route path="/favorites" element={<Favorites />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/settings" element={<Settings />} />
      </Route>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/signup" element={<SignUp />} />
    </Routes>

    /*
    <Routes>
      <Route
        path="/"
        element={
          isAuthenticated ? (
            <Layout>
              <Route path="/dashboard" element={<ParentDashboard />} />
              <Route path="/find" element={<Find />} />
              <Route path="/contacted" element={<Contacted />} />
              <Route path="/notifications" element={<Notifications />} />
              <Route path="/favorites" element={<Favorites />} />
              <Route path="/profile" element={<Profile />} />
              <Route path="/settings" element={<Settings />} />
            </Layout>
          ) : (
            <Navigate to="/login" state={{ from: location }} />
          )
        }
      />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/signup" element={<SignUp />} />
    </Routes>
    */
  );
}

export default App;
