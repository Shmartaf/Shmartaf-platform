import React, { createContext, useContext, useEffect, useState } from "react";
import { createSupabaseClient } from "./lib/supabaseClient";

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
      const response = await supabase.auth.signUp({ email, password });
      if (response.error) throw response.error; // Corrected the error handling
      setAuthState((prevState) => ({
        ...prevState,
        user: response.data.user,
      }));
    } catch (error) {
      console.error("Sign up failed", error);
      throw error;
    }
  };

  const login = async ({ email, password }) => {
    try {
      const response = await supabase.auth.signInWithPassword({
        email,
        password,
      });
      if (response.error) throw response.error; // Corrected the error handling
      setAuthState((prevState) => ({
        ...prevState,
        user: response.data.user,
        session: response.data.session,
      }));
    } catch (error) {
      console.error("Login failed", error);
      throw error;
    }
  };

  const logout = async () => {
    await supabase.auth.signOut();
    setAuthState({
      user: null,
      session: null,
      loading: false,
      isAuthenticated: false,
    });
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
