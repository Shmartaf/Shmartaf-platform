import Box from "@mui/material/Box";
import FavoriteCard from "../components/FavoriteCard";
// impport api

// babysitters = api.get("/babysitters)
const favorite = [
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
      {favorite.map((favorite) => (
        <FavoriteCard key={favorite.name} {...favorite} />
      ))}
    </Box>
  );
};
export default favorites;
