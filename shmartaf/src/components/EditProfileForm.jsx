import React, { useState } from "react";
import {
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Typography,
} from "@mui/material";

const EditProfileForm = ({ profileData, onSaveChanges, onClose }) => {
  const [editedProfile, setEditedProfile] = useState({ ...profileData });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEditedProfile((prevProfile) => ({
      ...prevProfile,
      [name]: value,
    }));
  };

  return (
    <>
      <DialogTitle>Edit Profile</DialogTitle>
      <DialogContent>
        <TextField
          label="Name"
          name="name"
          value={editedProfile.user.name}
          onChange={handleInputChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Phone"
          name="phone"
          value={editedProfile.user.phone}
          onChange={handleInputChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Email"
          name="email"
          value={editedProfile.user.email}
          onChange={handleInputChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="City"
          name="city"
          value={editedProfile.user.city}
          onChange={handleInputChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Street"
          name="street"
          value={editedProfile.user.street}
          onChange={handleInputChange}
          fullWidth
          margin="normal"
        />
        <FormControl fullWidth margin="normal">
          <InputLabel>Gender</InputLabel>
          <Select
            name="gender"
            value={editedProfile.user.gender}
            onChange={handleInputChange}
          >
            <MenuItem value="male">Male</MenuItem>
            <MenuItem value="female">Female</MenuItem>
          </Select>
        </FormControl>

        {/* Display children information */}
        <Typography variant="h6" mt={2}>
          Children
        </Typography>
        {editedProfile.childrens.map((child) => (
          <div key={child.id}>
            <Typography>
              Name:
              <TextField
                label="Name"
                name="name"
                value={child.name}
                onChange={handleInputChange}
                fullWidth
                margin="normal"
              />
            </Typography>
            <Typography>
              Birthdate:
              <TextField
                label="Birthdate"
                name="birthdate"
                value={child.birthdate}
                onChange={handleInputChange}
                fullWidth
                margin="normal"
              />
            </Typography>
            <Typography>
              Gender:
              <FormControl fullWidth margin="normal">
                <InputLabel>Gender</InputLabel>
                <Select
                  name="gender"
                  value={child.gender}
                  onChange={handleInputChange}
                >
                  <MenuItem value="male">Male</MenuItem>
                  <MenuItem value="female">Female</MenuItem>
                </Select>
              </FormControl>
            </Typography>
            {/* Display other child information as needed */}
            <hr />
          </div>
        ))}
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">
          Cancel
        </Button>
        <Button onClick={() => onSaveChanges(editedProfile)} color="primary">
          Save Changes
        </Button>
      </DialogActions>
    </>
  );
};

export default EditProfileForm;
