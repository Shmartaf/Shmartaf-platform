import Box from "@mui/material/Box";
import BabysitterCard from "../components/BabysitterCard/";
import { useContext } from "react";
import { BabysitterContext } from "../context/BabysitterContext";
// impport api

// babysitters = api.get("/babysitters)

const Find = () => {
  const { state, dispatch } = useContext(BabysitterContext);
  const { babysitters } = state;

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "row",
        gap: "20px",
        flexWrap: "wrap",
        padding: "20px 10px",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#F8F7F1",
      }}
    >
      {babysitters.map((babysitter) => (
        <BabysitterCard key={babysitter.name} {...babysitter} />
      ))}
    </Box>
  );
};
export default Find;
