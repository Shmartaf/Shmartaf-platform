import { Card } from "@mui/material";
import Box from "@mui/material/Box";
import parentprofile from "../components/parentprofile";
import Header from "../components/Header";
// impport api

// babysitters = api.get("/babysitters)
const parent = [
  {
    name: "Odel Levi",
    image: "https://i.pravatar.cc/300?img=1",
    desc: "Sociable, athletic, loves animals, available frequently, patient.",
    location: "Tel Aviv",
    rating: "4.50",
  },
];

const profile = () => {
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
      {parent.map((parent) => (
        <parentprofile key={parent.name} {...parent} />
      ))}
    </Box>
  );
};
export default parentprofile;
