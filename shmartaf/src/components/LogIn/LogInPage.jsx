import React from 'react';
import Header from './Header';
import LoginForm from './LogInForm';

const LoginPage = () => {
    const handleLoginSubmit = ({ email, password }) => {
        // Implement your login logic here using axios or any other method
        console.log(`Logging in with email: ${email} and password: ${password}`);
    };

    return (
        <section className="bg-gray-50 dark:bg-gray-900">
            <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <Header />
                <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                            Sign in to your account
                        </h1>
                        <LoginForm onSubmit={handleLoginSubmit} />
                    </div>
                </div>
            </div>
        </section>
    );
};

export default LoginPage;
