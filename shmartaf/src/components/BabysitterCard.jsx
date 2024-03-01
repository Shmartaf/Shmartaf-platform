import { Typography } from "@mui/material";
import Box from "@mui/material/Box";
import StarIcon from "@mui/icons-material/Star";
import FavoriteIcon from "@mui/icons-material/Favorite";
import FavoriteBorderIcon from "@mui/icons-material/FavoriteBorder";
import { useContext } from "react";
import { BabysitterContext } from "../context/BabysitterContext";

const BabysitterCard = (props) => {
  const { state, dispatch } = useContext(BabysitterContext);

  // const handleProfile = () => {
  //     console.log(props);
  //     dispatch({ type: "SET_SELECTED", payload: props });
  //   };

  const toggleFavorite = () => {
    dispatch({
      type: "UPDATE_BABYSITTER",
      payload: { ...props, isFavorite: !props.isFavorite },
    });
  };
  return (
    <Box className="babysitter-card">
      {/* <img src={props.image} /> */}
      <img src={`https://i.pravatar.cc/300?img=${props?.pictureid}`} />
      <div
        style={{
          cursor: "pointer",
          position: "absolute",
          right: "10px",
        }}
        onClick={toggleFavorite}>
        {props.isFavorite ? (
          <FavoriteIcon color="error" />
        ) : (
          <FavoriteBorderIcon />
        )}
      </div>
      <Box className="flex_row_center">
        <StarIcon sx={{ color: "#5B5CFD" }} />
        <Typography variant="h6">{props?.rating || "4.5"}</Typography>
      </Box>
      <Typography variant="h5" fontWeight={"bold"}>
        {props?.user?.name}
      </Typography>

      <Typography variant="h6" fontWeight={"bold"}>
        {props?.user?.street}, {props?.user?.city}
      </Typography>
      <Box className="flex_row_center" p={1}>
        <Typography>{props.description}</Typography>
      </Box>
    </Box>
  );
};
export default BabysitterCard;
