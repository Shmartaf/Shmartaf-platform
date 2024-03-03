import React, { useState, useContext } from "react";
import Header from "../components/LogIn/Header";
import LoginForm from "../components/LogIn/LogInForm";
import { useNavigate } from "react-router-dom";
import { AuthContext, AuthProvider, useAuth } from "../AuthContext";

const LoginPage = () => {
  const [showSignUp, setShowSignUp] = useState(false);
  const navigate = useNavigate();
  const login = useAuth().login;
  const handleLoginSubmit = async ({ email, password }) => {
    console.log(`Logging in with email: ${email} and password: ${password}`);
    try {
      await login({ email, password });
      console.log("Login successful should navigate to home page");
      navigate("/");
    } catch (error) {
      console.error("Login failed", error);
    }
  };

  const handleSignup = () => {
    setShowSignup(true);
  };

  return (
    <AuthProvider>
      <section className="bg-gray-50 dark:bg-gray-900">
        <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
          <Header />
          <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
            <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                {showSignUp
                  ? "Sign up for an account"
                  : "Sign in to your account"}
              </h1>
              {showSignUp ? (
                <SignupForm />
              ) : (
                <LoginForm
                  onSubmit={handleLoginSubmit}
                  onSignUp={handleSignup}
                />
              )}
            </div>
          </div>
        </div>
      </section>
    </AuthProvider>
  );
};
export default LoginPage;
