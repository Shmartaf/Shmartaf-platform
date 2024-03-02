import humanImage from "../assets/human.png";
import { Box, Button, Typography } from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import { useContext } from "react";
import { BabysitterContext } from "../context/BabysitterContext";

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
  const { user } = useContext(BabysitterContext).state;
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
          <img src={humanImage} style={{ width: "50px", height: "50px" }} />
          <Typography variant="h5">{user.name}</Typography>
        </div>
      </Box>

      <Typography variant="h6" mt={2}>
        First Name
      </Typography>
      <Typography>{user.name.split(" ")[0]}</Typography>
      <Typography variant="h6" mt={2}>
        Last Name
      </Typography>
      <Typography>
        {user.name.split(" ")[1]} {user.name.split(" ")[2]}
      </Typography>
      <Typography variant="h6" mt={2}>
        Phone
      </Typography>
      <Typography>{user.phone}</Typography>
      <Typography variant="h6" mt={2}>
        Email
      </Typography>
      <Typography>{user.email}</Typography>
      <Typography variant="h6" mt={2}>
        Location
      </Typography>
      <Typography>{user.city}</Typography>
      <Typography variant="h6" mt={2}>
        Address
      </Typography>
      <Typography>{user.street}</Typography>
      <Typography variant="h6" mt={2}>
        Description
      </Typography>
      <Typography>{user?.description}</Typography>
      <Box mt={2} display={"flex"} gap={"10px"}>
        <Button variant="contained">Add Child</Button>
        <Button variant="contained" startIcon={<EditIcon />}>
          Edit Profile
        </Button>
      </Box>
    </Box>
  );
};
export default Settings;
