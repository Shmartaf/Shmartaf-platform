// src/components/BabysitterSignup.jsx
import React from "react";
import Dropdown from "./Dropdown";

const BabysitterSignup = ({ onBabysitterSubmit }) => {
  // State for babysitter details
  const [babysitterDescription, setBabysitterDescription] = React.useState("");
  const [babysitterSkills, setBabysitterSkills] = React.useState([]);
  const [babysitterPicture, setBabysitterPicture] = React.useState("");

  // Sample list of skills for babysitters
  const babysitterSkillsOptions = [
    { value: "cpr_certified", label: "CPR Certified" },
    { value: "first_aid", label: "First Aid" },
    { value: "cooking", label: "Cooking" },
    // Add more skills as needed
  ];

  return (
    <div>
      <h2>Babysitter Details</h2>
      {/* Babysitter details inputs */}
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-900 dark:text-white">
          Description
        </label>
        <textarea
          value={babysitterDescription}
          onChange={(e) => setBabysitterDescription(e.target.value)}
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Tell us about yourself..."
          required
        />
      </div>
      {/* Skills dropdown for babysitters */}
      <Dropdown
        label="Skills"
        options={babysitterSkillsOptions}
        value={babysitterSkills}
        onChange={(selectedSkills) => setBabysitterSkills(selectedSkills)}
      />
      {/* Image upload for babysitter picture */}
      {/* ... Add image upload input */}
    </div>
  );
};

export default BabysitterSignup;
