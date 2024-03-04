import React, { createContext, useContext, useEffect, useState } from "react";
import { createSupabaseClient } from "./lib/supabaseClient";
import { BASE_URL } from "./api";

const findUserRole = async (user) => {
  try {
    // Ensure BASE_URL is correctly formatted without leading or trailing slashes if needed
    const url = `${BASE_URL}/users/${user.id}`;
    const response = await fetch(url);
    console.log(`Response:`, response);
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json(); // Correctly parse the JSON body
    console.log(`Data:`, data);
    
    return data.userType; // Adjust this according to the actual structure of your data
  } catch (error) {
    console.error("Failed to find user roles:", error);
    return null;
  }
};

const findUser = async (user) => {
  try {
    // Ensure BASE_URL is correctly formatted without leading or trailing slashes if needed
    const url = `${BASE_URL}/users/${user.id}`;
    const response = await fetch(url);
    console.log(`Response:`, response);
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json(); // Correctly parse the JSON body
    console.log(`Data:`, data);
    
    return data; // Adjust this according to the actual structure of your data
  } catch (error) {
    console.error("Failed to find user:", error);
    return null;
  }
};

// Create an AuthContext
export const AuthContext = createContext();

// AuthProvider component
export const AuthProvider = ({ children }) => {
  const [authState, setAuthState] = useState({
    user: null,
    session: null,
    loading: true,
    isAuthenticated: false,
  });

  const supabase = createSupabaseClient(); // Make sure to replace with your actual function

  useEffect(() => {
    const checkAuthentication = async () => {
      const { user, session } = authState;

      const isAuthenticated = !!user && !!session;

      setAuthState((prevState) => ({
        ...prevState,
        isAuthenticated,
        loading: false,
      }));
    };

    checkAuthentication();
  }, [authState.user, authState.session]);

  const signUp = async ({ email, password }) => {
    try {
      const { user, error } = await supabase.auth.signUp({ email, password });

      if (error) {
        throw error;
      }

      setAuthState((prevState) => ({
        ...prevState,
        user,
      }));
    } catch (error) {
      console.error("Sign up failed", error);
      throw error;
    }
  };

  const login = async ({ email, password }) => {
    try {
      const { data, error } = await supabase.auth.signInWithPassword({
        email,
        password,
      });
      const userData = await findUser(data.user);
      console.log("userData:", userData);
      data.user.userData = userData;
      setAuthState({
        user: data.user,
        session: data.session,
        loading: false,
        isAuthenticated: true,
      });

      if (error) {
        throw error;
      }
      return data;
    } catch (error) {
      console.error("Login failed", error);
      throw error;
    }
  };

  const logout = async () => {
    try {
      const response = await supabase.auth.signOut();
      setAuthState({
        user: null,
        session: null,
        loading: false,
        isAuthenticated: false,
      });
    } catch (error) {
      console.error("Logout failed", error);
      throw error;
    }
  };

  return (
    <AuthContext.Provider value={{ ...authState, login, logout, signUp }}>
      {children}
    </AuthContext.Provider>
  );
};

// useAuth hook
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
