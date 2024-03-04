import React, { createContext, useContext, useEffect, useState } from "react";
import { createSupabaseClient } from "./lib/supabaseClient";
import { BASE_URL } from "./api";

const findUserRole = (user) => {
  const roles = [];
  try {
    fetch(`${BASE_URL}/parents/${user.id}`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (data.length > 0) {
          roles.push("parent");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  catch (e) {
    console.log(e);
  }
  try {
    fetch(`${BASE_URL}/babysitters/${user.id}`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (data.length > 0) {
          roles.push("babysitter");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  catch (e) {
    console.log(e);
  }
  return roles;
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
      const roles = findUserRole(data.user);
      console.log("Roles:", roles);
      data.user.roles = roles;
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
