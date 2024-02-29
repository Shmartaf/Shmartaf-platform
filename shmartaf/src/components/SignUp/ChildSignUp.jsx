// src/components/ChildSignup.jsx
import React, { useEffect, useState } from "react";
import Dropdown from "./Dropdown";
import { BASE_URL } from "../../api";

const ChildSignup = ({ onChildChange, onRemoveChild, index }) => {
  const [childName, setChildName] = React.useState("");
  const [childBirthdate, setChildBirthdate] = React.useState("");
  const [childNeeds, setChildNeeds] = React.useState("");
  const [needsOptions, setNeedsOptions] = React.useState([]);

  useEffect(() => {
    // Fetch the needs from the server when the component mounts
    fetch(`${BASE_URL}/requirements?skip=0&limit=10`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        let needsOptions = data.map((need) => ({
          value: need.id,
          label: need.needname,
        }));
        // Now 'options' contains an array of objects with 'value' and 'label' properties
        // console.log(options);
        setNeedsOptions(needsOptions);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, []); // Empty dependency array ensures that this effect runs only once on mount

  return (
    <div key={index} className="mb-4">
      <h3>Child {index + 1}</h3>
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-900 dark:text-white">
          Name
        </label>
        <input
          type="text"
          value={childName}
          onChange={(e) => setChildName(e.target.value)}
          className="... (your styling)"
          placeholder="Child's Name"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-900 dark:text-white">
          Birthdate
        </label>
        <input
          type="text"
          value={childBirthdate}
          onChange={(e) => setChildBirthdate(e.target.value)}
          className="... (your styling)"
          placeholder="Child's Birthdate"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-900 dark:text-white">
          Needs
        </label>
        {/* Dropdown component for child's needs */}
        <Dropdown
          label="Child's Needs"
          options={needsOptions}
          value={childNeeds}
          onChange={(selectedOption) => setChildNeeds(selectedOption)}
        />
      </div>
      <button onClick={() => onRemoveChild(index)}>Remove Child</button>
    </div>
  );
};

export default ChildSignup;
