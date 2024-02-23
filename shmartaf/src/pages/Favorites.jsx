import Box from "@mui/material/Box";
import BabysitterCard from "../components/BabysitterCard";
// impport api

// babysitters = api.get("/babysitters)
const babysitters = [
  {
    name: "",
    image: "",
    desc: "",
    location: "",
    rating: "",
  },
  {
    name: "",
    image: "",
    desc: "",
    location: "",
    rating: "",
  },
  {
    name: "",
    image: "",
    rating: "",
    desc: "",
  },
  {
    name: "",
    image: "",
    rating: "",
    desc: "",
  },
];

const favorites = () => {
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
      }}
    >
      {babysitters.map((babysitter) => (
        <BabysitterCard key={babysitter.name} {...babysitter} />
      ))}
    </Box>
  );
};
export default favorites;
