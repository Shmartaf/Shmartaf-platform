import humanImage from "../assets/human.png";
import { Box, Button, Typography } from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import { useAuth } from "../AuthContext";
import { BASE_URL } from "../api";

// const profile = {
//   firstname: "Nurit",
//   lastname: "Levi",
//   phone: "058-1234567",
//   email: "nuritlevi@me.com",
//   location: "Rishon Lezion",
//   address: "123 Main Street",
//   description:
//     "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
//   image: humanImage,
//   tag: "6485",
//   rating: 4.5,
//   reviews: 100,
// };
const fatchProfile = (id) => {
  fetch(`${BASE_URL}/parents/${id}`)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      return data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}


const Settings = async () => {
  const { user } = useAuth ()
  console.log(user)
  const profile = await fatchProfile(user.id)
  console.log(profile)
  console.log(profile.data)
  console.log(profile['user']);
  console.log("Profile.user",profile.user)
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        flexGrow: 1,
        padding: "0px 30px",
        gap: "5px",
      }}
    >
      <Box
        sx={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
          alignItems: "center",
          width: "100%",
          padding: "10px 20px",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
          <img src={humanImage} style={{ width: "50px", height: "50px" }} />
          <Typography variant="h5">{data.user.name}</Typography>
        </div>
      </Box>

      <Typography variant="h6" mt={2}>
        First Name
      </Typography>
      <Typography>{data.user.name.split(" ")[0]}</Typography>
      <Typography variant="h6" mt={2}>
        Last Name
      </Typography>
      <Typography>
        {data.user.name.split(" ")[1]} {data.user.name.split(" ")[2]}
      </Typography>
      <Typography variant="h6" mt={2}>
        Phone
      </Typography>
      <Typography>{data.user.phone}</Typography>
      <Typography variant="h6" mt={2}>
        Email
      </Typography>
      <Typography>{data.user.email}</Typography>
      <Typography variant="h6" mt={2}>
        Location
      </Typography>
      <Typography>{data.user.city}</Typography>
      <Typography variant="h6" mt={2}>
        Address
      </Typography>
      <Typography>{data.user.street}</Typography>
      <Typography variant="h6" mt={2}>
        Description
      </Typography>
      <Typography>{data.user?.description}</Typography>
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
