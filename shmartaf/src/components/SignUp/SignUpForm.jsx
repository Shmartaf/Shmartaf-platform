// src/components/SignupForm.jsx
import React from 'react';
import Dropdown from './Dropdown';
import ParentSignup from './ParentSignUp';
import BabysitterSignup from './BabysitterSignup';
import CheckBox from './CheckBox';

const SignupForm = ({ onSubmit }) => {
    // State for general details
    const [name, setName] = React.useState('');
    const [gender, setGender] = React.useState('');
    const [email, setEmail] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [registrationDate, setRegistrationDate] = React.useState('');
    const [city, setCity] = React.useState('');
    const [street, setStreet] = React.useState('');
    const [phone, setPhone] = React.useState('');




    // State for user type
    const [showParent, setShowParent] = React.useState(false);
    const [showBabysitter, setShowBabysitter] = React.useState(false);

    // State for parent details
    const [parentDescription, setParentDescription] = React.useState('');
    const [children, setChildren] = React.useState([]);

    // State for babysitter details
    const [babysitterDescription, setBabysitterDescription] = React.useState('');
    const [babysitterSkills, setBabysitterSkills] = React.useState([]);
    const [babysitterPicture, setBabysitterPicture] = React.useState('');

    const handleParentType = () => {
        setShowParent(!showParent);
    };

    const handleBabysitterType = () => {
        setShowBabysitter(!showBabysitter);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Combine all the details and submit to the server
        const userDetails = {
            name,
            gender,
            email,
            password,
            registrationDate,
            city,
            street,
            phone,
            userType,
            parentDetails: {
                description: parentDescription,
                children,
            },
            babysitterDetails: {
                description: babysitterDescription,
                skills: babysitterSkills,
                picture: babysitterPicture,
            },
        };
        onSubmit(userDetails);
    };

    return (
        <form onSubmit={handleSubmit}>
            {/* General details inputs */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-900 dark:text-white">Name</label>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="Your Name"
                    required
                />
            </div>
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-900 dark:text-white">Gender</label>
                <select
                    value={gender}
                    onChange={(e) => setGender(e.target.value)}
                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    required
                >
                    <option value="" disabled>Select your gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    {/* Add more gender options if needed */}
                </select>
            </div>
            {/* ... Add other general details inputs */}

            {/* City dropdown */}
            <Dropdown
                label="City"
                options={[
                    { value: 'city1', label: 'City 1' },
                    { value: 'city2', label: 'City 2' },
                    { value: 'city3', label: 'City 3' },
                    {/* Add more cities as needed */ }
                ]}
                value={city}
                onChange={(selectedCity) => setCity(selectedCity)}
            />

            {/* ... (Additional details based on userType) */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-900 dark:text-white">User Type</label>
                <div className="flex items-center">
                    <CheckBox
                        value="parent"
                        onChange={() => handleParentType()}
                        label="Parent"
                    />
                    <CheckBox
                        value="babysitter"
                        onChange={() => handleBabysitterType()}
                        label="Babysitter"
                    />
                </div>
            </div>


            {(showParent || showBabysitter) && (
                <div>
                    {showParent && <ParentSignup />}
                    {showBabysitter && <BabysitterSignup />}
                </div>
            )}
            <button type="submit">Sign up</button>
        </form>
    );
};

export default SignupForm;
