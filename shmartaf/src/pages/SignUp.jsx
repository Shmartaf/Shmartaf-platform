// src/components/SignupPage.jsx
import React from 'react';
import Header from '../components/LogIn/Header';
import SignupForm from '../components/SignUp/SignUpForm';

const SignupPage = () => {
    const handleSignupSubmit = (userDetails) => {
        // Implement your signup logic here using axios or any other method
        console.log('Signing up with details:', userDetails);
    };

    return (
        <section className="bg-gray-50 dark:bg-gray-900">
            <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <Header />
                <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                            Sign up for your account
                        </h1>
                        <SignupForm onSubmit={handleSignupSubmit} />
                    </div>
                </div>
            </div>
        </section>
    );
};

export default SignupPage;
