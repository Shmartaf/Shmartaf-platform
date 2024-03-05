import { useState, useEffect } from "react";
import { Typography } from "@mui/material";
import Box from "@mui/material/Box";
import StarIcon from "@mui/icons-material/Star";
import FavoriteIcon from "@mui/icons-material/Favorite";
import FavoriteBorderIcon from "@mui/icons-material/FavoriteBorder";
import { get } from "../api";

const BabysitterCard = (props) => {
  const [babysitterDetails, setBabysitterDetails] = useState(null);

  useEffect(() => {
    console.log("props", props);
    const fetchDetails = async () => {
      try {
        const response = await get('babysitters', props.id);
        setBabysitterDetails(response);
      } catch (error) {
        console.error("Error fetching babysitter details:", error);
      }
    };

    if (props.id) {
      fetchDetails();
    }
  }, [props.id]);

  const toggleFavorite = () => {
    dispatch({
      type: "UPDATE_BABYSITTER",
      payload: { ...props, isFavorite: !props.isFavorite },
    });
  };
  return (
    <Box className="babysitter-card">
      <img src={`https://i.pravatar.cc/300?img=${babysitterDetails?.pictureid}`} />
      <div
        style={{
          cursor: "pointer",
          position: "absolute",
          right: "10px",
        }}
        onClick={toggleFavorite}
      >
        {props.isFavorite ? (
          <FavoriteIcon color="error" />
        ) : (
          <FavoriteBorderIcon />
        )}
      </div>
      <Box className="flex_row_center">
        <StarIcon sx={{ color: "#5B5CFD" }} />
        <Typography variant="h6">{babysitterDetails?.user?.rating || "4.5"}</Typography>
      </Box>
      <Typography variant="h5" fontWeight={"bold"}>
        {babysitterDetails?.user?.name}
      </Typography>

      <Typography variant="h6" fontWeight={"bold"}>
        {babysitterDetails?.user?.street}, {babysitterDetails?.user?.city}
      </Typography>
      <Box className="flex_row_center" p={1}>
        <Typography>{babysitterDetails?.description}</Typography>
      </Box>
    </Box>
  );
};

export default BabysitterCard;
