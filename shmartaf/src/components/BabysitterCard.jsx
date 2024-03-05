import React from 'react';
import { Typography, Box } from "@mui/material";
import StarIcon from "@mui/icons-material/Star";
//import FavoriteIcon from "@mui/icons-material/Favorite";
//import FavoriteBorderIcon from "@mui/icons-material/FavoriteBorder";
//import {toggleFavorite} from "../pages/Favorites";

// Adjust props to directly receive babysitter data and a toggleFavorite function
const BabysitterCard = () => {
  return (
    <Box className="babysitter-card">
      {/* <img src={`https://i.pravatar.cc/300?img=${babysitter.pictureid}`} alt="Babysitter" /> */}
      <div
  style={{ cursor: "pointer", position: "absolute", right: "10px" }}
  //onClick={toggleFavorite} // No need to pass arguments here
>
  {/* {isFavorite ? <FavoriteIcon color="error" /> : <FavoriteBorderIcon />} */}
</div>
      <Box className="flex_row_center">
        <StarIcon sx={{ color: "#5B5CFD" }} />
        <Typography variant="h6">{"4.5" /* Assuming a default rating, adjust as necessary */}</Typography>
      </Box>
      <Typography variant="h5" fontWeight="bold">
        {/* {babysitter.user.name} */}
      </Typography>
      <Typography
      variant="h6" fontWeight="bold">
      {/* {babysitter.user.street}, {babysitter.user.city} */}
      </Typography>
<Box className="flex_row_center" p={1}>
{/* <Typography>{babysitter.description}</Typography> */}
</Box>
</Box>
);
};

export default BabysitterCard;