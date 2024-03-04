import React, { useContext } from "react";
import Box from "@mui/material/Box";
import BabysitterCard from "../components/BabysitterCard";
import { BabysitterContext } from "../context/BabysitterContext";
import { useAuth } from "../AuthContext";
const Favorites = () => {
  const { state } = useContext(BabysitterContext);
  const { babysitters } = state;
  // we need to find the babysitters that are currently favorited by this user(parent)
  const { user} = useAuth();
  console.log(user);
  const favoriteBabysitters = babysitters.filter(
    (babysitter) => babysitter.isFavorite,
  );

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "row",
        gap: "20px",
        flexWrap: "wrap",
        padding: "20px 10px",
        justifyContent: "center",
        alignItems: "start",
        backgroundColor: "#F8F7F1",
        minHeight: "100vh",
      }}
    >
      {favoriteBabysitters.length > 0 ? (
        favoriteBabysitters.map((babysitter) => (
          <BabysitterCard key={babysitter.name} {...babysitter} />
        ))
      ) : (
        <div
          style={{
            flexGrow: 1,
            height: "100vh",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <p>No favorites</p>
        </div>
      )}
    </Box>
  );
};

export default Favorites;
