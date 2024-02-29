import { Card } from "@mui/material";
import Box from "@mui/material/Box";
import NotificationCard from "../components/NotificationCards";
// impport api

// babysitters = api.get("/babysitters)

const notification = [
  {
    name: "",
    desc: ".",
    location: "",
    date: "",
  },
  {
    name: "",
    desc: ".",
    location: "",
    date: "",
  },
  {
    name: "",
    desc: ".",
    location: "",
    date: "",
  },
  {
    name: "",
    desc: ".",
    location: "",
    date: "",
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
