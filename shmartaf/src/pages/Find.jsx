import { Card } from "@mui/material";
import Box from "@mui/material/Box";
import BabysitterCard from "../components/BabysitterCard";

const babysitters = [
  {
    name: "Odel Levi",
    image: "https://i.pravatar.cc/300?img=1",
    desc: "Sociable, athletic, loves animals, available frequently, patient.",
    location: "Tel Aviv",
    rating: "4.50",
  },
  {
    name: "Shai Damari",
    image: "https://i.pravatar.cc/300?img=2",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    location: "Haifa",
    rating: "4.75",
  },
  {
    name: "Nurit Levi",
    image: "https://i.pravatar.cc/300?img=3",
    rating: "3.90",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
  {
    name: "Tom Levi",
    image: "https://i.pravatar.cc/300?img=4",
    rating: "3.50",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
];

const Find = () => {
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
export default Find;
