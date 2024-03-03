import React, { useEffect } from "react";
import { Route, Routes, Navigate } from "react-router-dom";

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
import { AuthProvider, useAuth } from "./AuthContext";
import LoginPage from "./pages/LogInPage";
import SignUp from "./pages/SignUp";

function App() {
  const { isAuthenticated } = useAuth();

  useEffect(() => {
    // Check if the user is authenticated
    console.log("Is Authenticated:", isAuthenticated);
  }, [isAuthenticated]);

  return (
    // <SignUp />
    <AuthProvider>
      <Routes>
        <Route
          path="/"
          element={
            isAuthenticated ? (
              <Layout>
                <Route index element={<Dashboard />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/find" element={<Find />} />
                <Route path="/contacted" element={<Contacted />} />
                <Route path="/notifications" element={<Notifications />} />
                <Route path="/favorites" element={<Favorites />} />
                <Route path="/profile" element={<Profile />} />
                <Route path="/settings" element={<Settings />} />
              </Layout>
            ) : (
              <Navigate to="/login" />
            )
          }
        />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignUp />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
