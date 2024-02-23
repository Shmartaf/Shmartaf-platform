import { Card } from "@mui/material";
import Box from "@mui/material/Box";
import NotificationCard from "../components/NotificationCards";
// impport api

// babysitters = api.get("/babysitters)

const notification = [
  {
    name: "Odel Levi",
    desc: "Sociable, athletic, loves animals, available frequently, patient.",
    location: "Tel Aviv",
    date: " 23.3.23"
  },
  {
    name: "Shai Damari",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    location: "Haifa",
    date: " 28.3.23"
  },
  {
    name: "Shai Damari",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    location: "Haifa",
    date: " 11.3.23"
  },
  {
    name: "Shai Damari",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    location: "Haifa",
    date: " 22.3.23"
  },
];

const Notifications = () => {
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
      {notification.map((notification) => (
        <NotificationCard key={notification.name} {...notification} />
      ))}
    </Box>
  );
};
export default Notifications;
