import humanImage from "../assets/human.png";
import { Box, Button, Typography } from "@mui/material";
import EditIcon from '@mui/icons-material/Edit';

const profile = {
  firstname: "Nurit",
  lastname: "Levi",
  phone: "058-1234567",
  email: "nuritlevi@me.com",
  location: "Rishon Lezion",
  address: "123 Main Street",
  description:
    "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  image: humanImage,
  tag: "6485",
  rating: 4.5,
  reviews: 100,
};

const Settings = () => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        flexGrow: 1,
        padding: "0px 30px",
        gap: "5px",
      }}>
      <Box
        sx={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
          alignItems: "center",
          width: "100%",
          padding: "10px 20px",
        }}>
        <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
          <img src={profile.image} style={{ width: "50px", height: "50px" }} />
          <Typography variant="h5">{profile.firstname}</Typography>
        </div>
      </Box>

      <Typography variant="h6" mt={2}>
        First Name
      </Typography>
      <Typography>{profile.firstname}</Typography>
      <Typography variant="h6" mt={2}>
        Last Name
      </Typography>
      <Typography>{profile.lastname}</Typography>
      <Typography variant="h6" mt={2}>
        Phone
      </Typography>
      <Typography>{profile.phone}</Typography>
      <Typography variant="h6" mt={2}>
        Email
      </Typography>
      <Typography>{profile.email}</Typography>
      <Typography variant="h6" mt={2}>
        Location
      </Typography>
      <Typography>{profile.location}</Typography>
      <Typography variant="h6" mt={2}>
        Address
      </Typography>
      <Typography>{profile.address}</Typography>
      <Typography variant="h6" mt={2}>
        Description
      </Typography>
      <Typography>{profile.description}</Typography>
      <Box mt={2} display={"flex"} gap={"10px"}>
        <Button variant="contained">Add Child</Button>
        <Button variant="contained" startIcon={<EditIcon />}>Edit Profile</Button>
      </Box>
    </Box>
  );
};
export default Settings;
