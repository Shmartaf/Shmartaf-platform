// src/components/ParentSignup.jsx
import React from 'react';
import ChildSignup from './ChildSignUp';
import Dropdown from './Dropdown';

const ParentSignup = ({ onParentSubmit }) => {
    const [parentDescription, setParentDescription] = React.useState('');
    const [children, setChildren] = React.useState([]);

    const handleAddChild = () => {
        setChildren([...children, {}]); // Add an empty child object to the array
    };

    const handleRemoveChild = (index) => {
        const updatedChildren = [...children];
        updatedChildren.splice(index, 1);
        setChildren(updatedChildren);
    };

    const handleChildChange = (index, childData) => {
        const updatedChildren = [...children];
        updatedChildren[index] = childData;
        setChildren(updatedChildren);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Combine all the details and submit to the server
        const parentDetails = {
            parentDescription,
            children,
        };
        onParentSubmit(parentDetails);
    };

    return (
        <div>
            <h2>Parent Details</h2>
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-900 dark:text-white">Description</label>
                <textarea
                    value={parentDescription}
                    onChange={(e) => setParentDescription(e.target.value)}
                    className="... (your styling)"
                    placeholder="Tell us about yourself..."
                    required
                />
            </div>
            <div>
                {children.map((child, index) => (
                    <ChildSignup
                        key={index}
                        index={index}
                        onChildChange={(childData) => handleChildChange(index, childData)}
                        onRemoveChild={handleRemoveChild}
                    />
                ))}
            </div>
            <button onClick={handleAddChild}>Add Child</button>
            {/* ... (existing code) */}
        </div>
    );
};

export default ParentSignup;
